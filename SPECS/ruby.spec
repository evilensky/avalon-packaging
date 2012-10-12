%define JAVA_HOME /usr/java/latest/
%define AVALON_HOME /usr/local/avalon/
%define TOMCAT_HOME %{AVALON_HOME}tomcat/
%define PATCH  p286
%define RUBY_HOME   %{AVALON_HOME}%{name}-%{version}-%{PATCH}/

Name:           ruby
Version:        1.9.3
Release:        avalon%{?dist}
Summary:        Ruby runtime for Avalon

Group:          Avalon Project Team
License:        License 1.0
URL:            http://www.ruby-lang.com
Source0:        ruby-1.9.3-p286.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#BuildRequires:  
#Requires:       
#Requires:       

%description


%prep
%setup -q -n %{name}-%{version}-%{PATCH}


%build
%configure --prefix=%{RUBY_HOME} --enable-shared
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT%{RUBY_HOME}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{RUBY_HOME}*
%doc



%changelog
