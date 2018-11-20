/*
  compare reading speed between colomn/row major array

  Rongzhong Li
  September DOF, 2018
*/

#include "MemoryFree.h"
#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)

#define N 120
#define DOF 8

void setup() {
  Serial.begin(57600);
  randomSeed(micros) ;
  byte arr[N];
  double sum = 0;
  for (int i = 0; i < N; i++) {
    arr[i] = random(5);
    PT(arr[i]);
  }
  PTL();
  long prev = micros();
  for (int l = 0; l < 100; l++)
    for (int t = 0; t < N / DOF; t++)
      for (int idx = 0; idx < DOF; idx++) {
        sum += arr[t * DOF + idx];
      }
  PT("time: ");
  PTL(micros() - prev);
  PT("\tsum: ");
  PTL(sum);

  sum = 0;
  prev = micros();
  for (int l = 0; l < 100; l++)
    for (int idx = 0; idx < DOF; idx++)
      for (int t = 0; t < N / DOF; t++)
      {
        sum += arr[t * DOF + idx];
      }
  PT("time: ");
  PTL(micros() - prev);
  PT("\tsum: ");
  PTL(sum);
  //-------------
  byte *ptr[DOF];
  for (int idx = 0; idx < DOF; idx++) {
    ptr[idx] = new byte[N / DOF];
    for (int t = 0; t < N / DOF; t++)
      ptr[idx][t] = arr[t * DOF + idx];
  }

  sum = 0;
  prev = micros();
  for (int l = 0; l < 100; l++)
    for (int idx = 0; idx < DOF; idx++)
      for (int t = 0; t < N / DOF; t++)
      {
        sum += ptr[idx][t];
      }
  PT("time: ");
  PTL(micros() - prev);
  PT("\tsum: ");
  PTL(sum);

  sum = 0;
  prev = micros();
  for (int l = 0; l < 100; l++)
    for (int t = 0; t < N / DOF; t++)
      for (int idx = 0; idx < DOF; idx++) {
        sum += ptr[idx][t];
      }
  PT("time: ");
  PTL(micros() - prev);
  PT("\tsum: ");
  PTL(sum);

  //-------------

  byte *ptrT[DOF];
  for (int t = 0; t < N / DOF; t++) {
    ptrT[t] = new byte[DOF];
    for (int idx = 0; idx < DOF; idx++)
      ptrT[t][idx] = arr[t * DOF + idx];
  }

  sum = 0;
  prev = micros();
  for (int l = 0; l < 100; l++)
    for (int idx = 0; idx < DOF; idx++)
      for (int t = 0; t < N / DOF; t++)
      {
        sum += ptrT[t][idx];
      }
  PT("time: ");
  PTL(micros() - prev);
  PT("\tsum: ");
  PTL(sum);

  sum = 0;
  prev = micros();
  for (int l = 0; l < 100; l++)
    for (int t = 0; t < N / DOF; t++)
      for (int idx = 0; idx < DOF; idx++) {
        sum += ptrT[t][idx];
      }
  PT("time: ");
  PTL(micros() - prev);
  PT("\tsum: ");
  PTL(sum);

}
void loop() {}


/*
   output:
time: 109311
  sum: 22800.00
time: 109278
  sum: 22800.00
time: 112227
  sum: 22800.00
time: 127425
  sum: 22800.00
time: 113919
  sum: 22800.00
time: 112281
  sum: 22800.00
*/

