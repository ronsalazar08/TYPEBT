#! /usr/bin/python3

import os
import time

os.system("sudo hcitool dc 00:18:E4:34:CC:ED")
time.sleep(1)
os.system("sudo rfcomm connect hci0 00:18:E4:34:CC:ED 1")

    
