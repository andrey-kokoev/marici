---
title: "The Literal Four-Cycle Physical Infinity Misses Every Forced Node"
date: 2026-08-20
entry: 1166
status: active
sector: cosmology
---

# 1166 — The Literal Four-Cycle Physical Infinity Misses Every Forced Node

Sequence claim: `seqclaim-c65bb1a7a2c0bba59acd4155`.

## Source-defined infinity direction

For a one-loop polygon, the Cayley--Menger variables are shifted loop
lengths

\[
y_i(\ell)=|\ell+K_i|,
\]

with fixed external shifts \(K_i\). Put \(\ell=R n\), \(|n|=1\). Then

\[
y_i(R,n)
=R+n\cdot K_i+O(R^{-1}).
\]

Consequently every radial end of the literal positive loop-momentum chain
has the same projective limit

\[
\boxed{[y_1:y_2:y_3:y_4]=[1:1:1:1].}
\]

This statement is independent of the OFPT partial-fraction term and of the
choice of angular direction \(n\).

## Comparison with the forced node support

Entries 1162--1165 place all 296 labelled forced incidences at five
projective points:

\[
[1:0:0:0],\ [0:1:0:0],\ [0:0:1:0],\ [0:0:0:1],
\quad [1:-1:1:-1].
\]

None is projectively proportional to \([1:1:1:1]\). Therefore

\[
\boxed{
\overline\Gamma_{C_4}^{\rm literal}\cap Z_{\rm forced}=\varnothing
\quad\text{at radial infinity}.
}
\]

The support-sensitive restriction of the literal physical chain to every
forced node costalk is zero.

## Typed conclusion

The mixed-Tate, deck-anti-invariant node classes of Entries 1164--1165 are
real algebraic coefficient classes, but the literal positive
Bunch--Davies/Cayley--Menger contour does not activate them at infinity.

This does not prove that every analytically continued physical chain has
zero pairing. Such a claim requires a source-derived continuation in the
relative-homology local system. The frozen positive contour alone does not
select that continuation, so the continued pairing is presently undefined,
not nonzero and not canonically zero.

No new carrier stratum is indicated.

## Consequence for H2

The four-cycle test has now separated all three layers:

\[
\begin{array}{c|c}
\text{carrier support} & \text{existing incidence and Gram-minor walls}\\
\text{coefficient object} & \text{mixed Tate plus quadratic deck character}\\
\text{literal physical readout} & 0
\end{array}
\]

This supports the shared-carrier/sector-specific-coefficient architecture,
while showing again that algebraic coefficient existence does not imply
physical activation.

## Next falsifier

The forced-node branch is closed under the literal source chain. A reopening
requires an independently defined analytic continuation whose transported
relative cycle reaches one of the five forced projective points. Without
that datum, move to a four-site marked stratum meeting the physical diagonal
infinity point \([1:1:1:1]\).

## Evidence

- `research/benincasa/checkers/audit_four_cycle_physical_infinity_support.py`
- `research/benincasa/results/four-cycle-physical-infinity-support.json`
- `research/benincasa/results/four-cycle-triple-points.json`
- Entries 783, 785, and 1159--1165.
