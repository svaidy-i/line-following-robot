from machine import Pin
from picozero import LED,pico_led
import time

# Motor pins
rmr = LED(10)  # Right Motor Reverse
rmf = LED(11)  # Right Motor Forward
lmf = LED(12)  # Left Motor Forward
lmr = LED(13)  # Left Motor Reverse

# Sensor Pins
s1 = Pin(2, Pin.IN)
s2 = Pin(3, Pin.IN)
s3 = Pin(4, Pin.IN)
s4 = Pin(5, Pin.IN)
s5 = Pin(6, Pin.IN)

# Motor and Timing Constants
gr = 0.9  # Gear ratio
st = 0.3  # Step time
ms = 0.3  # Motor step duration

# Functions
def step_forward():
    # Move the robot forward by one step.
    lmf.on(ms * gr)
    rmf.on(ms)
    time.sleep(0.1)
    lmf.off()
    rmf.off()

def step_left():
    # Turn the robot left.
    rmf.on()
    lmr.off()
    time.sleep(st)
    rmf.off()
    lmr.off()
    
def inch_left():
    rmf.on()
    lmr.off()
    time.sleep(0.17)
    rmf.off()
    lmr.off()
    
    
def step_right():
    # Turn the robot right.
    lmf.on()
    rmr.off()
    time.sleep(st)
    lmf.off()
    rmr.off()

def inch_right():
    # Turn the robot right.
    lmf.on()
    rmr.off()
    time.sleep(0.17)
    lmf.off()
    rmr.off()
    
def stop():
    lmf.off()
    rmf.off()
    lmr.off()
    rmr.off()

def lost():
    pico_led.blink()
    time.sleep(st)
    pico_led.off
    step_forward()
    

def value():
    x = s1.value(), s2.value(), s3.value(), s4.value(), s5.value()  
    c = 0
    for i in range(5):
        y = x[i] * (2 ** i)  
        c += y
    return c

while True:
    time.sleep(0.3)
    read = value()
    print(read)
    # 0:black
    # 1:white
    if read == 0x1b or read == 0x11 or read == 0x13: #11011 and # 10001 and #10011
        step_forward()
    elif read == 0x17 :# 10111
        inch_left()
    elif read == 0x1d: #11101
        inch_right()
        
    elif read == 0x0 or read == 0x3 or read == 0x7 or read == 0xf : #00000 and #00011 and #00111 and #01111
        step_left()
        
    elif read == 0x10 or read == 0x18 or read == 0x1c or read == 0x1e : #10000 and #11000 and #11100 and #11110
        step_right()
        
    elif read == 0x1f : # 11111
        lost()
        
        
       