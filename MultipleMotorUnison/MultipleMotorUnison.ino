// #include <Servo.h>

// Servo myServo;  // Create a servo object

// void setup() {
//     myServo.attach(3); // Attach the servo to pin 9
// }

// void loop() {
//     myServo.write(180);  // Move to 60 degrees
//     delay(2000);        // Wait 1 second
//     myServo.write(0);   // Move back to 0 degrees
//     delay(2000);        // Wait 1 second
// }

#include <Servo.h>

Servo servos[4];  // Array to store 4 servo objects
int servoPins[4] = {3, 6, 9, 10};  // Pins for each servo

void setup() {
    for (int i = 0; i < 4; i++) {
        servos[i].attach(servoPins[i]);  // Attach each servo to its pin
    }
}

void loop() {
    // Move from 180° to 0°
    for (int i = 0; i < 4; i++) {
        servos[i].write(180);
    }

    delay(1000);  // Smooth motion
    
    // Move from 0° to 180°
    // Move from 180° to 0°
    for (int i = 0; i < 4; i++) {
        servos[i].write(0);
    }
    delay(1000);  // Smooth motion

}
