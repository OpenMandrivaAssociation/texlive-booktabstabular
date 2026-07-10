%global tl_name booktabstabular
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Automatic application of the booktabs style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/booktabstabular
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabstabular.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabstabular.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabstabular.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides wrapper environments around tabular and tabular*
that insert \toprule at the beginning, \bottomrule at the end, and
locally remap the legacy \hline and \cline commands to their booktabs
equivalents \midrule and \cmidrule. It also provides commands to
temporarily override the standard tabular and tabular* environments so
that existing documents can opt into this behaviour without rewriting
each table.

