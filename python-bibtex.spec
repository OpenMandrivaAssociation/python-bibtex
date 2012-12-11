Summary: BibTeX and recode bindings for python
Name: python-bibtex
Version: 1.2.5
Release: 4
Source0: http://prdownloads.sourceforge.net/pybliographer/%{name}-%{version}.tar.bz2
Patch: python-bibtex-1.2.4-format-strings.patch
# gw disable checks
# https://sourceforge.net/tracker/?func=detail&atid=104825&aid=1620002&group_id=4825
Patch1: python-bibtex-nocheck.patch
URL: http://pybliographer.org/
License: GPLv2+
Group: Development/Python
BuildRequires: recode-devel
BuildRequires: python-devel
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
python setup.py install --root=%{buildroot}

%files
%doc README
%py_platsitedir/*




%changelog
* Tue Nov 22 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.5-3mdv2012.0
+ Revision: 732426
- rebuild

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.2.5-2mdv2011.0
+ Revision: 598916
- rebuild for py2.7

* Sat Aug 07 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.5-1mdv2011.0
+ Revision: 567291
- update to new version 1.2.5

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.4-6mdv2010.0
+ Revision: 442032
- rebuild

* Sun Feb 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.4-5mdv2009.1
+ Revision: 343817
- update build deps
- disable checks, they fail with python 2.6
- update license
- fix C flags
- fix format strings

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.2.4-4mdv2009.0
+ Revision: 259498
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.4-3mdv2009.0
+ Revision: 247384
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.2.4-1mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.4-1mdv2008.0
+ Revision: 17968
- new version


* Sat Jan 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.0
+ Revision: 110994
- new version
- drop patch

* Sat Dec 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.2-7mdv2007.1
+ Revision: 101891
- fix build for new python
- rebuild

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - Rebuild against new python

* Fri Nov 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.2-5mdv2007.1
+ Revision: 76246
- bot rebuild
- bot rebuild
- bot rebuild
- Import python-bibtex

* Fri Nov 03 2006 Götz Waschk <waschk@mandriva.org> 1.2.2-2mdv2007.1
- mkrel

* Fri Oct 07 2005 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdk
- drop bundled recode, our recode package has the needed fix
- New release 1.2.2

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.2.1-2mdk
- Rebuild for new python

* Sat Aug 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.1-1mdk
- New release 1.2.1

* Sat May 01 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.0-1mdk
- New release 1.2.0

