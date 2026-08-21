# 1584 — The Global Time Root Does Not Determine Helicity Orientation

Date: 2026-08-21

Sequence claim: `seqclaim-1c3ad21033391a4b65ef537c`

## Result

Entry 126's global time-root \(\mathbb Z_2\) does not determine the orientation
of the transverse Ward plane required by Entry 1583.

An exact Lorentz-frame counterexample is

\[
P=\operatorname{diag}(1,-1,1,1),\qquad k=(1,0,0,1).
\]

It preserves the Lorentz metric, future time orientation, and the null ray
\([k]\).  Nevertheless it reverses spacetime orientation and one transverse
axis.  Consequently

\[
P_\perp J P_\perp^{-1}=-J,
\]

which swaps the two helicities.

The coefficient inventory therefore contains two separately typed binary
data:

1. the global time-root equalizer of Entry 126;
2. spacetime/transverse orientation generating the helicity lens.

Their underlying groups are both \(\mathbb Z_2\), but identifying them would be
an untyped quotient.  The fixed-kinematics Bell construction must retain both.

## Evidence

- `research/nima/check_time_root_vs_helicity_orientation.py`
- `research/nima/results/time-root-vs-helicity-orientation.json`
- `research/nima/time-root-vs-helicity-orientation.md`
- epistemic-graph event: `ev-000000001757-fd4d88de-9088-4844-9c0d-f48c250c128b`.
