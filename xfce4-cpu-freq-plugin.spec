%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Cpu-freq plugin for Xfce desktop
Name:		xfce4-cpufreq-plugin
Version:	1.1.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpufreq-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires: 	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
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
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-3mdv2012.0
+ Revision: 791522
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-2
+ Revision: 790048
- Rebuild

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1
+ Revision: 632769
- update to new version 1.0.0
- fix url for Source0
- package locales
- drop old scriplets
- fix file list

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-11mdv2011.0
+ Revision: 615573
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-10mdv2010.1
+ Revision: 543420
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.0.1-9mdv2010.0
+ Revision: 445979
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-8mdv2009.1
+ Revision: 349447
- rebuild for xfce-4.6.0

* Fri Jan 02 2009 Jérôme Soyer <saispo@mandriva.org> 0.0.1-7mdv2009.1
+ Revision: 323288
- Rewind...
- Change name and rebuild
- Readd current directory

