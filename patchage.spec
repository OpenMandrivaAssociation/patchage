Summary:	A modular patch bay for audio and MIDI systems
Name:	patchage
Version: 	1.0.10
Release:		2
License:	GPLv3+
Group:	Sound
Url:	https://gitlab.com/drobilla/patchage
Source0:	https://gitlab.com/drobilla/patchage/-/archive/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	desktop-file-utils
BuildRequires:	meson
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.14.0
BuildRequires:	pkgconfig(gtkmm-2.4) >= 2.12.0
BuildRequires:	pkgconfig(ganv-1) >= 1.5.2
BuildRequires:	pkgconfig(jack)

%description
This is a modular patch bay for audio and MIDI systems based on Jack and Alsa.

%files
%license COPYING
%doc AUTHORS NEWS
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_iconsdir}/hicolor/*x*/apps/%{name}.svg

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%meson

%meson_build


%install
%meson_install

# Fix Exec line in the desktop file
desktop-file-edit --set-key=Exec \
								--set-value=%{name} \
								%{buildroot}%{_datadir}/applications/%{name}.desktop
