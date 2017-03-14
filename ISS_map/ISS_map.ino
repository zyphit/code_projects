
/*  Practicing learning how to read serial data
    This sketch should read serial imputs in the form "x,y"
    The new coordinates are compared against the list of existing coordinates,
    and if the new coordinates are new then the list of coordinates are updated
    For now the results are printed to the serial monitor.  Eventually the sketch
    will instead use the serial data to update a 16x8 LED matrix to show the
    position of the ISS

#include <Wire.h>
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"
*/

int longlist[] = {0,0,0,0,0,0,0,0,0,0};
int latlist[] = {0,0,0,0,0,0,0,0,0,0};
int newlong = 0;
int newlat = 0;
const int LEDpin = 13;


void setup() {
  pinMode(LEDpin, OUTPUT);
  Serial.begin(9600);
  
  //matrix.begin(0x70);   //initialize LED matrix at 0x70 on HT16K33 LED matrix driver board
  
  for (int i = 0; i < 10; i++) {
    longlist[i] = i;
    latlist[i] = i;
    Serial.print(longlist[i]);
    Serial.print(" ");
    Serial.println(latlist[i]);
  }
 
  Serial.println("Arduino is ready!");

}

void loop() {
 getcoords();
 updatecoords();
 displaymatrix();
 //Serial.println("can you hear me now?");

}


void updatecoords() {
  //check if newest coordinate is different than most recent coordinate
  //then update lat/long list with new coordinates.

  if (newlong == longlist[0] && newlat == latlist[0]) {
    Serial.println("No new coordinates");
  }
  else {
    //shifts matrix coordinates up one index, then assigns new current coordinate as index 0.
    for (int i = 9; i > 0; i--) {
      longlist[i] = longlist[i - 1];
    }
    longlist[0] = newlong;
    for (int i = 9; i > 0; i--) {
      latlist[i] = latlist[i - 1];
    }
    latlist[0] = newlat;
    digitalWrite(LEDpin,HIGH);
    delay(250);
    digitalWrite(LEDpin,LOW);
  }
}

void getcoords() {
  // if there is serial data available, read it:
  while (Serial.available() > 0) {
    //look for the next valid interger in the incoming serial stream:
    //Should be sent in the form "x,y"
    Serial.println();
    newlong = Serial.parseInt();
    Serial.println(newlong);
    newlat = Serial.parseInt();
    Serial.println(newlat);
  }
}

void displaymatrix() {
  // prints the current values for longist[i] and latlist[i]
  Serial.println();
  for (int i = 0; i < 10; i++) {
    Serial.print("index ");
    Serial.print(i);
    Serial.print(" ");
    Serial.print(longlist[i]);
    Serial.print(" ");
    Serial.println(latlist[i]);
  }
  Serial.println();
    /*      In theory, this should illuminate the LEDs that correspond to the last ten ISS coordinates
            Needs testing!
 for (int i = 0; i < 10; i++){
     matrix.displaybuffer(longlist[i], latlist[i]);
 }
 matrix.writeDisplay();
 */
}


