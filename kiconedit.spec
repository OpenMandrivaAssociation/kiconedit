Summary:	KDE Icon Editor
Name:		kiconedit
Version: 	4.4.0
Release: 	2
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%name-%version.tar.bz2
License: 	GPLv2+
Group: 		Graphics
Url: 		https://www.kde.org
BuildRequires: 	kdelibs4-devel
%if %mdkversion < 200900
Obsoletes: 	kdegraphics-kiconedit < 1:3.5.10-3
Conflicts:	kde-l10n < 3.5.9-5
%endif
%if %mdkversion < 200100
Obsoletes:  kdegraphics3-kiconedit < 1:3.5.10-5
%endif

%description 
KDE Icon Editor.

%files -f %name.lang
%doc AUTHORS COPYING COPYING.DOC NEWS
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q
sed -i -e 's#<!DOCTYPE book PUBLIC "-//KDE//DTD DocBook XML V4\.1\.2-Based Variant V1\.1//EN" "dtd/kdex\.dtd" \[#<!DOCTYPE book PUBLIC "-//KDE//DTD DocBook XML V4.2-Based Variant V1.1//EN" "dtd/kdex.dtd" [#g' doc-translations/*_kiconedit/*/index.docbook
    
%build
%cmake_kde4
%make

%install
cd build
%{makeinstall_std}
cd -

%find_lang %name --with-html



