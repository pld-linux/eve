Summary:	Eve - web browser based on the EFL and EWebKit
Summary(pl.UTF-8):	Eve - przeglądarka WWW oparta na bibliotekach EFL i EWebKit
Name:		eve
Version:	0.3.0
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://download.enlightenment.org/snapshots/2010-12-03/%{name}-%{version}.tar.bz2
# Source0-md5:	9367fd8347d04a98796a0197deeaecbe
Patch0:		%{name}-update.patch
Patch1:		%{name}-link.patch
URL:		http://trac.enlightenment.org/e/wiki/Eve
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1.6
BuildRequires:	e_dbus-devel
BuildRequires:	edje
BuildRequires:	elementary-devel >= 0.8.0
BuildRequires:	ewebkit-devel
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	elementary-libs >= 0.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eve is a web browser based on the EFL and EWebKit, aimed primarily to
be used on mobile devices with touch screens - but it works like a
charm on the desktop, too.

%description -l pl.UTF-8
Eve to przeglądarka WWW oparta na bibliotekach EFL i EWebKit,
przeznaczona przede wszystkim dla urządzeń przenośnych z ekranami
dotykowymi - ale wdzięcznie działająca także na zwykłych komputerach
biurkowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/eve.desktop
%{_pixmapsdir}/eve.png
