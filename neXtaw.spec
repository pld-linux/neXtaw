Summary:	neXtaw is a replacement library for the Athena
Summary(pl):	neXtaw jest zamiennikiem biblioteki Athena
Name:		neXtaw
Version:	0.15.1
Release:	0.1
License:	GPL-like
Group:		Libraries
Source0:	http://siag.nu/pub/neXtaw/%{name}-%{version}.tar.gz
URL:		http://siag.nu/neXtaw/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
neXtaw is a replacement library for the Athena (libXaw) widget set. It
is based on Xaw3d, by Kaleb Keithley and is almost 100% backward
compatible with it. Its goal is to try to emulate the look and feel of
the N*XTSTEP GUI.

%description -l pl
#TODO

%package devel
Summary:	Header files for neXtaw library
Summary(pl):	Pliki nag³ówkowe biblioteki neXtaw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for neXtaw library.

%description devel -l pl
Pliki nag³ówkowe biblioteki neXtaw.

%package static
Summary:	Static neXtaw library
Summary(pl):	Statyczna biblioteka neXtaw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static neXtaw library.

%description static -l pl
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO doc/CHANGES doc/FAQ doc/README.XAW3D
%attr(755,root,root) %{_libdir}/lib*.so*

%files devel
%defattr(644,root,root,755)
%doc doc/app-defaults/*
%{_libdir}/lib*.la
%{_includedir}/X11/neXtaw

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
