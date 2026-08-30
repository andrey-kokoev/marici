# Theta finite-part extraction is not positive

## The tempting inference

Packets 188--189 construct the relative Euler detector as

\[
 \zeta(s)=\operatorname{FP}_{\varepsilon\downarrow0}
 \left[Z_{\rho,\varepsilon}(s)-B_{\rho,\varepsilon}(s)\right].
\]

For real `s` in an initial convergence chamber and a nonnegative regulator,
the regulated bulk `Z_{rho,epsilon}` is positive. It is tempting to try to
transport that positivity through the finite-part operation.

## Universal counterexample

Finite-part extraction is not order preserving. Fix `a>0`. For any real
constant `c`, set

\[
 F_\varepsilon=\varepsilon^{-a}+c.
\]

For all sufficiently small positive `epsilon`,

\[
 F_\varepsilon>0,
\]

but after subtracting its positive divergent boundary term,

\[
 \operatorname{FP}_{\varepsilon\downarrow0}
 \left(F_\varepsilon-\varepsilon^{-a}\right)=c.
\]

The finite part can therefore have either sign or vanish while the regulated
bulk remains strictly positive at every sufficiently fine scale.

More generally, if a regulated source has expansion

\[
 Z_\varepsilon=B_\varepsilon+C+o(1),
 \qquad B_\varepsilon\longrightarrow+\infty,
\]

then eventual positivity of `Z_epsilon` imposes no constraint on `C`.

## Consequence for the theta programme

Regulator universality proves that all admissible smoothing charts produce
the same relative section. It does not turn the finite-part map into a
positive functional. Even if \(Z_{\rho,\varepsilon}>0\) for every sufficiently
small \(\varepsilon\), it does not follow that

\[
 \operatorname{FP}(Z_{\rho,\varepsilon}-B_{\rho,\varepsilon})>0.
\]

This closes every RH route using only:

1. positivity of the heat- or Mellin-regulated theta bulk;
2. regulator independence of the boundary-subtracted finite part; and
3. passage to `epsilon=0` without a source-derived relative order law.

## Required replacement

Any surviving argument must control the bulk and boundary current jointly.
It needs an identity or cone on the relative pair

\[
 (Z_{\rho,\varepsilon},B_{\rho,\varepsilon}),
\]

preserved under Poisson sewing and regulator change, whose quotient readout
cannot vanish off the seam. Ordinary positivity on the first coordinate is
insufficient.

The smallest hostile falsifier for a proposed relative order is a positive
one-parameter family with negative or zero finite part that satisfies all of
the declared covariance axioms.

## Scope

This is a no-go theorem about proof architecture, not a statement about the
sign of `zeta(s)` or Xi. It says exactly which information is destroyed when
the boundary divergence is subtracted without a coupled order structure.
