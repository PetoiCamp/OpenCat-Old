/*
  Fade

  This example shows how to fade an LED on pin 9 using the analogWrite()
  function.

  The analogWrite() function uses PWM, so if you want to change the pin you're
  using, be sure to use another PWM capable pin. On most Arduino, the PWM pins
  are identified with a "~" sign, like ~3, ~5, ~6, ~9, ~10 and ~11.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Fade

  Modified by Rongzhong with array defination on pins for convinient looping. 
  Oct 2018
*/
#define PI 3.1416
int led[] = {8,9,10}; //BGR
int freq[3];
int period = 250;
int t = 0;

// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(57600);
  // declare pin 9 to be an output:
  for (int i : led)
    pinMode(i, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // set the brightness of pin 9:
  for (int i = 0; i < 3; i++) {

    // change the brightness for next time through the loop:
    if (t % period == 0)
      freq[i] = random(1, 6);
    analogWrite(led[i], 100 * (sin( 2 * PI * freq[i] * t / period) + 1)+20);
  }
  t++;
  // wait for 30 milliseconds to see the dimming effect
  delay(10000.0 / period);//10 seconds for one longest period
}
