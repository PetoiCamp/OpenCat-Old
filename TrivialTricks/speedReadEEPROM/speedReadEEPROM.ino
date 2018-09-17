/*
  speed of EEPROM reading

  Rongzhong Li
  September 8, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

#include<EEPROM.h>
void setup() {
  Serial.begin(57600);
  long x = 0;
  long prev = millis();
  for (int i = 0; i < 1000; i++)
    x += EEPROM.read(i);
  PTL(millis() - prev);
  PTL(x);
}

void loop()
{

}


