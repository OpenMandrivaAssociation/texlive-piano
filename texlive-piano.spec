%global tl_name piano
%global tl_revision 79662

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A LaTeX package for drawing piano diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/piano
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piano.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piano.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands to: draw a small 2 octaves piano keyboard
with up to 7 keys highlighted, draw a small 2 octaves piano keyboard
with up to 7 keys highlighted starting with the F key, draw a small 1
octave piano keyboard with up to 7 keys highlighted, draw a small 1
octave piano keyboard with up to 7 keys highlighted and starting with
the F key, draw a small 1 and half octave piano keyboard with up to 7
keys highlighted, draw a small 1 and half octave piano keyboard with up
to 7 keys highlighted.

