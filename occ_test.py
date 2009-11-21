#!/usr/bin/env python

import time
import sys
from hid import *

def int32(x):
   if x>0xFFFFFFFF:
      raise OverflowError
   if x>0x7FFFFFFF:
      x=int(0x100000000-x)
   if x<2147483648:
      return -x
   else:
      return -2147483648
   return x

ret = hid_init()
if ret != HID_RET_SUCCESS:
   sys.stderr.write("hid_init failed with return code %d.\n" % ret)

hid = hid_new_HIDInterface()
matcher = HIDInterfaceMatcher()

matcher.vendor_id = 0x03eb
matcher.product_id = 0x204f

last_sleeping = False

try:
   ret = hid_force_open(hid, 0, matcher, 3)
   if ret != HID_RET_SUCCESS:
      sys.stderr.write("hid_force_open failed with return code %d.\n" % ret)

   while 1:
      ret, bytes = hid_get_input_report(hid, (int32(0xff9c0001), int32(0xff9c0002)), 1)
      if ret != HID_RET_SUCCESS:
         sys.stderr.write("hid_get_input_report failed with return code %d.\n" % ret)
      else:
         if bytes[0] == '\x01':
            print "sleeping"
            if last_sleeping == False:
               os.system("xset dpms force off")
         else:
            if last_sleeping == True:
               os.system("xset dpms force on")
            print "awake"

         if bytes[0] == '\x01':
            last_sleeping = True
         else:
            last_sleeping = False
      time.sleep(5)

   ret = hid_close(hid)
   if ret != HID_RET_SUCCESS:
      sys.stderr.write("hid_close failed with return code %d.\n" % ret)
except KeyboardInterrupt:
   ret = hid_close(hid)
   if ret != HID_RET_SUCCESS:
      sys.stderr.write("hid_close failed with return code %d.\n" % ret)


hid_cleanup()

