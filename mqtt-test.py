# Will use this to make a solid MQTT test
# Using https://mqtthq.com/client

#%%
from time import sleep

import paho.mqtt.client as mqtt
import logzero
from logzero import logger
import datetime
import os
import atexit

#%%
pwd = os.getcwd()
LOG_FILENAME = pwd + '/log/test.log'
topic = "mqttHQ-client-test-3242342352341"
broker = "public.mqtthq.com"
if not os.path.isfile(LOG_FILENAME):
  os.mkdir(pwd + "/log")
logzero.logfile(LOG_FILENAME)

def on_exit():
  logger.info("Exit command given")
  client.publish(topic, payload="Exit command given", qos=0, retain=False)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

client.publish(topic, payload="Starting Test", qos=0, retain=False)

atexit.register(on_exit)

while True:
  timestamp = str((datetime.datetime.now()))
  timestamp = timestamp[0:19]
  logger.info("Test Alert at %s" % timestamp)
  client.publish(topic, payload="this is a test: " + timestamp, qos=0, retain=False)
  sleep(5)

sleep(1)


# %%
