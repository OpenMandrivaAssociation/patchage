Name:       patchage
Version:    0.5.0
Release:    1
Summary:    A modular patch bay for audio and MIDI systems
License:    GPLv2+
Group:      Sound
Url:        http://drobilla.net/software/patchage/
Source0:    http://download.drobilla.net/%{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  waf
BuildRequires:  desktop-file-utils
BuildRequires:  flowcanvas-devel >= 0.5.1
BuildRequires:  libglademm2.4-devel >= 2.6.0
BuildRequires:  raul-devel >= 0.7.0
BuildRequires:  jackit-devel >= 0.107.0
BuildRequires:  libalsa-devel
BuildRequires:  lash-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  boost-devel

%description
Patchage is a modular patch bay for audio and MIDI systems based on
Jack, Lash, and Alsa.

%prep
%setup -q

%build
%setup_compile_flags
./waf configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir} \
    --libdir=%{_libdir} \
    --configdir=%{_sysconfdir} \
    --includedir=%{_includedir} \
    --mandir=%{_mandir} \
    --htmldir=%{_defaultdocdir}

./waf build

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot}

# fix desktop file
sed -i -e 's:;Audio:;Audio;:' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install    --remove-key=Encoding \
            --remove-category=Application \
            --dir %{buildroot}%{_datadir}/applications \
            %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg


%changelog
* Tue Jan 19 2010 Jérôme Brenier <incubusss@mandriva.org> 0.4.4-2mdv2010.1
+ Revision: 493881
- fix License tag
- import patchage


