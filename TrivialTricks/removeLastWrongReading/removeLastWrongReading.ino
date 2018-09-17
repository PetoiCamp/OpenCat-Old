/*
  remember reading in a history list
  in case that the current reading is proven to be inaccurate later.
  the program will always use last correct reading.
  the inaccurate reading won't be added to the history.
  the rolling pointer to the history list reduces copy operations

  application: removing the wrong reading from MPU6050 when FIFO buffer overflows

  Rongzhong Li
  September 6, 2018
*/

#include <EEPROM.h>
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

#define HISTORY 4
int reading = 0;
char readLag[HISTORY];
int lag = 0;
void setup() {
  Serial.begin(57600);
}
void loop() {
  if ( Serial.available() > 0) {
    reading = Serial.read();
    if (reading > '7')
      reading = readLag[(lag - 1 + HISTORY) % HISTORY];
    else {
      readLag[lag] = reading;
      reading = readLag[(lag - 1 + HISTORY) % HISTORY];
      lag = (lag + 1) % HISTORY;
    }
    for (int i = 0; i < HISTORY; i++) {
      PT(readLag[i]);
      PT(' ');
    }
    PT(": ");
    PTL(reading - '0');
  }

  delay(500);

}
