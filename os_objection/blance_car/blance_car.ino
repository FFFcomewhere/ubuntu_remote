#include <PID_v1.h>
#include "Wire.h"
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"
MPU6050 mpu(0x68);

#define center  0x7F

//蓝牙名字 cking616
//蓝牙密码 1234

char flag=0;
char num=0;
double time;
signed int speeds = 0;
signed int oldspeed =0;
byte inByte ;
// MPU control/status vars
bool dmpReady = false;   
uint8_t mpuIntStatus;
uint8_t devStatus;   
uint16_t packetSize;   
uint16_t fifoCount;   
uint8_t fifoBuffer[64];  

signed int speedcount=0;

// orientation/motion vars
Quaternion q;           // [w, x, y, z]         quaternion container
VectorFloat gravity;    // [x, y, z]            gravity vector
float ypr[3];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector
float angle;
double Setpoint, Input, Output;
double kp = 8.8,ki = 5.0,kd = 0.29;//需要你修改的参数

double Setpoints, Inputs, Outputs;
double sp = 0.8,si = 0,sd = 0.22;//需要你修改的参数

unsigned char dl=17,count;

union{
        signed int all;
        unsigned char s[2];
}data;
  

volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
  mpuInterrupt = true;
}
PID myPID(&Input, &Output, &Setpoint,kp,ki,kd, DIRECT);

PID sPID(&Inputs, &Outputs, &Setpoints,sp,si,sd, DIRECT);

void motor(int v)
{
  if(v>0)
  {
    v+=dl;
    digitalWrite(6,0);
    digitalWrite(7,1);
    digitalWrite(8,1);
    digitalWrite(9,0);   
    analogWrite(10,v);
    analogWrite(11,v);
  }
  else if(v<0)
  {
    v=-v;
    v+=dl;
    digitalWrite(6,1);
    digitalWrite(7,0);
    digitalWrite(8,0);
    digitalWrite(9,1);   
    analogWrite(10,v);
    analogWrite(11,v);
  }
  else
  {
    analogWrite(10,0);
    analogWrite(11,0);  
  }
}

void motort(int v)
{
  if(v>0)
  {
    v+=dl;
    digitalWrite(8,1);
    digitalWrite(9,0);
    analogWrite(10,v);
  }
  else if(v<0)
  {
    v=-v;
    v+=dl;
    digitalWrite(8,0);
    digitalWrite(9,1);  
    analogWrite(10,v);
  }
  else
  {
    analogWrite(10,0);
  }
}

void setup()
{
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  digitalWrite(6,0);
  digitalWrite(7,1);
  digitalWrite(8,1);
  digitalWrite(9,0);
  analogWrite(10,0);
  analogWrite(11,0);
  Serial.begin(9600);
  Wire.begin();

  delay(100);
  
  Serial.println("Initializing I2C devices...");
  mpu.initialize();
  Serial.println("Testing device connections...");
  Serial.println(mpu.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");
  delay(2);
  Serial.println("Initializing DMP...");
  devStatus = mpu.dmpInitialize();
  if (devStatus == 0)
  {
    Serial.println("Enabling DMP...");
    mpu.setDMPEnabled(true);
    Serial.println("Enabling interrupt detection (Arduino external interrupt 0)...");
    attachInterrupt(0, dmpDataReady, RISING);
    mpuIntStatus = mpu.getIntStatus();
    Serial.println("DMP ready! Waiting for first interrupt...");
    dmpReady = true;
    packetSize = mpu.dmpGetFIFOPacketSize();
  }
  else
  {
    Serial.print("DMP Initialization failed (code ");
    Serial.print(devStatus);
    Serial.println(")");
  }
  
  Setpoint = 22.0;
  myPID.SetTunings(kp,ki,kd);
  myPID.SetOutputLimits(-255+dl,255-dl);
  myPID.SetSampleTime(5);
  myPID.SetMode(AUTOMATIC);

  sPID.SetTunings(sp,si,sd);
  sPID.SetOutputLimits(-10,70);
  sPID.SetSampleTime(200);
  sPID.SetMode(AUTOMATIC);


  attachInterrupt(1,speed,RISING);
}

void loop()
{
  if (!dmpReady)
    return;
  // wait for MPU interrupt or extra packet(s) available
  if (!mpuInterrupt && fifoCount < packetSize)
    return;
  mpuInterrupt = false;
  mpuIntStatus = mpu.getIntStatus();
  fifoCount = mpu.getFIFOCount();
  if ((mpuIntStatus & 0x10) || fifoCount == 1024)
  {
   mpu.resetFIFO();
  }
  else if (mpuIntStatus & 0x02)
  {
     while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();
     mpu.getFIFOBytes(fifoBuffer, packetSize);
     fifoCount -= packetSize;
     mpu.dmpGetQuaternion(&q, fifoBuffer);
     mpu.dmpGetGravity(&gravity, &q);
     mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);  //从DMP中取出Yaw、Pitch、Roll三个轴的角度，放入数组ypr。单位：弧度
     angle=-ypr[1] * 180/M_PI;
  }


  Inputs = speedcount;
   sPID.Compute();

    Setpoint = 22.0+Outputs;

  Input = angle;
  myPID.Compute();
  
  if(angle>60||angle<0)
  Output=0;
  if(flag)
  {
  motort(Output);
  flag=0;
  }
  else {
        motor(Output);
        
  }
  
  if (Serial.available() > 0) {
    inByte = Serial.read();
  }
  if(inByte == 'w'){
  kp+=0.5;}
  else if(inByte == 'q'){
  kp-=0.5;}
  else if(inByte == 'r'){
  ki+=10;}
  else if(inByte == 'e'){
  ki-=10;}
  else if(inByte == 'y'){
  kd+=0.01;}
  else if(inByte == 't'){
  kd-=0.01;}
  else if(inByte == 'i'){
  dl+=1;}
  else if(inByte == 'u'){
  dl-=1;}
  else if(inByte == 's'){
  sp+=0.1;}
  else if(inByte == 'a'){
  sp-=0.1;}
   else if(inByte == 'f'){
  si+=1;}
  else if(inByte == 'd'){
  si-=1;}
   else if(inByte == 'h'){
  sd+=0.01;}
  else if(inByte == 'g'){
  sd-=0.01;}
  else if(inByte == 'v'){
  Setpoints+=2;}
  else if(inByte == 'b'){
  Setpoints-=2;}
  else if(inByte == 'n'){
  Setpoints+=2;
  flag=1;}
  else if(inByte == 'm'){
  Setpoints-=2;
  flag=1;}

  inByte='x';

  sPID.SetTunings(sp,si,sd);  
  myPID.SetTunings(kp,ki,kd);  

  num++;
  if(num==20)
  {num=0;
  Serial.print(kp);
  Serial.print(',');
  Serial.print(ki);
  Serial.print(',');
  Serial.print(kd);
  Serial.print(',');
  Serial.print(dl);
  Serial.print("  ");
  Serial.print(sp);
  Serial.print(',');
  Serial.print(si);
  Serial.print(',');
  Serial.print(sd);
   Serial.print(',');
  Serial.println(angle);
  }

}



void speed()
{
        if(digitalRead(6)){
        speedcount+=1;
        }
        else
        speedcount-=1;
}
