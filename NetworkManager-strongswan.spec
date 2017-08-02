Name:      NetworkManager-strongswan
Version:   1.4.0
Release:   5%{?dist}
Summary:   NetworkManager strongSwan IPSec VPN plug-in
License:   GPLv2+
Group:     System Environment/Base
URL:       https://www.strongswan.org/
Source0:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2

# Bring back the D-Bus policy until new charon-nm is released
Patch0: 0001-Revert-nm-Move-the-D-Bus-policy-to-charon-nm.patch

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
%patch0 -p1


%build
autoreconf -f -i
%configure --disable-static --with-charon=%{_libexecdir}/strongswan/charon-nm
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}


%files -f %{name}.lang
%{_prefix}/lib/NetworkManager/VPN/nm-strongswan-service.name
%{_sysconfdir}/dbus-1/system.d/nm-strongswan-service.conf
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
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0-2
- Bring back the D-Bus policy until new charon-nm is released

* Wed Sep 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0-1
- New upstream release that integrates our NetworkManager 1.2 support

* Wed Mar 30 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-3.20160330libnm
- Update the NetworkManager 1.2 support patchset

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3.20151023libnm
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-2.20151023libnm
- Add the NetworkManager 1.2 support patchset

* Mon Oct 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-1
- Initial packaging
