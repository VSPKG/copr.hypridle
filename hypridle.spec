Name:           hypridle
Version:        0.1.2
Release:        1
Summary:        Hyprland's idle daemon.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hypridle
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  sdbus-cpp-devel

BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
Hyprland's idle daemon

%prep
%autosetup

%build
rm -rf ./* ./.*
git clone %{url} .
git checkout v%{version}
%cmake
%cmake_build

%install
install -m 755 -Dp %{__cmake_builddir}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Apr 26 2024 Vineel Sai <mail@vineelsai.com> 0.1.2-1
- new package built with tito
