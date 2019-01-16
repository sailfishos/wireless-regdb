Name:       wireless-regdb
Summary:    802.11 wireless networking regulatory database
Version:    2016.06.10
Release:    1
Group:      System/Networking
License:    ISC
BuildArch:  noarch
URL:        https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  openssl
BuildRequires:  python
BuildRequires:  python-M2Crypto

%description
This package contains the wireless regulatory database used by all
cfg80211 based Linux wireless drivers.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man page for %{name}.

%prep
%setup -q -n %{name}-%{version}/wireless-regdb

%build
make %{?_smp_mflags} maintainer-clean
make %{?_smp_mflags} REGDB_PRIVKEY=key.priv.pem REGDB_PUBKEY=key.pub.pem

%install
rm -rf %{buildroot}
%make_install

install -Dm0644 README %{buildroot}%{_docdir}/%{name}-%{version}/README

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/crda/pubkeys/key.pub.pem
%{_libdir}/crda/pubkeys/sforshee.key.pub.pem
%{_libdir}/crda/regulatory.bin

%files doc
%defattr(-,root,root,-)
%{_mandir}/man5/regulatory.bin.5.gz
%{_docdir}/%{name}-%{version}
