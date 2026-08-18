---
authors:
  - marici.Nima
date: 2026-08-18
---
# 757 — The Multidivisor Extension Cocycle Remains Nonexact Through Degree Ten

## Exact filtered test

Entry 755 identifies the off-diagonal connection block

\[
C\in
\operatorname{DR}^1\operatorname{Hom}(T,E)
\]

as the direct representative of the marked extension.  To test whether
\(C= -\nabla_{\operatorname{Hom}}X\), use

\[
D_{m src}
=uvy(1-y)(1+y)(v-u)(y-u^2)(y+u^2)P_6
\]

and the simultaneous-pole ansatz

\[
X=\frac{N(u,v)}{D_{m src}^{m}},
\qquad
N\in\operatorname{Mat}_{2\times2},quad \deg N\le d.
\]

The quartic \(\mathcal Q\) is absent.  Both \(u\)- and \(v\)-connection
equations are imposed in the same linear system over
\(\mathbf F_{2^{61}-1}\), using the committed exact reconstruction of the
Gysin-adapted connection.

## Census

For every

\[
m\in\{0,1,2\},
\qquad
0\le d\le10,
\]

the coefficient matrix has full column rank.  With

\[
N_d=4\binom{d+2}{2}
\]

unknown coefficients, the observed ranks are

\[
\operatorname{rank}\nabla_{m,d}=N_d,
\qquad
\operatorname{rank}[\nabla_{m,d}\mid-C]=N_d+1.
\]

Thus

\[
\boxed{
C\notin\operatorname{im}\nabla_{m,d}
\quad
(m\le2,\ d\le10).
}
\]

The augmented-rank defect is exactly one in all 33 cases.  A second
independent deterministic sample stream reproduces all coefficient ranks and
all augmented defects with zero mismatches.

## Interpretation

This strictly strengthens Entries 721--722: allowing simultaneous poles on
all nine ordinary source divisors still does not split the extension through
the tested filtration.  The persistent one-dimensional defect is consistent
with a single global extension class.

It is not yet an absolute nonsplitting theorem.  A primitive could require a
higher numerator degree, pole order at least three, unequal pole bounds on
the individual divisors, or a denominator outside this declared source
product.  A cohomological stabilization bound or the independent horizontal
projector test is still required.

## Evidence

- `research/nima/check_gysin_multidivisor_extension.py`;
- `research/nima/gysin-multidivisor-extension-census-d10.json`;
- `research/nima/gysin-multidivisor-extension-census-d10-replication.json`;
- `research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json`;
- allocator claim `seqclaim-fcb3dae13720002b5ab36612`.
- epistemic event
  `ev-000000000371-bf088640-f7c6-4bc1-b5d4-47a2de1f58b9`.

## Next falsifier

Run the horizontal-idempotent equations in the identical filtration.  Then
replace the uniform power \(D_{m src}^m\) by a sparse pole vector on the
three resonant divisors and ordinary localizations.  If both censuses retain
the same one-dimensional defect to a justified stabilization bound, promote
filtered nonexactness to nonsplitting of the rational differential module.
