#!/bin/sh
#start up script that is run when the PIKO desktop
#environment is selected at the login screen

openbox --replace &     #use openbox windowing engine over x11
cd /opt/piko    
xrandr -s 1024x768      #set monitor resolution
python occ_test.py &    #start occupancy sensor daemon listener
python main.py          #start kiosk application
killall python          #kill all scripts before exiting
