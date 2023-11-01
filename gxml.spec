
Name:    gxml
Summary: A documentation tool for Vala
License: GPL
Version: 0.10.0
Release: 1
Source0: %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: vala

%description
GXml is a GObject-based XML DOM API implementing at least W3C DOM Level 1 Core.
Its functionality is obtained by wrapping libxml2.

%prep
%setup -q

%build
%configure
make

%install
%make_install

%check
make check

%files
%doc AUTHORS ChangeLog COPYING README NEWS
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*
