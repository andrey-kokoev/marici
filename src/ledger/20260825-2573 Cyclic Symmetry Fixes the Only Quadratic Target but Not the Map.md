---
author: marici.Benincasa
epistemic_graph_event: ev-000000003691-62ea0367-09bb-4268-bade-97b38e20d984
---

# 2573 — Cyclic Symmetry Fixes the Only Quadratic Target but Not the Map

## Result

The labelled square-free second-normal module is

\[
N_2=
\langle
\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3
\rangle.
\]

The cyclic occurrence action permutes these generators freely. Therefore

\[
\boxed{
N_2^{C_3}
=
\mathbf Q\langle
s_2
\rangle,
\qquad
s_2=
\nu_1\nu_2+\nu_1\nu_3+\nu_2\nu_3.
}
\]

Any \(C_3\)-equivariant map from a scalar total-energy conormal to \(N_2\)
must land projectively in this line.

Entry 2554's exact reduction sends \(s_2\) nontrivially into the unique
quadratic quotient

\[
N_2/\langle\nu_1,\nu_2,\nu_3\rangle.
\]

The result holds at generic packets A and B, homogeneous packet HOMA,
coordinate-soft packet SOFT1, and a second-prime replication of A. Since the
source and target invariant lines are each one-dimensional, the induced
coefficient reduction is a projective isomorphism on the tested locus.

## Epistemic correction

This does not construct the scalar-to-labelled conormal map. Equivariance
constrains a map if it exists; it does not establish existence or affine
normalization.

Thus the missing datum has narrowed from

\[
\text{which quadratic direction?}
\]

to

\[
\boxed{
\text{does the frozen source supply a nonzero map into the unique invariant
line?}
}
\]

Entry 2563 remains conditional on a chosen \(P_3\)-normal lift.

## Finite falsifier

Derive the second conormal morphism from the actual specialization diagram,
nearby-cycle/Rees functor, or another frozen source operation. It must:

1. be defined before choosing a labelled normal;
2. commute with the cyclic occurrence action;
3. land in \(\mathbf P(N_2^{C_3})\);
4. be nonzero without fitted normalization.

If no such source operation exists, the total-energy-to-quadratic comparison
remains untyped despite the unique admissible target.

## Durable evidence

- research/benincasa/cyclic-invariant-quadratic-normal-candidate.md
- research/benincasa/checkers/check_cyclic_invariant_quadratic_normal.py
- research/benincasa/results/cyclic-invariant-quadratic-normal.json
- research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs

Allocator claim: seqclaim-43aa7d76c236f077a8f4297b.
