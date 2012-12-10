%define name	b5i2iso
%define version	0.2
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Convert Blindwrite CD Images to ISO
Source:		%{name}-%{version}.tar.bz2
URL:		http://developer.berlios.de/projects/b5i2iso/
License:	GPL
Group:		Archiving/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description 
B5I2ISO is a very simple utility to 
convert an BlindWrite image to the 
standard ISO-9660 format.

Usage: b5i2iso image.b5i <image.iso>

%prep
%setup -q
chmod 644 CHANGELOG

%build
gcc %optflags ./src/b5i2iso.c -o b5i2iso

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install b5i2iso %{buildroot}%{_bindir}/b5i2iso

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG
%{_bindir}/b5i2iso




%changelog
* Sat Sep 18 2010 Tomas Kindl <supp@mandriva.org> 0.2-6mdv2011.0
+ Revision: 579465
- rebuild
- fix changelog perms

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2010.0
+ Revision: 424006
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2009.0
+ Revision: 243133
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2mdv2008.1-current
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jul 31 2006 Lenny Cartier <lenny@mandriva.com> 0.2-2mdv2007.0
- rebuild

* Wed Jul 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-1mdk
- First Mandriva package from Michael Berger <webmaster@hmb-linux.de>

