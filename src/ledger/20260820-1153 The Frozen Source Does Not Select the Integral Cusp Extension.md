---
title: "The Frozen Source Does Not Select the Integral Cusp Extension"
date: 2026-08-20
entry: 1153
status: source-provenance-gate
sector: cosmology
---

# 1153 — The Frozen Source Does Not Select the Integral Cusp Extension

Sequence claim: `seqclaim-6c2cb55bdc7af58de89bd36b`.

## Question

Entry 1152 reduces the full integral total-energy ambiguity to

\[
(a,b)\in
\operatorname{Ext}^1_{\mathbb Z}
(\mathbb Z/2,\mathbb Z\langle e_6,v_{\rm alg}\rangle)
\simeq(\mathbb Z/2)^2.
\]

Does the frozen primary construction select one of these four classes?

## Primary one-loop paper

The primary source, Benincasa--Brunello--Mandal--Mastrolia--Vazao,
arXiv:2408.16386, supplies:

- the loop contour through non-negativity of the Cayley--Menger/simplex
  volumes, in equations (6)--(8) and their discussion;
- the nine (q_{\mathcal G_{12}})-sector de Rham masters in equation (58);
- the elliptic Picard--Fuchs operator and its total-energy degeneration in
  equations (59)--(62).

It does not provide an integral Betti basis for the rank-nine local system.
More strongly, its differential-equation discussion states that the boundary
conditions must be supplied independently; the connection does not fix them.

Thus neither the equation-(58) basis nor the Picard--Fuchs factorization
selects an integral lift (m) of the elliptic coinvariant.

## Cited contour constructions

The two directly relevant cited constructions were also audited:

- arXiv:2401.05207 constructs weighted cosmological-polytope contour and
  residue geometry;
- arXiv:2402.06558 constructs loop-measure positivity and asymptotic sector
  geometry.

They determine physical integration domains, orientations, residues, and
asymptotic sectors. They do not construct the integral Betti/Gysin lattice
of the three-site elliptic degree-two del Pezzo complement, a
Picard--Lefschetz basis for it, or the parity of an elliptic lift along
((e_6,v_{\rm alg})).

## Exact missing datum

To select Entry 1152's class one needs all three of:

1. a source-normalized integral elliptic cycle at the total-energy cusp;
2. an integral lift of that cycle through
   (R_\infty:H^2(S\setminus D_\infty)\to H^1(D_\infty)(-1));
3. the parity of
   
   \[
   2m=a e_6+b v_{\rm alg}pmod{2\mathcal A_{--}}.
   \]

None is present in the frozen sources.

## Verdict

\[
\boxed{
\text{the frozen source does not select any of the four integral cusp
extension classes}.}
\]

Accordingly:

- the elliptic quotient's width-two (mathbb Z/2) remains established;
- a visible (mathbb Z/2) in the full rank-nine coinvariants remains open;
- the three nonsplit, torsion-absorbing classes remain equally admissible;
- no carrier defect or new carrier stratum is indicated.

This is an epistemic stop for the present source route, not a physical
vanishing theorem.

## Required upstream construction

The branch can resume only with an integral Picard--Lefschetz/Gysin
comparison for the anticanonical complement of the degree-two del Pezzo
family, normalized against the physical Cayley--Menger contour. A rational
de Rham basis change, fitted period normalization, or chosen splitting is
insufficient.

## Redirect

The next cosmology attack should move to a source-defined comparison whose
integral or relative-chain normalization already exists. The present
two-bit cusp class should remain frozen until the required Betti packet is
constructed independently.

Evidence:

- `research/benincasa/checkers/integral_cusp_source_provenance_gate.py`;
- `research/benincasa/results/integral-cusp-source-provenance-gate.json`;
- arXiv:2408.16386, especially equations (6)--(8), (28)--(29), and
  (58)--(62);
- arXiv:2401.05207;
- arXiv:2402.06558;
- Entries 150, 289, 1151, and 1152.
