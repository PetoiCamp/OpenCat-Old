/*
  compare the different speed of array swapping mathods.

  application: check whether the comming command is different from the last one
  
  Rongzhong Li
  September 8, 2018
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
