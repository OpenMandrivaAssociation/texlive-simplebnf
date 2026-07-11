%global tl_name simplebnf
%global tl_revision 79057

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	A simple package to format Backus-Naur form (BNF)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simplebnf
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplebnf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplebnf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple way for typesetting grammars in Backus-
Naur form (BNF). The included bnf environment parses BNF expressions
(possibly annotated), so users can write readable BNF expressions in
their documents. It features a flexible configuration system, allowing
for the customization of the domain-specific language (DSL) used in
typesetting the grammar. Additionally, the package comes with sensible
defaults. The package requires expl3, xparse, mathtools, and
tabularray..

