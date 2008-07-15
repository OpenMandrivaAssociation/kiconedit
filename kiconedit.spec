Summary:	KDE Icon Editor
Name:		kiconedit
Version: 	4.0.98
Release: 	%mkrel 1
Source0: 	http://fr2.rpmfind.net/linux/KDE/unstable/4.0.98/src/extragear/%name-%version.tar.bz2
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
Conflicts:	kdegraphics-kiconedit < 1:3.5.9-8

%description 
KDE Icon Editor.

%if %mdkversion < 200900
%post
/sbin/ldconfig
%update_menus

%postun
/sbin/ldconfig
%update_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
