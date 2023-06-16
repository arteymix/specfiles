%define _missing_build_ids_terminate_build 0
%define _unpackaged_files_terminate_build 0
%global debug_package %{nil}

Name: browserpass-native
Version: 3.1.0
Release:        %{autorelease}
Summary: Browserpass - native messaging host

License: ISC
URL: https://github.com/browserpass/browserpass-native/
Source0: https://github.com/browserpass/browserpass-native/releases/download/3.1.0/browserpass-native-3.1.0-src.tar.gz

BuildRequires: go

%package firefox
Summary: Browserpass native messaging host for Firefox

%package chromium
Summary: Browserpass native messaging host for Chromium

%package chrome
Summary: Browserpass native messaging host for Chrome

%description
This is a host application for browserpass browser extension providing it
access to your password store. The communication is handled through Native
Messaging API.

%description firefox

%description chromium

%description chrome

%prep
%autosetup

%build
make configure
make

%install
DESTDIR=%{buildroot} make install
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/mozilla/native-messaging-hosts
cp %{buildroot}%{_libdir}/browserpass/hosts/firefox/com.github.browserpass.native.json %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/com.github.browserpass.native.json
mkdir -p %{buildroot}/etc/chromium/native-messaging-hosts
cp %{buildroot}%{_libdir}/browserpass/hosts/chromium/com.github.browserpass.native.json %{buildroot}/etc/chromium/native-messaging-hosts/com.github.browserpass.native.json
mkdir -p %{buildroot}/etc/opt/chrome/native-messaging-hosts
cp %{buildroot}%{_libdir}/browserpass/hosts/chromium/com.github.browserpass.native.json %{buildroot}/etc/opt/chrome/native-messaging-hosts/com.github.browserpass.native.json

%files
%license /usr/share/licenses/browserpass/LICENSE
%doc /usr/share/doc/browserpass/README.md
%{_bindir}/browserpass

%files firefox
%{_libdir}/mozilla/native-messaging-hosts/com.github.browserpass.native.json

%files chromium
/etc/chromium/native-messaging-hosts/com.github.browserpass.native.json

%files chrome
/etc/opt/chrome/native-messaging-hosts/com.github.browserpass.native.json
