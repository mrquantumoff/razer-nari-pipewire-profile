# Razer Nari pipewire profile

## Warning: I no longer use a Razer Nari headset. This means that this repo is no longer maintained. I won't be deleting the AUR package, since as far as I know the profile still works.

The Razer Nari is a gaming headset which has two stereo audio outputs. One for voice chat and one for the rest of the sound. It can be mixed between with a physical knob.

By default, pulseaudio/pipewire only enables the voice chat output. This profile enables the second (game) output and the udev rule makes sure this profile is used when plugging in the device.

This solves the problem when only **mono** output is recognized for Nari.

### Arch Linux

Install the package [from the AUR](https://aur.archlinux.org/packages/razer-nari-pipewire-profile/)


### Fedora Linux

Binary package is available in [releases tab](https://github.com/mrquantumoff/razer-nari-pipewire-profile/releases/download/v1.1/razer-nari-pipewire-profile-1.1-2.x86_64.rpm)

### Other Linux Systems
#### Automated script (Recommended)

```shell
curl -fssL https://github.com/mrquantumoff/razer-nari-pipewire-profile/raw/master/autoinstall.sh | sh
```
#### Or clone the repo ```cd``` in it and run ```./install.sh```

### Other

Install by copying the following files:

- `razer-nari-input.conf`, `razer-nari-output-game.conf`, and `razer-nari-output-chat.conf` to `/usr/share/pulseaudio/alsa-mixer/paths/`
- `razer-nari-usb-audio.conf` to `/usr/share/pulseaudio/alsa-mixer/profile-sets/`
- `91-pulseaudio-razer-nari.rules` to `/lib/udev/rules.d/`

Script:
```
cp razer-nari-input.conf /usr/share/alsa-card-profile/mixer/paths/
cp razer-nari-output-{game,chat}.conf  /usr/share/alsa-card-profile/mixer/paths/
cp razer-nari-usb-audio.conf /usr/share/alsa-card-profile/mixer/profile-sets/
cp 91-pulseaudio-razer-nari.rules /lib/udev/rules.d/
```

Reboot.

After that, plug in the device to see if it works.
