#include "SoftwareSerial.h"
#include <AFMotor.h>

#define BT_RXD A0
#define BT_TXD A1
AF_DCMotor motor_L(3);
AF_DCMotor motor_R(4);
const int max_speed = 200;
const int min_speed = 100;


SoftwareSerial Bluetooth(BT_RXD, BT_TXD);
void setup()
{
  Serial.begin(9600);
  Bluetooth.begin(9600);
}
void loop()
{
  byte byte_count=Bluetooth.available();
  if(byte_count)
  {
    Serial.print("Connected!");
    char inData = Bluetooth.read();
    if (String(inData)== "s")
    { 
      Serial.println("********* Start Motor *********");
      motor_L.run(FORWARD);motor_R.run(FORWARD);
      motor_L.setSpeed(min_speed);motor_R.setSpeed(min_speed);
      delay(100);
    }
    else if (String(inData)== "u")
     {Serial.println("********* Up *********");
      motor_L.run(FORWARD);motor_R.run(FORWARD);
      motor_L.setSpeed(max_speed);motor_R.setSpeed(max_speed);
      delay(100);
     }
    else if (String(inData)== "d")
     {Serial.println("********* down *********");
      motor_L.run(BACKWARD);motor_R.run(BACKWARD);
      motor_L.setSpeed(max_speed);motor_R.setSpeed(max_speed);
      delay(100);
     }
    else if (String(inData)== "l")
     {Serial.println("********* Left *********");
      motor_L.run(BACKWARD);motor_R.run(FORWARD);
      motor_L.setSpeed(min_speed);motor_R.setSpeed(max_speed);
      delay(100);
     }
    else if (String(inData)== "r")
     {Serial.println("********* Riight *********");
      motor_L.run(FORWARD);motor_R.run(BACKWARD);
      motor_L.setSpeed(max_speed);motor_R.setSpeed(min_speed);
      delay(100);
     }
    else {Serial.println("********* Stop *********");
      motor_L.run(RELEASE);motor_R.run(RELEASE);
      delay(100);
    }
}
}
