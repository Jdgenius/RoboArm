
#include <Servo.h>

int values[4];  // Array to store parsed values
Servo servos[4];  // Array to store 4 servo objects
int servoPins[4] = {3, 6, 9, 10};  // Pins for each servo

void setup() {
    for (int i = 0; i < 4; i++) {
        servos[i].attach(servoPins[i]);  // Attach each servo to its pin
    }

    Serial.begin(9600);  // Start serial communication
    Serial.println("Enter four numbers (0-180) separated by commas:");
}

void loop() {
    if (Serial.available()) {
        String input = Serial.readStringUntil('\n');  // Read the entire line until newline
        parseInput(input);

        for (int i = 0; i < 4; i++) {
          servos[i].write(values[i]);
        }

    }
}

void parseInput(String input) {
    int index = 0;
    char *ptr;
    char inputBuffer[20];  // Buffer for parsing

    input.toCharArray(inputBuffer, sizeof(inputBuffer)); // Convert String to char array
    ptr = strtok(inputBuffer, ",");  // Tokenize by comma

    while (ptr != NULL && index < 4) {
        values[index] = atoi(ptr);  // Convert to integer

        if (values[index] < 0 || values[index] > 180) {  // Validate range
            Serial.println("Error: Values must be between 0 and 180");
            return;
        }
                // Print assigned values
        Serial.print("Received: ");
        Serial.print(values[index]); Serial.print(", ");

        ptr = strtok(NULL, ",");  // Get next token
        index++;
    }
    Serial.print("\n");
}
