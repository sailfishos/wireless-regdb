Name:       wireless-regdb
Summary:    802.11 wireless networking regulatory database
Version:    2013.11.27
Release:    1
Group:      System/Networking
License:    ISC
BuildArch:  noarch
URL:        http://wireless.kernel.org/en/developers/Regulatory/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  openssl
BuildRequires:  python
BuildRequires:  python-M2Crypto

%description
This package contains the wireless regulatory database used by all
cfg80211 based Linux wireless drivers.


%prep
%setup -q -n %{name}-%{version}/wireless-regdb

%build
make %{?_smp_mflags} maintainer-clean
make %{?_smp_mflags} REGDB_PRIVKEY=key.priv.pem REGDB_PUBKEY=key.pub.pem

%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%doc LICENSE
%doc README
%{_libdir}/crda/pubkeys/key.pub.pem
%{_libdir}/crda/pubkeys/linville.key.pub.pem
%{_libdir}/crda/regulatory.bin
%doc %{_mandir}/man5/regulatory.bin.5.gz

