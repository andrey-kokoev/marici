---
title: "Higher Concurrence Cells Reduce the Four-Site Kummer Sector to Rank Eight"
date: 2026-08-20
entry: 1192
status: active-finite-model
sector: cosmology
---

# 1192 — Higher Concurrence Cells Reduce the Four-Site Kummer Sector to Rank Eight

Sequence claim: `seqclaim-f0c87d100b20f375b9084880`.

## Hard-to-vary claim

For the frozen 28-term four-site (q_{\mathcal G})-residue source packet,
the complete pair--triple--quadruple (H^0)-Čech complex has deck-odd
second cohomology of rank eight:

\[
\boxed{\dim H^2_- = 8.}
\]

Thus Entry 1190's rank-forty deck-odd pair-to-triple cokernel was not a
cohomology group. Fourfold concurrence boundaries kill 32 of those 40
directions. The surviving eight classes require no new carrier stratum.

## Missing cells exposed by the tetrahedra

Entry 1191 found alternating tetrahedral vectors in the left cokernel of
the pair-to-triple map. That shape is also the signed boundary of a
fourfold concurrence cell, so all source subsets of size at least four
were audited before retaining the interpretation.

Every term has genuine rank-three fourfold subsets:

\[
\begin{array}{c|c|c}
\text{geometric marks}&\text{fourfold cells}&\text{term count}\\
\hline
5&1&8\\
6&2&8\\
6&3&12.
\end{array}
\]

There are no nonempty source concurrences of size five or greater.

## Deck-resolved full differential

Let (C^1,C^2,C^3) be the (H^0) contributions of pair, triple, and
fourfold strata. The maps are the source-labelled signed simplicial
coboundaries. In the deck-even sector every nonempty stratum contributes
one generator. In the deck-odd sector:

- a split pair contributes its component difference;
- an off-branch triple or fourfold point contributes its deck difference;
- a ramification point contributes no odd generator.

Exact rational row reduction gives

\[
\begin{array}{c|c|c|c|c|c}
m&\#C^3&\#C^3_-&H^2_+&H^2_-&\text{terms}\\
\hline
5&1&0&3&0&8\\
6&2&1&8&1&8\\
6&3&2&7&0&12.
\end{array}
\]

Both compositions were checked termwise:

\[
d_2d_1=0
\]

in the even and odd complexes. Summing the source terms gives

\[
\boxed{(\dim H^2_+,\dim H^2_-)=(172,8).}
\]

## Interpretation

The fourfold cells are ordinary incidences of the already frozen marked
hyperplanes. Their correction therefore strengthens the carrier/coefficient
typing discipline: the apparent rank-forty Kummer packet was partly an
artifact of truncating the carrier incidence complex one degree too early.

The eight residual odd classes occur in exactly eight six-mark terms, one
per term. They are genuine cohomology of this finite (H^0)-Čech row, but
they are not yet physical periods or a global theorem. Their coefficient
type, cyclic assembly, higher-row differentials, and pairing with the
physical relative chain remain uncomputed.

The exact term indices split into the two source-derived free (C_4)
orbits

\[
\{2,9,12,22\},
\qquad
\{5,10,13,20\}.
\]

Hence the residual support has the rational occurrence character of two
regular modules,

\[
H^2_-\simeq \mathbf Q[C_4]^{\oplus2}
\]

as a labelled vector space. The serialized one-triple representatives are
quotient-basis choices; they are not asserted to transport literally
without pair-boundary corrections.

## Falsifier and next calculation

Freeze the two labelled (C_4)-orbit representatives and derive their
cyclic transport including pair-boundary corrections. Then test the next
available source residue/Gysin differential into or out of them. If it
kills them, the Kummer sector closes. If they survive, test physical-chain
activation without adding support cells.

## Artifacts

- `research/benincasa/checkers/four_site_qg_higher_concurrence_audit.py`
- `research/benincasa/results/four-site-qg-higher-concurrence-audit.json`
- `research/benincasa/checkers/four_site_qg_full_cech_h2.py`
- `research/benincasa/results/four-site-qg-full-cech-h2.json`

Entries 1189--1191 are superseded only where they identify the truncated
pair-to-triple cokernel with the final top-row object.
