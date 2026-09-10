%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Name:		kdominate
Version:	26.08.1
Release:	1
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Tactical tile-control game
URL:		https://apps.kde.org/kdominate/
License:	GPLv2+
Group:		Games
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KDEGames6)

%description
KDominate is a tactical game for one or two players. Players place
and convert tiles with the goal of controlling the majority of the
board.

%files -f %{name}.lang
%{_bindir}/kdominate
%{_datadir}/applications/org.kde.kdominate.desktop
%{_datadir}/config.kcfg/kdominate.kcfg
%{_datadir}/icons/hicolor/*/apps/kdominate.png
%{_datadir}/metainfo/org.kde.kdominate.metainfo.xml
%{_datadir}/qlogging-categories6/kdominate.*
