%global gemname hammer_cli_foreman
%global confdir hammer

%if 0%{?rhel} < 7
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Universal command-line interface for Foreman
Name: rubygem-%{gemname}
Version: 0.1.0
Release: 13%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli-foreman
Source0: %{gemname}-%{version}.gem
Source1: foreman.yml

%if !(0%{?rhel} > 6 || 0%{?fedora} > 18)
Requires: ruby(abi)
%endif

Requires: ruby(rubygems)
Requires: rubygem(hammer_cli) >= 0.0.18
BuildRequires: ruby(rubygems)
%if 0%{?fedora} || 0%{?rhel} > 6
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
mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/foreman.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/locale
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/foreman.yml
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.md
%doc %{geminstdir}/doc/host_create.md
%doc %{geminstdir}/doc/configuration.md
%doc %{geminstdir}/test


%changelog
* Sat May 17 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-13
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #116 from tstrachota/resolver (martin.bacovsky@gmail.com)
- Refs #5598 - fancy names for all id options (tstrachota@redhat.com)
- refs #3272 - default password will be going away (dcleal@redhat.com)
- Fixes #5657 - Latest string extract (bkearney@redhat.com)

* Wed May 07 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-12
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Fixes #5209 - setting infinite timeouts (tstrachota@redhat.com)

* Tue May 06 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-11
- add new file to package file list (jmontleo@redhat.com)

* Tue May 06 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-10
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- FIxes #5209 - negative timeout config value causes errors
  (tstrachota@redhat.com)
- Refs #4311 - additional tests for the id resolver and option builders
  (tstrachota@redhat.com)
- removed log_api_calls setting (tstrachota@redhat.com)
- Refs #4311 - single resource command, associated list command
  (tstrachota@redhat.com)
- Refs #4311 - test fixes (tstrachota@redhat.com)
- fix in String#format (tstrachota@redhat.com)
- Refs #4311 - get_resource_id refactoring (tstrachota@redhat.com)
- Refs #4311 - read and write commands merged (tstrachota@redhat.com)
- Fixes #4311 - searchables, id resolver and option builders
  (tstrachota@redhat.com)

* Fri May 02 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-9
- remove erroniously added README (jmontleo@redhat.com)

* Fri May 02 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-8
- Adjust macros to work with EL7 and rebuild

* Fri May 02 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-7
- make packaging changes to support RHEL 7 (jmontleo@redhat.com)
* Mon Mar 31 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-6
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Merge pull request #97 from StephanDollberg/3970_os_default_template
  (tstrachota@redhat.com)
- fixes 3970 - adds support for os default templates
  (stephan.dollberg@gmail.com)

* Thu Mar 27 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-5
- update confdir (jmontleo@redhat.com)

* Thu Mar 27 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-4
- update yml config location (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.1.0-3
- update rpm spec file to match upstream and add foreman.yml config
  (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add foreman.yml config
  (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add foreman.yml config
  (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add foreman.yml config
  (jmontleo@redhat.com)

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