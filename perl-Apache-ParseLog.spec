#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Apache
%define		pnam	ParseLog
Summary:	Apache::ParseLog - object-oriented Perl extension for parsing Apache log files
Summary(pl.UTF-8):	Apache::ParseLog - obiektowy moduł Perla do analizowania logów Apache
Name:		perl-Apache-ParseLog
Version:	1.02
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92bd6a964a55e8f7cf0f50dbf77a5280
URL:		http://search.cpan.org/dist/Apache-ParseLog/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::ParseLog provides an easy way to parse the Apache log files,
using object-oriented constructs. The data obtained using this module
are generic enough that it is flexible to use the data for your own
applications, such as CGI, simple text-only report generater, feeding
RDBMS, data for Perl/Tk-based GUI application, etc.

%description -l pl.UTF-8
Apache::ParseLog udostępnia łatwy sposób na analizowanie logów Apache
przy użyciu konstrukcji zorientowanych obiektowo. Dane, uzyskane przy
użyciu tego modułu są na tyle ogólne, że można ich w elastyczny sposób
używać we własnych aplikacjach, takich, jak CGI, proste tekstowe
generatory raportów, karmienie RDBMS, dane dla bazowanych na Perl/Tk
aplikacji GUI, itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
