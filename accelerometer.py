
# Device: GY-521
# https://openest.io/en/2020/01/21/mpu6050-accelerometer-on-raspberry-pi/
# https://circuitdigest.com/microcontroller-projects/mpu6050-gyro-sensor-interfacing-with-raspberry-pi/

# https://electrosome.com/interfacing-mpu-6050-gy-521-arduino-uno/
#sudo raspi-config # enable i2c
#sudo apt-get install -y build-essential python-dev python-pip
# sudo pip install RPi.GPIO
# sudo apt-get install -y python-smbus
# pip install mpu6050-raspberrypi    # instead of sudo pip install mpu6050



# USE THIS VERY EASY https://github.com/AaditT/mpu6050-with-Raspberry-Pi

# data is given 0 - 9 (0 - 90 degrees)

from mpu6050 import mpu6050
import time
import paho.mqtt.client as mqtt
import logzero
from logzero import logger
import datetime

mpu = mpu6050(0x68)
MOVEMENT_THRESHOLD = 0.5
DELAY = 0.5

pwd = "/home/pi/the-palantir"
LOG_FILENAME = pwd + '/log/accelerometer.log'
topic = "mqttHQ-client-test-3242342352341"
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

logzero.logfile(LOG_FILENAME)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

logger.info("Starting Accelerometer Monitoring")
client.publish(topic, payload="Starting Accelerometer Monitoring", qos=0, retain=False)

def trigger(axis):
    timestamp = str((datetime.datetime.now()))
    timestamp = timestamp[0:19]
    logger.info("Accelerometer Motion Detected on %s" % axis)
    client.publish(topic, payload=f"Accelerometer Motion Detected on {axis} @ " + timestamp, qos=0, retain=False)
    time.sleep(5)



while True:

    accel_data = mpu.get_accel_data()
    # logger.debug("Acc X : "+str(accel_data['x'] + 10))
    # logger.debug("Acc Y : "+str(accel_data['y'] + 10))
    # logger.debug("Acc Z : "+str(accel_data['z'] + 10))

    x = accel_data['x'] + 10
    y = accel_data['y'] + 10
    z = accel_data['z'] + 10
    time.sleep(DELAY)
    accel_data = mpu.get_accel_data()
    new_x = accel_data['x'] + 10
    new_y = accel_data['y'] + 10
    new_z = accel_data['z'] + 10
    
    new_number_plus_1_x = x + 1.0
    new_number_plus_1_y = y + 1.0
    new_number_plus_1_z = z + 1.0
    # logger.debug("new_x: %s" % new_x)
    # logger.debug("new number x: %s" % new_number_plus_1_x)
    # logger.debug("new_y: %s" % new_y)
    # logger.debug("new number y: %s" % new_number_plus_1_y)
    # logger.debug("new_z: %s" % new_z)
    # logger.debug("new number z: %s" % new_number_plus_1_z)
    if new_x > MOVEMENT_THRESHOLD + x or x > MOVEMENT_THRESHOLD + new_x:
        trigger("x")
    elif new_y > MOVEMENT_THRESHOLD + y or y > MOVEMENT_THRESHOLD + new_y:
        trigger("y")
    elif new_z > MOVEMENT_THRESHOLD + z or z > MOVEMENT_THRESHOLD + new_z:
        trigger("z")
    else:
        pass

