# https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio

# GPIO 27

from time import sleep
from gpiozero import MotionSensor
import paho.mqtt.client as mqtt
import logzero
from logzero import logger
import datetime

LOG_FILENAME = '/home/pi/log/pir.log'
topic = "mqttHQ-client-test-3242342352341"
broker = "public.mqtthq.com"
pir = MotionSensor(22)

def detectIntruders():
  pir.wait_for_motion()
  timestamp = str((datetime.datetime.now()))
  timestamp = timestamp[0:19]
  logger.info("PIR Motion Detected")
  client.publish(topic, payload="PIR Motion Detected @ " + timestamp, qos=0, retain=False)
  sleep(5)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

logzero.logfile(LOG_FILENAME)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

logger.info("Starting PIR Motion Monitoring")
client.publish(topic, payload="Starting PIR Motion Monitoring", qos=0, retain=False)



sleep(1)

while True:
  detectIntruders()