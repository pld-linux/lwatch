Summary:	Colourizing a system logs for easier reading
Summary(pl):	Kolorowanie logów systemowych w celu ³atwiejszego czytania
Name:		lwatch
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	90b054c2ca334cf01a7586c8cff8ab17
URL:		http://sourceforge.net/projects/lwatch/
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/*
