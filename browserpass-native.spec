%define _missing_build_ids_terminate_build 0
%define _unpackaged_files_terminate_build 0
%global debug_package %{nil}

Name: browserpass-native
Version: 3.1.0
Release: 3%{?dist}
Summary: Browserpass - native messaging host

License: ISC
URL: https://github.com/browserpass/browserpass-native/
Source0: https://github.com/browserpass/browserpass-native/releases/download/3.1.0/browserpass-native-3.1.0-src.tar.gz

BuildRequires: go

%package firefox
Summary: Browserpass native messaging host for Firefox
Requires: firefox

%package chromium
Summary: Browserpass native messaging host for Chromium
Requires: chromium

%package chrome
Summary: Browserpass native messaging host for Chrome
Requires: google-chrome-stable

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
%make_build

%install
%make_install
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/mozilla/native-messaging-hosts
cp %{buildroot}%{_libdir}/browserpass/hosts/firefox/com.github.browserpass.native.json %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/com.github.browserpass.native.json
mkdir -p %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts
cp %{buildroot}%{_libdir}/browserpass/hosts/chromium/com.github.browserpass.native.json %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/com.github.browserpass.native.json
mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/native-messaging-hosts
cp %{buildroot}%{_libdir}/browserpass/hosts/chromium/com.github.browserpass.native.json %{buildroot}%{_sysconfdir}/opt/chrome/native-messaging-hosts/com.github.browserpass.native.json
rm -r %{buildroot}%{_libdir}/browserpass

%files
%license %{_defaultlicensedir}/browserpass/LICENSE
%doc %{_docdir}/browserpass/README.md
%{_bindir}/browserpass

%files firefox
%{_libdir}/mozilla/native-messaging-hosts/com.github.browserpass.native.json

%files chromium
%{_sysconfdir}/chromium/native-messaging-hosts/com.github.browserpass.native.json

%files chrome
%{_sysconfdir}/opt/chrome/native-messaging-hosts/com.github.browserpass.native.json

%changelog
%autochangelog
