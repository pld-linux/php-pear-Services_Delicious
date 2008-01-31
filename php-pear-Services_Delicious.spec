%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Delicious
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Client for the del.icio.us web service
Summary(pl.UTF-8):	%{_pearname} - Klient sieciowej usługi del.icio.us
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	78ee07f4ffd9e49db023d85af9604a72
URL:		http://pear.php.net/package/Services_Delicious/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Client
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR-core
Requires:	php-pear-XML_Serializer >= 0.12.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_Delicious is a client for the REST-based web service of
del.icio.us.

del.icio.us is a social bookmarks manager. It allows you to easily add
sites you like to your personal collection of links, to categorize
those sites with keywords, and to share your collection not only
between your own browsers and machines, but also with others.

Services_Delicious allows you to select, add and delete your bookmarks
from any PHP script.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Servies_Delicious jest klientem opartej na REST usłudze sieciowej
del.icio.us.

del.icio.us jest społecznym zarządcą zakładek. Pozwala na łatwe
dodawanie stron do osobistej kolekcji odnośników, klasyfikowanie stron
według słów kluczowych, oraz dzielenie się kolekcją nie tylko z
różnymi przeglądarkami na różnych maszynach, ale także z innymi
osobami.

Services_Delicious pozwala na wybór, dodanie oraz usuwanie zakładek z
poziomu skryptu PHP.

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
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
