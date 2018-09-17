/*
  use of "define" in #if macro for multiple conditions

  Rongzhong Li
  September 8, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

#define a
//#define b

void setup() {
  Serial.begin(57600);
#if defined(a) && !defined(b)
  PTL("ab");
#endif
}

void loop() {

}
