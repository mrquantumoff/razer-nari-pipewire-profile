Name:       razer-nari-pipewire-profile
Version:    1.1
Release:    2
Summary:    Razer Nari Pipewire Profile
License:    FIXME
BuildArch:  x86_64
Requires:   pipewire-pulse,pipewire
BuildRequires:  install
Source0:    https://github.com/mrquantumoff/razer-nari-pipewire-profile/releases/download/v1.1/v1.1.tar.gz


%description
Razer Nari headsets pipewire profile

%prep
mv *  %builddir

%install
install -Dm644 -t "%buildroot/usr/share/alsa-card-profile/mixer/paths/" razer-nari-{input,output-{game,chat}}.conf
install -Dm644 -t "%buildroot/usr/share/alsa-card-profile/mixer/profile-sets/" razer-nari-usb-audio.conf
install -Dm644 -t "%buildroot/usr/lib/udev/rules.d/" 91-pulseaudio-razer-nari.rules

%files
/usr/share/alsa-card-profile/mixer/paths/razer-nari-input.conf
/usr/share/alsa-card-profile/mixer/paths/razer-nari-output-game.conf
/usr/share/alsa-card-profile/mixer/paths/razer-nari-output-chat.conf
/usr/lib/udev/rules.d/91-pulseaudio-razer-nari.rules

%changelog
Nothing