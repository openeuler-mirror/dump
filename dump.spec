Name:    dump
Epoch:   1
Version: 0.4
Release: 6
Summary: Programs for backing up and restoring ext2/3/4 filesystems
License: BSD
URL:     http://dump.sourceforge.net/
Source0: http://downloads.sourceforge.net/dump/dump-%{version}b47.tar.gz

Patch1:  0001-fix-multiple-define-for-gcc10.patch

BuildRequires: make e2fsprogs-devel readline-devel automake libtool
BuildRequires: bzip2-devel libselinux-devel zlib-devel lzo-devel

Requires: setup rmt

Obsoletes: dump-static
Provides:  dump-static

%description
The dump package contains both dump and restore.Dump examines files in a filesystem,
determines which ones need to be backed up, and copies those files to a specified disk,
tape or other storage medium. Subsequent incremental backups can then be layered on top of the full backup.
The restore command performs the inverse function of dump; it can restore a full backup of a filesystem.
Single files and directory subtrees may also be restored from full or partial backups in interractive mode.

%package_help

%prep
%autosetup -n %{name}-0.4b47 -p1

%build
autoreconf -fiv

export CFLAGS="$RPM_OPT_FLAGS -Wall -Wpointer-arith -Wstrict-prototypes \
-Wmissing-prototypes -Wno-char-subscripts -fno-strict-aliasing"

%configure  --disable-static --enable-transselinux --enable-largefile --disable-rmt --enable-qfa \
    --enable-readline --with-binmode=0755 --with-manowner=root --with-mangrp=root --with-manmode=0644
%make_build

%install
%make_install

pushd %{buildroot}
    ln -sf dump .%{_sbindir}/rdump
    ln -sf restore .%{_sbindir}/rrestore
    mkdir -p .%{_sysconfdir}
    > .%{_sysconfdir}/dumpdates
popd

%pre

%preun

%post

%postun

%files
%license COPYING AUTHORS
%doc KNOWNBUGS MAINTAINERS NEWS REPORTING-BUGS dump.lsm
%attr(0664,root,disk) %config(noreplace) %{_sysconfdir}/dumpdates
%{_sbindir}/*
%exclude %{_sbindir}/rmt

%files help
%doc INSTALL README TODO
%{_mandir}/*/*

%changelog
* Sat Oct 29 2022 wangzhiqiang <wangzhiqiang95@huawei.com> - 1:0.4-6
- modify source0 url

* Wed Nov 17 2021 Wenchao Hao <haowenchao@huawei.com> - 0.4-5
- Update to dump-0.4b47

* Wed Aug 04 2021 chenyanpanHW <chenyanpan@huawei.com> - 0.4-4
- DESC: delete BuildRequires gdb

* Fri Jul 30 2021 yanglongkang <yanglongkang@huawei.com> - 1:0.4-3
- fix multiple define for gcc10

* Sat Mar 21 2020 openEuler Buildteam <buildteam@openeuler.org> - 1:0.4-2
- Add build requires of gdb

* Fri Oct 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:0.4-1
- Package init
