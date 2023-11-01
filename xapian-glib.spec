Name:    xapian-glib
Version: 3.0.3
Release: 1%{?dist}
Summary: GObject bindings for Xapian

Group:   Development/Libraries
License: GPL
URL:     https://github.com/endlessm/xapian-glib
Source0: %{url}/releases/download/v%{version}/mustache-glib-%{version}.tar.bz2

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libxml-2.0)

%description
Xapian-GLib is a wrapper library that offers a C API and GObject types for the
Xapian database.

Xapian-GLib allows accessing the Xapian API in various languages, through the
GObject Introspection API.

%package devel
Summary: Build files for Xapian-GLib

%description devel
Provide the C headers and necessary build files.

%prep
%setup -q

%build
%configure
make %{am_flags}

%install
%make_install

%files
%doc README.md COPYING
%{_libdir}/*

%files devel
%{_datadir}/*
%{_includedir}/*
