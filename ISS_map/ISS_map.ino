
/*  Practicing learning how to read serial data
    This sketch should read serial imputs in the form "x,y"
    The new coordinates are compared against the list of existing coordinates,
    and if the new coordinates are new then the list of coordinates are updated
    For now the results are printed to the serial monitor.  Eventually the sketch
    will instead use the serial data to update a 16x8 LED matrix to show the
    position of the ISS
*/


int longlist[9];
int latlist[9];
int newlong = 0;
int newlat = 0;


void setup() {
  for (int i = 0; i < 10; i++) {
    longlist[i] = 0;
    latlist[i] = 0;
  }
  Serial.begin(9600);
  Serial.println("Arduino is read!");

}

void loop() {
  getcoords();
  updatecoords();
  displaymatrix();

}


void updatecoords() {
  //check if newest coordinate is different than most recent coordinate
  //then update lat/long list with new coordinates.

  if (newlong == longlist[0] || newlat == latlist[0]) {
    //not a new coordinate
  }
  else {
    //shifts matrix coordinates up one index, then assigns new current coordinate as index 0.
    for (int i = 9; i > 0; i--) {
      longlist[i] = longlist[i - 1];
    }
    longlist[0] = newlong;
    for (int i = 0; i > 0; i--) {
      latlist[i] = latlist[i - 1];
    }
    latlist[0] = newlat;
  }
}

void getcoords() {
  // if there is serial data available, read it:
  while (Serial.available() > 0) {
    //look for the next valid interger in the incoming serial stream:
    //Should be sent in the form "x,y"
    newlong = Serial.parseInt();
    newlat = Serial.parseInt();
  }
}

void displaymatrix() {
  // prints the current values for longist[i] and latlist[i]
  for (int i = 0; i < 10; i++) {
    Serial.print("index ");
    Serial.print(i);
    Serial.print(" ");
    Serial.print(longlist[i]);
    Serial.print(" ");
    Serial.println(latlist[i]);
  }
  Serial.println();

}















