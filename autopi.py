#!/bin/bash

apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6
echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free'
echo 'Add this in /etc/apt/sources.list'

sudo apt-get install tightvncserver -y
sudo apt-get install xrdp -y
service xrdp start

sudo apt-get install build-essential ruby-dev libpcap-dev net-tools -y
