%define name	b5i2iso
%define version	0.2
%define release %mkrel 4

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


