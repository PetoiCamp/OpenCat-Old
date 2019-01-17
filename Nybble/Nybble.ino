/* Main Arduino sketch for Nybble, the walking robot kitten.
   Updates should be posted on GitHub: https://github.com/PetoiCamp/OpenCat

   Rongzhong Li
   Aug. 27, 2018
   Copyright (c) 2018 Petoi LLC.

   This sketch may also includes others' codes under MIT or other open source liscence.
   Check those liscences in corresponding module test folders.
   Feel free to contact us if you find any missing references.

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
#define MAIN_SKETCH
#include <MemoryFree.h>
#include "WriteInstinct/OpenCat.h"

#include <I2Cdev.h>
#include <MPU6050_6Axis_MotionApps20.h>


#define PACKET_SIZE 42
#define OVERFLOW_THRESHOLD 128

//#if OVERFLOW_THRESHOLD>1024-1024%PACKET_SIZE-1   // when using (1024-1024%PACKET_SIZE) as the overflow resetThreshold, the packet buffer may be broken
// and the reading will be unpredictable. it should be replaced with previous reading to avoid jumping
#define FIX_OVERFLOW
//#endif
#define HISTORY 2
int8_t lag = 0;
float ypr[3];         // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector
float yprLag[HISTORY][2];

MPU6050 mpu;
#define OUTPUT_READABLE_YAWPITCHROLL
// MPU control/status vars
bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[PACKET_SIZE]; // FIFO storage buffer

// orientation/motion vars
Quaternion q;           // [w, x, y, z]         quaternion container
VectorFloat gravity;    // [x, y, z]            gravity vector

// ================================================================
// ===               INTERRUPT DETECTION ROUTINE                ===
// ================================================================

volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
  mpuInterrupt = true;
}

// https://brainy-bits.com/blogs/tutorials/ir-remote-arduino
#include <IRremote.h>

/*-----( Declare objects )-----*/
IRrecv irrecv(IR_RECIEVER);     // create instance of 'irrecv'
decode_results results;      // create instance of 'decode_results'
String translateIR() // takes action based on IR code received
// describing Remote IR codes.
{
  switch (results.value) { //why the program is printing the IR key twice? //Rz's note
    //IR signal    key on IR remote       //abbreviation of gaits   //gait/posture names
    case 0xFFA25D: PTLF(" CH-");          return (F("sit"));
    case 0xFF629D: PTLF(" CH");           return (F("d"));          //shutdown all servos
    case 0xFFE21D: PTLF(" CH+");          return (F("balance"));    //neutral standing


    case 0xFF22DD: PTLF(" |<<");          return (F("rc"));         //recover (turtle roll )
    case 0xFF02FD: PTLF(" >>|");          return (F("pu"));         // push up
    case 0xFFC23D: PTLF(" >||");          return (F("str"));        //stretch

    case 0xFFE01F: PTLF(" -");            return (F("buttUp"));     //butt up
    case 0xFFA857: PTLF(" +");            return (F("ly"));         //lay down crawling
    case 0xFF906F: PTLF(" EQ");           return (F("pee"));        //stand on three feet

    case 0xFF6897: PTLF(" 0");            return (F("trL"));        //trot left
    case 0xFF9867: PTLF(" 100+");         return (F("tr"));         //trot fast/run
    case 0xFFB04F: PTLF(" 200+");         return (F("trR"));        //trot right

    case 0xFF30CF: PTLF(" 1");            return (F("crL"));        //crawl left
    case 0xFF18E7: PTLF(" 2");            return (F("cr"));         //crawl fast
    case 0xFF7A85: PTLF(" 3");            return (F("crR"));        //crawl right

    case 0xFF10EF: PTLF(" 4");            return (F("bkL"));        // back left
    case 0xFF38C7: PTLF(" 5");            return (F("bk"));         //back
    case 0xFF5AA5: PTLF(" 6");            return (F("bkR"));        //back right

    case 0xFF42BD: PTLF(" 7");            return (F("calib"));      //calibration posture
    case 0xFF4AB5: PTLF(" 8");            return (F("zero"));       //customed skill
    case 0xFF52AD: PTLF(" 9");            return (F("zero"));       //customed skill

    case 0xFFFFFFFF: return (""); //Serial.println(" REPEAT");

    default: {
        Serial.println(results.value, HEX);
      }
      return ("");                      //Serial.println("null");
  }// End Case
  //delay(100); // Do not get immediate repeat //no need because the main loop is slow

  // The control could be organized in another way, such as:
  // forward/backward to change the gaits corresponding to different speeds.
  // left/right key for turning left and right
  // number keys for different postures or behaviors
}


char token;
#define CMD_LEN 10
char *lastCmd = new char[CMD_LEN];
char *newCmd = new char[CMD_LEN];
byte newCmdIdx = 0;
byte hold = 0;

uint8_t timer = 0;
//#define SKIP 1
#ifdef SKIP
byte updateFrame = 0;
#endif
byte firstWalkingJoint;
byte jointIdx = 0;


unsigned long usedTime = 0;

void checkBodyMotion()  {
  if (!dmpReady) return;
  // wait for MPU interrupt or extra packet(s) available
  //while (!mpuInterrupt && fifoCount < packetSize) ;
  if (mpuInterrupt || fifoCount >= packetSize)
  {
    // reset interrupt flag and get INT_STATUS byte
    mpuInterrupt = false;
    mpuIntStatus = mpu.getIntStatus();

    // get current FIFO count
    fifoCount = mpu.getFIFOCount();
    //PTL(fifoCount);
    // check for overflow (this should never happen unless our code is too inefficient)
    if ((mpuIntStatus & 0x10) || fifoCount > OVERFLOW_THRESHOLD) { //1024) {
      // reset so we can continue cleanly
      mpu.resetFIFO();
      // otherwise, check for DMP data ready interrupt (this should happen frequently)

      // -- RzLi --
#ifdef FIX_OVERFLOW
      PTLF("FIFO overflow! Using last reading!");
      lag = (lag - 1 + HISTORY) % HISTORY;
#endif
      // --
    }
    else if (mpuIntStatus & 0x02) {
      // wait for correct available data length, should be a VERY short wait
      while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();

      // read a packet from FIFO
      mpu.getFIFOBytes(fifoBuffer, packetSize);

      // track FIFO count here in case there is > 1 packet available
      // (this lets us immediately read more without waiting for an interrupt)
      fifoCount -= packetSize;

#ifdef OUTPUT_READABLE_YAWPITCHROLL
      // display Euler angles in degrees
      mpu.dmpGetQuaternion(&q, fifoBuffer);
      mpu.dmpGetGravity(&gravity, &q);
      mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
#ifdef MPU_YAW180
      ypr[2] = -ypr[2];
#else
      ypr[1] = -ypr[1] ;
#endif
#endif
      /*PT(ypr[1] * degPerRad);
        PTF("\t");
        PTL(ypr[2] * degPerRad);*/
      // overflow is detected after the ypr is read. it's necessary to keep a lag recrod of previous reading.  -- RzLi --
#ifdef FIX_OVERFLOW
      for (byte g = 0; g < 2; g++) {
        yprLag[lag][g] = ypr[g + 1] * degPerRad;
        ypr[g + 1] = yprLag[(lag - 1 + HISTORY) % HISTORY][g] * radPerDeg;
      }
      lag = (lag + 1) % HISTORY;
#endif
      // --
      //deal with accidents
      if (fabs(ypr[1])*degPerRad > LARGE_PITCH) {
        PT(ypr[1] * degPerRad);
        PTF("\t");
        PTL(ypr[2] * degPerRad);
        if (!hold) {
          token = 'k';
          strcpy(newCmd, ypr[1]*degPerRad > LARGE_PITCH ? "lifted" : "dropped");
          newCmdIdx = 1;
        }
        hold = 10;
      }
      // recover
      else if (hold) {
        if (hold == 10) {
          token = 'k';
          strcpy(newCmd, "balance");
          newCmdIdx = 1;
        }
        hold --;
        if (!hold) {
          char temp[CMD_LEN];
          strcpy(temp, newCmd);
          strcpy(newCmd, lastCmd);
          strcpy(lastCmd, temp);
          newCmdIdx = 1;
          meow();
        }
      }
      //calculate deviation
      for (byte i = 0; i < 2; i++) {
        RollPitchDeviation[i] = ypr[2 - i] * degPerRad - motion.expectedRollPitch[i];
        RollPitchDeviation[i] = sign(ypr[2 - i]) * max(fabs(RollPitchDeviation[i]) - levelTolerance[i], 0);//filter out small angles
      }
    }
  }
}

void setup() {
  // join I2C bus (I2Cdev library doesn't do this automatically)
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
  Wire.begin();
  //Wire.setClock(400000);
  TWBR = 24; // 400kHz I2C clock (200kHz if CPU is 8MHz)
#elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
  Fastwire::setup(400, true);
#endif

  Serial.begin(57600);
  Serial.setTimeout(10);
  while (!Serial);
  // wait for ready
  while (Serial.available() && Serial.read()); // empty buffer
  delay(100);
  PTLF("\n* Starting *");
  PTLF("Initializing I2C");
  PTLF("Connecting MPU6050...");
  mpu.initialize();
  //do
  {
    delay(1000);
    // verify connection
    PTLF("Testing connections...");
    PTL(mpu.testConnection() ? F("MPU successful") : F("MPU failed"));//sometimes it shows "failed" but is ok to bypass.
  } //while (!mpu.testConnection());

  // load and configure the DMP
  do {
    PTLF("Initializing DMP...");
    devStatus = mpu.dmpInitialize();
    // supply your own gyro offsets here, scaled for min sensitivity

    for (byte i = 0; i < 4; i++) {
      PT(EEPROMReadInt(MPUCALIB + 4 + i * 2));
      PT(" ");
    }
    PTL();
    mpu.setZAccelOffset(EEPROMReadInt(MPUCALIB + 4));
    mpu.setXGyroOffset(EEPROMReadInt(MPUCALIB + 6));
    mpu.setYGyroOffset(EEPROMReadInt(MPUCALIB + 8));
    mpu.setZGyroOffset(EEPROMReadInt(MPUCALIB + 10));
    // make sure it worked (returns 0 if so)
    if (devStatus == 0) {
      // turn on the DMP, now that it's ready
      PTLF("Enabling DMP...");
      mpu.setDMPEnabled(true);

      // enable Arduino interrupt detection
      PTLF("Enabling interrupt detection");
      attachInterrupt(0, dmpDataReady, RISING);
      mpuIntStatus = mpu.getIntStatus();

      // set our DMP Ready flag so the main loop() function knows it's okay to use it
      PTLF("DMP ready!");
      dmpReady = true;

      // get expected DMP packet size for later comparison
      packetSize = mpu.dmpGetFIFOPacketSize();
    } else {
      // ERROR!
      // 1 = initial memory load failed
      // 2 = DMP configuration updates failed
      // (if it's going to break, usually the code will be 1)
      PTLF("DMP failed (code ");
      PT(devStatus);
      PTLF(")");
      PTL();
    }
  } while (devStatus);

  //opening music
#if WalkingDOF == 8
  pinMode(BUZZER, OUTPUT);
  playMelody(MELODY);
#endif

  //IR
  {
    //PTLF("IR Receiver Button Decode");
    irrecv.enableIRIn(); // Start the receiver
  }

  assignSkillAddressToOnboardEeprom();
  PTL();

  // servo
  { pwm.begin();

    pwm.setPWMFreq(60 * PWM_FACTOR); // Analog servos run at ~60 Hz updates
    delay(200);

    //meow();
    strcpy(lastCmd, "rest");
    motion.loadBySkillName("rest");
    for (int8_t i = DOF - 1; i >= 0; i--) {
      pulsePerDegree[i] = float(PWM_RANGE) / servoAngleRange(i);
      servoCalibs[i] = servoCalib(i);
      calibratedDuty0[i] =  SERVOMIN + PWM_RANGE / 2 + float(middleShift(i) + servoCalibs[i]) * pulsePerDegree[i]  * rotationDirection(i) ;
      //PTL(SERVOMIN + PWM_RANGE / 2 + float(middleShift(i) + servoCalibs[i]) * pulsePerDegree[i] * rotationDirection(i) );
      calibratedPWM(i, motion.dutyAngles[i]);
      delay(100);
    }
    randomSeed(analogRead(0));//use the fluctuation of voltage caused by servos as entropy pool
    shutServos();
    token = 'd';
  }
  beep(30);

  pinMode(BATT, INPUT);
  pinMode(VCC, OUTPUT);
  pinMode(TRIGGER, OUTPUT); // Sets the trigPin as an Output
  pinMode(ECHO, INPUT); // Sets the echoPin as an Input
  digitalWrite(VCC, HIGH);
  int t = 0;
  int minDist, maxDist;
  while (0) {//disabled for now. needs virtual threading to reduce lag in motion.
    calibratedPWM(0, -10 * cos(t++*M_PI / 360));
    calibratedPWM(1, 10 * sin(t++ * 2 * M_PI / 360));
    digitalWrite(TRIGGER, LOW);
    delayMicroseconds(2);

    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(TRIGGER, HIGH);
    digitalWrite(BUZZER, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER, LOW);
    digitalWrite(BUZZER, LOW);

    // Reads the echoPin, returns the sound wave travel time in microseconds

    long duration = pulseIn(ECHO, HIGH, farTime);

    // Calculating the distance

    int distance = duration * 0.034 / 2; // 10^-6 * 34000 cm/s

    // Prints the distance on the Serial Monitor
    Serial.print("Distance: ");
    Serial.print(distance == 0 ? LONGEST_DISTANCE : distance);
    Serial.println(" cm");
  }
  meow();
}

void loop() {

  newCmd[0] = '\0';
  newCmdIdx = 0;
  // MPU block
#ifdef GYRO
  checkBodyMotion();
#endif
  // accident block
  //...
  //...
  //for obstacle avoidance and auto recovery

  // input block
  //else if (t == 0) {
  if (irrecv.decode(&results)) {
    if (translateIR() != "") {
      strcpy(newCmd, translateIR().c_str());
      if (!strcmp(newCmd, "d"))
        token = 'd';
      else if (!strcmp(newCmd, "rc")) {
        char **bList = new char*[10];
        bList[0] = "rc1";
        bList[1] = "rc2";
        bList[2] = "rc3";
        bList[3] = "rc4";
        bList[4] = "rc5";
        bList[5] = "rc6";
        bList[6] = "rc7";
        bList[7] = "rc8";
        bList[8] = "rc9";
        bList[9] = "rc10";
        float speedRatio[10] = {2, 2, 2, 10, 5, 10, 5, 5, 5, 2};
        int pause[10] = {500, 500, 500, 0, 0, 0, 0, 0, 500, 100};
        behavior( 10, bList, speedRatio, pause);
        strcpy(newCmd, "rest");

      }
      else if (!strcmp(newCmd, "pu")) {
        char **bList = new char*[2];
        bList[0] = "pu1";
        bList[1] = "pu2";
        float speedRatio[2] = {2, 2};
        int pause[2] = {0, 0};
        for (byte i = 0; i < 3; i++)
          behavior(2, bList, speedRatio, pause);
        strcpy(newCmd, "rest");
        meow();

      }
      else
        token = 'k';
      newCmdIdx = 2;
    }
    irrecv.resume(); // receive the next value
  }
  if ( Serial.available() > 0) {
    token = Serial.read();
    newCmdIdx = 3;
  }
  //}
  if (newCmdIdx) {
    PTL(token);
    beep(newCmdIdx * 4);
    // this block handles argumentless tokens
    if (token == 'h')
      PTLF("** Help Information **");// print the help document
    else if (token == 'd' ) {
      motion.loadBySkillName("rest");
      transform( motion.dutyAngles);
      PTLF("shut down servos");
      shutServos();
    }
    else if (token == 's') {
      PTLF("save calibration");
      saveCalib(servoCalibs);
    }
    else if (token == 'a') {
      PTLF("abort calibration");
      for (byte i = 0; i < DOF; i++) {
        servoCalibs[i] = servoCalib( i);
      }
    }
    // this block handles array like arguments
    else if (token == 'l' ) {
      byte len = Serial.read();
      PT(len);
      //        //PTLF("receiving 16 angle list in binary [ byte, ..., byte ] ");

      char *inBuffer = new char[len];
      //
      for (byte i = 0; i < len; i++) {
        inBuffer[i] = Serial.read();
        PT(inBuffer[i]);
        PTL();
      }
      if (len == DOF)
        allCalibratedPWM(inBuffer);
      else
        for (byte i = 0; i < len / 2; i++)
          calibratedPWM(inBuffer[i * 2], inBuffer[i * 2 + 1]);
      //          Serial.readBytes(inBuffer, DOF);
      //          //allCalibratedPWM(dutyAng+1);
      //          delay(200);
      //
      delete [] inBuffer;
    }
    else if (token == 'c' || token == 'm') {
      int8_t target[2] = {};
      String inBuffer = Serial.readStringUntil('\n');
      byte inLen = 0;
      strcpy(newCmd, inBuffer.c_str());
      char *pch;
      pch = strtok (newCmd, " ,");
      for (byte c = 0; pch != NULL; c++)
      {
        target[c] = atoi(pch);
        pch = strtok (NULL, " ,");
        inLen++;
      }

      if (token == 'c') {
        //PTLF("calibrating [ targetIdx, angle ]: ");
        if (strcmp(lastCmd, "c")) { //first time entering the calibration function
          motion.loadBySkillName("calib");
          transform( motion.dutyAngles);
        }
        if (inLen == 2)
          servoCalibs[target[0]] = target[1];
        PTL();
        for (byte i = 0; i < DOF; i++) {
          PT(i);
          PT(",\t");
        }
        PTL();
        printList(servoCalibs);
        yield();

      }
      else if (token == 'm') {
        //SPF("moving [ targetIdx, angle ]: ");
        motion.dutyAngles[target[0]] = target[1];
      }
      PT(token);
      printList(target, 2);

      int duty = SERVOMIN + PWM_RANGE / 2 + float(middleShift(target[0])  + servoCalibs[target[0]] + motion.dutyAngles[target[0]]) * pulsePerDegree[target[0]] * rotationDirection(target[0]);
      pwm.setPWM(pin(target[0]), 0,  duty);
    }

    else if (Serial.available() > 0) {
      String inBuffer = Serial.readStringUntil('\n');
      strcpy(newCmd, inBuffer.c_str());
    }
    while (Serial.available() && Serial.read()); //flush the remaining serial buffer in case the commands are parsed incorrectly
    //check above
    if (strcmp(newCmd, "") && strcmp(newCmd, lastCmd) ) {
      //      PT("compare lastCmd ");
      //      PT(lastCmd);
      //      PT(" with newCmd ");
      //      PT(token);
      //      PT(newCmd);
      //      PT("\n");
      if (token == 'w') {}; //some words for undefined behaviors

      if (token == 'k') { //validating key

        motion.loadBySkillName(newCmd);
        //motion.info();
        timer = 0;
        if (strcmp(newCmd, "balance") && strcmp(newCmd, "lifted") && strcmp(newCmd, "dropped") )
          strcpy(lastCmd, newCmd);
        // if posture, start jointIdx from 0
        // if gait, walking DOF = 8, start jointIdx from 8
        //          walking DOF = 12, start jointIdx from 4
        firstWalkingJoint = (motion.period == 1) ? 0 : DOF - WalkingDOF;
        postureOrWalkingFactor = (motion.period == 1 ? 1 : POSTURE_WALKING_FACTOR);
        jointIdx = firstWalkingJoint;
        transform( motion.dutyAngles,  1, firstWalkingJoint);

        if (!strcmp(newCmd, "rest")) {
          shutServos();
          token = 'd';
        }
      }
      else {
        lastCmd[0] = token;
        memset(lastCmd + 1, '\0', CMD_LEN - 1);
      }
    }
  }

  //motion block
  {
    if (token == 'k') {
#ifndef HEAD  //skip head
      if (jointIdx < 2)
        jointIdx = 2;
#endif

#ifndef TAIL  //skip tail
      if (jointIdx < 4)
        jointIdx = 4;
#endif
      if (jointIdx < firstWalkingJoint && motion.period > 1) {
        calibratedPWM(jointIdx, 0
#ifdef GYRO
                      + adjust(jointIdx)
#endif
                     );
      }
      else if (jointIdx >= firstWalkingJoint) {
        int dutyIdx = timer * WalkingDOF + jointIdx - firstWalkingJoint;
        calibratedPWM(jointIdx, motion.dutyAngles[dutyIdx]
#ifdef GYRO
                      + adjust(jointIdx)
#endif
                     );
      }
      jointIdx++;

      if (jointIdx == DOF) {
        jointIdx = 0;
        //PTL((float)analogRead(BATT) *  5.0 / 1024.0*3);
#ifdef SKIP
        if (updateFrame++ == SKIP) {
          updateFrame = 0;
#endif
          timer = (timer + 1) % motion.period;
#ifdef SKIP
        }
#endif
      }
    }
  }
}
