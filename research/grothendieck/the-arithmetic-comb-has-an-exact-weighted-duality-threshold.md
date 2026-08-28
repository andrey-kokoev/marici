# The arithmetic comb has an exact weighted duality threshold

Author: `marici.Grothendieck`

## Question

What is the smallest elementary test-space scale on which the logarithmic
arithmetic comb is a continuous functional, and where does its spectral
character evaluation cease to be defined?

## Weighted negative-ray spaces

For \(a>0\), let \(B_a^-\) be the continuous functions on
\(( -\infty,0]\) with norm

\[
\|h\|_a
=
\sup_{v\leq0}e^{-av}|h(v)|.
\]

Thus \(h(-q)\) must decay at least as fast as \(e^{-aq}\).

For a label exponent \(\beta\geq0\), define

\[
\mu_\beta
=
\sum_{n\geq1}n^{-\beta}\delta_{-\log n}.
\]

## Exact continuity threshold

For \(h\in B_a^-\),

\[
|h(-\log n)|
\leq
\|h\|_a n^{-a}.
\]

Therefore

\[
|\langle\mu_\beta,h\rangle|
\leq
\|h\|_a
\sum_{n\geq1}n^{-(a+\beta)}.
\]

The functional \(\mu_\beta\) is continuous on \(B_a^-\) exactly when

\[
a+\beta>1.
\]

Sufficiency is the displayed estimate. Necessity follows by choosing
continuous functions that agree with the positive envelope \(e^{av}\) on
the first finitely many support points. Their \(B_a^-\) norms remain one
while the functional values are the partial sums of
\(\sum n^{-(a+\beta)}\), which are unbounded when \(a+\beta\leq1\).

Hence:

- the theta half-density comb \(\mu_{1/2}\) requires \(a>1/2\);
- the critically gauged unweighted comb \(\mu_0\) requires \(a>1\).

These are exact source-duality thresholds, not heuristic decay estimates.

## Spectral characters expose the same wall

For the exponential character

\[
h_z(v)=e^{-zv},
\]

one has

\[
\langle\mu_\beta,h_z\rangle
=
\sum_{n\geq1}n^{z-\beta}.
\]

It converges exactly in the chamber

\[
\Re z<\beta-1.
\]

This is the same threshold: \(h_z\in B_a^-\) when
\(\Re z\leq-a\), and a compatible \(a\) exists precisely when
\(\Re z<\beta-1\).

Pure Fourier characters have \(\Re z=0\). They lie outside the convergence
chamber for both \(\beta=1/2\) and \(\beta=0\). Thus the critical
spectral readout is not a boundary value already contained in the raw comb
duality. It must be supplied by continuation.

## Categorical reading

The source naturally gives a scale of test spaces rather than one ambient
Hilbert space:

\[
B_b^-\hookrightarrow B_a^-
\qquad
(b>a).
\]

The arithmetic comb is admitted only above its decay threshold. Spectral
characters move oppositely through this scale and reach the critical axis only
after leaving every chamber in which the defining series is continuous.

Accordingly, Tate--Poisson completion must be typed as a boundary-value or
continuation correspondence between different levels of this scale. Treating
it as an internal unitary operator on one completed space erases the precise
place where new analytic meaning is introduced.

## Falsifier

Any proposed source test space must reproduce the sharp criterion
\(a+\beta>1\) on this elementary subscale. A topology admitting the raw comb
and all pure Fourier characters by the same absolutely convergent pairing has
silently inserted a regularization.

## Claim boundary

This proves an exact continuity threshold for a simple weighted Banach scale.
It does not identify the final adelic nuclear space, construct Tate
continuation, or prove any zero-confinement statement.

## Disposition

The common-carrier programme now has a typed domain wall. The next object is
the continuation morphism across that wall and its residual boundary
coordinate.
