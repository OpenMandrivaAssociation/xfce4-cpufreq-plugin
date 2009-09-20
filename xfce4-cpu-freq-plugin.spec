Summary:	Cpu-freq plugins for Xfce desktop
Name:		xfce4-cpufreq-plugin
Version:	0.0.1
Release:	%mkrel 9
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-cpufreq-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:  xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-cpu-freq-plugin
Obsoletes:	xfce4-cpu-freq-plugin < 0.0.1-6
Provides:	xfce4-cpu-freq-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
cpu freq plugin for the Xfce Desktop Environment. It provides a
simple system for managing the frequency of the CPU.

%prep
%setup -qn xfce4-cpu-freq-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
