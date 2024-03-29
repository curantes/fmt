#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fmt
Version  : 6.0.0
Release  : 1
URL      : https://github.com/fmtlib/fmt/archive/6.0.0.tar.gz
Source0  : https://github.com/fmtlib/fmt/archive/6.0.0.tar.gz
Summary  : A modern formatting library
Group    : Development/Tools
License  : MIT
Requires: fmt-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : glibc-dev

%description
This directory contains build support files such as
* CMake modules
* Build scripts
* qmake (static build with dynamic libc only)

%package dev
Summary: dev components for the fmt package.
Group: Development
Requires: fmt-lib = %{version}-%{release}
Provides: fmt-devel = %{version}-%{release}
Requires: fmt = %{version}-%{release}

%description dev
dev components for the fmt package.


%package lib
Summary: lib components for the fmt package.
Group: Libraries

%description lib
lib components for the fmt package.


%prep
%setup -q -n fmt-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570222489
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1570222489
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/fmt/chrono.h
/usr/include/fmt/color.h
/usr/include/fmt/compile.h
/usr/include/fmt/core.h
/usr/include/fmt/format-inl.h
/usr/include/fmt/format.h
/usr/include/fmt/locale.h
/usr/include/fmt/ostream.h
/usr/include/fmt/posix.h
/usr/include/fmt/printf.h
/usr/include/fmt/ranges.h
/usr/include/fmt/safe-duration-cast.h
/usr/lib64/cmake/fmt/fmt-config-version.cmake
/usr/lib64/cmake/fmt/fmt-config.cmake
/usr/lib64/cmake/fmt/fmt-targets-relwithdebinfo.cmake
/usr/lib64/cmake/fmt/fmt-targets.cmake
/usr/lib64/libfmt.so
/usr/lib64/pkgconfig/fmt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfmt.so.6
/usr/lib64/libfmt.so.6.0.0
