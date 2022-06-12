#!/bin/bash
git clone https://github.com/mrquantumoff/razer-nari-pipewire-profile.git >> /dev/null
cd razer-nari-pipewire-profile
echo "Installing pipewire profile"
sudo su -c 'chmod +x ./install.sh && ./install.sh'
echo "If you don't see any errors, profile was installed successfully. Please reboot your PC."
cd ..
rm -rf razer-nari-pipewire-profile
