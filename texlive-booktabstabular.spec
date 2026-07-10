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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides wrapper environments around tabular and tabular*
that insert \toprule at the beginning, \bottomrule at the end, and
locally remap the legacy \hline and \cline commands to their booktabs
equivalents \midrule and \cmidrule. It also provides commands to
temporarily override the standard tabular and tabular* environments so
that existing documents can opt into this behaviour without rewriting
each table.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/booktabstabular
%dir %{_datadir}/texmf-dist/source/latex/booktabstabular
%dir %{_datadir}/texmf-dist/tex/latex/booktabstabular
%doc %{_datadir}/texmf-dist/doc/latex/booktabstabular/README
%doc %{_datadir}/texmf-dist/doc/latex/booktabstabular/booktabstabular.pdf
%doc %{_datadir}/texmf-dist/source/latex/booktabstabular/booktabstabular.dtx
%doc %{_datadir}/texmf-dist/source/latex/booktabstabular/booktabstabular.ins
%{_datadir}/texmf-dist/tex/latex/booktabstabular/booktabstabular.sty
