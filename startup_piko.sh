#!/bin/sh
openbox --replace &
cd /opt/piko
xrandr -s 1024x768
python occ_test.py &
python main.py
killall python
