Summary:	XMMS-Shell is a simple utility for controlling XMMS externally.
#Summary(pl):
Name:		xmms-shell
Version:	0.99.0
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://telia.dl.sourceforge.net/sourceforge/xmms-shell/%{name}-%{version}.tar.gz
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

#%description -l pl
#

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
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/xmms-shell
