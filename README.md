# The Palentir

A remote eye to look over the things that matter most to you. Open source, secure, and controlled by you.


## Design

- 180 Degree Fisheye Camera 
    - Capture video around the Palentir when motion is detected. 

- Audio Detection 
    - Be alerted to loud sounds

- Accelerometer 
    - The 3-axis accelerometer detects movement of the Palentir and alerts you.

- PIR Motion Detection 
    - Be alerted when the presence of thermal changes in the environment including human, animal and other precense.

- Microwave Motion Detection 
    - This motion sensor can detect movement behind objects using microwaves :)

- Heartbeat 
    - Detect when device goes offline and can no longer be reached via network

---

## Networks

- Wifi - Use chosen wifi network, hotel or phone hotspot
- Cellular - 4G/LTE as a backup 
- Secure Communcations - Wireguard, SSH tunnelling, etc
    - Using AWS EC2 instances or possible private instances

---

## Considerations

- Queuing system. 
    - Example: If wifi isn't available, queue up alerts, and try 4g network
    - See if MQTT has this
- Force 4G/LTE only
    - For security reasons, force connection on 4G/LTE to prevent network attacks
- Data bandwidth control
    - Keep monthly data below 2GB a month. Keep connections and traffic minimal. Secure MQTT should assist
- Consider Wireguard for 4G and OpenVPN for hotel wifi possibly due to censorship or firewall... https://www.top10vpn.com/guides/wireguard-vs-openvpn/

---

## Notes/Suggestions from others

- send message to more than person
- consider a switch on the side, attached to a Small trinket, when the switch is turned off, it will send a alert to the pi, which will alert the owner the system is being shutdown. Then it will shutdown in 30 seconds. Upon turning the switch on, the raspberry ip will power on.
    - This can also connect to the current sensor and send readings back to the pi
    - could also possibly act as a heart beat/watchdog


--- 

Networking

wireguard server created via ALGO. From your laptop, set up algo and have it create an AWS Lightsail instance

if you need to ssh to the pi, ssh from the algo vpn server. Note: All ports on PI should be blocked from wifi network.
```
sudo ssh pi@10.49.0.2
```

If disabling ssh on wifi, you should enable ssh access via ethernet

build a simple bash or python script that checks connectivity. If there is no connectivity, disable
one interface and try the other, otherwise disable the other interface

---

https://mqtthq.com/client