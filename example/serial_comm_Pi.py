#!/usr/bin/python
''' RPi and Pico Communication'''
import serial
from time import sleep

ser = serial.Serial("/dev/ttyS0", 9600)

print("Starting UART COMM...")
ser.write(b"Hello Pico!")

try:
    while True:
        data_rec = ser.readline()  #read data comming from Pico
        #data_rec = ser.read()
        print("Recv. from Pico: ", data_rec.decode())
        sleep(0.1)
        ser.write(b"Hi Pico")   #send response over serial to Raspberry Pi
        sleep(1)
        
except KeyboardInterrupt:
    if ser != None:
        ser.close()