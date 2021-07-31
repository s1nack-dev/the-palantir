# This is the main python file

# upon boot, this will attempt to connect to the mqtt server
# will control other scripts via environment variables
# ie. armed=1 for on. armed=0 for off
# will send status update to mqtt server 
# Will announce if triggered
# ie. triggered=1 for yes. triggered=0 for no

import atexit
import subprocess
from time import sleep
import os

import logzero
from logzero import logger
import paho.mqtt.client as mqtt

MOTION_PIR = "motion-pir"
MOTION_MICROWAVE = "motion-microwave"
ACCELEROMETER = "accelerometer"

pwd = "/home/pi/the-palantir"
LOG_FILENAME = pwd + '/log/supervisor.log'
topic = "mqttHQ-client-test-3242342352341"
broker = "public.mqtthq.com"
if not os.path.isfile(LOG_FILENAME):
  os.mkdir(pwd + "/log")
logzero.logfile(LOG_FILENAME)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #logger.info(msg.topic+" "+str(msg.payload))
    message = (str(str(msg.payload).replace("b", "")).replace("'", ""))

def stop_service(service):
    bash_command = "systemctl start " + service
    process = subprocess.Popen(bash_command, stdout=subprocess.PIPE)
    output, error = process.communicate()

def stop_service(service):
    bash_command = "systemctl stop " + service
    process = subprocess.Popen(bash_command, stdout=subprocess.PIPE)
    output, error = process.communicate()

def on_exit():
    logger.info("Exit command triggered")
    client.publish(topic, payload="Exit command triggered", qos=0, retain=False)


def main():
   
    logger.info("Starting Supervisor")
    client.publish(topic, payload="Starting Supervisor", qos=0, retain=False)

    atexit.register(on_exit)

    client.loop_forever()

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, 1883, 60)
    main()


