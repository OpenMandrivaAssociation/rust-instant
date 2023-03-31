%bcond_with check
%global debug_package %{nil}

%global crate instant

Name:           rust-%{crate}
Version:        0.1.12
Release:        2
Summary:        Partial replacement for std::time::Instant that works on WASM too

# Upstream license specification: BSD-3-Clause
License:        BSD-3-Clause
URL:            https://crates.io/crates/instant
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0)
%if %{with check}
BuildRequires:  (crate(wasm-bindgen-test/default) >= 0.3.0 with crate(wasm-bindgen-test/default) < 0.4.0)
%endif
%endif

%global _description %{expand:
Partial replacement for std::time::Instant that works on WASM too.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant) = 0.1.12
Requires:       cargo
Requires:       (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOGS.md AUTHORS
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/default) = 0.1.12
Requires:       cargo
Requires:       crate(instant) = 0.1.12

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+inaccurate-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/inaccurate) = 0.1.12
Requires:       cargo
Requires:       crate(instant) = 0.1.12

%description -n %{name}+inaccurate-devel %{_description}

This package contains library source intended for building other packages
which use "inaccurate" feature of "%{crate}" crate.

%files       -n %{name}+inaccurate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+js-sys-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/js-sys) = 0.1.12
Requires:       cargo
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       crate(instant) = 0.1.12

%description -n %{name}+js-sys-devel %{_description}

This package contains library source intended for building other packages
which use "js-sys" feature of "%{crate}" crate.

%files       -n %{name}+js-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+now-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/now) = 0.1.12
Requires:       cargo
Requires:       crate(instant) = 0.1.12

%description -n %{name}+now-devel %{_description}

This package contains library source intended for building other packages
which use "now" feature of "%{crate}" crate.

%files       -n %{name}+now-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stdweb-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/stdweb) = 0.1.12
Requires:       cargo
Requires:       (crate(stdweb/default) >= 0.4.0 with crate(stdweb/default) < 0.5.0)
Requires:       (crate(stdweb/default) >= 0.4.0 with crate(stdweb/default) < 0.5.0)
Requires:       (crate(stdweb/default) >= 0.4.0 with crate(stdweb/default) < 0.5.0)
Requires:       crate(instant) = 0.1.12

%description -n %{name}+stdweb-devel %{_description}

This package contains library source intended for building other packages
which use "stdweb" feature of "%{crate}" crate.

%files       -n %{name}+stdweb-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-bindgen-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/wasm-bindgen) = 0.1.12
Requires:       cargo
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       (crate(web-sys/default) >= 0.3.0 with crate(web-sys/default) < 0.4.0) (crate(web-sys/Performance) >= 0.3.0 with crate(web-sys/Performance) < 0.4.0) (crate(web-sys/PerformanceTiming) >= 0.3.0 with crate(web-sys/PerformanceTiming) < 0.4.0) (crate(web-sys/Window) >= 0.3.0 with crate(web-sys/Window) < 0.4.0)
Requires:       (crate(web-sys/default) >= 0.3.0 with crate(web-sys/default) < 0.4.0) (crate(web-sys/Performance) >= 0.3.0 with crate(web-sys/Performance) < 0.4.0) (crate(web-sys/PerformanceTiming) >= 0.3.0 with crate(web-sys/PerformanceTiming) < 0.4.0) (crate(web-sys/Window) >= 0.3.0 with crate(web-sys/Window) < 0.4.0)
Requires:       (crate(web-sys/default) >= 0.3.0 with crate(web-sys/default) < 0.4.0) (crate(web-sys/Performance) >= 0.3.0 with crate(web-sys/Performance) < 0.4.0) (crate(web-sys/PerformanceTiming) >= 0.3.0 with crate(web-sys/PerformanceTiming) < 0.4.0) (crate(web-sys/Window) >= 0.3.0 with crate(web-sys/Window) < 0.4.0)
Requires:       crate(instant) = 0.1.12
Requires:       crate(instant/wasm-bindgen_rs) = 0.1.12

%description -n %{name}+wasm-bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "wasm-bindgen" feature of "%{crate}" crate.

%files       -n %{name}+wasm-bindgen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-bindgen_rs-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/wasm-bindgen_rs) = 0.1.12
Requires:       cargo
Requires:       (crate(wasm-bindgen/default) >= 0.2.0 with crate(wasm-bindgen/default) < 0.3.0)
Requires:       (crate(wasm-bindgen/default) >= 0.2.0 with crate(wasm-bindgen/default) < 0.3.0)
Requires:       (crate(wasm-bindgen/default) >= 0.2.0 with crate(wasm-bindgen/default) < 0.3.0)
Requires:       crate(instant) = 0.1.12

%description -n %{name}+wasm-bindgen_rs-devel %{_description}

This package contains library source intended for building other packages
which use "wasm-bindgen_rs" feature of "%{crate}" crate.

%files       -n %{name}+wasm-bindgen_rs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+web-sys-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(instant/web-sys) = 0.1.12
Requires:       cargo
Requires:       (crate(web-sys/default) >= 0.3.0 with crate(web-sys/default) < 0.4.0) (crate(web-sys/Performance) >= 0.3.0 with crate(web-sys/Performance) < 0.4.0) (crate(web-sys/PerformanceTiming) >= 0.3.0 with crate(web-sys/PerformanceTiming) < 0.4.0) (crate(web-sys/Window) >= 0.3.0 with crate(web-sys/Window) < 0.4.0)
Requires:       (crate(web-sys/default) >= 0.3.0 with crate(web-sys/default) < 0.4.0) (crate(web-sys/Performance) >= 0.3.0 with crate(web-sys/Performance) < 0.4.0) (crate(web-sys/PerformanceTiming) >= 0.3.0 with crate(web-sys/PerformanceTiming) < 0.4.0) (crate(web-sys/Window) >= 0.3.0 with crate(web-sys/Window) < 0.4.0)
Requires:       (crate(web-sys/default) >= 0.3.0 with crate(web-sys/default) < 0.4.0) (crate(web-sys/Performance) >= 0.3.0 with crate(web-sys/Performance) < 0.4.0) (crate(web-sys/PerformanceTiming) >= 0.3.0 with crate(web-sys/PerformanceTiming) < 0.4.0) (crate(web-sys/Window) >= 0.3.0 with crate(web-sys/Window) < 0.4.0)
Requires:       crate(instant) = 0.1.12

%description -n %{name}+web-sys-devel %{_description}

This package contains library source intended for building other packages
which use "web-sys" feature of "%{crate}" crate.

%files       -n %{name}+web-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
