%define name python-bibtex
%define version 1.2.5
%define release %mkrel 1

Summary: BibTeX and recode bindings for python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/pybliographer/%{name}-%{version}.tar.bz2
Patch: python-bibtex-1.2.4-format-strings.patch
# gw disable checks
# https://sourceforge.net/tracker/?func=detail&atid=104825&aid=1620002&group_id=4825
Patch1: python-bibtex-nocheck.patch
URL: http://pybliographer.org/
License: GPLv2+
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: recode-devel
BuildRequires: libpython-devel >= %pyver
BuildRequires: glib2-devel
BuildRequires: flex bison

%description
This python extension contains a BibTeX parser and a simple binding to
the GNU Recode library. They are intended to be used with pybliographer.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
CFLAGS="%optflags" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%py_platsitedir/*


