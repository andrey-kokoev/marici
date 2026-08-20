---
title: "Every Supported Four-Site Node Has a Mixed-Tate Marked Arrangement"
date: 2026-08-20
entry: 1180
status: active
sector: cosmology
---

# 1180 — Every Supported Four-Site Node Has a Mixed-Tate Marked Arrangement

Sequence claim: `seqclaim-a63e6d0bca9122f224c4c518`.

## Local arrangement audit

Entry 1178 gives 196 supported node occurrences across the 28 source OFPT
terms. For each occurrence, retain every labelled vanishing denominator and
linearize it in the projective chart \(y_1=1\) at the corresponding sign
node.

Repeated occurrence labels are retained, while equal geometric normals are
identified only for the local arrangement matroid. The exact census has
eight signatures:

\[
\begin{array}{c|c|c|c|c}
\text{label depth}&\text{distinct planes}&\text{rank}&b_{\rm OS}&\text{count}\\
\hline
2&2&2&(1,2,1)&32\\
3&2&2&(1,2,1)&32\\
3&3&3&(1,3,3,1)&32\\
4&2&2&(1,2,1)&8\\
4&3&3&(1,3,3,1)&64\\
4&4&3&(1,4,6,3)&4\\
5&4&3&(1,4,6,3)&16\\
6&4&3&(1,4,6,3)&8.
\end{array}
\]

Here \(b_{\rm OS}\) is computed from the exact intersection lattice and its
Möbius function.

## Hodge classification

Every local object is the complement of a rational central hyperplane
arrangement of rank at most three. Hence its Orlik--Solomon cohomology is
mixed Tate. The higher incidence depths alter multiplicities and extension
maps, but they introduce no elliptic or higher Hodge carrier at the nodes.

Thus the only possible remainder after Entry 1179 is

\[
\boxed{
\text{Tate/Kummer Čech extension data on the existing marked carrier}.
}
\]

No new carrier stratum and no new non-Tate coefficient type appears locally.

## Scope

This is a local matroid and Hodge-type result. It does not prove that the
global occurrence-resolved Čech differential is exact: repeated labels,
residue orientations, and the total-parity relation can still produce an
extension class among Tate pieces.

## Next falsifier

Construct the signed occurrence-resolved Čech differential for one term in
each of Entry 1178's four depth profiles. Map its degree-zero node packet to
Entry 1179's global total-parity quotient. Test the resulting cone. A
nonzero class is necessarily a Tate/Kummer coefficient extension; zero
homology closes the four-site node branch completely at the algebraic level.

## Evidence

- `research/benincasa/checkers/four_site_qg_node_local_arrangements.py`
- `research/benincasa/results/four-site-qg-node-local-arrangements.json`
- Entries 1178--1179.
