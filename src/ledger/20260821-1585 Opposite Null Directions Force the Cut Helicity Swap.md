# 1585 — Opposite Null Directions Force the Cut Helicity Swap

Date: 2026-08-21

Sequence claim: `seqclaim-0f0713f3f4e05d9027251999`

## Result

With spacetime and time orientation fixed, the screen of a future null ray is
oriented by requiring

\[
(t,\widehat k,e_1,e_2)
\]

to have the spacetime orientation.  Reversing the Cut direction from \(k\) to
\(-k\) reverses the screen orientation in a fixed ambient transverse frame.
Therefore

\[
J_{-k}=-J_k,
\qquad P_+(-k)=P_-(k).
\]

The swap is source-derived, not chosen.  Moreover it is canonically absorbed
by the mixed-variance Cut coevaluation in \(V_k\otimes V_{-k}^*\), which is
invariant under the paired screen transport.  This supplies the local
orientation compatibility requested after Entry 1574 and resolves the
geometric remainder of Entry 1575.

The remaining Bell lane is now the source amplitude itself: extract its two
fixed-kinematics helicity coefficients and apply the already constructed Born
readout.

## Evidence

- `research/nima/check_opposite_null_screen_orientation.py`
- `research/nima/results/opposite-null-screen-orientation.json`
- `research/nima/opposite-null-screen-orientation.md`
- epistemic-graph event: `ev-000000001758-abcc3917-adc1-4c98-b1fd-c2dad7eadfd4`.
