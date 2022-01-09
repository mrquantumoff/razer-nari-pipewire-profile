#!/bin/bash
cp razer-nari-input.conf /usr/share/alsa-card-profile/mixer/paths/
cp razer-nari-output-{game,chat}.conf /usr/share/alsa-card-profile/mixer/paths/
cp razer-nari-usb-audio.conf /usr/share/alsa-card-profile/mixer/profile-sets/
cp 91-pulseaudio-razer-nari.rules /lib/udev/rules.d/

