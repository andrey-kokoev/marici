---
title: "The Six First-Rees Germs Sew as a Source-Exact Cousin Vector"
date: 2026-08-20
entry: 1137
status: established-global-filtered
sector: cosmology
---

# 1137 — The Six First-Rees Germs Sew as a Source-Exact Cousin Vector

Sequence claim: `seqclaim-07cd890d9f05cb406e9cf5de`.

## Correct global object

The three rank-twelve residue surfaces are not an open cover, so Entry
1136's coherent germs cannot be Čech-glued. The frozen global object is the
six-occurrence Cousin packet of Entry 364.

In source occurrence order

\[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23),
\]

the source coefficients and residue orientations are all \(+1\). Entry
1134's normalized local pairing therefore gives the degree-one vector

\[
\boxed{
c_{e_6}^{(1)}=\frac14(1,1,1,1,1,1).
}
\]

All pairwise marked-Cut residues vanish, so

\[
d_1c_{e_6}^{(1)}=0.
\]

## Exactness

Entry 364 establishes

\[
d_0\Omega_{\rm src}=(1,1,1,1,1,1).
\]

Over the rational source coefficient system,

\[
\boxed{
c_{e_6}^{(1)}=d_0\left(\frac14\Omega_{\rm src}\right).
}
\]

Thus the six local germs genuinely assemble, but their assembled vector is
exact in the full source-defined Cousin complex.

If degree zero is truncated away, the same vector survives as a nonzero
first-Rees associated support grade. Consequently

\[
\boxed{
\text{nonzero physical filtered residue}
\not\Rightarrow
\text{new global cohomology class}.
}
\]

Occurrence forgetting gives

\[
\left(\frac12,\frac12,\frac12\right),
\]

the expected factor-two identification of the two lower-denominator
occurrences in each marked-Cut sector.

## Classification

- local physical pairing: nonzero, first higher-Rees grade;
- cyclic and reflection transport: coherent;
- global source packet: exact filtered residue;
- new rational global cohomology: none;
- new carrier datum: none.

This is a strong H2 outcome: existing carrier and Cousin/Gysin calculus,
with a sector-specific filtered coefficient class that disappears after the
full source differential is restored.

## Next falsifier

The rational global question is closed. The remaining nonredundant issue is
integral: \((1/4)\Omega_{\rm src}\) need not belong to the source integral
lattice. Compute the saturation of the six-vector relative to the primitive
degree-zero source generator. A surviving finite cokernel would be integral
coefficient torsion, not a new carrier class.

Evidence:

- `research/benincasa/checkers/rank12_e6_global_cousin_sewing.py`;
- `research/benincasa/results/rank12-e6-global-cousin-sewing.json`;
- Entries 353, 356, 364, and 1133--1136.
