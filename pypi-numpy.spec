#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: e36a856
#
Name     : pypi-numpy
Version  : 2.2.3
Release  : 289
URL      : https://files.pythonhosted.org/packages/fb/90/8956572f5c4ae52201fdec7ba2044b2c882832dcec7d5d0922c9e9acf2de/numpy-2.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/fb/90/8956572f5c4ae52201fdec7ba2044b2c882832dcec7d5d0922c9e9acf2de/numpy-2.2.3.tar.gz
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
BuildRequires : pypi(cython)
BuildRequires : pypi(meson_python)
BuildRequires : pypi-cython
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: timestamp.patch

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
Provides: pypi(numpy)
Provides: pypi(numpy)

%description python3
python3 components for the pypi-numpy package.


%prep
%setup -q -n numpy-2.2.3
cd %{_builddir}/numpy-2.2.3
%patch -P 1 -p1
pushd ..
cp -a numpy-2.2.3 buildavx2
popd
pushd ..
cp -a numpy-2.2.3 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739471579
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . setuptools
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-numpy
cp %{_builddir}/numpy-%{version}/.spin/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/4e1f58ec402d86cee7b2f8516dc6440094042864 || :
cp %{_builddir}/numpy-%{version}/doc/source/_static/scipy-mathjax/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/numpy-%{version}/numpy/_build_utils/tempita/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/860ce1e3089e4750ef43d9973281f1062f93636b || :
cp %{_builddir}/numpy-%{version}/numpy/_core/include/numpy/libdivide/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/c474367bace9239be97704a6272681c4c22ed9f6 || :
cp %{_builddir}/numpy-%{version}/numpy/_core/src/highway/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/58853eb8199b5afe72a73a25fd8cf8c94285174b || :
cp %{_builddir}/numpy-%{version}/numpy/_core/src/highway/LICENSE-BSD3 %{buildroot}/usr/share/package-licenses/pypi-numpy/8ef530850989072e75f6f743a03e377de4392a68 || :
cp %{_builddir}/numpy-%{version}/numpy/_core/src/highway/debian/copyright %{buildroot}/usr/share/package-licenses/pypi-numpy/7363889d9c7364f41a37d3efa2ec375bc836d916 || :
cp %{_builddir}/numpy-%{version}/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/02c3ba5d58e6a8a955b464ba01bf7af2828fd342 || :
cp %{_builddir}/numpy-%{version}/numpy/_core/src/umath/svml/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/377e8370e27122e828dfa74bd566dc98543e6bc8 || :
cp %{_builddir}/numpy-%{version}/numpy/fft/pocketfft/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/b1881ea58a8dacfb4e8965ca56be6cbbe9f53be1 || :
cp %{_builddir}/numpy-%{version}/numpy/linalg/lapack_lite/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3 || :
cp %{_builddir}/numpy-%{version}/numpy/ma/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34 || :
cp %{_builddir}/numpy-%{version}/numpy/random/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/64796c34e3592909154742074f735b89171a4418 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/distributions/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/df1c41ca8a294222a81f70a142832d6566fbd889 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/mt19937/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/50faca55f553c4ecd9f20c020176ca65324d3604 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/pcg64/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96 || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/philox/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b || :
cp %{_builddir}/numpy-%{version}/numpy/random/src/sfc64/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/1e0aa0638753b29e98ff682cff77d40ee4700250 || :
cp %{_builddir}/numpy-%{version}/tools/wheels/LICENSE_linux.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/70002ad5d9c5c71e1d428a0178a7c55a0a0ae7ea || :
cp %{_builddir}/numpy-%{version}/tools/wheels/LICENSE_osx.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/feedee8e73dc598dce10f55e28b47a6aa4c6dc4d || :
cp %{_builddir}/numpy-%{version}/tools/wheels/LICENSE_win32.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/5d55766efb25eeaa6963a8fbafea58223d2c94ba || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson/COPYING %{buildroot}/usr/share/package-licenses/pypi-numpy/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson/packaging/License.rtf %{buildroot}/usr/share/package-licenses/pypi-numpy/00dcd169768382e0b6a13d0d110266754fedb62b || :
cp %{_builddir}/numpy-%{version}/vendored-meson/meson/packaging/macpages/English.lproj/license.html %{buildroot}/usr/share/package-licenses/pypi-numpy/ed59b8ab4e260b632c935598bf0d1472e4e2dbdf || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} setuptools
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/f2py
/usr/bin/numpy-config

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/__multiarray_api.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/__ufunc_api.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/_neighborhood_iterator_imp.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/_numpyconfig.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/_public_dtype_api_table.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/arrayobject.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/arrayscalars.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/dtype_api.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/halffloat.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/ndarrayobject.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/ndarraytypes.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_1_7_deprecated_api.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_2_compat.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_2_complexcompat.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_3kcompat.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_common.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_cpu.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_endian.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_math.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_no_deprecated_api.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/npy_os.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/numpyconfig.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/random/bitgen.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/random/distributions.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/random/libdivide.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/ufuncobject.h
/usr/lib/python3.13/site-packages/numpy/_core/include/numpy/utils.h

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
/usr/share/package-licenses/pypi-numpy/58853eb8199b5afe72a73a25fd8cf8c94285174b
/usr/share/package-licenses/pypi-numpy/5d55766efb25eeaa6963a8fbafea58223d2c94ba
/usr/share/package-licenses/pypi-numpy/64796c34e3592909154742074f735b89171a4418
/usr/share/package-licenses/pypi-numpy/70002ad5d9c5c71e1d428a0178a7c55a0a0ae7ea
/usr/share/package-licenses/pypi-numpy/7363889d9c7364f41a37d3efa2ec375bc836d916
/usr/share/package-licenses/pypi-numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
/usr/share/package-licenses/pypi-numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
/usr/share/package-licenses/pypi-numpy/860ce1e3089e4750ef43d9973281f1062f93636b
/usr/share/package-licenses/pypi-numpy/8ef530850989072e75f6f743a03e377de4392a68
/usr/share/package-licenses/pypi-numpy/b1881ea58a8dacfb4e8965ca56be6cbbe9f53be1
/usr/share/package-licenses/pypi-numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
/usr/share/package-licenses/pypi-numpy/c474367bace9239be97704a6272681c4c22ed9f6
/usr/share/package-licenses/pypi-numpy/df1c41ca8a294222a81f70a142832d6566fbd889
/usr/share/package-licenses/pypi-numpy/ed59b8ab4e260b632c935598bf0d1472e4e2dbdf
/usr/share/package-licenses/pypi-numpy/feedee8e73dc598dce10f55e28b47a6aa4c6dc4d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
