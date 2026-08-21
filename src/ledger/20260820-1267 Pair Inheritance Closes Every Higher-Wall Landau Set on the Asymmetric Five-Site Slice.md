---
title: "Pair Inheritance Closes Every Higher-Wall Landau Set on the Asymmetric Five-Site Slice"
date: 2026-08-20
entry: 1267
status: active-finite-closure
author: marici.Benincasa
---

# 1267 — Pair Inheritance Closes Every Higher-Wall Landau Set on the Asymmetric Five-Site Slice

Sequence claim: `seqclaim-2109e2212300a67cc1b97900`.

## Labelled triple census

Regenerate every three-wall subset occurring in at least one of the 180
source OFPT terms. No cyclic quotient is taken. There are

\[
\boxed{1210}
\]

distinct labelled compatible triples.

Classify each triple solely through its three pair subobjects using Entries
1261, 1262, and 1266. The exact result is

\[
\begin{array}{c|r}
\text{inherited class}&\text{triple count}\\ \hline
\text{contains an empty pair locus}&1140\\
\text{contains a pair on existing total support}&70\\
\text{requires fresh three-wall elimination}&0
\end{array}
\]

Thus no triple can generate a new simultaneous Landau component.

## Higher active sets

Every compatible active set of cardinality at least three contains a
compatible triple. Each such triple is either empty because one pair has unit
resultant, or is restricted to the existing total-energy/soft support.

Consequently every higher active set inherits the same alternative:

\[
\boxed{
\text{empty stationary locus}
\quad\text{or}\quad
\text{existing one-wall/total/soft support}.
}
\]

No separate four-wall or higher elimination is required.

## Corrected physical conclusion

For Entry 1257's valid momentum-conserving rank-three family, the complete
source-compatible Landau hierarchy introduces no support beyond the frozen
labelled carrier:

\[
\boxed{
\text{partial energy}
+
\text{total energy}
+
\text{soft incidence}.
}
\]

This conclusion concerns rational-integrand Landau support. It does not
determine the integrated period, its coefficient local system, or physical
relative-chain activation.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_triple_inheritance.rs`
- `research/benincasa/results/five-site-asymmetric-triple-inheritance.json`

## Next falsifier

With carrier support now closed, construct the actual asymmetric five-site
period packet: retain all 180 terms and 32 Kummer sheets, then seek the
smallest source-derived Gauss--Manin coefficient block. Any new singular
divisor must be classified as coefficient support rather than inferred from
Landau incidence.
