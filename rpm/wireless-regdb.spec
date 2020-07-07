%global     _firmwarepath    /usr/lib/firmware
%global     _crdapath        /usr/lib/crda

Name:       wireless-regdb
Summary:    802.11 wireless networking regulatory database
Version:    2020.04.29
Release:    1
License:    ISC
BuildArch:  noarch
URL:        https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
Source0:    %{name}-%{version}.tar.bz2
Patch0:     0001-use-python3.patch
BuildRequires:  openssl
BuildRequires:  python3-base
BuildRequires:  python-M2Crypto

%description
This package contains the wireless regulatory database used by all
cfg80211 based Linux wireless drivers.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man page for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/wireless-regdb

%build
make maintainer-clean
make REGDB_PRIVKEY=key.priv.pem REGDB_PUBKEY=key.pub.pem

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot} FIRMWARE_PATH=%{_firmwarepath} CRDA_PATH=%{_crdapath}

install -Dm0644 README %{buildroot}%{_docdir}/%{name}-%{version}/README

%files
%defattr(-,root,root,-)
%license LICENSE
%{_crdapath}/pubkeys/key.pub.pem
%{_crdapath}/pubkeys/sforshee.key.pub.pem
%{_crdapath}/regulatory.bin
%{_firmwarepath}/regulatory.db
%{_firmwarepath}/regulatory.db.p7s

%files doc
%defattr(-,root,root,-)
%{_mandir}/man5/regulatory.bin.5.gz
%{_mandir}/man5/regulatory.db.5.gz
%{_docdir}/%{name}-%{version}
