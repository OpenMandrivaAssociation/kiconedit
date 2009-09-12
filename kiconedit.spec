Summary:	KDE Icon Editor
Name:		kiconedit
Version: 	4.3.0
Release: 	%mkrel 1
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%name-%version.tar.bz2
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
%if %mdkversion < 200900
Obsoletes: 	kdegraphics-kiconedit < 1:3.5.10-3
Conflicts:	kde-l10n < 3.5.9-5
%endif
%if %mdkversion < 200900
Obsoletes:  kdegraphics3-kiconedit < 1:3.5.10-5
%endif

%description 
KDE Icon Editor.

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
