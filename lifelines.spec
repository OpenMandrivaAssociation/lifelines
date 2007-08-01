%define name lifelines
%define version 3.0.50
%define release %mkrel 2
%define summary  A terminal based genealogy program

Summary: %{summary}
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group:  Databases 
Source:         http://prdownloads.sourceforge.net/lifelines/%{name}-%{version}.tar.bz2
URL:            http://lifelines.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libncurses-devel openjade >= 1.3.2-2mdk
BuildRequires: bison

%description
This program allows the tracking of genealogical information.  The lifelines
reports are the power of the system.

%prep 
%setup -q 

%build
%configure2_5x   

%make
 
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/reports
install -m 644 reports/CREDIT reports/README reports/boc.gif reports/*.ll reports/tree.* reports/index.html reports/ll.png  reports/st/*.ll $RPM_BUILD_ROOT%{_datadir}/%{name}/reports  
 
install -d -m 755 $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 docs/llines.1 $RPM_BUILD_ROOT/%{_mandir}/man1/llines.1

%find_lang %name
rm -rf %buildroot/%_datadir/doc/lifelines 
rm -f %buildroot/%_libdir/libarch.a

%clean
#m -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README* ChangeLog NEWS AUTHORS LICENSE docs/*.txt docs/*.pdf docs/*.html
%{_mandir}/man1/llines.1*
%{_mandir}/man1/btedit.1*
%{_mandir}/man1/dbverify.1*
%{_bindir}/btedit
%{_bindir}/llines 
%{_bindir}/llexec
%{_bindir}/dbverify 
%{_datadir}/%{name}