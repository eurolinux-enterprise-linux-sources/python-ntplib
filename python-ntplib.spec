Name:           python-ntplib
Version:        0.3.2
Release:        1%{?dist}
Summary:        Python module that offers a simple interface to query NTP servers

License:        LGPLv2+
URL:            http://pypi.python.org/pypi/ntplib/
Source0:        https://pypi.python.org/packages/source/n/ntplib/ntplib-%{?version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
The ntplib is a python module that offers a simple interface to query NTP
servers. It also provides utility functions to translate NTP fields' values to
text (mode, leap indicator...). Since it's pure Python, and only depends on core
modules, it should work on any platform with a Python implementation.

%prep
%setup -q -n ntplib-%{?version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc CHANGELOG COPYING.LESSER
%{python_sitelib}/*


%changelog
* Wed Feb 05 2014 Vratislav Podzimek <vpodzime@redhat.com> 0.3.2-1
- New upstream version ntplib-0.3.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Vratislav Podzimek <vpodzime@redhat.com> 0.3.1-1
- Initial release
