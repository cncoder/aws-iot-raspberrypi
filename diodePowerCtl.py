'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''
#!/usr/bin/python

# (just for Real environment) import GPOI
import RPi.GPIO as GPIO
import sys
import time

# Connect the diode to GPIO port 3
channel = 3

def setDiodeState(temp,desire_new_threshold):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    state = 0
    print("********setDiodeState:*******")
    print("The temp %f is and desire_new_threshold is %f " % (temp,desire_new_threshold))  
    # GPIO.setup(channel, GPIO.OUT)
    # desire "on"
    if (temp>desire_new_threshold):
        state = 1
        GPIO.output(channel, GPIO.HIGH)
    # desire "off"
    else:
        state = 0
        GPIO.output(channel, GPIO.LOW)
    time.sleep(2)
    # desire == "on"
    if (state == 1):
        return "ON"
    # desire == "off"
    elif (state == 0):
        return "OFF"
    else:
        return "error"