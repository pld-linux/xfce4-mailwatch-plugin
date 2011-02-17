Summary:	Multi-protocol, multi-mailbox mail watcher plugin for Xfce4 panel
Summary(pl.UTF-8):	Wtyczka powiadamiania o poczcie dla panelu Xfce4
Name:		xfce4-mailwatch-plugin
Version:	1.1.0
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://spuriousinterrupt.org/files/mailwatch/%{name}-%{version}.tar.bz2
# Source0-md5:	f84dce86be1d7f25f169f262aaacee4e
URL:		http://spuriousinterrupt.org/projects/xfce4-mailwatch-plugin/
BuildRequires:	gnutls-devel >= 1.2.0
BuildRequires:	libxfcegui4-devel >= 4.8.0
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-dirs >= 4.6
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce4 Mailwatch Plugin is a multi-protocol, multi-mailbox
mail watcher.
Currently, the protocols supported are:
  * IMAP (SSL/TLS and cleartext, CRAM-MD5)
  * POP3 (SSL/TLS and cleartext, CRAM-MD5)
  * Mbox mail spool (local)
  * Maildir mail spool (local)
  * MH-Maildir mail spool (local)
  * Google Mail (GMail) mailbox (remote)

%description -l pl.UTF-8
Wtyczka Mailwatch służy do powiadamiania o nadejściu nowej poczty,
Obecnie obsługuje następujące protokoły:
  * IMAP (SSL/TLS i czysty tekst, CRAM-MD5)
  * POP3 (SSL/TLS i czysty tekst, CRAM-MD5)
  * Mbox (lokalny)
  * Maildir (lokalny)
  * MH-Maildir (lokalny)
  * Google Mail (GMail) (zdalny)

%prep
%setup -q

%build
%configure \
	LIBS="$(pkg-config --libs libxfcegui4-1.0)" \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-mailwatch-plugin
%{_datadir}/xfce4/panel-plugins/mailwatch.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
