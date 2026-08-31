# Unit-clock flux-sector degeneracy gate: WP1072

## Question

Does the unit common-clock condition select a flux sector?

## Unit orbit

WP790 gives

\[
R_*^2=\frac{3An^2}{2B},
\qquad
\Delta_*=\frac{\sigma n}{R_*}.
\]

WP1061's unit common-clock condition is

\[
\frac BA=6n^2.
\]

On this entire orbit,

\[
R_*^2=\frac14,
\qquad
R_*=\frac12,
\qquad
M^2=\frac{1}{4R_*^2}=1.
\]

The WP1062 same-frame vector ratios remain

\[
\frac{p_1^2}{M^2}=4,
\qquad
\frac{p_2^2}{M^2}=16.
\]

## Exact sector degeneracy

The signed flux threshold is

\[
\Delta_*=\frac{\sigma n}{R_*}=2\sigma n.
\]

Thus the sectors

\[
(n,B/A)=(1,6),(2,24),(3,54)
\]

have identical radius, pole clock, and vector-KK ratios, but distinct signed
thresholds

\[
\Delta_*=2,4,6
\]

for \(\sigma=+1\). The mirror \((n,\sigma)=(1,-1)\) has the same clock data and
\(\Delta_*=-2\).

Off the unit orbit, for example \(B/A=12\) at \(n=1\),

\[
R_*^2=\frac18,
\qquad
M^2=2,
\]

so it is excluded by the common-clock condition.

## Boundary

Radius stabilization and the common clock therefore do not select \(n\) or
\(\sigma\). The remaining source law must prepare a flux sector and
orientation, or supply a calibrated flux-sensitive instrument together with a
source-authorized preparation.

No identification of \(n\) with an anomaly coefficient or family number is
made.

## Classification

Unit-clock flux-sector degeneracy gate. The scale blocker is narrowed from an
unfixed ratio to an exact invisible-sector orbit plus a signed flux readout.

Checker: `research/flavor/checkers/wp1072_unit_clock_flux_sector_degeneracy_gate.py`

Result: `results/wp1072_unit_clock_flux_sector_degeneracy_gate.json`
