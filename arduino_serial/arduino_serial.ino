// Serial sketch, read from serial port and blink LED according to the number that is transmitted over serial

/*
 * In python:
 * 
 * import serial
 * 
 * ser = serial.Serial('/dev/ttyUSB0', 9600)
 * 
 * ser.write('3'.encode('utf-8'))
 * 
 * You should get '3' blinks on the arduino.  Does not sanitize input for 1-9 only, watch out!
 */



const int LEDpin = 13;


void setup() {
  pinMode(LEDpin, OUTPUT);
  digitalWrite(LEDpin, LOW);

  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  for (int i = 1; i < 6; i++) { //blink 5 times for readiness.
    delay(250);
    digitalWrite(LEDpin, HIGH);
    delay(250);
    digitalWrite(LEDpin, LOW);
  }
}

void loop() {

  if(Serial.available()){
    blink(Serial.read() - '0');  //automagically converts the character '1'-'9' to decimal 1-9
  }
  delay(500);
}

void blink(int numberofTimes) {
  for (int i = 0; i < numberofTimes; i++) {
    digitalWrite(LEDpin, HIGH);
    delay(500);
    digitalWrite(LEDpin, LOW);
    delay(500);
  }
}

