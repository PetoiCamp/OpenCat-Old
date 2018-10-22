/*
  compare resource used with different implementation on array

  application: realtime change the value of a array with duplicated values

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

void printList(int arr[], int len) {
  for (int i = 0; i < len; i++) {
    PT(arr[i]);
    PT('\t');
  }
  PTL();
}
void printPtrList(int * arr[], int len) {
  for (int i = 0; i < len; i++) {
    PT(*(arr[i]));
    PT('\t');
  }
  PTL();
}

#define MACRO
#define REFERENCE

#ifdef MACRO
#define a 10
#define b 20
#define c 50
int arr[] = {a, b, c, b, c, a, c, a, b, a, b, c, a, b, c};
#else
#ifndef REFERENCE
int a = 10;
int  b = 20;
int c = 50;
int arr[] = {a, b, c, b, c, a, c, a, b, a, b, c, a, b, c};
#else
int a = 10;
int b = 20;
int c = 50;
int* arr[] = {&a, &b, &c, &b, &c, &a, &c, &a, &b, &a, &b, &c, &a, &b, &c};
#endif
#endif

void setup() {
  Serial.begin(57600);
#ifdef MACRO
  PTL("using macro!!");
  printList(arr, 9);
  //a=1;
  printList(arr, 9);
  PTL(freeMemory());
#else
#ifndef REFERENCE
  PTL("not reference");
  printList(arr, 9);
  a = 1;
  printList(arr, 9);
  PTL(freeMemory());
#else
  PTL("use reference");
  printPtrList(arr, 9);
  a = 1;
  printPtrList(arr, 9);
  PTL(freeMemory());
#endif
#endif
}
/*
  Output:

  9 elements

  Sketch uses 1994 bytes (6%) of program storage space. Maximum is 30720 bytes.
  Global variables use 224 bytes (10%) of dynamic memory
  using macro!!
  10  20  50  20  50  10  50  10  20
  10  20  50  20  50  10  50  10  20
  1818

  Sketch uses 2046 bytes (6%) of program storage space. Maximum is 30720 bytes.
  Global variables use 226 bytes (11%) of dynamic memory
  not reference
  10  20  50  20  50  10  50  10  20
  10  20  50  20  50  10  50  10  20
  1816

  Sketch uses 2016 bytes (6%) of program storage space. Maximum is 30720 bytes.
  Global variables use 230 bytes (11%) of dynamic memory
  use reference
  10  20  50  20  50  10  50  10  20
  1 20  50  20  50  1 50  1 20
  1812

  15 elements

  Sketch uses 2006 bytes (6%) of program storage space. Maximum is 30720 bytes.
  Global variables use 236 bytes (11%) of dynamic memory
  using macro!!
  10  20  50  20  50  10  50  10  20
  10  20  50  20  50  10  50  10  20
  1806

  Sketch uses 2070 bytes (6%) of program storage space. Maximum is 30720 bytes.
  Global variables use 238 bytes (11%) of dynamic memory
  not reference
  10  20  50  20  50  10  50  10  20
  10  20  50  20  50  10  50  10  20
  1804

  Sketch uses 2028 bytes (6%) of program storage space. Maximum is 30720 bytes.
  Global variables use 242 bytes (11%) of dynamic memory
  use reference
  10  20  50  20  50  10  50  10  20
  1 20  50  20  50  1 50  1 20
  1800

               program storage    SRAM
   Macro:           2xN           2xN
   variable:        4xN           2xN
   pointer:         2xN           2xN

    compare to Macro
                   program storage    SRAM
   variable:        +52,+64             +2
   pointer:         +22,+22             +6

   pointer array uses 4 more bytes than variable array

*/
void loop() {

}
