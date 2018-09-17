/*
  initializing array using constructor;

  Rongzhong Li
  September 16, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

#include<EEPROM.h>
void setup() {
  Serial.begin(57600);
  long a[6];
  for (byte i = 0; i < 6; i++)
    PTL(a[i]);
  PTL();
  long * b = new long[6](123);
  for (byte i = 0; i < 6; i++)
    PTL(b[i]);

}

void loop()
{

}


