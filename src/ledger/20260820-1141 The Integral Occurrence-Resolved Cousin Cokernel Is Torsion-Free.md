---
title: "The Integral Occurrence-Resolved Cousin Cokernel Is Torsion-Free"
date: 2026-08-20
entry: 1141
status: established-global-integral-comparison
sector: cosmology
---

# 1141 — The Integral Occurrence-Resolved Cousin Cokernel Is Torsion-Free

Sequence claim: `seqclaim-bc2dc6d328b0de58406ddd2b`.

## Physical integral Cousin map

Retain the six labelled occurrences of Entries 356 and 1137. In the
primitive local Betti bases of Entry 1140, the source incidence map is

\[
d_0^{\rm B}:\mathbb Z\longrightarrow\mathbb Z^6,
\qquad
1\longmapsto(1,1,1,1,1,1).
\]

The sole nonzero Smith invariant is \(1\). Therefore

\[
\boxed{\operatorname{coker}d_0^{\rm B}\simeq\mathbb Z^5,}
\]

with no integral torsion.

## Quarter-enlarged e6 lattice

Entry 1140 gives \(\eta_j=4\rho_j\) in every occurrence, where \(\eta_j\)
is the primitive Betti class and \(\rho_j\) is the source-normalized
first-Rees \(e_6\) generator. In the enlarged lattice

\[
L_\rho=\bigoplus_{j=1}^6\mathbb Z\rho_j,
\]

the same integral source boundary is represented by

\[
1\longmapsto(4,4,4,4,4,4).
\]

Its Smith invariant is \(4\), so

\[
\operatorname{coker}(d_0:L^0_{\rm B}\to L_\rho)
\simeq
\mathbb Z^5\oplus\mathbb Z/4.
\]

The order-four element is precisely Entry 1137's diagonal quarter-vector.
It is exact over \(\mathbb Q\), becoming the boundary of one quarter of the
primitive degree-zero source generator.

## Type verdict

The two cokernels answer different questions:

\[
\begin{array}{c|c}
\text{coefficient lattice}&\text{cokernel}\\
\hline
\text{physical integral Betti lattice}&\mathbb Z^5\\
\text{quarter-enlarged source-normalized }e_6\text{ lattice}
&\mathbb Z^5\oplus\mathbb Z/4
\end{array}
\]

Hence

\[
\boxed{
\text{the global }\mathbb Z/4\text{ is a de Rham/Betti lattice mismatch,}
\quad
\text{not physical integral hypercohomology torsion}.}
\]

Occurrence forgetting illustrates why labels matter: sending the primitive
six-vector to \((2,2,2)\) has Smith invariant \(2\) and manufactures a
\(\mathbb Z/2\) quotient. That quotient is an occurrence-identification
multiplicity, not torsion of the resolved physical complex.

## Consequence

The integral branch closes without a new carrier primitive. The physical
Betti complex is saturated and torsion-free; the source-normalized
first-Rees \(e_6\) coefficient object is a quarter-lattice enlargement.
This is sector-specific coefficient normalization inside the existing
occurrence-resolved Cousin calculus.

## Next falsifier

Return to the higher-Rees coefficient filtration and ask whether the
quarter-lattice extension is preserved by Gauss--Manin transport away from
the node. A failure of preservation would confine the index-four defect to
the special fiber; preservation would define a genuine rank-one Kummer or
Tate lattice local system. Do not infer either from the local Smith form.

Evidence:

- `research/benincasa/checkers/rank12_e6_integral_cousin_comparison.py`;
- `research/benincasa/results/rank12-e6-integral-cousin-comparison.json`;
- Entries 356, 1137, and 1139--1140.
