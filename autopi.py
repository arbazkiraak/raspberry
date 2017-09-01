#!/bin/bash

echo 'sudo nano /etc/dhcpcd.conf\
      interface eth0

      static ip_address=192.168.0.10/24
      static routers=192.168.0.1
      static domain_name_servers=192.168.0.1

      interface wlan0

      static ip_address=192.168.0.200/24
      static routers=192.168.0.1
      static domain_name_servers=192.168.0.1'
      



sudo raspi-config

apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6
echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free'
echo 'Add this in /etc/apt/sources.list'

apt-get update
apt-get upgrade

sudo apt-get install tightvncserver -y
sudo apt-get install xrdp -y
service xrdp start

apt-get install ruby -y
sudo apt-get install build-essential ruby-dev libpcap-dev net-tools -y
gem install bettercap

apt-get install apache2 -y

apt-get install virtualenv
virtualenv kiraak
source kiraak/bin/activate

Method 1:
pip install --upgrade pip
pip install PySock
pip install urllib3
sudo apt-get install python-dev python3-dev python-pip python3-pip
sudo apt-get install python-dev ipython jupyter-notebook
python2 -m pip install ipykernel
jupyter-notebook --no-browser --ip=192.168.0.108 --port=1337

Method 2: (InCorrect)

#https://www.anaconda.com/blog/developer-blog/conda-support-raspberry-pi-2-and-power8-le/
wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-armv7l.sh
bash Anaconda2-4.4.0-Linux-x86_64.sh
source ~/.bashrc
conda install anaconda-client
pip install --upgrade --force-reinstall --no-cache-dir jupyter

------------------------------------------

#P
