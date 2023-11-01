Name:       vast
Version:    master
Release:    1%{?dist}
Summary:    Deep learning with GNOME infrastructure

Group:      Development/Libraries
License:    LGPL
URL:        https://github.com/rainwoodman/vast
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
Summary:  Build files for Vast
Requires: vast

%description devel
Provides build files including C header, Vala bindings and GIR introspection
meta-data.

%prep
%autosetup -n vast-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check

%files
%doc README.rst
%{_libdir}/*
%exclude %{_libdir}/pkgconfig/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/vala/*
%{_datadir}/gir-1.0/*
