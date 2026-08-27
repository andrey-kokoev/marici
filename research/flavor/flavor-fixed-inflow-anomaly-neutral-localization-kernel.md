# Fixed-inflow anomaly-neutral localization kernel: WP756

## Question

If a higher source independently fixes the five-dimensional Chern–Simons
inflow level, does local anomaly cancellation then select the localization
class needed for the positive WP753 spectral index?

## Claim boundary

The admitted domain is the WP737 product-group gauge/link lift plus the
vectorlike mediator pairs already required by WP738. The comparison freezes
the gauge representations, four-dimensional zero-mode packet, local anomaly
equations, and Chern–Simons level. Only the bulk-versus-boundary placement of
an anomaly-neutral vectorlike pair is changed.

The faithful comparison coordinate is the complete five-dimensional lift:
localization class, inflow level, and degree-weighted spectral index

\[
\kappa=2+N_V-N_H.
\]

## Exact kernel

For one anomaly channel, local cancellation reads

\[
A_0=b_0+\frac{B}{2}+k,
\qquad
A_\pi=b_\pi+\frac{B}{2}-k.
\]

Consider a vectorlike pair with anomaly coefficients \(+1\) and \(-1\).
Placed together on one boundary, its net boundary anomaly is zero. Realized
in the bulk by two orbifold hypermultiplets, its net bulk anomaly is also zero.
Both lifts therefore have

\[
(A_0,A_\pi)=(0,0),
\qquad k=0,
\]

but their bulk hypermultiplet counts differ by two. Fixing \(k\) cannot see
this relocation because it lies in the kernel of the anomaly map.

The flavor packet provides a larger witness. With gauge fields and the link
in the bulk while the WP738 vectorlike mediators remain on a boundary,

\[
\kappa=2+15-4=13.
\]

Moving only those anomaly-neutral mediator pairs into the bulk adds
\(36+12=48\) hypermultiplet degrees and gives

\[
\kappa=13-48=-35.
\]

The local anomaly vector and fixed inflow level are unchanged, yet the sign
of the Scherk–Schwarz selector reverses.

## Disposition

Even independently fixed anomaly inflow does not select localization along
the anomaly-neutral matter kernel. It is neither a selector nor a
presentation rigidifier on that kernel: the admitted anomaly probe identifies
two physically different five-dimensional lifts whose radiative endpoint
orderings disagree.

This closes anomaly cancellation as the missing hard-to-vary explanation.
The successor principle must couple to anomaly-neutral matter placement. A
specified interaction geometry, boundary condition derived from a UV
construction, or normalizability/locality theorem could do so, but its
localization prediction must be frozen before computing \(\kappa\).

The smallest exact falsifier is one vectorlike \((+1,-1)\) pair. The broader
portal objective remains open: a surviving source must additionally fix the
portal magnitude, RG basin, threshold survival, descent to `physical16`, and
a calibrated physical instrument.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp756_fixed_inflow_anomaly_neutral_localization_kernel.py

Generated result:
research/flavor/results/wp756_fixed_inflow_anomaly_neutral_localization_kernel.json
