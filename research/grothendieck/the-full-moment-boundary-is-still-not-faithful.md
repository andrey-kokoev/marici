# The full moment boundary is still not faithful

## Question

Fourier transport of the logarithmic trace generates every archimedean
endpoint moment.  Does retaining the complete moment tower make the
archimedean observer faithful on the Schwartz source?

## A nonzero state with every moment zero

Choose a nonzero smooth function (b) whose compact Fourier-side support is
contained in

\[
[1,3].
\]

Let φ be its inverse Fourier transform.  Then φ is a nonzero Schwartz
function.  Because (b) vanishes on an open neighborhood of the origin,

\[
b^{(k)}(0)=0
\qquad
k\ge0.
\]

Fourier differentiation gives

\[
b^{(k)}(0)
=
(-2\pi i)^k
\int_{\mathbb R}x^k\phi(x)\,dx.
\]

Therefore

\[
\int_{\mathbb R}x^k\phi(x)\,dx=0
\qquad
k\ge0,
\]

although φ is nonzero.

## What the moment tower actually sees

The complete moment tower is the infinite Taylor jet of the Fourier
transform at the single point zero.  A smooth function is not determined by
that jet.  Flat functions and functions supported away from zero give an
infinite-dimensional invisible fiber.

Thus vanishing of all source moments does not imply φ equal to zero on the
Schwartz category.

The correction to the preceding result is precise.  Fourier naturality
forces every moment coordinate, but those coordinates still do not form a
faithful observer.  They are the endpoint germ of the full Hankel-transformed
trace.

## The faithful choices

There are only two source-authorized ways forward.

First, retain the complete transformed trace (Kh) as a function-valued
boundary port.  Since the original multiplicative trace is injective and
Fourier is invertible, this full port is faithful on the algebraic trace
range.

Second, prove independently that the admitted theta source module is
quasianalytic in the relevant Fourier coordinate, so its Taylor jet at zero
determines the entire transformed trace.  Gaussian analyticity on one orbit
does not establish this for the full constructor closure.  The hostile bump
must be excluded by a named source law rather than by choosing a convenient
topology.

## Revised observer object

The archimedean observer must therefore be typed as

\[
O_\infty^{\mathrm{trace}}
\longrightarrow
O_\infty^{\mathrm{mom}}
\longrightarrow
L_\infty^{\det},
\]

where the arrows are successive compressions:

- the full two-sign Fourier trace;
- its endpoint moment germ;
- the scalar determinant line.

Neither compression is automatically faithful.  The first arrow loses every
Fourier component flat at the endpoint, and the second retains only the
scalar completed determinant.

This produces a hierarchy rather than another arbitrary wall: full
relationship, then endpoint germ, then scalar readout.

The source category must state at which level each constructor and each RH
claim lives.

## Consequence for the categorical attack

The global metaplectic cell already acts faithfully on the full additive
source and its full trace range.  The unresolved task is no longer to invent
more endpoint coefficients.  It is to assemble the arithmetic primitive,
square, connected, and seam ports with the full function-valued
archimedean trace while preserving Fourier–Tate sewing.

Any proof that passes only through moments or the determinant line must first
prove quasianalyticity or accept the invisible bump fiber.

## Scope

The all-moments-zero Schwartz hostile is exact.  It disproves faithfulness of
the full moment tower on the ambient Schwartz source.  It does not disprove
faithfulness on a smaller source-derived quasianalytic module, which remains
to be constructed and justified.

## Result

The infinite archimedean moment wall is necessary but insufficient.  It is
only the endpoint germ of the full Fourier trace.  Completion-stable
observability requires the full function-valued trace, unless theta
constructors independently force a quasianalytic source class.
