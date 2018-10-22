/*
  compare speed and efficiency of multiple ways to update array elements

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
  byte c[] = {*ptr, *ptr, 3 * *ptr};
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
