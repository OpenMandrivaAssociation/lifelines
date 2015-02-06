Summary:	A terminal based genealogy program
Name:		lifelines
Version:	3.0.62
Release:	9
License:	MIT
Group:		Databases 
URL:		http://lifelines.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/lifelines/%{name}-%{version}.tar.bz2
Patch0:		lifelines-3.0.62-format-strings.patch
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	openjade
BuildRequires:	bison

%description
This program allows the tracking of genealogical information. The lifelines
reports are the power of the system.

%prep 
%setup -q 
%patch0 -p1
find . -type d -perm 0700 -exec chmod 0755 '{}' \;
find . -type f -perm 0700 -exec chmod 0644 '{}' \;
chmod 0755 ./configure

%build
%configure2_5x   

%make
 
%install
%makeinstall_std 
install -d -m 755 %{buildroot}%{_datadir}/%{name}/reports
install -m 644 reports/CREDIT reports/README reports/boc.gif reports/*.ll reports/tree.* reports/index.html reports/ll.png  reports/st/*.ll %{buildroot}%{_datadir}/%{name}/reports  
 
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 docs/llines.1 %{buildroot}%{_mandir}/man1/llines.1

rm -rf %{buildroot}%{_datadir}/doc/lifelines 
rm -f %{buildroot}%{_libdir}/libarch.a

%find_lang %{name}

%files -f %{name}.lang
%doc README* ChangeLog NEWS AUTHORS LICENSE docs/*.txt docs/*.pdf docs/*.html
%{_mandir}/man1/*
%{_bindir}/btedit
%{_bindir}/llines 
%{_bindir}/llexec
%{_bindir}/dbverify 
%{_datadir}/%{name}

