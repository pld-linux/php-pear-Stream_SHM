%include	/usr/lib/rpm/macros.php
%define         _class          Stream
%define         _subclass       SHM
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Shared Memory Stream
Summary(pl):	%{_pearname} - strumieniowy dostêp do pamiêci dzielonej
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
# Source0-md5:	4d2c3702fdee3ee9029f0728325ff081
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Stream_SHM/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Stream_SHM package provides a class that can be registered with
stream_register_wrapper() in order to have stream-based shared-memory
access.

This class has in PEAR status: %{_status}.

%description -l pl
Pakiet Stream_SHM udostêpnia klasê, która mo¿e byæ zarejestrowana przy
u¿yciu stream_register_wrapper(), aby mieæ oparty na strumieniach
dostêp do pamiêci dzielonej.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
