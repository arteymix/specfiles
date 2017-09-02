Name:    zotero
Version: 5.0.17
Release: 1%{?dist}
Summary: Your personal research assistant

License: GPL
URL:     https://www.zotero.org
Source0: %{url}/download/client/dl?channel=release&platform=linux-x86_64&version=%{version}#/%{name}-%{version}.tar.gz

%description
Zotero [zoh-TAIR-oh] is a free, easy-to-use tool to help you collect, organize,
cite, and share your research sources.

%prep
%autosetup -n Zotero_linux-x86_64

%install
mkdir -p %{buildroot}%{_datadir}
cp -R . %{buildroot}%{_datadir}/zotero

mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/zotero/zotero %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --set-key Exec --set-value 'zotero -url %U' --set-key Icon --set-value '%{_datadir}/pixmaps/zotero.ico' zotero.desktop

mkdir -p %{buildroot}%{_datadir}/pixmaps
install chrome/icons/default/main-window.ico %{buildroot}%{_datadir}/pixmaps/zotero.ico

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/zotero
