Name:      NetworkManager-strongswan
Version:   1.3.1
Release:   2.20151023libnm%{?dist}
Summary:   NetworkManager strongSwan IPSec VPN plug-in
License:   GPLv2+
Group:     System Environment/Base
URL:       https://www.strongswan.org/
Source0:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2

# https://github.com/strongswan/strongswan/pull/15
Patch1:    0001-nm-set-full-path-to-the-connection-editor-plugin.patch
Patch2:    0002-nm-drop-some-unneeded-dependencies.patch
Patch3:    0003-nm-drop-useless-calls-to-AC_SUBST.patch
Patch4:    0004-nm-split-the-plugin-into-two-halves.patch
Patch5:    0005-nm-check-for-libnm.patch
Patch6:    0006-nm-port-to-libnm.patch
Patch7:    0007-nm-replace-libgnomeui-with-libnma-for-password-dialo.patch
Patch8:    0008-nm-replace-libgnomekeyring-with-libsecret.patch
Patch9:    0009-nm-bump-to-GTK-3.0.patch
Patch10:   0010-nm-bump-minor-version-to-1.4.0.patch
Patch11:   0011-nm-install-the-.name-file-into-usr-lib-NetworkManage.patch

BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(dbus-glib-1) >= 0.30
BuildRequires: pkgconfig(gtk+-2.0) >= 2.6
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(NetworkManager) >= 1.1.0
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-glib-vpn)
BuildRequires: pkgconfig(libnm) >= 1.1.0
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1


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
%{_libdir}/NetworkManager/libnm-strongswan-properties.so
%exclude %{_libdir}/NetworkManager/libnm-strongswan-properties.la


%changelog
* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-2.20151023libnm
- Add the NetworkManager 1.2 support patchset

* Mon Oct 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-1
- Initial packaging
