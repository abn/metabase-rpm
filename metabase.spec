%define debug_package %{nil}

Name:           metabase
Version:        0.19.3
Release:        1%{?dist}
Summary:        Metabase

Group:          Applications/Databases
License:        AGPLv3.0
URL:            http://www.metabase.com/
Source0:        http://downloads.metabase.com/v%{version}/metabase.jar
Source1:        metabase.service
Source2:        metabase.sysconfig
Source3:        LICENSE

BuildRequires: systemd-units

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

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "%{name} user" %{name}
exit 0

%postun
getent passwd %{name} >/dev/null && userdel %{name}
getent group %{name} >/dev/null && groupdel %{name}

%clean

%files
%defattr(-,root,root,-)
%dir %attr(750, %{name}, %{name}) %{_sharedstatedir}/%{name}
%attr(644, %{name}, %{name}) %{_sharedstatedir}/%{name}/%{name}.jar
%attr(644, root, root) %{_unitdir}/%{name}.service
%config(noreplace) %attr(640, root, %{name}) %{_sysconfdir}/sysconfig/%{name}
%doc %{_docdir}/%{name}/LICENSE

%changelog
* Wed Aug 31 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.19.3-1
- v0.19.3

