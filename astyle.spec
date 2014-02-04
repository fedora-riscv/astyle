Name:           astyle
Version:        2.04
Release:        2%{?dist}
Summary:        Source code formatter for C-like programming languages

Group:          Development/Tools
License:        LGPLv3+
URL:            http://astyle.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}_linux.tar.gz

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

%build
chmod a-x src/*
chmod a-x doc/*

pushd build/gcc
    make CFLAGS="$RPM_OPT_FLAGS -fPIC" release static %{?_smp_mflags}

    # Do generating of the shared solibrary the scalapack.spec way
    mkdir solibrary
    cd solibrary
    ar xv ../bin/libastyle.a
    gcc -shared -o libastyle.so.2.0.0 *.o -Wl,-soname=libastyle.so.2
popd

%install
pushd build/gcc
    make prefix="%{buildroot}%{_prefix}" INSTALL="install -p" install
    #install -p -D -m 755 bin/libastyle.so $RPM_BUILD_ROOT%{_libdir}/libastyle.so
    install -p -D -m 755 solibrary/libastyle.so.2.0.0 $RPM_BUILD_ROOT%{_libdir}/libastyle.so.2.0.0
    pushd $RPM_BUILD_ROOT%{_libdir}
        ln -fs libastyle.so.2.0.0 libastyle.so.2
        ln -s libastyle.so.2.0.0 libastyle.so

    popd
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc doc/*.html
%{_bindir}/astyle
%{_libdir}/libastyle.so.*

%files devel
%{_libdir}/libastyle.so

%changelog
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
