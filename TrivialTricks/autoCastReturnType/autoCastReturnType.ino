/*
  auto cast to return type
  
  Rongzhong Li
  September 8, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

char a() {
  byte x = 85;
  return x;
}

char b() {
  byte x = 85;
  return (char)x;
}
void setup() {
  Serial.begin(57600);
  PTL(a());
  PTL(b());
}

void loop()
{

}


