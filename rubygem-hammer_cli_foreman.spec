%global gemname hammer_cli_foreman

%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Universal command-line interface for Foreman
Name: rubygem-%{gemname}
Version: 0.1.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli-foreman
Source0: %{gemname}-%{version}.gem
Source1: cli_config.yml

%if 0%{?rhel} == 6 || 0%{?fedora} < 19
Requires: ruby(abi)
%endif

Requires: ruby(rubygems)
Requires: rubygem(hammer_cli) >= 0.0.18
Requires: rubygem(foreman_api) >= 0.1.11
BuildRequires: ruby(rubygems)
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Hammer cli provides universal extendable CLI interface for ruby apps


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{_sysconfdir}/foreman
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/foreman/cli_config.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/locale
%{_sysconfdir}/foreman
%config(noreplace) %{_sysconfdir}/foreman/cli_config.yml
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec
%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.md
%doc %{geminstdir}/doc/host_create.md
%doc %{geminstdir}/test


%changelog
* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-1
- update rpm spec file version (jmontleo@redhat.com)
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Bump to 0.1.0 (martin.bacovsky@gmail.com)
- Fixes #4849 - Hammer fails silently when no cache is generated
  (martin.bacovsky@gmail.com)
- Fixed dep on rake (v 10.2.0 dropped support for ruby 1.8.x)
  (martin.bacovsky@gmail.com)
- Fixes #4476 - request localized api responses (tstrachota@redhat.com)
- Fixes #3598 - request timeout (tstrachota@redhat.com)
- Add provision_method to host creation (gsutclif@redhat.com)

* Fri Mar 21 2014 Jason Montleon <jmontleo@redhat.com> 0.0.18-8
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Merge pull request #108 from mbacovsky/4697_dashes_in_commands
  (martin.bacovsky@gmail.com)
- fIXes #4697 - Unify format of hammer commands (dashes in names)
  (mbacovsk@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.0.18-7
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Merge pull request #106 from tstrachota/set_param (tstrachota@redhat.com)
- Fixes #4674 - Server formatter fails on not symbol keys (mbacovsk@redhat.com)
- Merge pull request #89 from mbacovsky/3897_apipie_bindings
  (martin.bacovsky@gmail.com)
- Ref #3897 - dynamic bindings (mbacovsk@redhat.com)
- Merge pull request #105 from bkearney/bkearney/zanata (tstrachota@redhat.com)
- refs #4572 - unable to delete parameter (tstrachota@redhat.com)
- Merge pull request #104 from tstrachota/set_param (tstrachota@redhat.com)
- fixes #4587 - adds host option to pass root password
  (stephan.dollberg@gmail.com)
- add zanata translation information (bkearney@redhat.com)
- fixes #4572 - unable to set parameter (tstrachota@redhat.com)

* Mon Mar 17 2014 Jason Montleon <jmontleo@redhat.com> 0.0.18-6
- update katello module name in cli_config.yml (jmontleo@redhat.com)

* Mon Mar 17 2014 Jason Montleon <jmontleo@redhat.com> 0.0.18-5
- package new locale files (jmontleo@redhat.com)

* Mon Mar 17 2014 Jason Montleon <jmontleo@redhat.com> 0.0.18-4
- fixes #4589 - adds conditional output field to show network interfaces
  (stephan.dollberg@gmail.com)
- Fixes #4473 - i18n support (tstrachota@redhat.com)

* Wed Mar 12 2014 Jason Montleon <jmontleo@redhat.com> 0.0.18-3
- add cli_config.yml (jmontleo@redhat.com)

* Wed Mar 12 2014 Jason Montleon <jmontleo@redhat.com> 0.0.18-2
- new package built with tito

* Wed Jan 29 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.18-1
- Bump to 0.0.18 (mbacovsk@redhat.com)

* Thu Jan 23 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.17-1
- Bump to 0.0.17 (mbacovsk@redhat.com)

* Tue Jan 21 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.16-1
- Bump to 0.0.16 (mbacovsk@redhat.com)

* Thu Dec 19 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.15-1
- Bump to 0.0.15 (mbacovsk@redhat.com)

* Wed Dec 18 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.13-1
- Bump to 0.0.13 (mbacovsk@redhat.com)

* Thu Dec 05 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.12-1
- Bump to 0.0.12 (mbacovsk@redhat.com)

* Tue Nov 26 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.11-1
- Bump to 0.0.11 (mbacovsk@redhat.com)

* Fri Nov 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.10-1
- bump to 0.0.10 (mbacovsk@redhat.com)
- updated dependencies

* Mon Nov 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.9-2
- Mark cli_config.yml as a config file (dcleal@redhat.com)
- Update default config for Foreman installation and non-root users
  (dcleal@redhat.com)

* Tue Oct 29 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.9-1
- Update to Hammer CLI Foreman 0.0.9

* Wed Oct 23 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.8-1
- Rebase to 0.0.8 (mbacovsk@redhat.com)

* Thu Oct 10 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.7-1
- Bumped to 0.0.7 (mbacovsk@redhat.com)
- Fixed default config file
- remove deps on awesome_print and terminal-table

* Tue Oct 08 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.6-1
- Update to the latest version of Hammer CLI Foreman

* Thu Sep 26 2013 Sam Kottler <shk@redhat.com> 0.0.5-1
- Bump the version in the spec (shk@redhat.com)
- Update to the latest version (shk@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-2
- Use rubygems-devel on fedora instead of custom macros (shk@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-1
- Remove the 0.0.1 gem bin (shk@redhat.com)
- Bump to version 0.0.3 (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.1-5
- Add configuration to install (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.1-4
- Version bump for rebuild

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.1-3
- Bump version

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com>
- Initial import of the gem (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> - 0.0.1-1
- Initial package
