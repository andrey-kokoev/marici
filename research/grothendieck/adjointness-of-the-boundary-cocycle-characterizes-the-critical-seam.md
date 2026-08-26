# Adjointness of the boundary cocycle characterizes the critical seam

## Bounded question

At a scalar zero, the exceptional reciprocal prime currents become summable.
Does that completion upgrade automatically make the two sector currents
adjoints, or is adjointness an additional condition?

## Centered interval incidence

For the positive completed half-line source (A), define

\[
B_\ell^+(z)=\int_0^\ell A(v)e^{izv}\,dv,
\qquad
H_+(z)=\int_0^\infty A(v)e^{izv}\,dv.
\]

The centered incidence is

\[
R_\ell^+(z)
=
B_\ell^+(z)-H_+(z)
=
-\int_\ell^\infty A(v)e^{izv}\,dv.
\]

It decays super-polynomially when (ell=k\log p), so every centered prime
sum converges even in the primitive channel. It is not determined by the
single value (H_+(z)): varying (ell) recovers the full tail profile through

\[
\partial_\ell R_\ell^+(z)=A(\ell)e^{iz\ell}.
\]

Thus centered interval incidence has genuine observation-rank increment.

## Reciprocal and adjoint operations

Reciprocal-sheet transport sends

\[
B_\ell^+(z)
\longmapsto
B_\ell^-(z)=B_\ell^+(-z).
\]

Since (A) is real,

\[
\overline{B_\ell^+(z)}
=
B_\ell^+(-\overline z).
\]

Therefore reciprocal transport agrees with Hilbert adjunction on the complete
boundary family precisely when

\[
B_\ell^+(-z)=B_\ell^+(-\overline z)
\]

for every (ell>0).

Differentiating in (ell) and using (A(\ell)>0) gives

\[
e^{-iz\ell}=e^{-i\overline z\ell}
\]

for every (ell>0). This is equivalent to

\[
\operatorname{Im}z=0.
\]

In the Fourier coordinate used for the centered Mellin transform, the real
(z)-axis is the critical seam. Hence adjointness of the complete continuous
boundary cocycle characterizes the seam exactly.

## What a zero does and does not imply

At a scalar zero, the leading rank-one divergence of the primitive and square
prime currents disappears. Their centered reciprocal sums become genuine
summable outputs. But convergence imposes no equality between
(B_\ell^+(-z)) and (B_\ell^+(-\overline z)).

Thus there are two distinct transitions:

1. scalar zero: the exceptional prime currents become summable;
2. critical seam: reciprocal transport becomes Hilbert adjunction.

The first does not algebraically imply the second. Off-seam hostile zeros have
the same completion-class upgrade while failing the adjoint boundary law.

## Conditional confinement theorem

Suppose a source-derived zero-to-state construction proves that every
summability-upgraded zero state extends to a star-compatible representation of
the complete continuous boundary cocycle. Then the preceding characterization
forces

\[
\operatorname{Im}z=0,
\]

and hence places the zero on the critical seam.

The missing RH-strength statement is therefore no longer positivity. It is an
extension theorem:

> Every zero-induced completion-class upgrade extends from the discrete prime
> boundary packets to the source-continuous adjoint boundary cocycle.

This statement has a sharp hostile falsifier. Construct an off-seam zero whose
primitive and square currents converge and test whether its discrete prime
packets admit such a star-compatible continuous extension. If they do, the
route fails. If they do not for a source-visible reason, that reason is the
candidate confinement mechanism.
