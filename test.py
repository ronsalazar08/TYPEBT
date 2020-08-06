#!/usr/bin/env python3
import serial
import time
import subprocess as sp
from pynput.keyboard import Key, Controller

keyboard = Controller()
while 1:
    try:
        ser = serial.Serial('/dev/rfcomm0', baudrate=9600)
        ser.flushInput()
        #def type():
        s = None
        while True: 
            s = str(ser.readline().decode().strip('\r\n'))
            s = s.upper()
            #print(s)
            keyboard.type(s)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
    except:
        sp.Popen(['python3','con.py'])
        sp.Popen(['python3','msgBox.py'])
        print("re-connecting")
        time.sleep(3)
        pass
        

