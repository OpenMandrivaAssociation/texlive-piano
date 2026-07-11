%global tl_name piano
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typeset a basic 2-octave piano diagram
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/piano
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piano.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piano.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package adds the \keyboard[1][2]..[7] command to your project. When
used, it draws a small 2 octaves piano keyboard on your document, with
up to 7 keys highlighted. Keys go : Co, Cso, Do, Dso, Eo, Fo, Fso, Go,
Gso, Ao, Aso, Bo, Ct, Cst, Dt, Dst, Et, Ft, Fst, Gt, Gst, At, Ast and
Bt. (A working example is included in the README file.)

