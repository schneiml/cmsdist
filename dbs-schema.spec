### RPM cms dbs-schema DBS_1_0_1
Requires: gcc-wrapper

%define cvstag %v
Source: cvs://:pserver:anonymous@cmscvs.cern.ch:2401/cvs_server/repositories/CMSSW?passwd=AA_:yZZ3e&module=DBS/Schema/NeXtGen&export=DBS/Schema/NeXtGen&tag=-r%{cvstag}&output=/dbs-schema.tar.gz
Requires: mysql oracle

%prep
%setup -n DBS
%build
## IMPORT gcc-wrapper
(make DBSHOME=%_builddir/DBS/Schema/NeXtGen )

%install
mkdir -p %{i}/etc/profile.d
ls -l Schema/NeXtGen
cp -r Schema/NeXtGen/* %{i}/

(echo "#!/bin/sh"; \
 echo "source $ORACLE_ROOT/etc/profile.d/init.sh"; \
 echo "source $MYSQL_ROOT/etc/profile.d/init.sh"; \
 ) > %{i}/etc/profile.d/dependencies-setup.sh

(echo "#!/bin/tcsh"; \
 echo "source $ORACLE_ROOT/etc/profile.d/init.csh"; \
 echo "source $MYSQL_ROOT/etc/profile.d/init.csh"; \
 ) > %{i}/etc/profile.d/dependencies-setup.csh

%post
%{relocateConfig}etc/profile.d/dependencies-setup.sh
%{relocateConfig}etc/profile.d/dependencies-setup.csh
