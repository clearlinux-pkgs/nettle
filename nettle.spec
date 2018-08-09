#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF3599FF828C67298 (nisse@lysator.liu.se)
#
Name     : nettle
Version  : 3.4
Release  : 34
URL      : https://mirrors.kernel.org/gnu/nettle/nettle-3.4.tar.gz
Source0  : https://mirrors.kernel.org/gnu/nettle/nettle-3.4.tar.gz
Source99 : https://mirrors.kernel.org/gnu/nettle/nettle-3.4.tar.gz.sig
Summary  : Nettle low-level cryptographic library (symmetric algorithms)
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0+ LGPL-3.0
Requires: nettle-bin
Requires: nettle-lib
Requires: nettle-license
Requires: p11-kit
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gmp-dev
BuildRequires : gmp-dev32
BuildRequires : gmp-lib32
BuildRequires : openssl-dev
BuildRequires : texinfo

%description
What is GNU Nettle? A quote from the introduction in the Nettle Manual:
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space. In most contexts, you need more than the basic
cryptographic algorithms, you also need some way to keep track of available
algorithms, their properties and variants. You often have some algorithm
selection process, often dictated by a protocol you want to implement.

And as the requirements of applications differ in subtle and not so
subtle ways, an API that fits one application well can be a pain to use
in a different context. And that is why there are so many different
cryptographic libraries around.

Nettle tries to avoid this problem by doing one thing, the low-level
crypto stuff, and providing a simple but general interface to it.
In particular, Nettle doesn't do algorithm selection. It doesn't do
memory allocation. It doesn't do any I/O.

The idea is that one can build several application and context specific
interfaces on top of Nettle, and share the code, test cases, benchmarks,
documentation, etc. Examples are the Nettle module for the Pike
language, and LSH, which both use an object-oriented abstraction on top
of the library.

%package bin
Summary: bin components for the nettle package.
Group: Binaries
Requires: nettle-license

%description bin
bin components for the nettle package.


%package dev
Summary: dev components for the nettle package.
Group: Development
Requires: nettle-lib
Requires: nettle-bin
Provides: nettle-devel

%description dev
dev components for the nettle package.


%package dev32
Summary: dev32 components for the nettle package.
Group: Default
Requires: nettle-lib32
Requires: nettle-bin
Requires: nettle-dev

%description dev32
dev32 components for the nettle package.


%package doc
Summary: doc components for the nettle package.
Group: Documentation

%description doc
doc components for the nettle package.


%package extras
Summary: extras components for the nettle package.
Group: Default

%description extras
extras components for the nettle package.


%package lib
Summary: lib components for the nettle package.
Group: Libraries
Requires: nettle-license

%description lib
lib components for the nettle package.


%package lib32
Summary: lib32 components for the nettle package.
Group: Default
Requires: nettle-license

%description lib32
lib32 components for the nettle package.


%package license
Summary: license components for the nettle package.
Group: Default

%description license
license components for the nettle package.


%prep
%setup -q -n nettle-3.4
pushd ..
cp -a nettle-3.4 build32
popd
pushd ..
cp -a nettle-3.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533697256
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-openssl --enable-shared --enable-static  --enable-x86-aesni
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --disable-openssl --enable-shared --enable-static  --enable-x86-aesni   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --disable-openssl --enable-shared --enable-static  --enable-x86-aesni
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make -C testsuite check
make -C ../buildavx2/testsuite check
make -C ../build32/testsuite check

%install
export SOURCE_DATE_EPOCH=1533697256
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/nettle
cp COPYING.LESSERv3 %{buildroot}/usr/share/doc/nettle/COPYING.LESSERv3
cp COPYINGv2 %{buildroot}/usr/share/doc/nettle/COPYINGv2
cp COPYINGv3 %{buildroot}/usr/share/doc/nettle/COPYINGv3
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/nettle-hash
%exclude /usr/bin/nettle-lfib-stream
%exclude /usr/bin/pkcs1-conv
%exclude /usr/bin/sexp-conv
/usr/bin/haswell/nettle-hash
/usr/bin/haswell/nettle-lfib-stream
/usr/bin/haswell/nettle-pbkdf2
/usr/bin/haswell/pkcs1-conv
/usr/bin/haswell/sexp-conv
/usr/bin/nettle-pbkdf2

%files dev
%defattr(-,root,root,-)
/usr/include/nettle/aes.h
/usr/include/nettle/arcfour.h
/usr/include/nettle/arctwo.h
/usr/include/nettle/asn1.h
/usr/include/nettle/base16.h
/usr/include/nettle/base64.h
/usr/include/nettle/bignum.h
/usr/include/nettle/blowfish.h
/usr/include/nettle/buffer.h
/usr/include/nettle/camellia.h
/usr/include/nettle/cast128.h
/usr/include/nettle/cbc.h
/usr/include/nettle/ccm.h
/usr/include/nettle/cfb.h
/usr/include/nettle/chacha-poly1305.h
/usr/include/nettle/chacha.h
/usr/include/nettle/ctr.h
/usr/include/nettle/curve25519.h
/usr/include/nettle/des-compat.h
/usr/include/nettle/des.h
/usr/include/nettle/dsa-compat.h
/usr/include/nettle/dsa.h
/usr/include/nettle/eax.h
/usr/include/nettle/ecc-curve.h
/usr/include/nettle/ecc.h
/usr/include/nettle/ecdsa.h
/usr/include/nettle/eddsa.h
/usr/include/nettle/gcm.h
/usr/include/nettle/gosthash94.h
/usr/include/nettle/hkdf.h
/usr/include/nettle/hmac.h
/usr/include/nettle/knuth-lfib.h
/usr/include/nettle/macros.h
/usr/include/nettle/md2.h
/usr/include/nettle/md4.h
/usr/include/nettle/md5-compat.h
/usr/include/nettle/md5.h
/usr/include/nettle/memops.h
/usr/include/nettle/memxor.h
/usr/include/nettle/nettle-meta.h
/usr/include/nettle/nettle-stdint.h
/usr/include/nettle/nettle-types.h
/usr/include/nettle/pbkdf2.h
/usr/include/nettle/pgp.h
/usr/include/nettle/pkcs1.h
/usr/include/nettle/poly1305.h
/usr/include/nettle/pss-mgf1.h
/usr/include/nettle/pss.h
/usr/include/nettle/realloc.h
/usr/include/nettle/ripemd160.h
/usr/include/nettle/rsa.h
/usr/include/nettle/salsa20.h
/usr/include/nettle/serpent.h
/usr/include/nettle/sexp.h
/usr/include/nettle/sha.h
/usr/include/nettle/sha1.h
/usr/include/nettle/sha2.h
/usr/include/nettle/sha3.h
/usr/include/nettle/twofish.h
/usr/include/nettle/umac.h
/usr/include/nettle/version.h
/usr/include/nettle/yarrow.h
/usr/lib64/haswell/libhogweed.so
/usr/lib64/haswell/libnettle.so
/usr/lib64/libhogweed.so
/usr/lib64/libnettle.so
/usr/lib64/pkgconfig/hogweed.pc
/usr/lib64/pkgconfig/nettle.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libhogweed.so
/usr/lib32/libnettle.so
/usr/lib32/pkgconfig/32hogweed.pc
/usr/lib32/pkgconfig/32nettle.pc
/usr/lib32/pkgconfig/hogweed.pc
/usr/lib32/pkgconfig/nettle.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/haswell/libhogweed.so.4
/usr/lib64/haswell/libhogweed.so.4.4
/usr/lib64/haswell/libnettle.so.6
/usr/lib64/haswell/libnettle.so.6.4

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/haswell/libhogweed.so.4
%exclude /usr/lib64/haswell/libhogweed.so.4.4
%exclude /usr/lib64/haswell/libnettle.so.6
%exclude /usr/lib64/haswell/libnettle.so.6.4
/usr/lib64/libhogweed.so.4
/usr/lib64/libhogweed.so.4.4
/usr/lib64/libnettle.so.6
/usr/lib64/libnettle.so.6.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libhogweed.so.4
/usr/lib32/libhogweed.so.4.4
/usr/lib32/libnettle.so.6
/usr/lib32/libnettle.so.6.4

%files license
%defattr(-,root,root,-)
/usr/share/doc/nettle/COPYING.LESSERv3
/usr/share/doc/nettle/COPYINGv2
/usr/share/doc/nettle/COPYINGv3
