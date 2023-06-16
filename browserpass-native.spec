%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

Name: browserpass-native
Version: 3.1.0
Release:        %{autorelease}
Summary: Browserpass - native messaging host

License: ISC
URL: https://github.com/browserpass/browserpass-native/
Source0: https://github.com/browserpass/browserpass-native/releases/download/3.1.0/browserpass-native-3.1.0-src.tar.gz

BuildRequires: go

%description
This is a host application for browserpass browser extension providing it
access to your password store. The communication is handled through Native
Messaging API.

%package firefox
Summary: Browserpass extension for Firefox

%description firefox
Test

%prep
%autosetup

%build
make configure
make

%install
DESTDIR=%{buildroot} make install
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/mozilla/native-messaging-hosts
ln -s ../../browserpass/hosts/firefox/com.github.browserpass.native.json %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/com.github.browserpass.native.json

%files
%license /usr/share/licenses/browserpass/LICENSE
%doc /usr/share/doc/browserpass/README.md
%{_bindir}/browserpass
%{_libdir}/browserpass

%files firefox
%{_libdir}/mozilla/native-messaging-hosts/com.github.browserpass.native.json

%changelog
