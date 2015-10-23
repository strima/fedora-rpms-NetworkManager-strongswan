Name:      NetworkManager-strongswan
Version:   1.3.1
Release:   1%{?dist}
Summary:   NetworkManager strongSwan IPSec VPN plug-in
License:   GPLv2+
Group:     System Environment/Base
URL:       https://www.strongswan.org/
Source0:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(dbus-glib-1) >= 0.30
BuildRequires: pkgconfig(gtk+-2.0) >= 2.6
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(NetworkManager) >= 0.9.0
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-glib-vpn)
BuildRequires: intltool

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
%configure --disable-static --with-charon=%{_libexecdir}/strongswan/charon-nm
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}


%files -f %{name}.lang
%{_sysconfdir}/NetworkManager/VPN/nm-strongswan-service.name
%{_sysconfdir}/dbus-1/system.d/nm-strongswan-service.conf
%{_libexecdir}/nm-strongswan-auth-dialog
%doc NEWS


%files gnome
%{_datadir}/gnome-vpn-properties/strongswan
%{_libdir}/NetworkManager/libnm-strongswan-properties.so
%exclude %{_libdir}/NetworkManager/libnm-strongswan-properties.la


%changelog
* Mon Oct 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-1
- Initial packaging
