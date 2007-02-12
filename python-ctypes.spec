#
# TODO:
# - move the scripts from the wrap subpackage to /usr/bin?
%define 	module ctypes

Summary:	Python package to call functions in dynamic linked libraries
Summary(pl.UTF-8):   Pakiet Pythona do wywoływania funkcji w bibliotekach linkowanych dynamicznie
Name:		python-%{module}
Version:	0.9.9.6
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	6c7240608d564018ef8254721fde0012
URL:		http://starship.python.net/crew/theller/ctypes/
BuildRequires:	libffi-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	libffi
Requires:	python >= 2.3
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
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/
%{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/*.so
