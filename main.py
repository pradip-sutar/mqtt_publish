import time
from threading import *
# import RPi.GPIO as GPIO
from time import sleep
import threading
from datetime import datetime
import client as c
import json
import random
 

mqtt = c.iotMQTT()

 

main_thread = threading.current_thread()

 

 

#IOT Data Uploading
def doFeed():
    threading.Timer(1.0,doFeed).start()
    # a=open('cputemperature.txt','r')
    # b=a.read()
    # c=open('ph_data.txt','r')
    # d=c.read()
    # e=open('orp_data.txt','r')
    # f=e.read()
    # g=open('DO_data.txt','r')
    # h=g.read()
    now = datetime.now()
    date_tm = now.strftime("%Y-%m-%d %H:%M:%S")
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "ORP", "paramValue":f}) 
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "DO", "paramValue": h})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "Ph", "paramValue": d})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "CPU_TEMPERATURE", "paramValue": b})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "Current", "paramValue": 5})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "voltage", "paramValue": 25})
    # mqtt.postHeartBeat()
    mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "current", "paramValue":random.randrange(100,200)},"812786545337875") 
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "Sensor2", "paramValue": 10})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "Sensor3", "paramValue": 10})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "Sensor4", "paramValue": 10})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "Current", "paramValue": 10})
    # mqtt.postDataFeed({"dataPoint":date_tm, "paramType": "voltage", "paramValue": 10})
    print(date_tm)

sleep(.6)

threading.Timer(5.0,doFeed).start()

mqtt.lp()