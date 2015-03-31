Summary:	Multi-protocol, multi-mailbox mail watcher plugin for Xfce4 panel
Summary(pl.UTF-8):	Wtyczka powiadamiania o poczcie dla panelu Xfce4
Name:		xfce4-mailwatch-plugin
Version:	1.2.0
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mailwatch-plugin/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	7263114ec0f2987a3aff15afeeb45577
Patch0:		mbox-refresh-interval.patch
URL:		http://spuriousinterrupt.org/projects/xfce4-mailwatch-plugin/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	gnutls-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.8.0
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
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libmailwatch.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

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
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmailwatch.so
%{_datadir}/xfce4/panel/plugins/mailwatch.desktop
%{_iconsdir}/hicolor/*/apps/*
