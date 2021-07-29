# RCWL-0516
# https://github.com/lesp/electromaker-RCWL-0516
# https://www.electromaker.io/tutorial/blog/using-a-doppler-radar-sensor-with-the-raspberry-pi-12


from gpiozero import DigitalInputDevice
import datetime
#from picamera import PiCamera
from signal import pause
import paho.mqtt.client as mqtt
import logzero
from logzero import logger
import datetime

LOG_FILENAME = '/home/pi/log/radar.log'
topic = "mqttHQ-client-test-3242342352341"
broker = "public.mqtthq.com"

radar = DigitalInputDevice(17, pull_up=False, bounce_time=2.0)
#camera = PiCamera()
#camera.resolution = (1024, 768)

def detector():
    timestamp = str((datetime.datetime.now()))
    timestamp = timestamp[0:19]
    logger.info("Radar Motion Detected")
    client.publish(topic, payload="Radar Motion Detected @ " + timestamp, qos=0, retain=False)
  
    #camera.capture(timestamp+".jpg")

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

logger.info("Starting Radar Motion Monitoring")
client.publish(topic, payload="Starting Radar Motion Monitoring", qos=0, retain=False)

    
radar.when_activated = detector
pause()