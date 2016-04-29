#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nettle
Version  : 3.2
Release  : 16
URL      : https://ftp.gnu.org/gnu/nettle/nettle-3.2.tar.gz
Source0  : https://ftp.gnu.org/gnu/nettle/nettle-3.2.tar.gz
Summary  : Nettle low-level cryptographic library (symmetric algorithms)
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0+ LGPL-3.0
Requires: nettle-bin
Requires: nettle-lib
Requires: nettle-doc
BuildRequires : gmp-dev
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


%package doc
Summary: doc components for the nettle package.
Group: Documentation

%description doc
doc components for the nettle package.


%package lib
Summary: lib components for the nettle package.
Group: Libraries

%description lib
lib components for the nettle package.


%prep
%setup -q -n nettle-3.2

%build
%configure --disable-static --enable-shared --enable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
cd testsuite ; make check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/nettle-hash
%exclude /usr/bin/nettle-lfib-stream
%exclude /usr/bin/pkcs1-conv
%exclude /usr/bin/sexp-conv
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
/usr/include/nettle/hmac.h
/usr/include/nettle/knuth-lfib.h
/usr/include/nettle/macros.h
/usr/include/nettle/md2.h
/usr/include/nettle/md4.h
/usr/include/nettle/md5-compat.h
/usr/include/nettle/md5.h
/usr/include/nettle/memxor.h
/usr/include/nettle/nettle-meta.h
/usr/include/nettle/nettle-stdint.h
/usr/include/nettle/nettle-types.h
/usr/include/nettle/pbkdf2.h
/usr/include/nettle/pgp.h
/usr/include/nettle/pkcs1.h
/usr/include/nettle/poly1305.h
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
