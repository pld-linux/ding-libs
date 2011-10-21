#
# Conditional build:
%bcond_without	tests		# build without tests

%define		collection_version	0.6.1
%define		dhash_version		0.4.3
%define		ini_config_version	0.6.2
%define		path_utils_version	0.2.1
%define		ref_array_version	0.1.2
Summary:	"Ding is not GLib" assorted utility libraries
Name:		ding-libs
Version:	0.1.3
# NOTE: do not decrease Release on Version change, unless ALL subpackage versions have been increased too
Release:	1
License:	LGPL v3+
Group:		Development/Libraries
URL:		http://fedorahosted.org/sssd/
Source0:	http://fedorahosted.org/releases/d/i/ding-libs/%{name}-%{version}.tar.gz
# Source0-md5:	b4f5e03b0b1bd0ab765902a7a466f749
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	check-devel
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	m4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of helpful libraries used by projects such as SSSD.

%package -n libcollection
Summary:	Collection data-type for C
Version:	%{collection_version}
License:	LGPL v3+
Group:		Development/Libraries

%description -n libcollection
A data-type to collect data in a hierarchical structure for easy
iteration and serialization

%package -n libcollection-devel
Summary:	Development files for libcollection
Version:	%{collection_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libcollection = %{collection_version}-%{release}

%description -n libcollection-devel
A data-type to collect data in a hierarchical structure for easy
iteration and serialization

%package -n libdhash
Summary:	Dynamic hash table
Version:	%{dhash_version}
License:	LGPL v3+
Group:		Development/Libraries

%description -n libdhash
A hash table which will dynamically resize to achieve optimal storage
& access time properties

%package -n libdhash-devel
Summary:	Development files for libdhash
Version:	%{dhash_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libdhash = %{dhash_version}-%{release}

%description -n libdhash-devel
A hash table which will dynamically resize to achieve optimal storage
& access time properties

%package -n libini_config
Summary:	INI file parser for C
Version:	%{ini_config_version}
License:	LGPL v3+
Group:		Development/Libraries

%description -n libini_config
Library to process config files in INI format into a libcollection
data structure

%package -n libini_config-devel
Summary:	Development files for libini_config
Version:	%{ini_config_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libini_config = %{ini_config_version}-%{release}

%description -n libini_config-devel
Library to process config files in INI format into a libcollection
data structure

%package -n libpath_utils
Summary:	Filesystem Path Utilities
Version:	%{path_utils_version}
License:	LGPL v3+
Group:		Development/Libraries

%description -n libpath_utils
Utility functions to manipulate filesystem pathnames

%package -n libpath_utils-devel
Summary:	Development files for libpath_utils
Version:	%{path_utils_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libpath_utils = %{path_utils_version}-%{release}

%description -n libpath_utils-devel
Utility functions to manipulate filesystem pathnames

%package -n libref_array
Summary:	A refcounted array for C
Version:	%{ref_array_version}
License:	LGPL v3+
Group:		Development/Libraries

%description -n libref_array
A dynamically-growing, reference-counted array

%package -n libref_array-devel
Summary:	Development files for libref_array
Version:	%{ref_array_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libref_array = %{ref_array_version}-%{release}

%description -n libref_array-devel
A dynamically-growing, reference-counted array

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make} all docs

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove .la files created by libtool
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# Remove the example files from the output directory
# We will copy them directly from the source directory
# for packaging
%{__rm} \
    $RPM_BUILD_ROOT%{_docdir}/ding-libs/README.* \
    $RPM_BUILD_ROOT%{_docdir}/ding-libs/examples/dhash_example.c \
    $RPM_BUILD_ROOT%{_docdir}/ding-libs/examples/dhash_test.c

# Remove document install script. RPM is handling this
%{__rm} -f */doc/html/installdox

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libcollection -p /sbin/ldconfig
%postun	-n libcollection -p /sbin/ldconfig

%post	-n libdhash -p /sbin/ldconfig
%postun	-n libdhash -p /sbin/ldconfig

%post	-n libini_config -p /sbin/ldconfig
%postun	-n libini_config -p /sbin/ldconfig

%post	-n libpath_utils -p /sbin/ldconfig
%postun	-n libpath_utils -p /sbin/ldconfig

%post	-n libref_array -p /sbin/ldconfig
%postun	-n libref_array -p /sbin/ldconfig

%files -n libcollection
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcollection.so.*.*.*
%ghost %{_libdir}/libcollection.so.2

%files -n libcollection-devel
%defattr(644,root,root,755)
%doc collection/doc/html
%{_includedir}/collection.h
%{_includedir}/collection_tools.h
%{_includedir}/collection_queue.h
%{_includedir}/collection_stack.h
%{_libdir}/libcollection.so
%{_pkgconfigdir}/collection.pc

%files -n libdhash
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdhash.so.*.*.*
%{_libdir}/libdhash.so.1

%files -n libdhash-devel
%defattr(644,root,root,755)
%doc dhash/README.dhash
%doc dhash/examples
%{_includedir}/dhash.h
%{_libdir}/libdhash.so
%{_pkgconfigdir}/dhash.pc

%files -n libini_config
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libini_config.so.*.*.*
%ghost %{_libdir}/libini_config.so.2

%files -n libini_config-devel
%defattr(644,root,root,755)
%doc ini/doc/html/
%{_includedir}/ini_config.h
%{_libdir}/libini_config.so
%{_pkgconfigdir}/ini_config.pc

%files -n libpath_utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpath_utils.so.*.*.*
%ghost %{_libdir}/libpath_utils.so.1

%files -n libpath_utils-devel
%defattr(644,root,root,755)
%doc path_utils/README.path_utils
%doc path_utils/doc/html
%{_includedir}/path_utils.h
%{_libdir}/libpath_utils.so
%{_pkgconfigdir}/path_utils.pc

%files -n libref_array
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libref_array.so.*.*.*
%ghost %{_libdir}/libref_array.so.1

%files -n libref_array-devel
%defattr(644,root,root,755)
%doc refarray/README.ref_array
%doc refarray/doc/html
%{_includedir}/ref_array.h
%{_libdir}/libref_array.so
%{_pkgconfigdir}/ref_array.pc
