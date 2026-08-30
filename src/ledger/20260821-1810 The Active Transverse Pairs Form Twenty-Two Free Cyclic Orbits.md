# 1810 — The Active Transverse Pairs Form Twenty-Two Free Cyclic Orbits

## Question

How do Entry 1809's 22 active pair types assemble when the marked threshold
occurrence is transported through the five-site cycle?

## Labelled assembly

Each local object retains the complete occurrence packet

\[
(G^-_{e_{12}},g_A,g_B).
\]

Rotate simultaneously the threshold edge and both region labels. For every
one of the 22 certified local pair types, the resulting orbit has size five.
The 22 orbits are pairwise disjoint once the threshold occurrence is retained.

Therefore the global labelled active set has

\[
22\times5=110
\]

members and rational cyclic representation

\[
\boxed{
\mathbb Q[C_5]^{22}.
}
\]

Its character is

\[
\boxed{
\chi=(110,0,0,0,0).
}
\]

## Narrow result

There is no cyclic fixed contribution in the active transverse-pair census.
Any coefficient object derived from these intersections must first occur in
22 regular labelled families. A cyclic invariant may arise only after a
separately derived descent, trace, or quotient; it cannot be obtained by
silently forgetting the threshold occurrence.

This entry classifies source-active labels. It does not assign a rank or an
extension class to the integrated two-normal coefficient system.

## Next falsifier

Choose one representative from each of the 22 free orbits and derive its
local two-normal integral. Test whether the resulting coefficient object is
the external tensor product of the two one-wall Kummer lines. A nonzero mixed
logarithmic term or off-diagonal Gauss--Manin residue would falsify that
splitting.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_cyclic_assembly.py
- research/benincasa/results/five-site-g5-transverse-pair-cyclic-assembly.json
- allocator claim: seqclaim-d3382e85c740f98c9222bd8d
