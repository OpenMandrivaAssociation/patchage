Name:       patchage
Version:    1.0.10
Release:    1
Summary:    A modular patch bay for audio and MIDI systems
License:    GPLv2+
Group:      Sound
Url:        http://drobilla.net/software/patchage/
Source0:    http://download.drobilla.net/%{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  meson
BuildRequires:  desktop-file-utils
#BuildRequires:  flowcanvas-devel >= 0.5.1
BuildRequires:  pkgconfig(libglademm-2.4) >= 2.6.0
#BuildRequires:  raul-devel >= 0.7.0
BuildRequires:  pkgconfig(jack) >= 0.107.0
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(lash-1.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ganv-1)
BuildRequires:  pkgconfig(fmt)

%description
Patchage is a modular patch bay for audio and MIDI systems based on
Jack, Lash, and Alsa.

%prep
%setup -q

%build
%meson

%meson_build

%install
%meson_install

%files
%defattr(-,root,root,-)
%doc AUTHORS
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/patchage.mo
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_iconsdir}/hicolor/*x*/apps/patchage.svg


%changelog
* Tue Jan 19 2010 Jérôme Brenier <incubusss@mandriva.org> 0.4.4-2mdv2010.1
+ Revision: 493881
- fix License tag
- import patchage


