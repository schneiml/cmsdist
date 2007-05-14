### RPM external hector 1_3_2
%define rname Hector
%define realversion %(echo %v | cut -d- -f1 )
Requires: root
Source: http://www.fynu.ucl.ac.be/themes/he/ggamma/hector/%{rname}_%{realversion}.tbz

%prep

%setup -q -n %{rname}

%build
export ROOTSYS=$ROOT_ROOT/root
export PATH=$PATH:$ROOTSYS/bin 
make 



%install

tar -c . | tar -x -C %i

