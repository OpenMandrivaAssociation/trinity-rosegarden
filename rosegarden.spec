%bcond clang 1
%bcond lirc 1
%bcond gamin 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg rosegarden
%define tde_prefix /opt/trinity


%define _disable_ld_no_undefined 1

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.7.0
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Music editor and MIDI/audio sequencer [Trinity]
Group:		Applications/Multimedia
URL:		http://www.rosegardenmusic.com/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWANT_SOUND=ON
BuildOption:    -DWANT_JACK=ON
BuildOption:    -DWANT_DSSI=ON
BuildOption:    -DWANT_LIRC=%{!?with_lirc:OFF}%{?with_lirc:ON} 
BuildOption:    -DWANT_PCH=OFF
BuildOption:    -DWANT_TEST=OFF
BuildOption:    -DWANT_DEBUG=OFF
BuildOption:    -DWANT_FULLDBG=OFF
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires: libtool

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:	fftw-devel
BuildRequires:	fontconfig-devel

# LO support
BuildRequires:  pkgconfig(liblo)

# DSSI support
BuildRequires:  pkgconfig(dssi)

# LRDF support
BuildRequires:  pkgconfig(lrdf)

# LADSPA support
BuildRequires:	ladspa-devel

# RAPTOR support
BuildRequires:  pkgconfig(raptor)

# JACK support
BuildRequires:  pkgconfig(jack)

# ACL support
BuildRequires:  pkgconfig(libacl)

# LIRC support
%{?with_lirc:BuildRequires:	pkgconfig(lirc)}

# IDN support
BuildRequires:  pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:  pkgconfig(gamin)}

Requires:		lilypond
Requires:		perl-XML-Twig

Requires:		libsndfile-progs

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


Requires:		%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Rosegarden is a TDE application which provides a mixed Audio/MIDI
sequencer (for playback and recording), a multi-track editor, music
editing using both piano-roll and score notation, MIDI file IO,
lilypond and Csound files export, etc.

%package data
Group:			Applications/Multimedia
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:		music editor and MIDI/audio sequencer data files [Trinity]

%description data
Rosegarden is a TDE application which provides a mixed Audio/MIDI
sequencer (for playback and recording), a multi-track editor, music
editing using both piano-roll and score notation, MIDI file IO,
lilypond and Csound files export, etc.

This package provides the data files necessary for running Rosegarden


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
# Unwanted files
%__rm -f %{?buildroot}%{tde_prefix}/%{_lib}/*.a

%find_lang %{tde_pkg}


%files
%defattr(-,root,root,-)
%{tde_prefix}/bin/rosegarden
%{tde_prefix}/bin/rosegarden-audiofile-importer
%{tde_prefix}/bin/rosegarden-lilypondview
%{tde_prefix}/bin/rosegarden-project-package
%{tde_prefix}/bin/rosegardensequencer
%{tde_prefix}/share/man/man1/rosegarden-audiofile-importer.1*
%{tde_prefix}/share/man/man1/rosegarden-lilypondview.1*
%{tde_prefix}/share/man/man1/rosegarden-project-package.1*
%{tde_prefix}/share/man/man1/rosegarden.1*

%files data -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_prefix}/share/applications/tde/rosegarden.desktop
%{tde_prefix}/share/apps/profiles/rosegarden.profile.xml
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/rosegarden
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/rosegarden
%lang(ja) %{tde_prefix}/share/doc/tde/HTML/ja/rosegarden
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/rosegarden
%{tde_prefix}/share/apps/rosegarden
%{tde_prefix}/share/icons/hicolor/*/*/*
%{tde_prefix}/share/icons/locolor/*/*/*
%{tde_prefix}/share/mimelnk/audio/x-rosegarden-device.desktop
%{tde_prefix}/share/mimelnk/audio/x-rosegarden.desktop
%{tde_prefix}/share/mimelnk/audio/x-rosegarden21.desktop
%{tde_prefix}/share/mimelnk/audio/x-soundfont.desktop

