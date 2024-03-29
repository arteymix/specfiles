%define squash_api_version 0.7
%define squash_version 0.7.0

Name:           squash
Version:        %{squash_version}
Release:        1%{?dist}
Summary:        Compression abstraction library
License:        MIT
URL:            https://quixdb.github.io/squash
Source0:        https://github.com/quixdb/squash/releases/download/v%{squash_version}/squash-%{squash_version}.tar.bz2

BuildRequires:  cmake ragel snappy-devel zlib-devel xz-devel bzip2-devel lzo-devel lz4-devel
%if 0%{?fedora} >= 25
BuildRequires:  libzstd-devel zpaq-devel
%endif
Recommends:     squash-plugin-brieflz squash-plugin-brotli squash-plugin-bsc squash-plugin-bzip2 squash-plugin-crush squash-plugin-csc squash-plugin-density squash-plugin-doboz squash-plugin-fari squash-plugin-fastlz squash-plugin-gipfeli squash-plugin-heatshrink squash-plugin-libdeflate squash-plugin-lz4 squash-plugin-lzf squash-plugin-lzfse squash-plugin-lzg squash-plugin-lzham squash-plugin-lzjb squash-plugin-lzma squash-plugin-lzo squash-plugin-miniz squash-plugin-ms-compress squash-plugin-ncompress squash-plugin-quicklz squash-plugin-snappy squash-plugin-wflz squash-plugin-yalz77 squash-plugin-zlib squash-plugin-zlib-ng squash-plugin-zling squash-plugin-zpaq squash-plugin-zstd

%description
Squash provides a single API to access many compression libraries,
allowing applications a great deal of flexibility in choosing
compression algorithms, including the option to pass that choice along
to the user.

%prep
%autosetup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_BINDIR=%{_bindir} -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} -DCMAKE_INSTALL_SBINDIR=%{_sbindir} -DCMAKE_INSTALL_SHAREDSTATEDIR=%{_sharedstatedir} -DCMAKE_INSTALL_DATAROOTDIR=%{_datarootdir} -DCMAKE_INSTALL_DATADIR=%{_datadir} -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} -DCMAKE_INSTALL_INFODIR=%{_infodir} -DCMAKE_INSTALL_MANDIR=%{_mandir} -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_libdir}/libsquash*
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/squash
%{_mandir}/man1/squash.1.*
%{_libdir}/squash/%{squash_api_version}/plugins/copy/libsquash%{squash_api_version}-plugin-copy.so
%{_libdir}/squash/%{squash_api_version}/plugins/copy/squash.ini


%package devel
Group: Development/Libraries
Summary: Development package for Squash
Requires: squash

%description devel
The squash-devel package contains files necessary
for building software using the Squash compression library.
%files devel
%{_includedir}/squash-%{squash_api_version}/*
%{_libdir}/pkgconfig/squash-%{squash_api_version}.pc
%{_datadir}/vala/vapi/squash-*.vapi
%{_libdir}/cmake/Squash-%{squash_version}/SquashConfig.cmake


####
## Plugins
####

# BriefLZ
%package plugin-brieflz
Summary: BriefLZ plugin for Squash
Requires: squash
License: zlib and MIT

%description plugin-brieflz
BriefLZ plugin for Squash

%files plugin-brieflz
%{_libdir}/squash/%{squash_api_version}/plugins/brieflz/libsquash%{squash_api_version}-plugin-brieflz.so
%{_libdir}/squash/%{squash_api_version}/plugins/brieflz/squash.ini


# Brotli
%package plugin-brotli
Summary: Brotly plugin for Squash
Requires: squash
License: Apache 2.0 and MIT

%description plugin-brotli
Brotli plugin for Squash

%files plugin-brotli
%{_libdir}/squash/%{squash_api_version}/plugins/brotli/libsquash%{squash_api_version}-plugin-brotli.so
%{_libdir}/squash/%{squash_api_version}/plugins/brotli/squash.ini


# libbsc
%package plugin-bsc
Summary: libbsc plugin for Squash
Requires: squash
License: Apache 2.0 and MIT

%files plugin-bsc
%{_libdir}/squash/%{squash_api_version}/plugins/bsc/libsquash%{squash_api_version}-plugin-bsc.so
%{_libdir}/squash/%{squash_api_version}/plugins/bsc/squash.ini

%description plugin-bsc
libbsc plugin for Squash


# bzip2
%package plugin-bzip2
Summary: bzip2 plugin for Squash
Requires: squash bzip2-libs
License: zlib and MIT

%description plugin-bzip2
bzip2 plugin for Squash

%files plugin-bzip2
%{_libdir}/squash/%{squash_api_version}/plugins/bzip2/libsquash%{squash_api_version}-plugin-bzip2.so
%{_libdir}/squash/%{squash_api_version}/plugins/bzip2/squash.ini


# CRUSH
%package plugin-crush
Summary: CRUSH plugin for Squash
Requires: squash
License: Public Domain and MIT

%description plugin-crush
CRUSH plugin for Squash

%files plugin-crush
%{_libdir}/squash/%{squash_api_version}/plugins/crush/libsquash%{squash_api_version}-plugin-crush.so
%{_libdir}/squash/%{squash_api_version}/plugins/crush/squash.ini


# CSC
# %package plugin-csc
# Summary: CSC plugin for Squash
# Requires: squash
# License: Public Domain and MIT

# %description plugin-csc
# CSC plugin for Squash

# %files plugin-csc
# %{_libdir}/squash/%{squash_api_version}/plugins/csc/libsquash%{squash_api_version}-plugin-csc.so
# %{_libdir}/squash/%{squash_api_version}/plugins/csc/squash.ini


# DENSITY
# %package plugin-density
# Summary: DENSITY plugin for Squash
# Requires: squash
# License: 3-clause BSD and MIT

# %description plugin-density
# DENSITY plugin for Squash

# %files plugin-density
# %{_libdir}/squash/%{squash_api_version}/plugins/density/libsquash%{squash_api_version}-plugin-density.so
# %{_libdir}/squash/%{squash_api_version}/plugins/density/squash.ini


# Doboz
# %package plugin-doboz
# Summary: Doboz plugin for Squash
# Requires: squash
# License: zlib and MIT

# %description plugin-doboz
# Doboz plugin for Squash

# %files plugin-doboz
# %{_libdir}/squash/%{squash_api_version}/plugins/doboz/libsquash%{squash_api_version}-plugin-doboz.so
# %{_libdir}/squash/%{squash_api_version}/plugins/doboz/squash.ini


# FastARI
%package plugin-fari
Summary: FastARI plugin for Squash
Requires: squash
License: GPLv3+ and MIT

%description plugin-fari
FastARI plugin for Squash

%files plugin-fari
%{_libdir}/squash/%{squash_api_version}/plugins/fari/libsquash%{squash_api_version}-plugin-fari.so
%{_libdir}/squash/%{squash_api_version}/plugins/fari/squash.ini


# FastLZ
%package plugin-fastlz
Summary: FastLZ plugin for Squash
Requires: squash
License: MIT

%description plugin-fastlz
FastLZ plugin for Squash

%files plugin-fastlz
%{_libdir}/squash/%{squash_api_version}/plugins/fastlz/libsquash%{squash_api_version}-plugin-fastlz.so
%{_libdir}/squash/%{squash_api_version}/plugins/fastlz/squash.ini


# Gipfeli
%package plugin-gipfeli
Summary: Gipfeli plugin for Squash
Requires: squash
License: 3-clause BSD

%description plugin-gipfeli
Gipfeli plugin for Squash

%files plugin-gipfeli
%{_libdir}/squash/%{squash_api_version}/plugins/gipfeli/libsquash%{squash_api_version}-plugin-gipfeli.so
%{_libdir}/squash/%{squash_api_version}/plugins/gipfeli/squash.ini


# Heatshrink
%package plugin-heatshrink
Summary: Heatshrink plugin for Squash
Requires: squash
License: ISC and MIT

%description plugin-heatshrink
Heatshrink plugin for Squash

%files plugin-heatshrink
%{_libdir}/squash/%{squash_api_version}/plugins/heatshrink/libsquash%{squash_api_version}-plugin-heatshrink.so
%{_libdir}/squash/%{squash_api_version}/plugins/heatshrink/squash.ini


# libdeflate
%package plugin-libdeflate
Summary: libdeflate plugin for Squash
Requires: squash
License: Public Domain and MIT

%description plugin-libdeflate
libdeflate plugin for Squash

%files plugin-libdeflate
%{_libdir}/squash/%{squash_api_version}/plugins/libdeflate/libsquash%{squash_api_version}-plugin-libdeflate.so
%{_libdir}/squash/%{squash_api_version}/plugins/libdeflate/squash.ini


# LZ4
%package plugin-lz4
Summary: LZ4 plugin for Squash
Requires: squash lz4-devel
License: 3-clause BSD and MIT

%description plugin-lz4
LZ4 plugin for Squash

%files plugin-lz4
%{_libdir}/squash/%{squash_api_version}/plugins/lz4/libsquash%{squash_api_version}-plugin-lz4.so
%{_libdir}/squash/%{squash_api_version}/plugins/lz4/squash.ini


# liblzf
%package plugin-lzf
Summary: LZF plugin for Squash
Requires: squash
License: MIT and 2-clause BSD or GPLv2

%description plugin-lzf
LZF plugin for Squash

%files plugin-lzf
%{_libdir}/squash/%{squash_api_version}/plugins/lzf/libsquash%{squash_api_version}-plugin-lzf.so
%{_libdir}/squash/%{squash_api_version}/plugins/lzf/squash.ini


# LZFSE
%package plugin-lzfse
Summary: LZFSE plugin for Squash
Requires: squash
License: 3-clause BSD and MIT

%description plugin-lzfse
LZFSE plugin for Squash

%files plugin-lzfse
%{_libdir}/squash/%{squash_api_version}/plugins/lzfse/libsquash%{squash_api_version}-plugin-lzfse.so
%{_libdir}/squash/%{squash_api_version}/plugins/lzfse/squash.ini


# liblzg
%package plugin-lzg
Summary: liblzg plugin for Squash
Requires: squash
License: zlib and MIT

%description plugin-lzg
liblzg plugin for Squash

%files plugin-lzg
%{_libdir}/squash/%{squash_api_version}/plugins/lzg/libsquash%{squash_api_version}-plugin-lzg.so
%{_libdir}/squash/%{squash_api_version}/plugins/lzg/squash.ini


# LZHAM
%package plugin-lzham
Summary: LZHAM plugin for Squash
Requires: squash
License: MIT

%description plugin-lzham
LZHAMW plugin for Squash

%files plugin-lzham
%{_libdir}/squash/%{squash_api_version}/plugins/lzham/libsquash%{squash_api_version}-plugin-lzham.so
%{_libdir}/squash/%{squash_api_version}/plugins/lzham/squash.ini


# LZJB
%package plugin-lzjb
Summary: LZJB plugin for Squash
Requires: squash
License: CDDL and MIT

%description plugin-lzjb
LZJB plugin for Squash

%files plugin-lzjb
%{_libdir}/squash/%{squash_api_version}/plugins/lzjb/libsquash%{squash_api_version}-plugin-lzjb.so
%{_libdir}/squash/%{squash_api_version}/plugins/lzjb/squash.ini


# LZMA
%package plugin-lzma
Summary: LZMA plugin for Squash
Requires: squash xz-libs
License: Public Domain and MIT

%description plugin-lzma
LZMA plugin for Squash

%files plugin-lzma
%{_libdir}/squash/%{squash_api_version}/plugins/lzma/libsquash%{squash_api_version}-plugin-lzma.so
%{_libdir}/squash/%{squash_api_version}/plugins/lzma/squash.ini


# LZO
%package plugin-lzo
Summary: LZO plugin for Squash
Requires: squash lzo
License: GPLv2?+ and MIT

%description plugin-lzo
LZO plugin for Squash

%files plugin-lzo
%{_libdir}/squash/%{squash_api_version}/plugins/lzo/libsquash%{squash_api_version}-plugin-lzo.so
%{_libdir}/squash/%{squash_api_version}/plugins/lzo/squash.ini


# MiniZ
%package plugin-miniz
Summary: miniz plugin for Squash
Requires: squash
License: Public Domain and MIT

%description plugin-miniz
miniz plugin for Squash

%files plugin-miniz
%{_libdir}/squash/%{squash_api_version}/plugins/miniz/libsquash%{squash_api_version}-plugin-miniz.so
%{_libdir}/squash/%{squash_api_version}/plugins/miniz/squash.ini


# MS Compress
%package plugin-ms-compress
Summary: ms-compress plugin for Squash
Requires: squash
License: GPLv3+ and MIT

%description plugin-ms-compress
ms-compress plugin for Squash

%files plugin-ms-compress
%{_libdir}/squash/%{squash_api_version}/plugins/ms-compress/libsquash%{squash_api_version}-plugin-ms-compress.so
%{_libdir}/squash/%{squash_api_version}/plugins/ms-compress/squash.ini


# ncompress
%package plugin-ncompress
Summary: ncompress plugin for Squash
Requires: squash
License: Public Domain and MIT

%description plugin-ncompress
ncompress plugin for Squash

%files plugin-ncompress
%{_libdir}/squash/%{squash_api_version}/plugins/ncompress/libsquash%{squash_api_version}-plugin-ncompress.so
%{_libdir}/squash/%{squash_api_version}/plugins/ncompress/squash.ini


# QuickLZ
%package plugin-quicklz
Summary: QuickLZ plugin for Squash
Requires: squash
License: MIT and GPLv1, GPLv2, or GPLv3

%description plugin-quicklz
QuickLZ plugin for Squash

%files plugin-quicklz
%{_libdir}/squash/%{squash_api_version}/plugins/quicklz/libsquash%{squash_api_version}-plugin-quicklz.so
%{_libdir}/squash/%{squash_api_version}/plugins/quicklz/squash.ini


# Snappy
%package plugin-snappy
Summary: Snappy plugin for Squash
Requires: squash snappy
License: 3-clause BSD and MIT

%description plugin-snappy
Snappy plugin for Squash

%files plugin-snappy
%{_libdir}/squash/%{squash_api_version}/plugins/snappy/libsquash%{squash_api_version}-plugin-snappy.so
%{_libdir}/squash/%{squash_api_version}/plugins/snappy/squash.ini


# wfLZ
%package plugin-wflz
Summary: wfLZ plugin for Squash
Requires: squash
License: WTFPL and MIT

%description plugin-wflz
wfLZ plugin for Squash

%files plugin-wflz
%{_libdir}/squash/%{squash_api_version}/plugins/wflz/libsquash%{squash_api_version}-plugin-wflz.so
%{_libdir}/squash/%{squash_api_version}/plugins/wflz/squash.ini


# yalz77
%package plugin-yalz77
Summary: yalz77 plugin for Squash
Requires: squash
License: Public Domain and MIT

%description plugin-yalz77
yalz77 plugin for Squash

%files plugin-yalz77
%{_libdir}/squash/%{squash_api_version}/plugins/yalz77/libsquash%{squash_api_version}-plugin-yalz77.so
%{_libdir}/squash/%{squash_api_version}/plugins/yalz77/squash.ini


# zlib
%package plugin-zlib
Summary: zlib plugin for Squash
Requires: squash zlib
License: zlib and MIT

%description plugin-zlib
zlib plugin for Squash

%files plugin-zlib
%{_libdir}/squash/%{squash_api_version}/plugins/zlib/libsquash%{squash_api_version}-plugin-zlib.so
%{_libdir}/squash/%{squash_api_version}/plugins/zlib/squash.ini


# zlib-ng
%package plugin-zlib-ng
Summary: zlib-ng plugin for Squash
Requires: squash
License: zlib and MIT

%description plugin-zlib-ng
zlib-ng plugin for Squash

%files plugin-zlib-ng
%{_libdir}/squash/%{squash_api_version}/plugins/zlib-ng/libsquash%{squash_api_version}-plugin-zlib-ng.so
%{_libdir}/squash/%{squash_api_version}/plugins/zlib-ng/squash.ini


# zling
%package plugin-zling
Summary: zling plugin for Squash
Requires: squash
License: 3-clause BSD and MIT

%description plugin-zling
zling plugin for Squash

%files plugin-zling
%{_libdir}/squash/%{squash_api_version}/plugins/zling/libsquash%{squash_api_version}-plugin-zling.so
%{_libdir}/squash/%{squash_api_version}/plugins/zling/squash.ini


%package plugin-zpaq
Summary: ZPAQ plugin for Squash
Requires: squash zpaq-devel
License: Public Domain and MIT

%description plugin-zpaq
ZPAQ plugin for Squash

%files plugin-zpaq
%{_libdir}/squash/%{squash_api_version}/plugins/zpaq/libsquash%{squash_api_version}-plugin-zpaq.so
%{_libdir}/squash/%{squash_api_version}/plugins/zpaq/squash.ini


# zstd
%package plugin-zstd
Summary: zstd plugin for Squash
Requires: squash
%if 0%{?fedora} >= 25
Requires: libzstd
%else
Provides: bundled(zstd)
%endif
License: 2-clause BSD and MIT

%description plugin-zstd
zstd plugin for Squash

%files plugin-zstd
%{_libdir}/squash/%{squash_api_version}/plugins/zstd/libsquash%{squash_api_version}-plugin-zstd.so
%{_libdir}/squash/%{squash_api_version}/plugins/zstd/squash.ini


####
## Change Log
####

%changelog
* Thu Nov  3 2016 Evan Nemerson <evan@nemerson.com>
- Initial packaging

