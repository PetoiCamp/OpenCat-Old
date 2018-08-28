/* credit to:
 * https://github.com/deviceai/arduino_sensors/blob/master/IRremote/ir_test_code.ino
 * 
 * Go to the library manager of Arduino IDE (instruction: https://www.arduino.cc/en/Guide/Libraries), 
 * search and install IRremote.
 * Rongzhong Li
 * August 2017
*/

#include "IRremote.h"

int receiver = 4; // Signal Pin of IR receiver to Arduino Pin 4

/*-----( Declare objects )-----*/
IRrecv irrecv(receiver);     // create instance of 'irrecv'
decode_results results;      // create instance of 'decode_results'

void setup()   /*----( SETUP: RUNS ONCE )----*/
{
  Serial.begin(57600);
  Serial.println("IR Receiver Button Decode");
  irrecv.enableIRIn(); // Start the receiver

}/*--(end setup )---*/


void loop()   /*----( LOOP: RUNS CONSTANTLY )----*/
{
  if (irrecv.decode(&results)) // have we received an IR signal?

  {
    translateIR();
    irrecv.resume(); // receive the next value
  }
}/* --(end main loop )-- */

/*-----( Function )-----*/
void translateIR() // takes action based on IR code received

// describing Remote IR codes

{

  switch (results.value)

  {

    case 0xFF629D: Serial.println(" FORWARD"); break;
    case 0xFF22DD: Serial.println(" LEFT");    break;
    case 0xFF02FD: Serial.println(" -OK-");    break;
    case 0xFFC23D: Serial.println(" RIGHT");   break;
    case 0xFFA857: Serial.println(" REVERSE"); break;
    case 0xFF6897: Serial.println(" 1");    break;
    case 0xFF9867: Serial.println(" 2");    break;
    case 0xFFB04F: Serial.println(" 3");    break;
    case 0xFF30CF: Serial.println(" 4");    break;
    case 0xFF18E7: Serial.println(" 5");    break;
    case 0xFF7A85: Serial.println(" 6");    break;
    case 0xFF10EF: Serial.println(" 7");    break;
    case 0xFF38C7: Serial.println(" 8");    break;
    case 0xFF5AA5: Serial.println(" 9");    break;
    case 0xFF42BD: Serial.println(" *");    break;
    case 0xFF4AB5: Serial.println(" 0");    break;
    case 0xFF52AD: Serial.println(" #");    break;
    case 0xFFFFFFFF: Serial.println(" REPEAT"); break;

    default:
      Serial.print("other button");

      Serial.print("\t");
      Serial.println(results.value, HEX);
  }// End Case

  delay(500); // Do not get immediate repeat


}
