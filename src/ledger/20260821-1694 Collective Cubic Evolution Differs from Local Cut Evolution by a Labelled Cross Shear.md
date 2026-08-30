# 1694 — Collective Cubic Evolution Differs from Local Cut Evolution by a Labelled Cross Shear

## Cut-compatibility falsifier

Entry 1693 derives a physical second-grade fourth cumulant from exact cubic
evolution.  Compare collective evolution with cardinality-weighted evolution
of two independent blocks followed by Cut merge.

## Two-block calculation

Use

\[
Q=\frac{Q_1+Q_2}{\sqrt2},
\qquad
P=\frac{P_1+P_2}{\sqrt2}.
\]

Collective cubic evolution gives

\[
P\longmapsto
P-\frac t2(Q_1^2+2Q_1Q_2+Q_2^2).
\]

Evolving each block for the cardinality-rescaled time

\[
\tau=\frac{t}{\sqrt2}
\]

and then merging gives

\[
P\longmapsto
P-\frac t2(Q_1^2+Q_2^2).
\]

Therefore

\[
\boxed{
\Theta_P=-tQ_1Q_2.
}
\]

For independent centered Gaussian blocks with variances `a_1,a_2`,

\[
\langle\Theta_P\rangle=0,
\qquad
\langle\Theta_P^2\rangle=t^2a_1a_2.
\]

## Narrow result

\[
\boxed{
\text{the cubic Cut defect is an existing labelled mixed-occurrence coefficient, first visible at second moment order.}
}
\]

This is the concrete Gaussian internal-pushforward realization of Entry 1667's
abstract binary cocycle.  Entry 1677's complete joint-cumulant tensor already
contains the `Q_1Q_2` slot.  No ternary coherence cell or new carrier stratum
is required.

The result does not show that the defect is removable.  It shows that deleting
mixed occurrence coefficients would erase genuine collective dynamics.

## Durable artifacts

- `research/benincasa/checkers/cubic_cut_cross_shear.rs`
- `research/benincasa/results/cubic-cut-cross-shear.json`
- `research/benincasa/cubic-cut-cross-shear.md`

## Next falsifier

Generalize the cross shear to unequal occurrence blocks.  Determine whether
all pairwise terms assemble by the existing complete labelled joint-cumulant
functor under three-block reassociation, and verify the Entry 1667 cocycle on
the exact density-state orbit rather than only at the operator level.
