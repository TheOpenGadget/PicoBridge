from machine import Pin, UART,SPI
import time
from time import sleep

# Initialize output pin to control onboard LED
led = Pin("LED", Pin.OUT)

uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

uart.write(b"Hello RPi, Pico here")
sleep(0.1)

while 1:
    if uart.any():
        led.on()
        data_Read = uart.read() #read data comming from Raspberry Pi
        print("Data recv: ", data_Read)
        uart.write(b"Hello from Pico\n") #Send data to Raspberry Pi
        sleep(0.5)
        led.off()
    sleep(0.1)
    




