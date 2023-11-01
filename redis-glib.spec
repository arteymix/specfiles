
Name:    redis-glib
Summary: A Redis Driver for GObject Based Applications
License: GPL
Version: 0.1.3
Release: 1
Source0: redis-%{version}.tar.gz

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(hiredis)

%description
This library piggy backs on top of the hiredis high-performance client
library for Redis. It provides integration with the main loop, as well
as the ability to work with higher level structures as compared to the
strings used by redis.

%prep
%setup -q -n redis-%{version}

%build
%configure
touch Redis-1.0.typelib Redis-1.0.gir
make -W Redis-1.0.typelib

%install
%make_install

%files
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
