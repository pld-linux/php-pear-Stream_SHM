%include	/usr/lib/rpm/macros.php
%define		_class		Stream
%define		_subclass	SHM
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - shared memory stream
Summary(pl.UTF-8):	%{_pearname} - strumieniowy dostęp do pamięci dzielonej
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4d2c3702fdee3ee9029f0728325ff081
URL:		http://pear.php.net/package/Stream_SHM/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Stream_SHM package provides a class that can be registered with
stream_register_wrapper() in order to have stream-based shared-memory
access.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet Stream_SHM udostępnia klasę, która może być zarejestrowana przy
użyciu stream_register_wrapper(), aby mieć oparty na strumieniach
dostęp do pamięci dzielonej.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
