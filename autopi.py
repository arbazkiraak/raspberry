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


apt-get install virtualenv
virtualenv kiraak
source kiraak/bin/activate
wget https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh
bash Anaconda2-4.4.0-Linux-x86_64.sh
