#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)
#define PTF(s) Serial.print(F(s))//trade flash memory for dynamic memory with F() function
#define PTLF(s) Serial.println(F(s))

#include <EEPROM.h>
//#include <avr/eeprom.h> // doesn't work. <EEPROM.h> works
#define BUZZER 4
#define MELODY 1023 //melody will be saved at the end of the 1KB EEPROM, and is read reversely. That allows some flexibility on the melody length. 
#define PIN 0
#define CALIB 16
#define MIDSHIFT 32
#define ROTDIRECTION 48
#define RANGERATIO 64
#define MPUCALIB 80
void beep(byte note, float duration = 10, int pause = 0, byte repeat = 1 ) {
  if (note == 0) {//rest note
    analogWrite(BUZZER, 0);
    delay(duration);
    return;
  }
  int freq = 220 * pow(1.059463, note-1);// 1.059463 comes from https://en.wikipedia.org/wiki/Twelfth_root_of_two
  float period = 1000000.0 / freq;
  for (byte r = 0; r < repeat; r++) {
    for (float t = 0; t < duration * 1000; t += period) {
      analogWrite(BUZZER, 150);      // Almost any value can be used except 0 and 255
      // experiment to get the best tone
      delayMicroseconds(period/2);          // rise for half period
      analogWrite(BUZZER, 0);       // 0 turns it off
      delayMicroseconds(period/2);          // down for half period
    }
    delay(pause);
  }
}
void playMelody(int start) {
  byte len = (byte)EEPROM.read(start) / 2;
  for (int i = 0; i < len; i++)
    beep(EEPROM.read(start - 1 - i), 1000 / EEPROM.read(start - 1 - len - i), 100);
}

#define DOF 16

// credit to Adafruit PWM servo driver library
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

// Depending on your servo make, the pulse width min and max may vary, you
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)
#define BOUND 1/8
#define RANGE (SERVOMAX - SERVOMIN)
// our servo # counter

int8_t servoCalibs[DOF] = {};
char currentAng[DOF] = {};
int calibratedDuty0[DOF];

