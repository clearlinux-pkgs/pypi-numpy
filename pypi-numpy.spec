#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v3
# autospec commit: c1050fe
#
Name     : pypi-numpy
Version  : 1.26.3
Release  : 271
URL      : https://files.pythonhosted.org/packages/d0/b0/13e2b50c95bfc1d5ee04925eb5c105726c838f922d0aaddd57b7c8be0f8b/numpy-1.26.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/d0/b0/13e2b50c95bfc1d5ee04925eb5c105726c838f922d0aaddd57b7c8be0f8b/numpy-1.26.3.tar.gz
Summary  : Fundamental package for array computing in Python
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT NCSA Python-2.0 Zlib
Requires: pypi-numpy-bin = %{version}-%{release}
Requires: pypi-numpy-license = %{version}-%{release}
Requires: pypi-numpy-python = %{version}-%{release}
Requires: pypi-numpy-python3 = %{version}-%{release}
Requires: gcc-libs-math
Requires: openblas
BuildRequires : buildreq-distutils3
BuildRequires : gfortran
BuildRequires : meson
BuildRequires : ninja
BuildRequires : openblas
BuildRequires : pypi(colorama)
BuildRequires : pypi(cython)
BuildRequires : pypi(pyproject_metadata)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-cython
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: timestamp.patch
Patch2: more-avx.patch

%description
Notes for the numpy/tools/swig directory
========================================

%package bin
Summary: bin components for the pypi-numpy package.
Group: Binaries
Requires: pypi-numpy-license = %{version}-%{release}

%description bin
bin components for the pypi-numpy package.


%package dev
Summary: dev components for the pypi-numpy package.
Group: Development
Requires: pypi-numpy-bin = %{version}-%{release}
Provides: pypi-numpy-devel = %{version}-%{release}
Requires: pypi-numpy = %{version}-%{release}

%description dev
dev components for the pypi-numpy package.


%package license
Summary: license components for the pypi-numpy package.
Group: Default

%description license
license components for the pypi-numpy package.


%package python
Summary: python components for the pypi-numpy package.
Group: Default
Requires: pypi-numpy-python3 = %{version}-%{release}

%description python
python components for the pypi-numpy package.


%package python3
Summary: python3 components for the pypi-numpy package.
Group: Default
Requires: python3-core
Provides: pypi(libquadmath)
Provides: pypi(numpy)

%description python3
python3 components for the pypi-numpy package.


%prep
%setup -q -n numpy-1.26.3
cd %{_builddir}/numpy-1.26.3
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a numpy-1.26.3 buildavx2
popd

%build
## build_prepend content
CFLAGS="`sed -E 's/-fno-trapping-math//' <<<$CFLAGS`"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1704298034
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . setuptools
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
## build_prepend content
CFLAGS="`sed -E 's/-fno-trapping-math//' <<<$CFLAGS`"
## build_prepend end
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . setuptools
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
CFLAGS="`sed -E 's/-fno-trapping-math//' <<<$CFLAGS`"
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-numpy
cp %{_builddir}/numpy-%{version}/.spin/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/4e1f58ec402d86cee7b2f8516dc6440094042864 || :
cp %{_builddir}/numpy-%{version}/doc/source/_static/scipy-mathjax/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/numpy-%{version}/numpy/core/include/numpy/libdivide/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/c474367bace9239be97704a6272681c4c22ed9f6 || :
cp %{_builddir}/numpy-%{version}/numpy/core/src/npysort/x86-simd-sort/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/02c3ba5d58e6a8a955b464ba01bf7af2828fd342 || :
cp %{_builddir}/numpy-%{version}/numpy/core/src/umath/svml/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/377e8370e27122e828dfa74bd566dc98543e6bc8 || :
cp %{_builddir}/numpy-%{version}/numpy/linalg/lapack_lite/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3 || :
cp %{_builddir}/numpy-%{version}/numpy/ma/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34 || :
cp %{_builddir}/numpy-%{version}/numpy/random/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/64796c34e3592909154742074f735b89171a4418 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/distributions/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/df1c41ca8a294222a81f70a142832d6566fbd889 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/mt19937/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/50faca55f553c4ecd9f20c020176ca65324d3604 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/pcg64/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/philox/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/sfc64/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/1e0aa0638753b29e98ff682cff77d40ee4700250 || :
cp %{_builddir}/numpy-%{version}/tools/npy_tempita/license.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08 || :
cp %{_builddir}/numpy-%{version}/tools/wheels/LICENSE_linux.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/dd13c47dd4a157285c2f0cd05b8881d395e4ad02 || :
cp %{_builddir}/numpy-%{version}/tools/wheels/LICENSE_osx.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/811e206e4dbc31ed213972546bffacd6d90189dd || :
cp %{_builddir}/numpy-%{version}/tools/wheels/LICENSE_win32.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/7ff03195bdd67b59d1e052d21b80bada9132bb7d || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson-python/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/d35307a363044e8931785c522493cbde4429981a || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson-python/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/d35307a363044e8931785c522493cbde4429981a || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson/COPYING %{buildroot}/usr/share/package-licenses/pypi-numpy/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson/packaging/License.rtf %{buildroot}/usr/share/package-licenses/pypi-numpy/00dcd169768382e0b6a13d0d110266754fedb62b || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson/packaging/macpages/English.lproj/license.html %{buildroot}/usr/share/package-licenses/pypi-numpy/ed59b8ab4e260b632c935598bf0d1472e4e2dbdf || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} setuptools
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/f2py

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/__multiarray_api.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/__ufunc_api.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/_dtype_api.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/_numpyconfig.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/arrayobject.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/arrayscalars.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/experimental_dtype_api.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/halffloat.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/ndarrayobject.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/ndarraytypes.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/noprefix.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_3kcompat.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_common.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_cpu.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_endian.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_interrupt.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_math.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/npy_os.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/numpyconfig.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/old_defines.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/random/bitgen.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/random/distributions.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/random/libdivide.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/ufuncobject.h
/usr/lib/python3.12/site-packages/numpy/core/include/numpy/utils.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-numpy/00dcd169768382e0b6a13d0d110266754fedb62b
/usr/share/package-licenses/pypi-numpy/02c3ba5d58e6a8a955b464ba01bf7af2828fd342
/usr/share/package-licenses/pypi-numpy/1e0aa0638753b29e98ff682cff77d40ee4700250
/usr/share/package-licenses/pypi-numpy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-numpy/377e8370e27122e828dfa74bd566dc98543e6bc8
/usr/share/package-licenses/pypi-numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3
/usr/share/package-licenses/pypi-numpy/4e1f58ec402d86cee7b2f8516dc6440094042864
/usr/share/package-licenses/pypi-numpy/50faca55f553c4ecd9f20c020176ca65324d3604
/usr/share/package-licenses/pypi-numpy/64796c34e3592909154742074f735b89171a4418
/usr/share/package-licenses/pypi-numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
/usr/share/package-licenses/pypi-numpy/7ff03195bdd67b59d1e052d21b80bada9132bb7d
/usr/share/package-licenses/pypi-numpy/811e206e4dbc31ed213972546bffacd6d90189dd
/usr/share/package-licenses/pypi-numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
/usr/share/package-licenses/pypi-numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
/usr/share/package-licenses/pypi-numpy/c474367bace9239be97704a6272681c4c22ed9f6
/usr/share/package-licenses/pypi-numpy/d35307a363044e8931785c522493cbde4429981a
/usr/share/package-licenses/pypi-numpy/dd13c47dd4a157285c2f0cd05b8881d395e4ad02
/usr/share/package-licenses/pypi-numpy/df1c41ca8a294222a81f70a142832d6566fbd889
/usr/share/package-licenses/pypi-numpy/ed59b8ab4e260b632c935598bf0d1472e4e2dbdf
/usr/share/package-licenses/pypi-numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
