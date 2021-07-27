# Will use this to make a solid MQTT test
# Using https://mqtthq.com/client

#%%
from time import sleep

import paho.mqtt.client as mqtt
import logging
import logging.config
import datetime

#%%

LOG_FILENAME = '/home/pi/logs/motion-pir.log'
#logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
topic = "mqttHQ-client-test-324234235234"
broker = "public.mqtthq.com"

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


while True:
  print('this is a test!')
  timestamp = str((datetime.datetime.now()))
  timestamp = timestamp[0:19]
  print("Image captured at",timestamp)
  client.publish(topic, payload="this is a test: " + timestamp, qos=0, retain=False)
  sleep(5)

sleep(1)


# %%
