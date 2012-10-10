%define JAVA_HOME /usr/java/latest/
%define AVALON_HOME /usr/local/avalon/
%define TOMCAT_HOME %{AVALON_HOME}tomcat/
%define APR /usr/bin/apr-1-config


Name:           tomcat
Version:        7.0.32
Release:        avalon%{?dist}
Summary:        Tomcat for the Avalon Video System, repackaging binary jar files.

Group:          Avalon Project Team
License:        License 1.0
URL:            http://tomcat.apache.org/
Source0:        apache-tomcat-7.0.32.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  jdk
Requires(pre):  shadow-utils 

%description


%pre
getent group tomcat >/dev/null || groupadd -r GROUPNAME
getent passwd tomcat7 >/dev/null || \
    useradd -r -g tomcat -d /user/local/avalon/tomcat -s /sbin/nologin \
    -c "Tomcat 7 account for Avalon" tomcat7
exit 0

%prep

%setup -n apache-%{name}-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%TOMCAT_HOME
cp -ar %{_builddir}/apache-%{name}-%{version}/* ${RPM_BUILD_ROOT}/%TOMCAT_HOME

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{TOMCAT_HOME}*
%doc



%changelog
