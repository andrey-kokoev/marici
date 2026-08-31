# Symmetric-production-law cofiber: WP1076

## Question

Do the admitted \(SU(6)\) symmetries derive the production mixing required by
WP1075?

## Candidate laws

The localized branch distribution is

\[
q=\frac1{23}(6,8,1,4,2,2).
\]

WP1075's event target is six weights \(1/4\).

### Parent-blind propagation

A common production amplitude per parent component preserves the
dimension-weighted distribution \(q\). This does not match the event target.

### Localized doublet exchange

After one-quartet localization, the parent-sector weights are

\[
\frac1{23}(15,6,2),
\]

not three equal weights. Full \(\overline6\)-parent exchange is broken by the
localization choice. Exchanging only the two bulk doublets leaves \(q\)
unchanged because they already have equal weights, so it also fails.

### Branch democracy

Equal weight per localized branch gives

\[
\left(\frac16,\frac16,\frac16,\frac16,\frac16,\frac16\right),
\]

and gain \(3/2\) then gives the WP1075 target. But the six branches are not
one symmetry orbit: their dimensions and
\(SU(4)\times SU(2)\times U(1)\) quantum numbers differ. The current
artifacts provide no all-branch permutation symmetry, no common production
kernel, and no source-derived gain \(3/2\).

## Boundary

This cofiber does not rule out a future nonsymmetric production kernel. It
shows that the currently admitted parent symmetry, localized exchange
symmetry, and common clock do not derive the required coupling matrix.

## Classification

Symmetric-production cofiber. C1 is blocked for current artifacts: the
coupling matrix requires source dynamics beyond the verified group and clock
data.

Checker: `research/flavor/checkers/wp1076_symmetric_production_law_cofiber.py`

Result: `results/wp1076_symmetric_production_law_cofiber.json`
