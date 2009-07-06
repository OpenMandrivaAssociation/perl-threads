%define upstream_name    threads
%define upstream_version 1.73

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: Perl interpreter-based threads
License: GPL+ or Artistic
Group:   Development/Perl
Url:     http://search.cpan.org/dist/%{upstream_name}
Source0: http://search.cpan.org/CPAN/authors/id/J/JD/JDHEDDEN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::testlib)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(overload)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

