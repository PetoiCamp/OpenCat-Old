/*
  remember reading in a history list
  in case that the current reading is proven to be inaccurate later.
  the program will always use last correct reading.
  the inaccurate reading won't be added to the history.
  the rolling pointer to the history list reduces copy operations

  application: removing the wrong reading from MPU6050 when FIFO buffer overflows

  Rongzhong Li
  September 6, 2018

  The MIT License

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
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
