Name:           eucalyptus-java-deps
Version:        4.3
Release:        0%{?build_id:.%build_id}%{?dist}
Summary:        Eucalyptus cloud java dependencies

License:        ASL 2.0 and (ASL 2.0 and BSD) and (ASL 2.0 or EPL) and (ASL 2.0 and LGPLv2+) and (ASL 2.0 or LGPLv2+ or MPLv1.1) and BSD and BSD with advertising and CC-BY and CC-BY-SA and ((CDDL or GPLv2 with exceptions) and ASL 2.0) and CPAL and CPL and ISC and MIT and LGPLv2 and LGPLv2+ and Public Domain and WTFPL
URL:            https://github.com/eucalyptus/eucalyptus-cloud-libs
Source0:        %{tarball_basedir}.tar.xz

BuildArch:      noarch

# Disable automatic OSGI Provides because these don't land in the
# usual systemwide locations
%global __provides_exclude_from ^%{_datadir}/eucalyptus/.*.jar$

Provides:       eucalyptus-java-deps-devel = %{name}-%{release}


%description
This package contains java dependencies for the Eucalyptus cloud
platform.


%prep
%setup -q -n %{tarball_basedir}


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc README
%license licenses/*
%{_datarootdir}/eucalyptus/*.jar


%changelog
* Fri Mar 25 2016 Garrett Holmstrom <gholms@hpe.com>
- Created
