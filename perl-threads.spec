%define upstream_name    threads
%define upstream_version 1.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary: Perl interpreter-based threads
License: GPL+ or Artistic
Group:   Development/Perl
Url:     http://search.cpan.org/dist/%{upstream_name}
Source0: http://search.cpan.org/CPAN/authors/id/J/JD/JDHEDDEN/threads-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::testlib)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(overload)
BuildRequires: perl-devel

Provides:  perl(threads)

%description
Perl 5.6 introduced something called interpreter threads. Interpreter
threads are different from _5005threads_ (the thread model of Perl 5.005)
by creating a new Perl interpreter per thread, and not sharing any data or
state between threads by default.

Prior to Perl 5.8, this has only been available to people embedding Perl,
and for emulating fork() on Windows.

The _threads_ API is loosely based on the old Thread.pm API. It is very
important to note that variables are not shared between threads, all
variables are by default thread local. To use shared variables one must
also use the threads::shared manpage:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.810.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.810.0-1mdv2011.0
+ Revision: 596734
- update to 1.81

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.770.0-3mdv2011.0
+ Revision: 562464
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.770.0-2mdv2011.0
+ Revision: 555202
- rebuild for 5.12

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.770.0-1mdv2010.1
+ Revision: 527742
- update to 1.77
- add missing buildrequires:
- update to 1.76

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.750.0-1mdv2010.1
+ Revision: 471061
- update to 1.75

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.740.0-2mdv2010.0
+ Revision: 420991
- rebuild
- update to 1.74

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.740.0-1mdv2010.0
+ Revision: 416987
- update to 1.74

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.730.0-1mdv2010.0
+ Revision: 392732
- update to 1.73
- using %%perl_convert_version
- fixed license field

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.72-1mdv2010.0
+ Revision: 372412
- update to new version 1.72
- update source url

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.71-3mdv2010.0
+ Revision: 372408
- rebuild

* Sat Jan 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.71-2mdv2009.1
+ Revision: 330688
- forcing missing provide - man, when are we going to remove this
  find-provides-but-remove-lowercase-ones stupidity? lowercase module
  names are totally legit within perl, so why are we filtering them out?!

* Sat Jan 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.71-1mdv2009.1
+ Revision: 330591
- import perl-threads


* Sat Jan 17 2009 cpan2dist 1.71-1mdv
- initial mdv release, generated with cpan2dist





