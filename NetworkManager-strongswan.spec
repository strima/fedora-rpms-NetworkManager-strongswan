Name:      NetworkManager-strongswan
Version:   1.4.0
Release:   1%{?dist}
Summary:   NetworkManager strongSwan IPSec VPN plug-in
License:   GPLv2+
Group:     System Environment/Base
URL:       https://www.strongswan.org/
Source0:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(dbus-glib-1) >= 0.30
BuildRequires: pkgconfig(gtk+-2.0) >= 2.6
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(NetworkManager) >= 1.1.0
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-glib-vpn)
BuildRequires: pkgconfig(libnm) >= 1.1.0
BuildRequires: pkgconfig(libnm-gtk)
BuildRequires: pkgconfig(libnma) >= 1.1.0
BuildRequires: intltool
BuildRequires: autoconf libtool

Requires: NetworkManager
Requires: %{_libexecdir}/strongswan/charon-nm

%global _privatelibs libnm-openswan-properties[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
This package contains software for integrating the strongSwan IPSec VPN
with NetworkManager.


%package gnome
Summary: NetworkManager VPN plugin for strongswan - GNOME files
Group:   System Environment/Base

Requires: NetworkManager-strongswan = %{version}-%{release}
Requires: nm-connection-editor

%description gnome
This package contains software for integrating the strongSwan IPSec VPN
with the graphical desktop.


%prep
%setup -q


%build
autoreconf -f -i
%configure --disable-static --with-charon=%{_libexecdir}/strongswan/charon-nm
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}


%files -f %{name}.lang
%{_prefix}/lib/NetworkManager/VPN/nm-strongswan-service.name
%{_libexecdir}/nm-strongswan-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan.so
%exclude %{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan.la
%doc NEWS


%files gnome
%{_sysconfdir}/NetworkManager/VPN/nm-strongswan-service.name
%{_datadir}/gnome-vpn-properties/strongswan
%{_datadir}/appdata/NetworkManager-strongswan.appdata.xml
%{_libdir}/NetworkManager/libnm-strongswan-properties.so
%exclude %{_libdir}/NetworkManager/libnm-strongswan-properties.la


%changelog
* Wed Sep 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0
- New upstream release that integrates our NetworkManager 1.2 support

* Wed Mar 30 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-3.20160330libnm
- Update the NetworkManager 1.2 support patchset

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3.20151023libnm
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-2.20151023libnm
- Add the NetworkManager 1.2 support patchset

* Mon Oct 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-1
- Initial packaging
