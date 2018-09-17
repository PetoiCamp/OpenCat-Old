/*
  allocate array from a function call and keep the content using reference

  Rongzhong Li
  September 8, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

void newArrayRef(char * &a, int n) {
  a = new char[n];
  a[0] = 'h';
}

void newArray(char * a, int n) {
  a = new char[n];
  a[0] = 'h';
}
#include<EEPROM.h>
void setup() {
  Serial.begin(57600);
  char *a;
  newArray(a, 10);
  PTL((char)a[0]);
  newArrayRef(a, 10);
  PTL((char)a[0]);
}

void loop()
{

}


