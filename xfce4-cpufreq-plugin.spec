%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	Cpu-freq plugin for Xfce desktop
Name:		xfce4-cpufreq-plugin
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpufreq-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires: 	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-cpu-freq-plugin
Obsoletes:	xfce4-cpu-freq-plugin <= 0.0.1-11
Provides:	xfce4-cpu-freq-plugin

%description
CPU freq plugin for the Xfce Desktop Environment. It provides a
simple system for managing the frequency of the CPU.

%prep
%setup -q


%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libcpufreq.so*
%{_datadir}/xfce4/panel/plugins/cpufreq.desktop
%{_iconsdir}/*/*/apps/xfce4-cpufreq-plugin.png

