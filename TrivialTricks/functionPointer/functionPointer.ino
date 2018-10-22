/*
  use function pointer for similar function call with same arguments.

  application: reading from progmem and eeprom

  Rongzhong Li
  September 8, 2018

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
