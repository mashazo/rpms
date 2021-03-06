# $Id$
# Authority: cmr

Summary: Nagios plugin to store Nagios data in a relational database 
Name: ndoutils
Version: 1.4
Release: 0.beta8.1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.nagios.org/

Source: http://downloads.sourceforge.net/project/nagios/ndoutils-1.x/ndoutils-1.4b8/ndoutils-1.4b8.tar.gz
Source1: ndoutils-init
Source2: ndoutils-config
Source3: ndomod-config
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel
BuildRequires: postgresql-devel
Requires: nagios >= 3.0.0
Requires: mysql
Requires: postgresql

%description
NDOUtils allows you to export current and historical data from one or more Nagios
instances to a MySQL database. Several community addons use this as one of their
data sources.

%prep
%setup -n ndoutils-%{version}b8

%build
%configure --with-mysql-lib="%{_libdir}/mysql/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ndomod-3x.o %{buildroot}%{_libexecdir}/ndomod-3x.o
%{__install} -Dp -m0755 src/ndo2db-3x %{buildroot}%{_sbindir}/ndo2db-3x
%{__mkdir} -p %{buildroot}/%{_datadir}/ndoutils
%{__cp} -r  db/* %{buildroot}%{_datadir}/ndoutils
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/init.d
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/nagios
%{__sed} -e 's*@CONFDIR@*%{_sysconfdir}/nagios*' -e 's*@SBINDIR@*%{_sbindir}*' %{SOURCE1} > %{buildroot}/%{_sysconfdir}/init.d/ndoutils
%{__sed} -e 's*@localstatedir@*%{_localstatedir}*' %{SOURCE2} > %{buildroot}/%{_sysconfdir}/nagios/ndo2db.cfg
%{__sed} -e 's*@localstatedir@*%{_localstatedir}*' %{SOURCE3} > %{buildroot}/%{_sysconfdir}/nagios/ndomod.cfg

%post
/sbin/chkconfig --add ndoutils

%preun
if [ $1 -eq 0 ]; then
    /sbin/service ndoutils stop &>/dev/null || :
    /sbin/chkconfig --del ndoutils
fi


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README REQUIREMENTS TODO UPGRADING config/*
%{_libexecdir}/ndomod-3x.o
%{_sbindir}/ndo2db-3x
%attr(755,root,root) %{_sysconfdir}/init.d/ndoutils
%{_sysconfdir}/nagios/ndo2db.cfg
%{_sysconfdir}/nagios/ndomod.cfg
%{_datadir}/ndoutils/*


%changelog
* Tue Oct 27 2009 Christoph Maser <cmr@financial.com> - 1.4-0.beta8.1
- Update to 1.4-0.beta8.1

* Thu Jan 15 2009 Christoph Maser <cmr@financial.com> - 1.4-0.beta7.3
- fix %{_datarootdir} -> %{_datadir}

* Fri Jan 02 2009 Christoph Maser <cmr@financial.com> - 1.4-0.beta7.2
- Added ndomod.cfg
- Added database scripts

* Tue Dec 30 2008 Christoph Maser <cmr@financial.com> - 1.4-0.beta7.1
- Changed version String so it can be updated by a 1.4 final
- Added init-script
- Added config-file
- Added chkconfig actions  (%post,%preun)

* Thu Nov 06 2008 Christoph Maser <cmr@financial.com> - 1.4b7-0.beta7
- Initial package.
