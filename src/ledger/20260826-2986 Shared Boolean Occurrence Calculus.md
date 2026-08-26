---
author: marici.Benincasa
date: 2026-08-26
---
# 2986 — Shared Boolean Occurrence Calculus

## Scope

This entry extracts an exact finite incidence-algebra pattern from three existing constructions. It does not assert that the pattern is physically accessible, that all sector operations commute, or that a support-sensitive derived enhancement already exists.

## Claim under test

Three independently derived constructions instantiate one finite labelled calculus:

1. occurrence-resolved Cut/Koszul complexes;
2. Boolean score tomography of deletion routes;
3. second-normal Gram cross-effects in cosmology.

The narrow conjecture is that these are realizations of a shared Boolean occurrence calculus. This is a candidate common calculus, not yet a universal Marici primitive.

## Frozen abstract data

Let (L) be a finite set of labelled occurrences and let (mathcal P(L)) be its Boolean subset category. A sector supplies a covariant or contravariant packet

\[
F:\mathcal P(L)\longrightarrow\mathcal C,
\]

where (mathcal C) is an additive or derived target category. The variance, support, coefficient object, and physical readout are sector data. They are not supplied by the Boolean calculus.

For a scalar packet (f:\mathcal P(L)\to R), define the upper zeta transform

\[
(Zf)(T)=\sum_{S\supseteq T}f(S)
\]

and Möbius inversion

\[
(\mu g)(S)=\sum_{T\supseteq S}(-1)^{|T|-|S|}g(T).
\]

For (T\subseteq L), define the labelled cross-effect at the empty vertex by

\[
\operatorname{cr}_T(F)
=
\sum_{U\subseteq T}(-1)^{|T|-|U|}F(U).
\]

Translations to another cube vertex use the same labelled finite-difference operators. An ordering of (L) supplies the ordinary cubical signs and hence the normalized cubical/Koszul complex.

## Finite structural statements

### Möbius faithfulness

On the complete labelled cube,

\[
\mu Z=Z\mu=1.
\]

Therefore the complete zeta tower reconstructs the labelled route packet exactly. This is algebraic faithfulness only. It does not prove that a physical instrument has access to every zeta coordinate.

### Degree filtration

If (F) is polynomial of Boolean degree at most (d), every cross-effect of order greater than (d) vanishes. The nonzero cross-effects provide its normalized interaction grades.

### Label equivariance

Every permutation of (L) acts functorially on vertices, zeta coordinates, cross-effects, and cubical signs. Occurrence labels may be transported; they may not be discarded without a separately derived descent map.

### Independent-interface realization

When each occurrence (e\in L) carries a two-term complex (K_e), the tensor product

\[
K_L=\bigotimes_{e\in L}K_e
\]

is the cubical/Koszul realization of the Boolean packet. Physical diagonal specialization is an augmentation after occurrence resolution, not a replacement for the resolved cube.

## Three existing realizations

### Resolved Cut and partial energy

For compatible cut interfaces,

\[
K_C^{\mathcal E}=\bigotimes_{e\in C}K_e^{\mathcal E}.
\]

The Boolean vertices record which labelled interface occurrences are selected. The cubical differential records their compatible additions with signs. Diagonal identification (y_{e,+}=y_{e,-}) is a later physical augmentation.

### Boolean score tomography

For labelled deletion routes (v_S), the complete mixed-score packet obeys

\[
M_T=\sum_{S\supseteq T}v_S.
\]

This is exactly the upper Boolean zeta transform. Möbius inversion recovers every (v_S). The theorem establishes joint formal faithfulness of the complete finite score tower, while leaving instrument authority and physical accessibility separate.

### Cosmological Gram normal module

Let

\[
a_i=X_i^2,
\qquad
\nu_i=P_i^2-X_i^2,
\]

and define

\[
G(S)=\lambda
\left(
a_1+\mathbf 1_{1\in S}\nu_1,
a_2+\mathbf 1_{2\in S}\nu_2,
a_3+\mathbf 1_{3\in S}\nu_3
\right).
\]

The labelled second cross-effects are

\[
\Delta_i\Delta_jG=-2\nu_i\nu_j,
\]

while

\[
\Delta_1\Delta_2\Delta_3G=0.
\]

Hence the previously identified second-normal module

\[
N_2=\langle\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle
\]

is exactly the degree-two Boolean cross-effect module of the energy-to-momentum Gram adapter. The rank-three module is labelled, not an unstructured three-dimensional coincidence.

## Type separation

The architecture has four separately typed parts: Carrier labels and admissible faces; the sector packet (F); Boolean transforms; and the physical readout.

The shared calculus supplies zeta aggregation, Möbius inversion, cross-effects, and cubical coherence. It does not supply:

- the sector coefficient object;
- a physical chain or instrument;
- access to the complete score tower;
- a descent that forgets occurrence labels;
- commutativity of sector operations.

## Prohibited inferences

Do not infer that:

- a formally faithful complete cube is physically observable;
- equal aggregate values identify labelled packets when only a projection is measured;
- a partial cube determines missing vertices;
- labels can be collapsed because their scalar formulas coincide;
- every pair of occurrence operations commutes strictly;
- Boolean organization alone determines sector ontology.

## First hostile falsifier

Take two independently source-derived occurrence operations (d_i,d_j) in a sector where order may matter. Compute the square

\[
d_id_jF
\quad\text{versus}\quad
d_jd_iF.
\]

Classify exactly one of the following:

1. strict commutation;
2. commutation through a source-derived canonical homotopy;
3. a typed defect supported on an already frozen stratum;
4. failure of the Boolean extraction because no admissible coherence exists.

No fitted homotopy or new support cell may be introduced after seeing the defect.

## Narrow result

The same labelled Boolean incidence algebra is now derived in three distinct contexts. In the cosmological Gram problem it explains both the rank and the labels of (N_2), and identifies the energy-to-momentum adapter as a cross-effect construction rather than an unspecified comparison map.

This supports extraction of a shared Boolean occurrence calculus as reusable Marici machinery. Promotion to core requires the noncommuting-face falsifier and at least one support-sensitive derived realization to pass without post hoc repair.

## Durable verification

- Ledger sequence claim: `seqclaim-8bc129430cf3916c0e1c70ba`.
- Commit introducing this entry: `fd2970b0`.
- Epistemic graph admission: `ev-000000005388-2f5520df-adbe-4aa3-9f27-ea6e570b4456`.
- No new checker was required: the entry compiles exact identities already established in the three cited source packets.
