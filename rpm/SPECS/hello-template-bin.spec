Name: hello
Version: 0.1
Release: 1
License: probably not
Summary: The hello world app
Group: bogus/dummy
%description
This is the long description of the hello world app.

%package test

Summary: Debug information for package %{name}
Group: dev/dummy

%description test
This package provides debug information for package %{hello}.

%prep

%build
set -e
make release -C %{buildsubdir}

%install

mkdir -p %{buildroot}/usr/local/bin

cp %{buildsubdir}/hello %{buildroot}/usr/local/bin/

/usr/lib/rpm/find-debuginfo.sh %{buildsubdir}

%pre
echo "This is the hello world package preinstall script"

%clean
set -e
rm -rf %{buildroot}

%files
/usr/local/bin/hello

%files test
%dir /usr/lib/debug
%dir /usr/lib/debug/usr
%dir /usr/lib/debug/usr/local
%dir /usr/lib/debug/usr/local/bin
/usr/lib/debug/usr/local/bin/hello.debug
