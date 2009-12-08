#!/usr/bin/env python

import time
import os
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

last_sleeping = True

first_read = True

try:
   ret = hid_force_open(hid, 0, matcher, 3)
   if ret != HID_RET_SUCCESS:
      sys.stderr.write("hid_force_open failed with return code %d.\n" % ret)

   while 1:
      ret, bytes = hid_interrupt_read(hid, 0x81, 1, 1000)
      if ret != HID_RET_SUCCESS and ret != HID_RET_FAIL_INT_READ:
         sys.stderr.write("hid_interrupt_read failed with return code %d.\n" % ret)
      elif ret != HID_RET_FAIL_INT_READ:
         if first_read:
            first_read = False
         else:
            if bytes[0] == '\x01':
               os.system("xset dpms force off")
            else:
               os.system("xset dpms force on")
#         for byte in bytes:
#            print "%02x" % ord(byte),
#         if (len(bytes) > 0):
#            print ""
#         if bytes[0] == '\x01':
#            if last_sleeping == False:
#               os.system("xset dpms force off")
#         else:
#            if last_sleeping == True:
#               os.system("xset dpms force on")
#            if bytes[0] == '\x01':
#               last_sleeping = True
#            else:
#               last_sleeping = False

   ret = hid_close(hid)
   if ret != HID_RET_SUCCESS:
      sys.stderr.write("hid_close failed with return code %d.\n" % ret)
except KeyboardInterrupt:
   ret = hid_close(hid)
   if ret != HID_RET_SUCCESS:
      sys.stderr.write("hid_close failed with return code %d.\n" % ret)


hid_cleanup()

