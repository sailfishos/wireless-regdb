Name:       wireless-regdb
Summary:    802.11 wireless networking regulatory database
Version:    2015.06.05
Release:    1
Group:      System/Networking
License:    ISC
BuildArch:  noarch
URL:        http://wireless.kernel.org/en/developers/Regulatory/
Source0:    http://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-2013.01.11.tar.xz
BuildRequires:  openssl
BuildRequires:  python
BuildRequires:  python-M2Crypto

%description
This package contains the wireless regulatory database used by all
cfg80211 based Linux wireless drivers.


%prep
%setup -q -n %{name}-%{version}

%build
cd %{name}
# There is is already verified binary in upstream git tree
# and we trust it is ok for now as otherwise we would need to have
# our own keys to sign it.
#make maintainer-clean
#make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
cd %{name}
%make_install


%files
%defattr(-,root,root,-)
%doc %{name}/LICENSE
%doc %{name}/README
%{_libdir}/crda/pubkeys/*.pem
%{_libdir}/crda/regulatory.bin
%doc %{_mandir}/man5/regulatory.bin.5.gz
