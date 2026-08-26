# Detector annihilation of the portal lift kernel

Work package: WP588  
Owner: marici.Figueiredo

## Problem

WP587 gives a rank-two source-derived projection from portal settings into
\((\kappa_t^2,\kappa_4)\), but its lift into a complete generator packet is
not unique. This packet determines exactly when that nonuniqueness is harmless
for a detector.

Let \(P\) project the full generator packet onto the known coupling pair, and
let \(D\) be a calibrated detector-response map on the full packet.

## Descent theorem

The detector response is independent of every choice of lift precisely when

\[
Dv=0
\qquad (v\in\ker P).
\]

Equivalently, there is a map \(K\) such that

\[
D=KP.
\]

This is both necessary and sufficient. Sufficiency follows because two lifts
differ by a map into \(\ker P\). Necessity follows by comparing a lift with
that lift plus each kernel direction.

For one omitted coordinate, write

\[
P=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix},
\qquad
D=\begin{pmatrix}u&v&w\end{pmatrix}.
\]

Then \(D\) annihilates the lift kernel exactly when \(w=0\). Its response on
the WP587 lift is

\[
DL_{a,b}=\begin{pmatrix}-u+aw&v+bw\end{pmatrix}.
\]

Thus every dependence on the unknown completion is carried by the detector's
omitted-coordinate coefficient \(w\).

## Minimal rank-two detector

The inclusive-Higgs row

\[
D_r=\begin{pmatrix}1&0&0\end{pmatrix}
\]

annihilates the lift kernel but has source rank one. A calibrated quartic row

\[
D_q=\begin{pmatrix}0&1&0\end{pmatrix}
\]

would also annihilate it. Stacking these rows gives the exact source response

\[
\begin{pmatrix}D_r\\D_q\end{pmatrix}L
=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
\]

which has rank two independently of the unknown lift.

By contrast, the row \((0,1,1)\) is quartic-sensitive but does not descend:
its response depends on the omitted tangent coefficient and may cancel.

## Physical gate

WP588 is a conditional detector-descent and rank theorem, not a new
instrument. A publication-bound quartic-sensitive completed record must
establish one of two facts:

1. its calibrated response factors through the admitted coupling pair; or
2. every detector-sensitive coordinate outside that pair has a source-derived
   portal tangent.

The present HHH releases establish neither condition on the nonzero-mixing
portal domain. No selector, rigidifier, or reference port is introduced.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp588_detector_lift_kernel_annihilation.py

The generated result is
research/flavor/results/wp588_detector_lift_kernel_annihilation.json.
