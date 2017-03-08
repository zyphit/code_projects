import requests
import csv
import math
import time

url = "http://astroviewer-sat2a.appspot.com/orbit"
lastsave = 0
check_interval = 120
start_time = time.time()
step = 0

def ISSLATLONG():

# reads url and stuffs contents into a list
    with requests.Session() as s:
        download = s.get(url)
        decoded_conten = download.content.decode('utf-8')
        cr = csv.reader(decoded_conten.splitlines(), delimiter=',')
        my_list = list(cr)

# few steps to convert large list of strings into lat/long of ISS
    location = my_list[4]   #just the list index of interest
    location_str = ''.join(location)    #now it's a string.
    latlong = location_str.split(' ') # new list with space delimiters
    stn_lat = latlong[9]
    stn_long = latlong[7]
    print('The ISS is over ',stn_lat,' ',stn_long)


# raw lat/longs seema little out from what the source website is reporting
# my intended use for these numbers is okay with +/- 1 degree
# because I'll be plotting the station position in boxes of 13x22 degrees
# this script will eventually become a function that just returns the
# current lat/long of the station.

# now to convert lat/long to grid coordinates for 8x16 LED matrix

# convert -55 to +55 --> 0 to +110
    grid_lat = float(stn_lat) + 55
# divide by LED cell height, and round up for cell number.
    grid_y = math.ceil(grid_lat/13.75)

# convert -180 to + 180 --> 0 to +360
    grid_long = float(stn_long) + 180
# divide by LED cell weidth, and round up for cell number.
    grid_x = math.ceil(grid_long/22.5)

    print('Map grid ',grid_x,' ',grid_y)


# grid_y and grid_x to be reported to the arduino which will light
# up the corresponding LED.

# See about adding a timeout condition so that if the script is unable
# to access the url then another character is sent to the arduino
# and a "los telemetry" light is activated.

while 1:
    if time.time() - lastsave > check_interval:
        lastsave = time.time()
        if step == 0:
            print('This is the first measurement')
        else:
            print('Number of readings: ',step)
            print('Mission Time: ',(round((lastsave-start_time),1)/60),'minutes')
        step = step + 1
        ISSLATLONG()
        print()
