# https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio

# GPIO 27

from time import sleep
from gpiozero import MotionSensor
import paho.mqtt.client as mqtt
import logging
import logging.config

LOG_FILENAME = '/home/pi/logs/motion-pir.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
topic = "mqtt_topic_goes_here"
broker = "mqtt.eclipse.org"

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

def detectIntruders():
  pir.wait_for_motion()
  print('Intruder Alert!')
  client.publish(topic, payload=None, qos=0, retain=False)
  sleep(5)

pir = MotionSensor(22)

while True:
  detectIntruders()