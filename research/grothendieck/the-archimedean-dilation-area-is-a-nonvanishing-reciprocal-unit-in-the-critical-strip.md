# The archimedean dilation area is a nonvanishing reciprocal unit in the critical strip

## Gaussian infinitesimal area

Use the Fourier-fixed Gaussian

\[
f(x)=e^{-\pi x^2}
\]

and multiplicative Haar measure \(d^\times x=dx/|x|\).  Its local Tate
integral is

\[
Z_{\infty,s}(f)
=
\int_{\mathbb R^\times}
e^{-\pi x^2}|x|^s\,d^\times x
=
\pi^{-s/2}\Gamma(s/2).
\]

For the dilation orbit \(f_t(x)=f(e^{-t}x)\),

\[
Z_{\infty,s}(f_t)=e^{st}Z_{\infty,s}(f),
\qquad
f_t(0)=1.
\]

The oriented infinitesimal boundary area is therefore

\[
A_\infty(s)
=
s\pi^{-s/2}\Gamma(s/2)
=
2\pi^{-s/2}\Gamma(1+s/2).
\]

It is holomorphic and nonzero throughout the critical strip

\[
0<\operatorname{Re}s<1.
\]

## Reciprocal sewing

The reflected sheet contributes

\[
A_\infty(1-s)
=
(1-s)\pi^{-(1-s)/2}\Gamma((1-s)/2),
\]

which is likewise holomorphic and nonzero in the critical strip.  Their ratio

\[
\gamma_\infty(s)
=
\frac{A_\infty(1-s)}{A_\infty(s)}
\]

is therefore an invertible meromorphic transition.  On the critical seam,

\[
s=\frac12+it,
\qquad
1-s=\overline s,
\]

reality of the Gaussian Mellin transform gives

\[
|\gamma_\infty(s)|=1.
\]

Thus the real place explains the unitary seam but cannot generate a
nontrivial zero inside the strip.

## All local boundary minors are units

The finite-place calculation gives unit area exactly.  The archimedean area
is a nonvanishing unit in the critical strip.  Consequently no individual
local boundary determinant loses rank at a nontrivial Riemann zero.

This rules out the local-puncture interpretation in its literal form.  A
nontrivial zero cannot be a puncture of one finite valuation sector or of the
Gaussian dilation cell.  It can arise only after the global assembly map
combines locally invertible comparison data into the distinguished scalar
section.

The distinction is the same one already exposed by the metaplectic control
problem:

- every local transition may be invertible;
- their normalized product may define a nonzero line;
- a particular global section of that line may still vanish.

Therefore the next object is not another local determinant.  It is the
global aggregation or trace map from the tensor product of local unit lines
to the completed theta section.  That map must retain cross-place
correlations absent from the product of local two-by-two minors.

## Sharp boundary

The local programme has now explained two things and excluded a third:

1. finite Tate normalization explains exact local flatness;
2. the archimedean gamma transition explains why the seam is unitary;
3. neither explains why the distinguished global section vanishes only on
   that seam.

The RH-bearing invariant must therefore live in global correlation or
aggregation, not local scalarization.  Any proposed proof that locates a
nontrivial zero in a vanishing local boundary minor contradicts these exact
unit calculations.

