Name:           jhbuild
Version:        3.12.0
Release:        1%{?dist}
Summary:        JHBuild is a tool designed to ease building colelctions of source packages

License:        GPL
URL:            https://wiki.gnome.org/Projects/Jhbuild
Source0:        jhbuild-3.12.0.tar.xz

#BuildRequires:
#Requires:

%description
JHBuild is a tool designed to ease building collections of source packages,
called “modules”. JHBuild uses “module set” files to describe the modules
available to build. The “module set” files include dependency information that
allows JHBuild to discover what modules need to be built and in what order.

JHBuild was originally written for building GNOME, but has since been extended
to be usable with other projects. A “module set” file can be hosted on a web
server, allowing for build rules independent of the JHBuild project.

JHBuild can build modules from a variety of sources, including CVS, Subversion,
Bazaar, Darcs, Git and Mercurial repositories, as well as Tar and Zip archives
hosted on web or FTP sites. JHBuild can build modules using a variety of build
systems, including Autotools, CMake, WAF, Python Distutils and Perl Makefiles.

JHBuild is not intended as a replacement for the distribution's package
management system. Instead, it makes it easy to build software into a separate
install prefix without interfering with the rest of the system.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc
%{_bindir}/*
%{python_sitelib}/*
%{_datadir}/*


%changelog
* Wed Feb 10 2016 Guillaume Poirier-Morency
- Initial import for the latest stable release of jhbuild
