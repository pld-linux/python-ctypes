%define 	module ctypes

Summary:	Python package to call functions in dynamic linked libraries
Summary(pl):	Pakiet Pythona do wywo³ywania funkcji w bibliotekach linkowanych dynamicznie
Name:		python-%{module}
Version:	0.6.3
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	db17353042d9b96c9187fb8c4507f79f
URL:		http://
BuildRequires:	libffi-devel
Requires:	libffi
Requires:	python >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ctypes is a Python package to create and manipulate C data types in
Python, and to call functions in dynamic link libraries/shared dlls.
It allows wrapping these libraries in pure Python.

%description -l pl
ctypes to pakiet Pythona do tworzenia i obróbki typów danych z C w
Pythonie oraz wywo³ywania funkcji z dynamicznie linkowanych i
wspó³dzielonych bibliotek. Umo¿liwia obudowywanie tych bibliotek w
czystym Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
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
