%define name		libdvbpsi
%define version		1.3.3
%define release		1

%define lib_name	%{name}

%define redhat 1
%if %redhat
# some mdk macros that do not exist in rh
%define configure2_5x CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=%{_libdir}
%define make %__make
%define makeinstall_std %__make DESTDIR="$RPM_BUILD_ROOT" install
# adjust define for Redhat.
%endif

Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections.
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2.1
URL:		http://developers.videolan.org/libdvbpsi/
Group:		System/Libraries
Source:		http://www.videolan.org/pub/videolan/libdvbpsi/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root
Provides:	%name
Prefix:         /usr

%description
libdvbpsi is a simple library designed for MPEG 2 TS and DVB PSI tables
decoding and generating. The important features are:
 * PAT decoder and genarator.
 * PMT decoder and generator.

%package -n %{lib_name}-devel
Summary:	Development tools for programs which will use the libdvbpsi library.
Group:		Development/C
Provides:	%name-devel = %version-%release
Requires:	%{lib_name} = %version-%release

%description -n %{lib_name}-devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will manipulate MPEG 2 and DVB PSI
information using the %{name} library.

If you are going to develop programs which will manipulate MPEG 2 and DVB PSI
information you should install %{name}-devel.  You'll also need to have
the %name package installed.

%prep
%setup -q -n %{lib_name}-%{version}

%build
%configure2_5x --enable-release
%make 

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING ChangeLog
%{_libdir}/*.so.*
%{_libdir}/*.so

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc COPYING NEWS
%{_libdir}/*a
%{_libdir}/pkgconfig/libdvbpsi.pc
%{_includedir}/*

%changelog
* Thu Aug 22 2019 Jean-Paul Saman <jpsaman@videolan.org - 1.3.3
- bugfixes

* Mon Oct 16 2017 Jean-Paul Saman <jpsaman@videolan.org - 1.3.2
- bugfixes

* Tue Feb 7 2017 Jean-Paul Saman <jpsaman@videolan.org - 1.3.1
- bugfixes

* Thu Mar 26 2015 Jean-Paul Saman <jpsaman@videolan.org> - 1.3.0
- bugfixes and new descriptors

* Thu Apr 21 2011 Jean-Paul Saman <jpsaman@videolan.org>
- Correctly build rpm package on x86_64
- Enable debug symbols in build (usefull for %name-debuginfo package)

* Fri Nov 19 2010 Jean-Paul Saman <jpsaman@videolan.org>
- Relicensed under LGPLv2.1

* Fri Apr 23 2010 Jean-Paul Saman <jpsaman@videolan.org>
- generalized libdvbpsi.spec

* Tue Apr 13 2010 Jean-Paul Saman <jpsaman@videolan.org>
- add pkgconfig file libdvbpsi.pc
- removed packager and vendor from specfile, these should
  be supplied by the package builder from ~/.rpmmacros

* Tue Dec 18 2007 Jean-Paul Saman <jpsaman@videolan.org>
- New VBI data descriptor support
- 0.1.7 release

* Thu Oct 22 2007 Jean-Paul Saman <jpsaman@videolan.org>
- New cat support
- Fix EIT discontinuities
- new example tool for checking an MPEG-2 TS file
- 0.1.6 release

* Thu Sep 22 2005 Jean-Paul Saman <jpsaman@videolan.org>
- Remove conflicting redefine of release
- Fix typo's

* Wed Jul 6 2005 Sam Hocevar <sam+rpm@zoy.org>
- 0.1.5 release.

* Fri Jan 2 2004 Sam Hocevar <sam@zoy.org>
- 0.1.4 release.

* Tue Jul 29 2003 Yves Duret <yves@zarb.org>
- 0.1.3 release.

* Fri Dec 13 2002 Yves Duret <yves@zarb.org> 0.1.2-2mdk
- s#Copyright#License#
- include the libtool .la files.
- use macros.
- update URL: tag.

* Fri Oct 11 2002 Samuel Hocevar <sam@zoy.org>
- 0.1.2 release.

* Sat May 18 2002 Arnaud de Bossoreille de Ribou <bozo@via.ecp.fr>
- 0.1.1 release.

* Mon Apr 8 2002 Arnaud de Bossoreille de Ribou <bozo@via.ecp.fr>
- split into two separate packages.

* Thu Apr 4 2002 Jean-Paul Saman <saman@natlab.research.philips.com>
- first version of package for redhat systems.

