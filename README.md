# The Palentir

A remote eye to look over the things that matter most to you. Open source, secure, and controlled by you.


## Design

180 Degree Fisheye Camera - Capture video around the Palentir when motion is detected. 

Audio Detection - Be alerted to loud sounds

Accelerometer - The 3-axis accelerometer detects movement of the Palentir and alerts you.

PIR Motion Detection - Be alerted when the presence of thermal changes in the environment including human, animal and other precense.

Microwave Motion Detection - This motion sensor can detect movement behind objects using microwaves :)

Heartbeat - Detect when device goes offline and can no longer be reached via network

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

