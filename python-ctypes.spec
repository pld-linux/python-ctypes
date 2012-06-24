%define 	module ctypes

Summary:	Python package to call functions in dynamic linked libraries
Summary(pl):	Pakiet Pythona do wywo�ywania funkcji w bibliotekach linkowanych dynamicznie
Name:		python-%{module}
Version:	0.9.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	0bf48717513a45350081b78b79caf703
URL:		http://starship.python.net/crew/theller/ctypes/
BuildRequires:	libffi-devel
Requires:	libffi
Requires:	python >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ctypes is a Python package to create and manipulate C data types in
Python, and to call functions in dynamic link libraries/shared dlls.
It allows wrapping these libraries in pure Python.

%description -l pl
ctypes to pakiet Pythona do tworzenia i obr�bki typ�w danych z C w
Pythonie oraz wywo�ywania funkcji z dynamicznie linkowanych i
wsp�dzielonych bibliotek. Umo�liwia obudowywanie tych bibliotek w
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

rm $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
