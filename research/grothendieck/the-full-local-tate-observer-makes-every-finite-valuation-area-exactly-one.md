# The full local Tate observer makes every finite valuation area exactly one

## Replace the static Haar projection

The local area \(1-p^{-1}\) was obtained from evaluation and additive Haar
volume.  The spectral theta/Tate system carries a stronger observer.  With
multiplicative Haar measure normalized by

\[
\operatorname{vol}(\mathbb Z_p^\times)=1,
\]

define, initially for \(\operatorname{Re}s>0\),

\[
Z_{p,s}(f)
=
\int_{\mathbb Q_p^\times}
f(x)|x|_p^s\,d^\times x.
\]

For the adjacent valuation cells

\[
f_{0,p}=1_{\mathbb Z_p},
\qquad
f_{1,p}=1_{p\mathbb Z_p},
\]

one has

\[
Z_{p,s}(f_{0,p})
=
\sum_{j\ge0}p^{-js}
=
\frac{1}{1-p^{-s}},
\]

and

\[
Z_{p,s}(f_{1,p})
=
\sum_{j\ge1}p^{-js}
=
\frac{p^{-s}}{1-p^{-s}}.
\]

Both functions take value one at the origin.  Therefore the ordered boundary
bivector evaluates on the ordered adjacent-cell two-cycle as

\[
(\epsilon_p\wedge Z_{p,s})
(f_{1,p}\wedge f_{0,p})
=
\frac{1-p^{-s}}{1-p^{-s}}
=1.
\]

The identity is exact before global multiplication and continues
meromorphically wherever the separate local expressions are represented.

## Consequences

Every finite place carries a canonical unit determinant line when the full
Tate observer is retained.  Hence for every finite prime cutoff

\[
\prod_{p\le X}
(\epsilon_p\wedge Z_{p,s})(\chi_p)
=1.
\]

There is no finite-place volume collapse in the complete spectral chart.
The earlier product

\[
\prod_{p\le X}(1-p^{-1})
\]

is the scalar shadow obtained after projecting the full Tate observer to its
static additive-Haar component at \(s=1\).  Its square countercurrent
renormalization is correct within that projected chart, but the complete
local Euler tower already packages the cancellation exactly.

This explains why the finite divisor system repeatedly appeared flat.  The
Euler denominator is not an external correction to the adjacent-cell area;
it is the response of the full local observer to the vacuum cell.

## The obstruction moves to infinity

The finite valuation lattice has a canonical first proper subcell.  The real
place has a continuous dilation orbit and no distinguished adjacent step.
For a source vector \(f\), put

\[
f_t(x)=f(e^{-t}x).
\]

Then

\[
Z_{\infty,s}(f_t)=e^{st}Z_{\infty,s}(f),
\qquad
\epsilon_\infty(f_t)=\epsilon_\infty(f).
\]

The infinitesimal two-cycle \(\dot f_0\wedge f\) consequently has area,
up to its declared orientation,

\[
s\,f(0)Z_{\infty,s}(f).
\]

For the Fourier-fixed Gaussian this is the gamma-completion factor multiplied
by \(s\).  Unlike the finite local areas, it is not identically one.

Thus the scalarization frontier is now irreducibly archimedean and
continuous-scale:

1. finite places normalize to unit area through their full Tate observers;
2. the real place contributes the nontrivial infinitesimal dilation area;
3. reciprocal sewing must compare that area with its reflected mate;
4. the resulting global boundary current must match the doubled Green law.

## Scope

This theorem does not remove prime arithmetic from the completed scalar
section.  It shows that one particular local boundary determinant is a
normalization identity and therefore cannot itself carry RH orientation.
Arithmetic remains in the labelled transition system and in how the global
section is assembled.  Any proof that attributes a nontrivial finite-place
boundary volume to this exact two-by-two minor has projected away the Euler
response that makes the minor unit.

