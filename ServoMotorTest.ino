#include <Servo.h>  // Include the Servo library

Servo myServo;      // Create a servo object

void setup() {
  myServo.attach(3);  // Attach the servo to PWM pin 3
  //myServo.write(0);
}

void loop() {
  //Sweep from 0° to 180°
  for (int angle = 0; angle <= 60; angle++) {
    myServo.write(angle);  // Set servo position
    delay(15);             // Wait for the servo to reach the position
  }
  
  // Sweep back from 180° to 0°
  for (int angle = 60; angle >= 0; angle--) {
    myServo.write(angle);
    delay(15);
  }
  
}