
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
mpu = mpu6050(0x68)

threshold = 0.5
while True:

    accel_data = mpu.get_accel_data()
    print("Acc X : "+str(accel_data['x']))
    print("Acc Y : "+str(accel_data['y']))
    print("Acc Z : "+str(accel_data['z']))
    print()

    x = accel_data['x']
    time.sleep(0.5)
    accel_data = mpu.get_accel_data()
    new_x = accel_data['x']
    print(new_x)
    print("new number: ", x + 1.0)
    if new_x > threshold + x or new_x > threshold - x:
        print("alarmed at: ",new_x)
        print('movement detected')
    

