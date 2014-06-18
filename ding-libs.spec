#
# Conditional build:
%bcond_without	tests		# build without tests

%define		basicobjects_version	0.1.1
%define		collection_version	0.6.2
%define		dhash_version		0.4.3
%define		ini_config_version	1.1.0
%define		path_utils_version	0.2.1
%define		ref_array_version	0.1.4
Summary:	"Ding is not GLib" assorted utility libraries
Summary(pl.UTF-8):	"Ding is not GLib" - niepowiązane ze sobą biblioteki narzędzi
Name:		ding-libs
Version:	0.4.0
# NOTE: do not decrease Release on Version change, unless ALL subpackage versions have been increased too
Release:	3
License:	GPL v3+ (basicobjects), LGPL v3+ (collection, dhash, ini, path_utils, ref_array)
Group:		Libraries
Source0:	https://fedorahosted.org/releases/d/i/ding-libs/%{name}-%{version}.tar.gz
# Source0-md5:	8da087a535b66968797f337ce2c44a4e
URL:		https://fedorahosted.org/sssd/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	check-devel >= 0.9.5
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of helpful libraries used by projects such as SSSD.

%description -l pl.UTF-8
Zbiór przydatnych bibliotek, używanych przez projekty takie jak SSSD.

%package -n libbasicobjects
Summary:	Basic object types for C
Summary(pl.UTF-8):	Podstawowe typy obiektów dla C
Version:	%{basicobjects_version}
License:	GPL v3+
Group:		Libraries

%description -n libbasicobjects
Basic object types for C.

%description -n libbasicobjects -l pl.UTF-8
Podstawowe typy obiektów dla C.

%package -n libbasicobjects-devel
Summary:	Development files for libbasicobjects
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libbasicobjects
Version:	%{basicobjects_version}
License:	GPL v3+
Group:		Development/Libraries
Requires:	libbasicobjects = %{basicobjects_version}-%{release}

%description -n libbasicobjects-devel
Development files for libbasicobjects.

%description -n libbasicobjects-devel -l pl.UTF-8
Pliki programistyczne biblioteki libbasicobjects.

%package -n libbasicobjects-static
Summary:	Static libbasicobjects library
Summary(pl.UTF-8):	Statyczna biblioteka libbasicobjects
Version:	%{basicobjects_version}
License:	GPL v3+
Group:		Development/Libraries
Requires:	libbasicobjects-devel = %{basicobjects_version}-%{release}

%description -n libbasicobjects-static
Static libbasicobjects library.

%description -n libbasicobjects-static -l pl.UTF-8
Statyczna biblioteka libbasicobjects.

%package -n libcollection
Summary:	Collection data-type for C
Summary(pl.UTF-8):	Typ danych kolekcji dla C
Version:	%{collection_version}
License:	LGPL v3+
Group:		Libraries

%description -n libcollection
A data-type to collect data in a hierarchical structure for easy
iteration and serialization.

%description -n libcollection -l pl.UTF-8
Typ danych do gromadzenia danych w strukturze hierarchicznej w celu
łatwego iterowania i serializowania.

%package -n libcollection-devel
Summary:	Development files for libcollection
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libcollection
Version:	%{collection_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libcollection = %{collection_version}-%{release}

%description -n libcollection-devel
Development files for libcollection.

%description -n libcollection-devel -l pl.UTF-8
Pliki programistyczne biblioteki libcollection.

%package -n libcollection-static
Summary:	Static libcollection library
Summary(pl.UTF-8):	Statyczna biblioteka libcollection
Version:	%{collection_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libcollection-devel = %{collection_version}-%{release}

%description -n libcollection-static
Static libcollection library.

%description -n libcollection-static -l pl.UTF-8
Statyczna biblioteka libcollection.

%package -n libdhash
Summary:	Dynamic hash table
Summary(pl.UTF-8):	Dynamiczna tablica haszująca
Version:	%{dhash_version}
License:	LGPL v3+
Group:		Libraries

%description -n libdhash
A hash table which will dynamically resize to achieve optimal storage
& access time properties.

%description -n libdhash -l pl.UTF-8
Tablica haszująca dynamicznie zmieniająca rozmiar, aby osiągnąć
optymalne właściwości zajętości pamięci i czasu dostępu.

%package -n libdhash-devel
Summary:	Development files for libdhash
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libdhash
Version:	%{dhash_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libdhash = %{dhash_version}-%{release}

%description -n libdhash-devel
Development files for libdhash.

%description -n libdhash-devel -l pl.UTF-8
Pliki programistyczne biblioteki libdhash.

%package -n libdhash-static
Summary:	Static libdhash library
Summary(pl.UTF-8):	Statyczna biblioteka libdhash
Version:	%{dhash_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libdhash-devel = %{dhash_version}-%{release}

%description -n libdhash-static
Static libdhash library.

%description -n libdhash-static -l pl.UTF-8
Statyczna biblioteka libdhash.

%package -n libini_config
Summary:	INI file parser for C
Summary(pl.UTF-8):	Analizator plików INI dla C
Version:	%{ini_config_version}
License:	LGPL v3+
Group:		Libraries
Requires:	libbasicobjects = %{basicobjects_version}-%{release}
Requires:	libcollection = %{collection_version}-%{release}
Requires:	libpath_utils = %{path_utils_version}-%{release}
Requires:	libref_array = %{ref_array_version}-%{release}

%description -n libini_config
Library to process config files in INI format into a libcollection
data structure.

%description -n libini_config -l pl.UTF-8
Biblioteka do przetwarzania plików konfiguracyjnych w formacie INI do
struktury danych libcollection.

%package -n libini_config-devel
Summary:	Development files for libini_config
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libini_config
Version:	%{ini_config_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libbasicobjects-devel = %{basicobjects_version}-%{release}
Requires:	libcollection-devel = %{collection_version}-%{release}
Requires:	libini_config = %{ini_config_version}-%{release}
Requires:	libpath_utils-devel = %{path_utils_version}-%{release}
Requires:	libref_array-devel = %{ref_array_version}-%{release}

%description -n libini_config-devel
Development files for libini_config.

%description -n libini_config-devel -l pl.UTF-8
Pliki programistyczne biblioteki libini_config.

%package -n libini_config-static
Summary:	Static libini_config library
Summary(pl.UTF-8):	Statyczna biblioteka libini_config
Version:	%{ini_config_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libini_config-devel = %{ini_config_version}-%{release}

%description -n libini_config-static
Static libini_config library.

%description -n libini_config-static -l pl.UTF-8
Statyczna biblioteka libini_config.

%package -n libpath_utils
Summary:	Filesystem Path Utilities
Summary(pl.UTF-8):	Narzędzia do operowania na ścieżkach w systemie plików
Version:	%{path_utils_version}
License:	LGPL v3+
Group:		Libraries

%description -n libpath_utils
Utility functions to manipulate filesystem pathnames.

%description -n libpath_utils -l pl.UTF-8
Funkcje narzędziowe do operowania na ścieżkach w systemie plików.

%package -n libpath_utils-devel
Summary:	Development files for libpath_utils
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libpath_utils
Version:	%{path_utils_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libpath_utils = %{path_utils_version}-%{release}

%description -n libpath_utils-devel
Development files for libpath_utils.

%description -n libpath_utils-devel -l pl.UTF-8
Pliki programistyczne biblioteki libpath_utils.

%package -n libpath_utils-static
Summary:	Static libpath_utils library
Summary(pl.UTF-8):	Statyczna biblioteka libpath_utils
Version:	%{path_utils_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libpath_utils-devel = %{path_utils_version}-%{release}

%description -n libpath_utils-static
Static libpath_utils library.

%description -n libpath_utils-static -l pl.UTF-8
Statyczna biblioteka libpath_utils.

%package -n libref_array
Summary:	A refcounted array for C
Summary(pl.UTF-8):	Tablica z licznikiem odwołań dla C
Version:	%{ref_array_version}
License:	LGPL v3+
Group:		Libraries

%description -n libref_array
A dynamically-growing, reference-counted array.

%description -n libref_array -l pl.UTF-8
Dynamicznie rosnąca tablica z licznikiem odwołań.

%package -n libref_array-devel
Summary:	Development files for libref_array
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libref_array
Version:	%{ref_array_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libref_array = %{ref_array_version}-%{release}

%description -n libref_array-devel
Development files for libref_array.

%description -n libref_array-devel -l pl.UTF-8
Pliki programistyczne biblioteki libref_array.

%package -n libref_array-static
Summary:	Static libref_array library
Summary(pl.UTF-8):	Statyczna biblioteka libref_array
Version:	%{ref_array_version}
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libref_array-devel = %{ref_array_version}-%{release}

%description -n libref_array-static
Static libref_array library.

%description -n libref_array-static -l pl.UTF-8
Statyczna biblioteka libref_array.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

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

%post	-n libbasicobjects -p /sbin/ldconfig
%postun	-n libbasicobjects -p /sbin/ldconfig

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

%files -n libbasicobjects
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbasicobjects.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbasicobjects.so.0

%files -n libbasicobjects-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbasicobjects.so
%{_includedir}/simplebuffer.h
%{_pkgconfigdir}/basicobjects.pc

%files -n libbasicobjects-static
%defattr(644,root,root,755)
%{_libdir}/libbasicobjects.a

%files -n libcollection
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcollection.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcollection.so.4

%files -n libcollection-devel
%defattr(644,root,root,755)
%doc collection/doc/html
%attr(755,root,root) %{_libdir}/libcollection.so
%{_includedir}/collection.h
%{_includedir}/collection_tools.h
%{_includedir}/collection_queue.h
%{_includedir}/collection_stack.h
%{_pkgconfigdir}/collection.pc

%files -n libcollection-static
%defattr(644,root,root,755)
%{_libdir}/libcollection.a

%files -n libdhash
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdhash.so.*.*.*
%attr(755,root,root) %{_libdir}/libdhash.so.1

%files -n libdhash-devel
%defattr(644,root,root,755)
%doc dhash/README.dhash dhash/examples
%attr(755,root,root) %{_libdir}/libdhash.so
%{_includedir}/dhash.h
%{_pkgconfigdir}/dhash.pc

%files -n libdhash-static
%defattr(644,root,root,755)
%{_libdir}/libdhash.a

%files -n libini_config
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libini_config.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libini_config.so.5

%files -n libini_config-devel
%defattr(644,root,root,755)
%doc ini/doc/html
%attr(755,root,root) %{_libdir}/libini_config.so
%{_includedir}/ini_comment.h
%{_includedir}/ini_config.h
%{_includedir}/ini_configobj.h
%{_includedir}/ini_valueobj.h
%{_pkgconfigdir}/ini_config.pc

%files -n libini_config-static
%defattr(644,root,root,755)
%{_libdir}/libini_config.a

%files -n libpath_utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpath_utils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpath_utils.so.1

%files -n libpath_utils-devel
%defattr(644,root,root,755)
%doc path_utils/README.path_utils path_utils/doc/html
%attr(755,root,root) %{_libdir}/libpath_utils.so
%{_includedir}/path_utils.h
%{_pkgconfigdir}/path_utils.pc

%files -n libpath_utils-static
%defattr(644,root,root,755)
%{_libdir}/libpath_utils.a

%files -n libref_array
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libref_array.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libref_array.so.1

%files -n libref_array-devel
%defattr(644,root,root,755)
%doc refarray/README.ref_array refarray/doc/html
%attr(755,root,root) %{_libdir}/libref_array.so
%{_includedir}/ref_array.h
%{_pkgconfigdir}/ref_array.pc

%files -n libref_array-static
%defattr(644,root,root,755)
%{_libdir}/libref_array.a
