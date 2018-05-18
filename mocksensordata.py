import time,sys
import random

# Get all sensor data, and return sensordata['temp'],['mois'],['light']
def getSensorData():
    mosfet = 6
    sensordata = {}
    try:
        # Mock data
        #print("temp =", temp)
        sensordata["temp"] = random.randint(0,30)
        sensordata["mois"] = random.randint(0,500)
        sensordata["light"] = random.randint(0,700)
        time.sleep(.5)
        return sensordata

    except KeyboardInterrupt:
        print ("Test by Mock","KeyboardInterrupt!")
    except TypeError:
        REPORTER = "Please power off your raspberry3, and start it again!"
        print ("Raspberry3 overcurrent",REPORTER)
    except IOError:
        print ("Error")