# Diagonal prime det3 pushes all zero content into primitive continuation

## Native diagonal model

On the labelled prime Hilbert space, define

\[
K(s)e_p=p^{-s}e_p.
\]

For (sigma=\operatorname{Re}s>0),

\[
\lVert K(s)\rVert=2^{-\sigma}<1.
\]

Hence (I-K(s)) is invertible by the Neumann series throughout that
half-plane.

Moreover,

\[
\lVert K(s)\rVert_3^3
=
\sum_p p^{-3\sigma}.
\]

This converges whenever

\[
\sigma>\frac13.
\]

Thus the third regularized determinant

\[
\det_3(I-K(s))
\]

is defined and zero-free on the larger half-plane
(operatorname{Re}s>1/3).

## Exact Euler decomposition

For (operatorname{Re}s>1), absolute convergence gives

\[
\log\zeta(s)
=
\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k}.
\]

The regularized determinant satisfies

\[
\log\det_3(I-K(s))
=
-\sum_p\sum_{k\ge3}\frac{p^{-ks}}{k}.
\]

Define the first two Euler currents

\[
J_1(s)=\sum_p p^{-s},
\qquad
J_2(s)=\frac12\sum_p p^{-2s}.
\]

Then

\[
\zeta(s)
=
\frac{e^{J_1(s)+J_2(s)}}{\det_3(I-K(s))}
\]

in the domain of absolute Euler convergence.

This is the exact scalar realization of the three-level prime filtration.

## Convergence split

The three pieces have sharply different domains:

- the regularized tail exists for (operatorname{Re}s>1/3);
- the square current converges for (operatorname{Re}s>1/2);
- the primitive current converges only for (operatorname{Re}s>1).

Therefore, between the Euler half-plane and the critical half-plane, neither
the Schatten-three determinant nor the square current is the obstruction. The
entire missing continuation is concentrated in (J_1), together with the
endpoint and archimedean completion required at (s=1).

## No-go consequence

Suppose one could derive a finite analytic continuation of the primitive
current into the open half-plane (operatorname{Re}s>1/2), compatible with the
Euler identity and the endpoint correction. Its exponential would be
nonvanishing there. The square exponential is also nonvanishing, and the
regularized determinant is already zero-free. The completed Euler object would
therefore be zero-free in that half-plane.

Thus a source-derived analytic primitive continuation with the required sewing
law is already RH-strength content. The Schatten-three determinant does not
explain it; it isolates it.

Constructing (J_1) by taking a logarithm of the known completed zeta or xi
section is circular, because the existence of that analytic logarithm is
equivalent to zero-freeness on the chosen domain.

## Role of the first two currents

The square current has a legitimate determinant-frame role and reaches the
critical boundary from the open right side. The primitive current is different:
its continuation is not a harmless exponential normalization. A global finite
choice of its logarithmic branch is obstructed exactly by zeros and the pole.

This sharpens the earlier interpretation:

- \(k\ge3\) supplies a zero-free regularized determinant tail;
- (k=2) supplies a convergent boundary-frame correction in the open critical
  half-plane;
- (k=1) carries the unresolved analytic continuation and monodromy;
- endpoint and gamma terms type the pole and reciprocal sewing.

## Finite falsifier

Any proposed primitive-current continuation must be constructed without
dividing by the completed scalar or taking its logarithm. At finite cutoff,
verify the exact identity

\[
\log\zeta_X(s)
-J_{1,X}(s)
-J_{2,X}(s)
+\log\det_3(I-K_X(s))
=0.
\]

Then test whether the proposed (J_{1,X}) converges locally uniformly on every
compact subset of (operatorname{Re}s>1/2) after the declared endpoint
renormalization.

One compact set with a non-Cauchy primitive sequence closes the continuation
route. A continuation defined from the scalar completed section is rejected as
authority transported backward from the desired readout.

## Decisive boundary

The diagonal prime determinant gives a source-native zero-free tail but no RH
orientation. It proves that the live arithmetic problem is the primitive
current's source-derived continuation and its compatibility with completion.

Unless a new source operation constructs that continuation independently, the
Schatten-three determinant programme has only reorganized the RH-equivalent
obstruction.
