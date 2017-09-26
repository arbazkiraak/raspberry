#!/bin/bash

--------------------------------------------------
root@raspberrypi:/home/pi# cat /etc/dhcpcd.conf
# A sample configuration for dhcpcd.
# See dhcpcd.conf(5) for details.

# Allow users of this group to interact with dhcpcd via the control socket.
#controlgroup wheel

# Inform the DHCP server of our hostname for DDNS.
hostname

# Use the hardware address of the interface for the Client ID.
clientid
# or
# Use the same DUID + IAID as set in DHCPv6 for DHCPv4 ClientID as per RFC4361.
#duid

# Persist interface configuration when dhcpcd exits.
persistent

# Rapid commit support.
# Safe to enable by default because it requires the equivalent option set
# on the server to actually work.
option rapid_commit

# A list of options to request from the DHCP server.
option domain_name_servers, domain_name, domain_search, host_name
option classless_static_routes
# Most distributions have NTP support.
option ntp_servers
# Respect the network MTU.
# Some interface drivers reset when changing the MTU so disabled by default.
#option interface_mtu

# A ServerID is required by RFC2131.
require dhcp_server_identifier

# Generate Stable Private IPv6 Addresses instead of hardware based ones
slaac private

# A hook script is provided to lookup the hostname if not set by the DHCP
# server, but it should not be run by default.
nohook lookup-hostname

interface eth0
static ip_address=192.168.0.110
static routers=192.168.0.1
static domain_name_servers=192.168.0.1

interface wlan0
static ip_address=192.168.0.110
static routers=192.168.0.1
static domain_name_servers=192.168.0.1

---------------------------------
root@raspberrypi:/home/pi# cat /etc/network/interfaces
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

iface eth0 inet manual

allow-hotplug wlan0
iface wlan0 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
---------------------------------------------------------------------


sudo raspi-config
enabled SSH

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
