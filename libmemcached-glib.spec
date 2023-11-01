Name:    libmemcached-glib
Version: 1.0%{?dist}
Summary: GLib wrapper around libmemcached and libmemcachedutil

Group:   Development/Libraries
License: LGPL
URL:     https://github.com/arteymix/%{name}
Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BUildRequires: pkgconfig(gio-2.0)
BUildRequires: pkgconfig(libmemcached)
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: vala-tools

%description
Memcached-GLib is a GLib-friendly wrapper around libmemcached and
libmemcachedutil libraries.

%configure
%meson

%build
mkdir build && cd build
%meson . build
ninja-build -D build -v

%install
DESTDIR=%{buildroot} ninja-build -D build -v install

%check
ninja-build -D build -v test

%files
%doc README.md COPYING
%{_libdir}/*

%files devel
%{_includedir}/*
%{_datadir}/*
