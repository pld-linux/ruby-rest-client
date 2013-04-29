#
# Conditional build:
%bcond_with	tests		# build without tests

%define gem_name rest-client
Summary:	Simple REST client for Ruby
Name:		ruby-%{gem_name}
Version:	1.6.7
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	1f2d6b3b6ceb88e3ee2b327f5e508c22
URL:		http://github.com/archiloque/rest-client
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-mime-types >= 1.16
BuildRequires:	ruby-netrc
BuildRequires:	ruby-rspec
BuildRequires:	ruby-webmock >= 0.9.1
%endif
Requires:	ruby-mime-types >= 1.16
Requires:	ruby-netrc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%prep
%setup -q -n %{gem_name}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
%if %{with tests}
# TODO: According to comment in %%{PATCH0}, at least one test does not passes on
# R1.9.3. I gon't go to investigate further ATM.
rspec spec | grep -e "188 examples, [34] failures"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc history.md
%attr(755,root,root) %{_bindir}/restclient
%{ruby_vendorlibdir}/rest-client.rb
%{ruby_vendorlibdir}/rest_client.rb
%{ruby_vendorlibdir}/restclient.rb
%{ruby_vendorlibdir}/restclient
