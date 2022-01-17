#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-numpy
Version  : 1.22.1
Release  : 215
URL      : https://files.pythonhosted.org/packages/0a/c8/a62767a6b374a0dfb02d2a0456e5f56a372cdd1689dbc6ffb6bf1ddedbc0/numpy-1.22.1.zip
Source0  : https://files.pythonhosted.org/packages/0a/c8/a62767a6b374a0dfb02d2a0456e5f56a372cdd1689dbc6ffb6bf1ddedbc0/numpy-1.22.1.zip
Summary  : NumPy is the fundamental package for array computing with Python.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT NCSA Zlib
Requires: pypi-numpy-bin = %{version}-%{release}
Requires: pypi-numpy-license = %{version}-%{release}
Requires: pypi-numpy-python = %{version}-%{release}
Requires: pypi-numpy-python3 = %{version}-%{release}
Requires: gcc-libs-math
Requires: openblas
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : gfortran
BuildRequires : openblas
BuildRequires : pypi(cython)
BuildRequires : pypi(packaging)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : python3-dev
Patch1: avx2-distutils.patch
Patch2: avx2-fortran-distutils.patch
Patch3: timestamp.patch
Patch4: cve-2017-12852.nopatch
Patch5: 0001-AVX-Support-for-static-lib.patch
Patch6: 0001-add-numpy-benchmarks-for-pgo.patch
Patch7: 0001-make-distutils-support-PGO-options.patch
Patch8: build.patch

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

%description python3
python3 components for the pypi-numpy package.


%prep
%setup -q -n numpy-1.22.1
cd %{_builddir}/numpy-1.22.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642444768
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . setuptools
python3 -m build --wheel --skip-dependency-check --no-isolation

## build_append content
export OPT_GENERATE="-fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic -lgcov"
export OPT_USE="-fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "

# doing PGO profile build
rm -rf build  # make clean
NPY_DISTUTILS_APPEND_FLAGS=1 PGO_OPTS="${OPT_GENERATE}" python3 setup.py build --fcompiler=gnu95 %{?_smp_mflags}

# profile using numpy-benchmarks
export PGO_NUMPY_LIB_PATH=`ls -d $PWD/build/lib.linux-*`
# *.so.avx512 profiling
time PYTHONPATH="${PGO_NUMPY_LIB_PATH}" python3 Tools/numpy-benchmarks/benchall.py
# *.so.avx2 profiling
find -name "*.so.avx512" -exec rm {} \;
time PYTHONPATH="${PGO_NUMPY_LIB_PATH}" python3 Tools/numpy-benchmarks/benchall.py
# *.so profiling
find -name "*.so.avx2" -exec rm {} \;
time PYTHONPATH="${PGO_NUMPY_LIB_PATH}" python3 Tools/numpy-benchmarks/benchall.py

# using PGO to compile
rm -rf build  # make clean
NPY_DISTUTILS_APPEND_FLAGS=1 PGO_OPTS="${OPT_USE}" python3 setup.py build --fcompiler=gnu95 %{?_smp_mflags}
## build_append end
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-numpy
cp %{_builddir}/numpy-1.22.1/doc/source/_static/scipy-mathjax/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/numpy-1.22.1/numpy/core/include/numpy/libdivide/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/c474367bace9239be97704a6272681c4c22ed9f6
cp %{_builddir}/numpy-1.22.1/numpy/core/src/umath/svml/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/377e8370e27122e828dfa74bd566dc98543e6bc8
cp %{_builddir}/numpy-1.22.1/numpy/linalg/lapack_lite/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3
cp %{_builddir}/numpy-1.22.1/numpy/ma/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
cp %{_builddir}/numpy-1.22.1/numpy/random/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/64796c34e3592909154742074f735b89171a4418
cp %{_builddir}/numpy-1.22.1/numpy/random/src/distributions/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/df1c41ca8a294222a81f70a142832d6566fbd889
cp %{_builddir}/numpy-1.22.1/numpy/random/src/mt19937/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/50faca55f553c4ecd9f20c020176ca65324d3604
cp %{_builddir}/numpy-1.22.1/numpy/random/src/pcg64/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
cp %{_builddir}/numpy-1.22.1/numpy/random/src/philox/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
cp %{_builddir}/numpy-1.22.1/numpy/random/src/sfc64/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-numpy/1e0aa0638753b29e98ff682cff77d40ee4700250
cp %{_builddir}/numpy-1.22.1/tools/npy_tempita/license.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08
cp %{_builddir}/numpy-1.22.1/tools/wheels/LICENSE_linux.txt %{buildroot}/usr/share/package-licenses/pypi-numpy/92e11f80803790b67495703271b70d4ae0588f88
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} setuptools
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/f2py
/usr/bin/f2py3
/usr/bin/f2py3.10

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/__multiarray_api.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/__ufunc_api.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/_numpyconfig.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/arrayobject.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/arrayscalars.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/experimental_dtype_api.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/halffloat.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/libdivide/libdivide.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/ndarrayobject.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/ndarraytypes.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/noprefix.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_3kcompat.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_common.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_cpu.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_endian.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_interrupt.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_math.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/npy_os.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/numpyconfig.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/old_defines.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/oldnumeric.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/random/bitgen.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/random/distributions.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/ufuncobject.h
/usr/lib/python3.10/site-packages/numpy/core/include/numpy/utils.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-numpy/1e0aa0638753b29e98ff682cff77d40ee4700250
/usr/share/package-licenses/pypi-numpy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-numpy/377e8370e27122e828dfa74bd566dc98543e6bc8
/usr/share/package-licenses/pypi-numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3
/usr/share/package-licenses/pypi-numpy/50faca55f553c4ecd9f20c020176ca65324d3604
/usr/share/package-licenses/pypi-numpy/64796c34e3592909154742074f735b89171a4418
/usr/share/package-licenses/pypi-numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
/usr/share/package-licenses/pypi-numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
/usr/share/package-licenses/pypi-numpy/92e11f80803790b67495703271b70d4ae0588f88
/usr/share/package-licenses/pypi-numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
/usr/share/package-licenses/pypi-numpy/c474367bace9239be97704a6272681c4c22ed9f6
/usr/share/package-licenses/pypi-numpy/df1c41ca8a294222a81f70a142832d6566fbd889
/usr/share/package-licenses/pypi-numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*