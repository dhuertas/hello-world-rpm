
%_topdir      /home/dhuertas/hello/rpm

%_builddir    %{_topdir}/BUILD

%_rpmdir      %{_topdir}/RPMS

%_specdir     %{_topdir}/SPECS

%buildroot    %{_builddir}/%{name}-%{version}

%buildsubdir  %{_topdir}/../src
