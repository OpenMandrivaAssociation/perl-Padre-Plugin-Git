%define upstream_name    Padre-Plugin-Git
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.11
Release:	1

Summary:	Simple Git interface for Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/Padre-Plugin-Git-0.11.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Test::More)
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
Simple Git interface for Padre.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
xvfb-run perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#xvfb-run make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 653610
- rebuild for updated spec-helper

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 572236
- update to 0.03

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 444126
- running makefile.pl in a virtual frame buffer
- skipping tests
- running tests in a virtual frame-buffer
- import perl-Padre-Plugin-Git


* Thu Sep 17 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

