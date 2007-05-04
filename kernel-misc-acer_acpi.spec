#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
#
%define _rel		1
%define _orig_name	acer_acpi

Summary:	Linux driver for Acer notebook hardware control
Summary(pl.UTF-8):	Sterownik dla Linuksa do kontroli urządzeń w notebookach Acer
Name:		kernel-misc-%{_orig_name}
Version:	0.3
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://www.archernar.co.uk/acer_acpi/acer_acpi-%{version}.tar.gz
# Source0-md5:	4971a569800757b87041bc542f675743
URL:		http://www.archernar.co.uk/
BuildRequires:	%{kgcc_package}
%{?with_dist_kernel:BuildRequires:	kernel-module-build >= 3:2.6.20.2}
BuildRequires:	rpmbuild(macros) >= 1.379
%{?with_dist_kernel:%requires_releq_kernel}
Requires(post,postun):	/sbin/depmod
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux kernel module to allow control of some of the hardware on later
model Acer (and other Wistron OEM) laptops.

%description -l pl.UTF-8
Moduł jądra Linuksa pozwalający kontrolować część sprzętu w nowszych
laptopach Acera (i innych Wistron OEM).

%prep
%setup -q -n %{_orig_name}-%{version}

%build
%build_kernel_modules -m %{_orig_name}

%install
rm -rf $RPM_BUILD_ROOT
%install_kernel_modules -m %{_orig_name} -d misc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel-misc-%{_orig_name}
%depmod %{_kernel_ver}

%postun	-n kernel-misc-%{_orig_name}
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
%doc NEWS INSTALL README
/lib/modules/%{_kernel_ver}/misc/*.ko*
