# $Id$
# Authority: dries
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graph-Easy

Summary: Create graphs
Name: perl-Graph-Easy
Version: 0.36
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graph-Easy/

Source: http://search.cpan.org/CPAN/authors/id/T/TE/TELS/graph/Graph-Easy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module let's you create graphs (nodes/vertices connected by edges/arcs,
not pie charts!) and then lay them out on a flat surface.

Once laid out, the graph can be converted into various output formats like
ASCII art, HTML or SVG. You can also output the graph in graphviz format
and let dot do the layout for you.

Graphs can be generated by Perl code, or parsed from a simple text format
that is human readable and maintainable.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Graph/Easy.pm
%{perl_vendorlib}/Graph/Easy/

%changelog
* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Initial package.
