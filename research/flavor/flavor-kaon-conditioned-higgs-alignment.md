# Kaon-conditioned Higgs alignment

## Cross-instrument question

WP474 asks whether the flavor-current scale forced by WP461 lies inside the
Higgs-rate-compatible coefficient cone derived in WP473. This is a conditional
composition: it inherits WP461's 5-TeV pole benchmark, provisional kaon
likelihood, and threshold envelope. It does not turn those assumptions into a
source law.

At `y=1`, the common-clock vacuum relation is

\[
{f\over v}=\sqrt{3\over a},
\qquad a=3\left({v\over f}\right)^2.
\]

Using `v=0.24622 GeV` and WP461's exact conditional lower bound on `f`, the
current instrument therefore supplies an upper bound on `a`.

## Exact alignment result

The checker imports WP461's exact algebraic bound rather than its rounded
decimal. The resulting `a` ceiling is of order `10^-9`, many orders below the
WP473 Higgs-rate ceiling

\[
a\leq{242\over2379}\simeq0.1017
\]

for `y=1`.

The dilation pole's Higgs residue is monotone in `a` and obeys

\[
Z_D^{(H)}={a\over a+2}.
\]

At the kaon-conditioned ceiling it is below `10^-9`. Consequently the
orthogonal Higgs residue budget `2/(a+2)` differs from unity only at that scale
and comfortably exceeds the frozen PDG rate lower edge `2379/2500`.

This repairs WP473's unit-geometry rate obstruction by moving to a physically
constrained hierarchical geometry, not by adding a fitted production
amplitude.

## What is and is not selected

The kaon instrument constrains `a`; it does not source-select it. WP461 also
froze the 5-TeV vector pole, so its value

\[
{g_Ff\over v}={2500\sqrt6\over123}\simeq49.79
\]

remains a benchmark readout, not a prediction. The common-clock source action
selects the relational formula, while the kaon and pole instruments restrict
or calibrate coordinates within that family.

## Next gate

The hierarchical `a` value changes the entire scalar Hessian relative to
WP468–WP471. A new spectrum must be computed with `eta` fixed by an independent
source mechanism or explicitly calibrated to the Higgs mass. The Higgs rate
must then remain withheld, and all scalar/vector widths must be recomputed in
the multi-PeV flavor-scale threshold domain.

Smallest falsifiers are failure of the exact `a` ceiling to lie below
`242/2379`, or a non-projector production effect invalidating the residue-only
rate map.
