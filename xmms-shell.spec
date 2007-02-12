Summary:	XMMS-Shell is a simple utility for controlling XMMS externally
Summary(pl.UTF-8):	XMMS-Shell to proste narzędzie do zewnętrznej kontroli XMMS-a
Name:		xmms-shell
Version:	0.99.3
Release:	3
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/xmms-shell/%{name}-%{version}.tar.gz
# Source0-md5:	7c59ff584ae146282259fd6cdc8fe669
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-playlist.patch
Patch2:		%{name}-shuffle.patch
URL:		http://www.loganh.com/xmms-shell/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS-Shell is a simple utility for controlling XMMS externally.
Although XMMS itself provides some similar functionality, XMMS lacks a
few important command line options to allow one to perform certain
tasks, such as volume control, easily manipulating a playlist, and
more. XMMS-Shell is intended to make up for these deficiencies.

%description -l pl.UTF-8
XMMS-Shell to proste narzędzie do zewnętrznej kontroli XMMS-a. Pomimo
że sam XMMS udostępnia podobną funkcjonalność, brakuje mu kilku
ważnych poleceń, pozwalających na wykonywanie niektórych zadań, takich
jak kontrola głośności, łatwe modyfikowanie playlisty itp. XMMS-Shell
ma za zadanie wyeliminowanie tych utrudnień.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/xmms-shell
%{_mandir}/man1/xmms-shell.1*
