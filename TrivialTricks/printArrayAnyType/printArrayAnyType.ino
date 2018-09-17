/*
  print array contents of any type

  Rongzhong Li
  September 16, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

template <typename T> void printList(T *arr, byte len = 16) {
  for (byte i = 0; i < len; i++) {
    PT((T)(arr[i]));
    PT('\t');
  }
  PTL();
}

void setup() {
  Serial.begin(57600);
  char a[3]={'a','b','c'};
  printList(a,3);
  double b[2]={1.3,4};
  printList(b,2);
  String c[3]={"hello","world"};
  printList(c,2);
 
}

void loop()
{

}


