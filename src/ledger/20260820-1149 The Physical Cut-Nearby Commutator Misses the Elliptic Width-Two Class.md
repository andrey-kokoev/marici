---
title: "The Physical Cut-Nearby Commutator Misses the Elliptic Width-Two Class"
date: 2026-08-20
entry: 1149
status: established-cross-comparison
sector: cosmology
---

# 1149 — The Physical Cut-Nearby Commutator Misses the Elliptic Width-Two Class

Sequence claim: `seqclaim-37c6b2c9973c5c42bef61c4c`.

## Hard-to-vary claim

The source-normalized physical Cut--nearby commutator of Entry 226 might
activate the integral width-two elliptic coinvariant found in Entry 1147.
The finite test is the typed composite

\[
\mathcal C_{\rm phys}
\longrightarrow \mathcal M_q^{(9)}
\xrightarrow{R_\infty}\mathbb V_{\rm ell}(-1)
\longrightarrow\operatorname{coker}(T-I).
\]

No comparison map or lattice normalization is added.

## Frozen physical commutator

Entry 226 computes, in the equation-(58) master order,

\[
[\psi_{E_T=0},\operatorname{Res}_{q_{\mathcal G_{12}}=0}]
=
\left(
0,0,-\frac{2\pi^2}{x},0,-\frac{2\pi^2}{y},
-\frac{2\pi^2}{xy},0,0,0
\right).
\]

On the nonsoft open set (xy(x+y)\ne0), clearing its common nonzero scalar
gives the source ratio

\[
e_3:e_5:e_6=y:x:1.
\]

The physical class is therefore nonzero and supported termwise on

\[
\langle e_3,e_5,e_6\rangle.
\]

## Infinity-Gysin image

Entry 150 proves that the source blocks containing (e_3) and (e_5) map
identically to zero under (R_\infty). It also proves separately, from the
absence of a logarithmic pole at infinity, that

\[
R_\infty(e_6)=0.
\]

Hence the vanishing is termwise rather than a rational cancellation:

\[
\boxed{
R_\infty
\bigl([
\psi_{E_T=0},\operatorname{Res}_{q_{\mathcal G_{12}}=0}]
\bigr)=0.}
\]

This integral zero remains zero after nearby cycles and after passage to the
width-two coinvariant

\[
\operatorname{coker}(T-I)
\simeq \mathbb Z\oplus\mathbb Z/2.
\]

In particular, the physical comparison has zero image in its
(\mathbb Z/2) summand.

## Verdict

The conjectured activation is falsified:

\[
\boxed{
\text{the physical Cut--nearby commutator is nonzero, but it does not
activate the elliptic width-two class}.}
\]

The two structures coexist in different coefficient layers:

- the physical commutator is a third-Rees algebraic Tate/Kummer class in the
  rank-seven kernel of (R_\infty);
- the (mathbb Z/2) class is the integral shadow of the elliptic
  total-energy cusp;
- their source-defined comparison is zero before taking coinvariants.

Therefore neither the transverse base corner nor the physical relative
commutator supplies a carrier explanation for the elliptic torsion. No new
carrier datum is indicated.

## Classification

- existing carrier: total-energy and marked-Cut divisors with their frozen
  weighted comparison;
- algebraic coefficient support: the entire nonzero physical commutator;
- Legendre/Gauss--Manin coefficient data: the width-two coinvariant;
- map between them in this comparison: zero;
- genuinely new carrier datum: none.

## Next falsifier

Compute the integral saturation of the algebraic commutator inside the
rank-seven kernel before cyclic assembly. The normalized vector
((y,x,1)) is visibly primitive in the displayed three-master lattice; the
remaining question is whether cyclic occurrence sewing introduces any
integral index or extension that is invisible over the rational connection.

Evidence:

- `research/benincasa/checkers/cut_nearby_elliptic_z2_exclusion.py`;
- `research/benincasa/results/cut-nearby-elliptic-z2-exclusion.json`;
- Entries 150, 226, 317, 318, 1147, and 1148.
