Name:       razer-nari-pipewire-profile
Version:    1.1
Release:    2
Summary:    Razer Nari Pipewire Profile
License:    MIT
BuildArch:  x86_64
Requires:   pipewire-pulseaudio,pipewire
BuildRequires: coreutils wget

%description
Razer Nari headsets pipewire profile

%build
wget https://github.com/mrquantumoff/razer-nari-pipewire-profile/archive/refs/tags/v1.1.tar.gz
tar -xpvf v1.1.tar.gz
cd razer-nari-pipewire-profile-1.1

mv razer-nari-{input,output-{game,chat}}.conf %_builddir
mv razer-nari-usb-audio.conf %_builddir
mv 91-pulseaudio-razer-nari.rules %_builddir

%install
install -Dm644 -t "%buildroot/usr/share/alsa-card-profile/mixer/paths/" razer-nari-{input,output-{game,chat}}.conf
install -Dm644 -t "%buildroot/usr/share/alsa-card-profile/mixer/profile-sets/" razer-nari-usb-audio.conf
install -Dm644 -t "%buildroot/usr/lib/udev/rules.d/" 91-pulseaudio-razer-nari.rules

%files
/usr/share/alsa-card-profile/mixer/paths/razer-nari-input.conf
/usr/share/alsa-card-profile/mixer/paths/razer-nari-output-game.conf
/usr/share/alsa-card-profile/mixer/profile-sets/razer-nari-usb-audio.conf
/usr/share/alsa-card-profile/mixer/paths/razer-nari-output-chat.conf
/usr/lib/udev/rules.d/91-pulseaudio-razer-nari.rules

%changelog
* Fri Sep 16 2022 Demir Yerli <mrquantumoff@protonmail.com> - 1.1-2
- Initial package