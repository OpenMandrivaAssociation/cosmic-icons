Name:           cosmic-icons
Version:        1.0.0
%define beta beta.1
Release:        %{?beta:0.%{beta}.}1
Summary:        System76 Cosmic icon theme for Linux
License:        CC-BY-SA-4.0 AND GPL-3.0-only
Group:          Icons/Cosmic
URL:            https://github.com/pop-os/cosmic-icons
Source0:        https://github.com/pop-os/cosmic-icons/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
BuildRequires:  just
BuildRequires:  zstd
BuildArch:      noarch
Requires:       pop-icon-theme

%description
These are the icons used by the COSMIC DE, created by System76

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -p1

%build
# nothing to build
#just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE COPYING
%doc README.md
%{_datadir}/icons/Cosmic
