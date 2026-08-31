# Soft-channel reweighting rank gate: WP1075

## Question

What reweighting structure is required to map the six soft branch weights to
WP1052's six event-role weights?

## Source and target distributions

The localized branch dimensions give the normalized source distribution

\[
q=\frac1{23}(6,8,1,4,2,2).
\]

WP1052's six event atoms each have weight \(1/4\), so the target role vector is

\[
r=\left(\frac14,\frac14,\frac14,\frac14,\frac14,\frac14\right).
\]

The totals differ:

\[
\sum_i q_i=1,
\qquad
\sum_j r_j=\frac32.
\]

## Failed maps

Dimension-weighted identity propagation gives \(q\), not \(r\).

No permutation can map \(q\) to \(r\), because their entries differ.

A common-gain diagonal map would require branch-dependent gains

\[
\left(
\frac{23}{24},
\frac{23}{32},
\frac{23}{4},
\frac{23}{16},
\frac{23}{8},
\frac{23}{8}
\right),
\]

so no diagonal common-gain law exists.

## Minimal rank-one solution

Complete uniform mixing

\[
U=\frac16J_6
\]

maps every normalized source distribution to

\[
Uq=\left(\frac16,\frac16,\frac16,\frac16,\frac16,\frac16\right).
\]

A common gain

\[
g=\frac32
\]

then gives

\[
gUq=r.
\]

This is a rank-one solution, but it is only a target-compatible constructor.
The same \(U\) maps even a hostile source concentrated on one branch to the
same uniform event weights. Therefore \(U\) cannot be inferred from WP1052's
rows alone; it must be derived from production/decay dynamics.

## Boundary

The next source must derive the coupling matrix, its mixing rank, and the
gain \(3/2\), or derive a different source-authorized nonuniform map.

## Classification

Soft-channel reweighting rank gate. It gives C1 an exact matrix law and
hostiles rather than an unspecified coupling map.

Checker: `research/flavor/checkers/wp1075_soft_channel_reweighting_rank_gate.py`

Result: `results/wp1075_soft_channel_reweighting_rank_gate.json`
