Summary:	Colourizing a system logs for easier reading
Summary(pl):	Kolorowanie logów systemowych w celu ³atwiejszego czytania
Name:		lwatch
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	25e5778ac0199a02288a0caf1c13e21b
URL:		http://sourceforge.net/projects/lwatch/
# Should be used, but it's not:
#BuildRequires:	docbook-utils
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lwatch is a log parser/analyzer written in C with the PCRE library. It
is small and efficient. You are able to define your own colors using
regexp patterns. The biggest advantage compared to other tools written
in Perl is its speed.

%description -l pl
lwatch to analizator logów napisany w C z u¿yciem biblioteki PCRE.
Jest ma³y i wydajny. Pozwala definiowaæ w³asne kolory przy u¿yciu
wzorców bêd±cych wyra¿eniami regularnymi. Najwiêksz± zalet± w
porównaniu do innych narzêdzi, napisanych w Perlu, jest szybko¶æ.

%prep
%setup -q

%build
%configure \
	--enable-input=/var/lib/%{name}/syslog.fifo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%attr(750,root,root) %dir /var/lib/%{name}
%attr(640,root,root) /var/lib/%{name}/syslog.fifo
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
