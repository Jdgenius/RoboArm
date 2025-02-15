int val1, val2, val3, val4;

void setup() {
    Serial.begin(9600);  // Start serial communication
    Serial.println("Enter four numbers (0-180) separated by commas:");
}

void loop() {
    if (Serial.available()) {
        String input = Serial.readStringUntil('\n');  // Read the entire line until newline
        parseInput(input);
    }
}

void parseInput(String input) {
    int values[4];  // Array to store parsed values
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
        ptr = strtok(NULL, ",");  // Get next token
        index++;
    }

    if (index == 4) {  // Ensure exactly 4 values were received
        val1 = values[0];
        val2 = values[1];
        val3 = values[2];
        val4 = values[3];

        // Print assigned values
        Serial.print("Received: ");
        Serial.print(val1); Serial.print(", ");
        Serial.print(val2); Serial.print(", ");
        Serial.print(val3); Serial.print(", ");
        Serial.println(val4);
    } else {
        Serial.println("Error: Please enter exactly four numbers separated by commas.");
    }
}
