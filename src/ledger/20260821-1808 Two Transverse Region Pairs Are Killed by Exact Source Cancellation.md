# 1808 — Two Transverse Region Pairs Are Killed by Exact Source Cancellation

## Question

Do all source-supported transverse pairs of five-site region walls activate a
two-wall coefficient object?

## Census

Entry 1804 leaves 34 transverse pairs among the nine supported region walls.
On one physical sheet their source co-occurrence census is:

\[
10\ \text{source-absent pairs},
\qquad
24\ \text{source-supported pairs}.
\]

A direct double-residue discovery census isolates all 24 supported pairs away
from deeper marked incidences. Twenty-two are numerically nonzero. Two vanish
on both physical sheets:

\[
(g_{15},g_{34}),
\qquad
(g_{23},g_{45}).
\]

## Exact cancellation identities

For the first pair, the two source terms differ only by the remaining walls
\(g_{1345}\) and \(g_{234}\). Their coefficient vectors obey

\[
\boxed{
g_{1345}+g_{234}=G^-_{e_{12}}+g_{34}.
}
\]

Hence on

\[
G^-_{e_{12}}=g_{34}=0
\]

the two remaining denominators are negatives, and their residues cancel.

Likewise, the second pair has remaining walls \(g_{145}\) and \(g_{2345}\),
with

\[
\boxed{
g_{145}+g_{2345}=G^-_{e_{12}}+g_{45}.
}
\]

Thus its two source terms cancel on

\[
G^-_{e_{12}}=g_{45}=0.
\]

These are exact identities of the frozen labelled linear forms. No numerical
fitting or coefficient normalization enters.

## Narrow result

Base transversality and source co-occurrence do not suffice to activate a
two-wall coefficient object. The source incidence algebra supplies an
additional cancellation differential that kills two transverse pair types.

Therefore the current partition of the 34 transverse pairs is

\[
\boxed{
10\ \text{source absent}
\;|\;
2\ \text{exactly cancelled}
\;|\;
22\ \text{candidate active}.
}
\]

The nonvanishing of the final 22 remains discovery-level until exact
certification. No tensor-product coefficient object is assigned to them yet.

## Next falsifier

Certify the remaining 22 double-residue coefficients exactly. Then classify
their cyclic orbits and test whether each local normal-crossing integral is a
plain tensor product of rank-one Kummer lines or carries a source-derived
extension.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_source_census.py
- research/benincasa/results/five-site-g5-transverse-pair-source-census.json
- research/benincasa/checkers/five_site_g5_transverse_pair_exact_cancellations.py
- research/benincasa/results/five-site-g5-transverse-pair-exact-cancellations.json
- allocator claim: seqclaim-d26f37622a9b5256f2eca35a
