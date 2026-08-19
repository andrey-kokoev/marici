# 906 — The First Mixed Six-Point Basis Corner Has No Numerical Coherence Defect

> **Variance correction (Entry 908).** The original checker serialized both kernels as right-by-left matrices and multiplied them without transposing the dense kernel. Entry 908 repairs the map to \(T=M_{\rm block}K_{\rm dense}\) in contraction variance, equivalently \(M_{\rm block}\mathcal S^T\). The numerical conclusion survives with the corrected checker; Entry 908's values supersede the numbers below.

## Frozen comparison

Retain Entry 905's canonical transition

\[
T=M_{\rm block}K_{\rm dense}.
\]

The first mixed corner is

\[
D_+=(s_{23}=0),
\qquad
D_-=(s_{235}=0).
\]

Entry 905 gives

\[
\operatorname{ord}_{D_+}\det T=+1,
\qquad
\operatorname{ord}_{D_-}\det T=-1.
\]

Thus this corner compares a zero modification with a pole modification and cannot be audited from determinant support alone.

## Ordered normalization

The pole normal is fixed by the source sine propagator. Define

\[
\widehat T
=
\sin(\pi s_{235})T.
\]

No factor of \(s_{23}\) is inserted: its role is a zero modification, not a pole removal.

Compare the two hierarchical limits

\[
\mathsf L_{-+}
=
\lim_{s_{23}\to0}
\lim_{s_{235}\to0}widehat T,
\]

and

\[
\mathsf L_{+-}
=
\lim_{s_{235}\to0}
\lim_{s_{23}\to0}widehat T.
\]

Numerically these are implemented without setting either singular matrix directly:

\[
(s_{23},s_{235})=(h,h^2)
\]

and

\[
(s_{23},s_{235})=(h^2,h),
\]

for

\[
h=10^{-2},5\cdot10^{-3},2.5\cdot10^{-3},1.25\cdot10^{-3},6.25\cdot10^{-4}.
\]

## Full-matrix result

Both complete \(6\times6\) matrix sequences converge at first order. For three independent generic tangential kinematic slices, the last raw maximum-entry discrepancies are

\[
6.91\cdot10^{-3},
\qquad
7.87\cdot10^{-3},
\qquad
9.50\cdot10^{-3}.
\]

First-order Richardson extrapolation reduces them to

\[
8.59\cdot10^{-5},
\qquad
1.26\cdot10^{-4},
\qquad
2.06\cdot10^{-4}.
\]

The discrepancy decreases with the cutoff on every slice; no nonzero limiting commutator is observed.

The durable checker and packet are

research/benincasa/marici-gm/src/bin/string_six_point_mixed_corner.rs

and

research/benincasa/string-six-point-mixed-corner.json.

## Narrow result

At the first zero/pole channel corner,

\[
\boxed{
\mathsf L_{-+}=\mathsf L_{+-}
}
\]

to the precision and convergence order of the three-slice full-matrix audit.

Thus no numerical Beck--Chevalley/coherence defect is detected at

\[
s_{23}=s_{235}=0.
\]

## Epistemic boundary

This is not yet an exact symbolic equality. The calculation establishes convergent, slice-independent numerical evidence for the complete matrix, not merely its determinant. It does not authorize an all-corner or all-arity theorem.

## Next falsifier

The next useful move is an exact local certificate. Replace the floating hierarchical limits by a bivariate Laurent calculation over a large prime, extract the coefficient of the normalized exceptional grade, and verify equality of the two iterated coefficient maps. If exact equality holds at two primes and generic tangential samples, the numerical conclusion can be promoted to a finite algebraic certificate.
