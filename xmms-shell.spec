Summary:	XMMS-Shell is a simple utility for controlling XMMS externally
Summary(pl):	XMMS-Shell to proste narzêdzie do zewnêtrznej kontroli XMMS-a
Name:		xmms-shell
Version:	0.99.3
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sourceforge/xmms-shell/%{name}-%{version}.tar.gz
# Source0-md5:	7c59ff584ae146282259fd6cdc8fe669
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
more. XMMS-Shell is intended to make up for these defficiencies.

%description -l pl
XMMS-Shell to proste narzêdzie do zewnêtrznej kontroli XMMS-a. Pomimo
¿e sam XMMS udostêpnia podobn± funkcjonalno¶æ, brakuje mu kilku
wa¿nych poleceñ, pozwalaj±cych na wykonywanie niektórych zadañ, takich
jak kontrola g³o¶no¶ci, ³atwe modyfikowanie playlisty itp. XMMS-Shell
ma za zadanie wyeliminowanie tych utrudnieñ.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
aclocal
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
