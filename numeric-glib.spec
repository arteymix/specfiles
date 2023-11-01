Name:       numeric-glib
Version:    master
Release:    1%{?dist}
Summary:    Numeric data types for GLib via GCC extensions

Group:      Development/Libraries
License:    LGPL
URL:        https://github.com/arteymix/numeric-glib
Source0:    %{url}/archive/%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: gobject-introspection
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: vala
BuildRequires: vala-tools

%description

%package devel
Summary:  Build files for Numeric-GLib
Requires: numeric-glib

%description devel
Provides build files including C header, Vala bindings and GIR introspection
meta-data.

%prep
%autosetup -n numeric-glib-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%{_libdir}/*
%exclude %{_libdir}/pkgconfig/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/vala/*
