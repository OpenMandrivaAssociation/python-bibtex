%define name python-bibtex
%define version 1.2.4
%define release %mkrel 1

Summary: BibTeX and recode bindings for python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/pybliographer/%{name}-%{version}.tar.bz2
URL: http://pybliographer.org/
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: recode-devel
BuildRequires: libpython-devel >= %pyver
BuildRequires: glib2-devel
BuildRequires: flex

%description
This python extension contains a BibTeX parser and a simple binding to
the GNU Recode library. They are intended to be used with pybliographer.

%prep
%setup -q

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%py_platsitedir/*


