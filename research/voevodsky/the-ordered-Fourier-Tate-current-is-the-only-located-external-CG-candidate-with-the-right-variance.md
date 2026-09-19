# The ordered Fourier--Tate current is the only located external CG candidate with the right variance

The repository contains several independently derived arithmetic currents, but
they do not have equal suitability for the external `CG` comparison.

The primitive, prime-square, and connected determinant currents are the
logarithmic cumulants of the bordered prime determinant.  They correctly build
the multigraded determinant line, but no current theorem makes them act on the
ordered pair/Green state or couples them to the archimedean antisymmetric
coordinate before scalarization.  They are therefore valid characteristic
strata, not yet a mixed `CG` current.

The ordered source current has the required variance.  For the completed theta
forcing `f`, define

\[
C_f(z)=2\int_{v>q}f(q)f(v)\sinh(z(v-q))\,dq\,dv.
\]

Superexponential decay makes `C_f` entire with all parameter derivatives, and
the independent Green calculation gives

\[
C_f(z)=-\int_0^\infty r_\Delta(q;z)\,dq,
\qquad
r_\Delta=-f(q)(u_z(q)-v_z(q)).
\]

Thus this current already has:

- an independent source integral;
- an exact Green-response realization;
- odd reciprocal character;
- degree-minus-one dilation behavior;
- completed analytic-domain and Fubini control.

Its remaining gate is one functorial Fourier--Tate square.  If
`FT_src` denotes source completion and `FT_bdry` the declared relative boundary
transport, one must prove

\[
FT_{\rm bdry}(C_f)
=
C_{FT_{\rm src}f}
\]

in the multigraded boundary line, retaining primitive, square, connected,
seam, and archimedean coordinates.  Scalar functional-equation agreement is
insufficient because it can erase the odd order current.

Consequently the candidate inventory narrows as follows:

1. determinant cumulants: correct characteristic line, wrong current type
   unless a mixed action is added;
2. strict passive return: Green-typed but zero-free and divisor-blind;
3. ordered Fourier--Tate current: correct source, Green, reciprocal, and
   dilation variance; transport square still open.

The next nonredundant test is therefore the Fourier--Tate naturality of the
ordered current, not another determinant expansion or internal Stokes
identity.
