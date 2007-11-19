# $Id$
# Authority: dries
# Upstream: Ash Berlin, C<ash$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-File

Summary: File based storage model for Catalyst
Name: perl-Catalyst-Model-File
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-File/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Model-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1 
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl >= 2:5.8.1 

%description
File based storage model for Catalyst.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Catalyst::Model::File.3pm*
%doc %{_mandir}/man3/Catalyst::Helper::Model::File.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Helper/
%dir %{perl_vendorlib}/Catalyst/Helper/Model/
#%{perl_vendorlib}/Catalyst/Helper/Model/File/
%{perl_vendorlib}/Catalyst/Helper/Model/File.pm
%dir %{perl_vendorlib}/Catalyst/Model/
#%{perl_vendorlib}/Catalyst/Model/File/
%{perl_vendorlib}/Catalyst/Model/File.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
