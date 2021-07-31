Add file to /etc/systemd/system/ directory
sudo cp files/systemd/* /etc/systemd/system/
Then run sudo systemctl enable fancontrol.service

sudo systemctl enable palantir_accelerometer.service
sudo systemctl enable palantir_motion-microwave.service
sudo systemctl enable palantir_motion-pir.service
sudo systemctl enable palantir_supervisor.service