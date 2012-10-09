%define JAVA_HOME=/usr/java/latest

Name:           tomcat-native
Version:        1.1.24
Release:        avalon%{?dist}
Summary:        Tomcat Native integration for RHEL6 Apache

Group:          Avalon Project Team
License:        License 1.0
URL:            http://tomcat.apache.org/native-doc/
Source0:        tomcat-native-1.1.24.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  apr-devel 
BuildRequires:  openssl-devel
#Requires:       tomcat 

%description


%prep
%setup -q -n tomcat-native-1.1.24/jni/native


%build
%configure --with-apr=/usr/bin/apr-1-config --with-java-home=/usr/java/latest --with-ssl=yes --prefix=/usr/local/tomcat/
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
   /usr/lib64/libtcnative*
   /usr/lib64/pkgconfig/tcnative-1.pc
%doc



%changelog
