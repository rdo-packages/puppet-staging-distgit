Name:			puppet-staging
Version:		XXX
Release:		XXX
Summary:		Compressed file staging and deployment
License:		Apache-2.0

URL:			https://github.com/nanliu/puppet-staging

Source0:		https://github.com/nanliu/puppet-staging/archive/%{version}.tar.gz

BuildArch:		noarch

Requires:		puppet >= 2.7.0

%description
Compressed file staging and deployment

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/staging/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/staging/



%files
%{_datadir}/openstack-puppet/modules/staging/


%changelog

