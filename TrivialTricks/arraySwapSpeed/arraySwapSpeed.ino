/*
  compare the different speed of array swapping mathods.

  application: check whether the comming command is different from the last one

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

void swapValue(char a[], char b[]) {
  char temp[10];
  strcpy(temp, a);
  strcpy(a, b);
  strcpy(b, temp);
}
void swapPtr(char * &a, char * &b) {//notice: not swapPtr(char * a, char * b) !!
  char *temp;
  temp = a;
  a = b;
  b = temp;
}
void setup() {
  Serial.begin(57600);
  char cmd[] = "hello";
  char lastCmd[] = "world";
  long prev = millis();
  for (long i = 0; i < 100000 - 1; i++) {
    char temp[10];
    strcpy(temp, cmd);
    strcpy(cmd, lastCmd);
    strcpy(lastCmd, temp);
  }
  PTL(millis() - prev);
  PTL(lastCmd);

  for (long i = 0; i < 100000 - 1; i++) {
    swapValue(cmd, lastCmd);
  }
  PTL(millis() - prev);
  PTL(lastCmd);

  char *cmdPtr = "hello";
  char *lastCmdPtr = "world";
  prev = millis();
  for (long i = 0; i < 100000 - 1 ; i++) {
    char *temp;
    temp = cmdPtr;
    cmdPtr = lastCmdPtr;
    lastCmdPtr = temp;
  }
  PTL(millis() - prev);
  PTL(lastCmdPtr);

  PT(cmdPtr);
  PT("\t");
  PTL(lastCmdPtr);
  prev = millis();
  for (long i = 0; i < 100000 - 1 ; i++) {
    swapPtr(cmdPtr, lastCmdPtr);
  }
  PTL(millis() - prev);
  PT(cmdPtr);
  PT("\t");
  PTL(lastCmdPtr);
}

void loop() {

}
