#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-MockTime
Version  : 0.17
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/D/DD/DDICK/Test-MockTime-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DD/DDICK/Test-MockTime-0.17.tar.gz
Summary  : 'Replaces actual time with simulated time '
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Test::MockTime - Replaces actual time with simulated time
VERSION
Version 0.17

%package dev
Summary: dev components for the perl-Test-MockTime package.
Group: Development
Provides: perl-Test-MockTime-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-MockTime package.


%prep
%setup -q -n Test-MockTime-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/MockTime.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::MockTime.3
