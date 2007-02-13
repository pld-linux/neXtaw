Summary:	neXtaw - a replacement library for the Athena
Summary(pl.UTF-8):	neXtaw - zamiennik biblioteki Athena
Name:		neXtaw
Version:	0.15.1
Release:	0.1
License:	GPL-like
Group:		Libraries
Source0:	http://siag.nu/pub/neXtaw/%{name}-%{version}.tar.gz
URL:		http://siag.nu/neXtaw/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xincludedir	/usr/X11R6/include

%description
neXtaw is a replacement library for the Athena (libXaw) widget set. It
is based on Xaw3d, by Kaleb Keithley and is almost 100% backward
compatible with it. Its goal is to try to emulate the look and feel of
the N*XTSTEP GUI.

%description -l pl.UTF-8
neXtaw to zamiennik biblioteki zestawu widgetów Athena (libXaw). Jest
oparty na Xaw3d Kaleba Keithleya i jest z nią prawie w 100% wstecznie
kompatybilna. Celem jest próba emulacji wyglądu i zachowania GUI
N*XTSTEP.

%package devel
Summary:	Header files for neXtaw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki neXtaw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for neXtaw library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki neXtaw.

%package static
Summary:	Static neXtaw library
Summary(pl.UTF-8):	Statyczna biblioteka neXtaw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static neXtaw library.

%description static -l pl.UTF-8
Statyczna biblioteka neXtaw.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_xincludedir}
mv $RPM_BUILD_ROOT%{_includedir}/X11 $RPM_BUILD_ROOT%{_xincludedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO doc/CHANGES doc/FAQ doc/README.XAW3D
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/app-defaults/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_xincludedir}/X11/neXtaw

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
