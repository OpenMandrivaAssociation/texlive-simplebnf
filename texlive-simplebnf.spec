Name:		texlive-simplebnf
Version:	64091
Release:	2
Summary:	A simple package to format Backus-Naur form (BNF)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simplebnf
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplebnf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplebnf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a simple way to format Backus-Naur form
(BNF). The included bnfgrammar environment parses BNF
expressions (possibly annotated), so users can write readable
BNF expressions in their documents. The package requires expl3,
xparse, and mathtools.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/simplebnf
%doc %{_texmfdistdir}/doc/latex/simplebnf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
