# spec file for package nodejs-nodejs-util-deprecate
%{?scl:%scl_package nodejs-nodejs-util-deprecate}
%{!?scl:%global pkg_name %{name}}

%global npm_name util-deprecate
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-util-deprecate
Version:	1.0.1
Release:	1%{?dist}
Summary:	The Node.js `util.deprecate()` function with browser support
Url:		https://github.com/TooTallNate/util-deprecate
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%description
The Node.js `util.deprecate()` function with browser support

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
echo "Error: no test specified" && exit 1
%endif

%files
%{nodejs_sitelib}/util-deprecate

%doc README.md LICENSE

%changelog
* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build
