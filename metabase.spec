%define debug_package %{nil}
%define __jar_repack  %{nil}

Name:           metabase
Version:        0.20.0
Release:        1%{?dist}
Summary:        Metabase

Group:          Applications/Databases
License:        AGPLv3.0
URL:            http://www.metabase.com/
Source0:        http://downloads.metabase.com/v%{version}/metabase.jar
Source1:        metabase.service
Source2:        metabase.sysconfig
Source3:        LICENSE
Source4:        metabase.sh

BuildRequires: systemd

Requires(pre): shadow-utils
Requires:      systemd java-headless

%description
Metabase is the easy, open source way for everyone in your company to ask 
questions and learn from data.

%prep

%build

%install
install -D %{SOURCE0} %{buildroot}/%{_sharedstatedir}/%{name}/%{name}.jar
install -D %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -D %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -D %{SOURCE3} %{buildroot}/%{_docdir}/%{name}/LICENSE
install -D %{SOURCE4} %{buildroot}/%{_bindir}/metabase

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "%{name} user" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%clean

%files
%defattr(-,root,root,-)
%dir %attr(755, %{name}, %{name}) %{_sharedstatedir}/%{name}
%attr(755, root, root) %{_bindir}/metabase
%attr(644, %{name}, %{name}) %{_sharedstatedir}/%{name}/%{name}.jar
%attr(644, root, root) %{_unitdir}/%{name}.service
%config(noreplace) %attr(640, root, %{name}) %{_sysconfdir}/sysconfig/%{name}
%doc %{_docdir}/%{name}/LICENSE

%changelog
* Mon Oct 17 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.20.0-1
- upgrade to 0.20.0

* Mon Sep 05 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.19.3-1
- upgrade to 0.19.3

* Mon Sep 05 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.19.2-5
- introduce wrapper script and java options

* Sun Sep 04 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.19.2-4
- improve adherence to fedora packaging guidelines

* Fri Sep 02 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.19.2-3
- set __jar_repack to nill

* Wed Aug 31 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.19.2-2
- fix %postun

* Wed Aug 31 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.19.2-1
- revert to 0.19.2

