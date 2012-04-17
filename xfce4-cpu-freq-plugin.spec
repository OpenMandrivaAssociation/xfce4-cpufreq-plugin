%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Cpu-freq plugin for Xfce desktop
Name:		xfce4-cpufreq-plugin
Version:	1.0.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpufreq-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:  xfce4-panel-devel >= 4.8.0
BuildRequires:	libxfcegui4-devel >= 4.8.0
BuildRequires:	libxfce4util-devel >= 4.8.0
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-cpu-freq-plugin
Obsoletes:	xfce4-cpu-freq-plugin <= 0.0.1-11
Provides:	xfce4-cpu-freq-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
CPU freq plugin for the Xfce Desktop Environment. It provides a
simple system for managing the frequency of the CPU.

%prep
%setup -q


%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
