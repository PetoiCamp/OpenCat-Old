#define PT(s) Serial.print(s)  //makes life easier
#define PTL(s) Serial.println(s)
void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  delay(1);
  byte b = 5;
  byte*ptr = &b;
  byte *a[] = {&b, &b, &b};
  for (byte i = 0; i < 3; i++)
    PTL(*a[i]);
  PTL();
  b = 10;
  for (byte i = 0; i < 3; i++)
    PTL(*a[i]);
  byte c[] = {*ptr, *ptr, 3* *ptr};
  PTL();
  for (byte i = 0; i < 3; i++)
    PTL(c[i]);
  PTL();
  b = 7;
  for (byte i = 0; i < 3; i++)
    PTL(c[i]);
  PTL();
  *ptr = 11;
  PTL(b);
  for (byte i = 0; i < 3; i++)
    PTL(c[i]);
   

}

void loop() {
  // put your main code here, to run repeatedly:

}
