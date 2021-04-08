Name:		gaudit
Version:	0.1
Release:	1%{?dist}
Summary:	Proof of concept virtual domain guest fs auditing utility

License:        N/A

Group:		Applications/System

Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	coreutils
Requires:       libvirt-client
Requires:       libguestfs-tools-c
Requires:       rkhunter
Requires:       fuse
Requires:       sed
Requires:       gawk

%description
Proof of concept utility to demonstrate how to perform security audits of 
running libvirt virtual domain filesystems using the libguestfs FUSE 
utility. Also logs report data which reports can be generated from afterwards.

%prep
%setup -q


%build
# N/A

%install
rm -rf $RPM_BUILD_ROOT

#Install the config file
install -Dp -m0600 gaudit.conf $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}.conf

#Install the executables
install -Dp -m0755 gaudit $RPM_BUILD_ROOT/%{_bindir}/gaudit
install -Dp -m0755 gaudit-tui $RPM_BUILD_ROOT/%{_bindir}/gaudit-tui

#Install the man page
install -Dp -m0644 gaudit.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/gaudit.8.gz

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc %{_mandir}/man8/%{name}.8.gz
%{_bindir}/%{name}
%{_bindir}/%{name}-tui
%{_sysconfdir}/%{name}.conf

%changelog
* Fri Nov 18 2011 Adam Miller <ajm023@shsu.edu> - 0.1-1
- Package it up so we can get some demo awesomeness going!

