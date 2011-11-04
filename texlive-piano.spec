# revision 21574
# category Package
# catalog-ctan /macros/latex/contrib/piano
# catalog-date 2011-03-01 13:06:36 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-piano
Version:	1.0
Release:	1
Summary:	Typeset a basic 2-octave piano diagram
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/piano
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piano.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piano.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This package adds the \keyboard[1][2]..[7] command to your
project. When used, it draws a small 2 octaves piano keyboard
on your document, with up to 7 keys highlighted. Keys go : Co,
Cso, Do, Dso, Eo, Fo, Fso, Go, Gso, Ao, Aso, Bo, Ct, Cst, Dt,
Dst, Et, Ft, Fst, Gt, Gst, At, Ast and Bt. (A working example
is included in the README file.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/piano/piano.sty
%doc %{_texmfdistdir}/doc/latex/piano/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
