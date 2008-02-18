Name:           astyle
Version:        1.21
Release:        7%{?dist}
Summary:        Source code formatter for C-like programming languages

Group:          Development/Tools
License:        LGPL
URL:            http://astyle.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}_linux.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.


%prep
%setup -q -n %{name}


%build
g++ -o astyle $RPM_OPT_FLAGS src/*.cpp
chmod a-x src/*
chmod a-x doc/*


%install
rm -rf $RPM_BUILD_ROOT
%{_bindir}/install -p -D -m 755 astyle $RPM_BUILD_ROOT%{_bindir}/astyle


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/astyle

%doc doc/*.html

%changelog
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
