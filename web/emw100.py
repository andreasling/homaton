# from __future__ import print_function
# import sys
import time
import RPi.GPIO as GPIO

T_emw = 600/1000000.0

emwPre = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

emwUnits = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], # 0
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0]  # 1
]

emwButtons = [
    [0,0], # 0
    [0,1], # 1
    [1,0], # 2
    [1,1]  # 3
]

# todo: calculate?
emwExtra = [
    [ # unit 0
        [1, 1, 0, 0], # 0
        [0, 0, 1, 1], # 1
        [0, 1, 1, 0], # 2
        [1, 1, 1, 0]  # 3
    ],
    [ # unit 1
        [1, 1, 1, 1], # 0
        [0, 0, 0, 0], # 1
        [0, 1, 0, 1], # 2
        [1, 1, 0, 1]  # 3
    ]
]

emwCommand = [
    [0, 0, 0, 0], # off
    [1, 1, 1, 1]  # on
]

emwPhysicalBits = [
    [1, 0, 0, 1, 0], # 0
    [0, 1, 0, 1, 0]  # 1
]

gpioBits = [ GPIO.LOW, GPIO.HIGH ]

def sendEmw(gpio, unit, button, command):
    for i in xrange(0, 5):
        bits = emwUnits[unit] + emwButtons[button] + emwExtra[unit][button] + emwCommand[command]

        physicalBits = list(toPhysicalEmwBits(bits))
        sendPhysicalEmwBits(gpio, emwPre + physicalBits)

        time.sleep(T_emw * 30)

def toPhysicalEmwBits(bits):
    for bit in bits:
        for physicalBit in emwPhysicalBits[bit]:
            yield physicalBit

def sendPhysicalEmwBits(gpio, bits):
    sendPhysicalBits(gpio, bits, T_emw)

def sendPhysicalBits(gpio, bits, period):
    for bit in bits:
        sendPhysicalBit(gpio, bit, period)
    # todo here or elsewhere make sure output is low when done: GPIO.output(gpio, GPIO.LOW);

def sendPhysicalBit(gpio, value, period):
    GPIO.output(gpio, gpioBits[value])
    time.sleep(period)
