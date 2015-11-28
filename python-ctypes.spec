#
# TODO:
# - move the scripts from the wrap subpackage to /usr/bin?
%define 	module ctypes

Summary:	Python package to call functions in dynamic linked libraries
Summary(pl.UTF-8):	Pakiet Pythona do wywoływania funkcji w bibliotekach linkowanych dynamicznie
Name:		python-%{module}
Version:	1.0.2
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/ctypes/%{module}-%{version}.tar.gz
# Source0-md5:	94ff7aa7f7f71b23bac8a98065d77743
URL:		http://starship.python.net/crew/theller/ctypes/
# modified libffi included
#BuildRequires:	libffi-devel
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-modules >= 2.3
# ctypes already included in python 2.5
BuildRequires:	python < 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ctypes is a Python package to create and manipulate C data types in
Python, and to call functions in dynamic link libraries/shared dlls.
It allows wrapping these libraries in pure Python.

%description -l pl.UTF-8
ctypes to pakiet Pythona do tworzenia i obróbki typów danych z C w
Pythonie oraz wywoływania funkcji z dynamicznie linkowanych i
współdzielonych bibliotek. Umożliwia obudowywanie tych bibliotek w
czystym Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/
%{py_sitedir}/ctypes
%attr(755,root,root) %{py_sitedir}/_ctypes.so
%attr(755,root,root) %{py_sitedir}/_ctypes_test.so
