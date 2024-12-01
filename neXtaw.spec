Summary:	neXtaw - a replacement library for the Athena
Summary(pl.UTF-8):	neXtaw - zamiennik biblioteki Athena
Name:		neXtaw
Version:	0.15.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://siag.nu/pub/neXtaw/%{name}-%{version}.tar.gz
# Source0-md5:	1c9cbcef735d8e26f3e48bd529aca6a7
URL:		http://siag.nu/neXtaw/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel

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

install -d app-defaults-examples
cp -p doc/app-defaults/* app-defaults-examples
%{__rm} app-defaults-examples/Makefile*

%build
%configure \
	LIBS="-lXt -lX11"
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
%doc AUTHORS COPYING ChangeLog README TODO doc/{CHANGES,FAQ,README.XAW3D} app-defaults-examples
%attr(755,root,root) %{_libdir}/libneXtaw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libneXtaw.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libneXtaw.so
%{_libdir}/libneXtaw.la
%{_includedir}/X11/neXtaw

%files static
%defattr(644,root,root,755)
%{_libdir}/libneXtaw.a
