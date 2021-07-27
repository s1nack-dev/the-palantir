sudo yum update -y
sudo yum install git -y
git clone https://github.com/trailofbits/algo.git
cd algo
sudo yum -y install epel-release
sudo yum -y install python36-virtualenv
sudo yum install python-pip
pip install -U pip
pip install -U virtualenv
virtualenv -p python3 .env
source .env/bin/activate
python3 -m pip install -U pip virtualenv
python3 -m pip install -r requirements.txt
./algo


---


install docker
https://docs.docker.com/engine/install/ubuntu/

docker run -itd -p 1883:1883 -v $PWD/mosquitto.conf:/mosquitto/config/mosquitto.conf -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto