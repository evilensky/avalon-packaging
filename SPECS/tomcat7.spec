%define JAVA_HOME /usr/java/latest/
%define AVALON_HOME /usr/local/
%define TOMCAT_HOME %{AVALON_HOME}tomcat/
%define APR /usr/bin/apr-1-config


Name:           tomcat
Version:        7.0.32
Release:        1%{?dist}
Summary:        Tomcat for the Avalon Video System, repackaging binary jar files.

Group:          Avalon Project Team
License:        Yes
URL:            http://tomcat.apache.org/
Source0:        apache-tomcat-7.0.32.tar.gz
Source1:        tomcat
Source2:        tomcat_sysconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires: 
Requires:       java-1.6.0-sun
Requires:       tomcat-native
Requires(pre):  shadow-utils 

%description


%pre
getent group tomcat >/dev/null || groupadd -r tomcat
getent passwd tomcat7 >/dev/null || \
    useradd -r -g tomcat -d /user/local/tomcat -s /sbin/nologin \
    -c "Tomcat 7 account for Avalon" tomcat7
exit 0

%prep

%setup -n apache-%{name}-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%TOMCAT_HOME
mkdir -p ${RPM_BUILD_ROOT}/var/log/tomcat7
mkdir -p ${RPM_BUILD_ROOT}/etc/rc.d/init.d
mkdir -p ${RPM_BUILD_ROOT}/etc/sysconfig/

cp -ar %{_builddir}/apache-%{name}-%{version}/* ${RPM_BUILD_ROOT}/%{TOMCAT_HOME}
cp -ar %{SOURCE1} ${RPM_BUILD_ROOT}/etc/rc.d/init.d/
cp -ar %{SOURCE2} ${RPM_BUILD_ROOT}/etc/sysconfig/tomcat

rm -rf ${RPM_BUILD_ROOT}%{TOMCAT_HOME}logs
ln -s  /var/log/tomcat7 ${RPM_BUILD_ROOT}%{TOMCAT_HOME}logs

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(755,tomcat7,tomcat,755)
%{TOMCAT_HOME}
/var/log/tomcat7

%config(noreplace) %attr(755,root,root)/etc/rc.d/init.d/tomcat
%config(noreplace) %attr(755,root,root)/etc/sysconfig/tomcat



%changelog
