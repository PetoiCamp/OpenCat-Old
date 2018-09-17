/*
  use function pointer for similar function call with same arguments.

  application: reading from progmem and eeprom

  Rongzhong Li
  September 8, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

#define FUNC_PTR
int add(int a, int b) {
  PT(a);
  PT('\t');
  PTL(b);
  return a + b;
}

int minus(int a, int b) {
  PT(a);
  PT('\t');
  PTL(b);
  return a - b;
}

void setup() {
  Serial.begin(57600);
# ifdef FUNC_PTR
  int (*calculate)(int, int);
  calculate = &add;
  PTL(calculate(2, 3));
  calculate = &minus;
  PTL(calculate(4, 3));
#else
  PTL(add(2, 3));
  PTL(minus(4, 3));
#endif
}

void loop() {

}
