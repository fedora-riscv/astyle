Name:           astyle
Version:        2.05.1
Release:        4%{?dist}
Summary:        Source code formatter for C-like programming languages

%global soversion 2.05

Group:          Development/Tools
License:        LGPLv3+
URL:            http://astyle.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}_linux.tar.gz
# publish API used by Code::Blocks IDE
Patch0:         %{name}-2.04-indent-api.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

%package devel
Summary:        Source code formatter for C-like programming languages
Group:          Development/Tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

This package contains the shared library.


%prep
%setup -q -n %{name}
%patch0 -p1 -b .indent-api

%build
chmod a-x src/*
chmod a-x doc/*

pushd src
    # it's much easier to compile it here than trying to fix the Makefile
    g++ $RPM_OPT_FLAGS -fPIC -c ASBeautifier.cpp ASEnhancer.cpp ASFormatter.cpp ASResource.cpp
    g++ -shared -o libastyle-%{soversion}.so *.o -Wl,-soname,libastyle-%{soversion}.so
    ln -s libastyle-%{soversion}.so libastyle.so
    g++ $RPM_OPT_FLAGS -c ASLocalizer.cpp astyle_main.cpp
    g++ $RPM_OPT_FLAGS -o astyle ASLocalizer.o astyle_main.o -L. -lastyle
popd

%install
pushd src
    mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

    install -p -m 755 astyle $RPM_BUILD_ROOT%{_bindir}
    install -p -m 755 libastyle-%{soversion}.so $RPM_BUILD_ROOT%{_libdir}
    cp -P libastyle.so $RPM_BUILD_ROOT%{_libdir}
    install -p -m 644 astyle.h $RPM_BUILD_ROOT%{_includedir}
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc doc/*.html
%{_bindir}/astyle
%{_libdir}/libastyle-*.so

%files devel
%{_libdir}/libastyle.so
%{_includedir}/astyle.h

%changelog
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.05.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.05.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Dec 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.05.1-1
- update to 2.05.1 (#1175136), but stay at same soversion for library

* Thu Nov 20 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.05-1
- update to 2.05 (#1166336)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Dan Horák <dan[at]danny.cz> - 2.04-3
- compile directly in %%build so the astyle binary links against our library
- include public header file in devel subpackage
- use full version info in soname as there is no API/ABI compatibility guaranteed

* Fri Jan 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.04-2
- build shared library without SONAME (opened bug upstream to provide a SONAME in the next release, #1054422)
- remove defattr
- remove clean section

* Tue Nov  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.04-1
- update to new version (fixes #1025982, #996008)

* Tue Jul 30 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.03-1
- update to new version (fixes #990162)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.02.1-1
- update to new version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.01-1
- update to new version

* Sat Jan 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.24-1
- update to new version
- change license to LGPLv3+ (changed since 1.23, but missed there)

* Tue Oct 13 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.23-1
- Update to new version
- patch from Sep 24 2008 not needed anymore for gcc-4.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.21-9
- Fixed build failure with gcc-4.3. Closes Red Hat Bugzilla bug #433971.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.21-8
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.21-7
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.21-6
- Rebuild for selinux ppc32 issue.

* Mon Jul 2 2007 Adam M. Dutko <gnome at dux-linux org> 1.21-5
- Fixed sourceforge Source0 link.
- Updated to 1.21.

* Tue Jun 19 2007 Adam M. Dutko <gnome at dux-linux org> 1.20.2-4
- Removed macros from changelog
- Formatted changelog from 1.20.2-2

* Tue Jun 19 2007 Adam M. Dutko <gnome at dux-linux org> 1.20.2-3
- Changed licensing to LGPL from GPL
- Removed execute bit from src/*
- Used bindir/install instead of /usr/bin/install

* Thu Jun 14 2007 Mary Ellen Foster <mefoster gmail com> 1.20.2-2
- Modifications from Ralf Corsepius (thanks!):
- Eliminated use of build/Makefile; just compile and install directly
- Use bindir rather than /usr/bin

* Sat May 12 2007 Adam Monsen <haircut@gmail.com> 1.20.2-1
- removed Makefile patch

* Thu Sep 21 2006 Mary Ellen Foster <mefoster gmail com> 1.19-1
- Initial package
