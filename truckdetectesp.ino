const int ledUphillGreen = 13;     // Uphill Green LED
const int ledUphillRed = 12;       // Uphill Red LED
const int ledDownhillGreen = 14;   // Downhill Green LED
const int ledDownhillRed = 27;     // Downhill Red LED

void setup() {
  Serial.begin(9600);  // Set baud rate (match with Python script)

  pinMode(ledUphillGreen, OUTPUT);
  pinMode(ledUphillRed, OUTPUT);
  pinMode(ledDownhillGreen, OUTPUT);
  pinMode(ledDownhillRed, OUTPUT);

  // Initially, assume no trucks — both greens ON
  digitalWrite(ledUphillGreen, HIGH);
  digitalWrite(ledUphillRed, LOW);
  digitalWrite(ledDownhillGreen, HIGH);
  digitalWrite(ledDownhillRed, LOW);
}

void loop() {
  if (Serial.available() > 0) {  // Check if data is received
    char receivedChar = Serial.read();  // Read one byte

    // Turn off all LEDs first
    digitalWrite(ledUphillGreen, LOW);
    digitalWrite(ledUphillRed, LOW);
    digitalWrite(ledDownhillGreen, LOW);
    digitalWrite(ledDownhillRed, LOW);

    if (receivedChar == '0') {
      // No truck detected: Uphill Green + Downhill Green ON
      digitalWrite(ledUphillGreen, HIGH);
      digitalWrite(ledDownhillGreen, HIGH);
      Serial.println("No truck detected: Uphill GREEN and Downhill GREEN ON");

    } else if (receivedChar == 'B') {
      // Both trucks detected: Uphill Green + Downhill Red ON
      digitalWrite(ledUphillGreen, HIGH);
      digitalWrite(ledDownhillRed, HIGH);
      Serial.println("Truck detected on both sides: Uphill GREEN and Downhill RED ON");

    } else if (receivedChar == 'U') {
      // Truck detected uphill: Uphill Green + Downhill Red ON
      digitalWrite(ledUphillGreen, HIGH);
      digitalWrite(ledDownhillRed, HIGH);
      Serial.println("Truck detected Uphill: Uphill GREEN and Downhill RED ON");

    } else if (receivedChar == 'D') {
      // Truck detected downhill: Uphill Red + Downhill Green ON
      digitalWrite(ledUphillRed, HIGH);
      digitalWrite(ledDownhillGreen, HIGH);
      Serial.println("Truck detected Downhill: Uphill RED and Downhill GREEN ON");
    }
  }
}
