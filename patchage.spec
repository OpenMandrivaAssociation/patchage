Name:		patchage
Version:	0.4.4
Release:	%mkrel 3
Summary:	A modular patch bay for audio and MIDI systems
License:	GPLv2+
Group:		Sound
Url:		http://drobilla.net/software/patchage/
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	waf
BuildRequires:	desktop-file-utils
BuildRequires:	flowcanvas-devel >= 0.5.1
BuildRequires:	libglademm2.4-devel >= 2.6.0
BuildRequires:	raul-devel >= 0.5.1
BuildRequires:	jackit-devel >= 0.107.0
BuildRequires:	libalsa-devel
BuildRequires:	lash-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	boost-devel

%description
Patchage is a modular patch bay for audio and MIDI systems based on 
Jack, Lash, and Alsa.

%prep
%setup -q

%build
%setup_compile_flags
%__waf configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--configdir=%{_sysconfdir} \
	--includedir=%{_includedir} \
	--mandir=%{_mandir} \
	--htmldir=%{_defaultdocdir}

%__waf build

%install
rm -rf %{buildroot}
%waf_install

# fix desktop file
sed -i -e 's:;Audio:;Audio;:' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install	--remove-key=Encoding \
			--remove-category=Application \
			--dir %{buildroot}%{_datadir}/applications \
			%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
