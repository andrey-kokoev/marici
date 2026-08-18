---
authors:
  - marici.Nima
date: 2026-08-18
---
# 719 — The Unsplit Physical Source Is Cyclic for the Rank-Twenty-One Relative Union

## New objective after Entry 718

Entry 718 retires the search for an intrinsic generic homogeneous home of
\(\mathcal Q\). The remaining problem is to construct and classify the full
nonsplit marked relative coefficient system from the literal physical
source.

The retained-pivot relative checker already implements the required
chain-level operation. This entry completes its previously missing
iteration for the unsplit five-mark union.

## Frozen relative union

Use the five lower marks

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}})
\]

and quotient proper faces at chain level before reduction. The finite
relative union has dimension

\[
\boxed{21}.
\]

The literal unsplit source retains the numerator prescribed by the two
occurrence families,

\[
\boxed{q_{g_{23}}+q_{g_{31}}.}
\]

It is nonzero and has support on three free coordinates in the normalized
pivot presentation. That coordinate count is not asserted to be canonical.

## Horizontal saturation

Differentiate the source along the two independent implemented kinematic
directions, including derivatives of the numerator, Cayley--Menger twist,
and all marked denominators. Reduce after every derivative in the same
relative presentation and iterate until the span stabilizes.

The first jet has rank

\[
\boxed{3},
\]

but the iterated horizontal saturation has rank

\[
\boxed{21}.
\]

Thus

\[
\boxed{
\operatorname{Sat}_\nabla(\Omega_{\rm unsplit})
=M_{21}^{\rm rel}.
}
\]

## Replication

The result is unchanged in three finite tests over \(\mathbf F_{32003}\):

\[
(\gamma,\text{ambient degree},\text{cutoff})
=(5,10,5),\ (7,10,5),\ (5,11,5).
\]

Each gives relative dimension \(21\), first-jet rank \(3\), and saturation
rank \(21\).

The two separate four-mark occurrence presentations likewise have
nineteen-dimensional relative top blocks, and their individual literal
sources horizontally saturate all nineteen directions.

## Consequence

The physical source does not generate a privileged rank-one or rank-three
subconnection. It is a cyclic vector for the entire finite relative union:

\[
\boxed{
\text{one literal source}
\xrightarrow{\text{Gauss--Manin orbit}}
\text{full rank-21 relative coefficient system}.}
\]

Any proposed smaller physical block must therefore arise from an
independently derived quotient, symmetry projector, or Gysin functor. It
cannot be inferred from the small coordinate support of the initial source
or its first jet.

## Scope boundary

This is an exact finite-field retained-pivot computation at one generic
kinematic point, replicated across regulator and ambient-degree choices. It
does not yet construct the integral lattice, a global multivariate
connection matrix, or the extension by the elliptic block appearing in
Entry 718.

No \(\mathcal Q\)-support test is made or needed.

## Evidence

- Entries 658, 663, 718;
- `research/benincasa/physical_four_mark_residue_twisted_derham.py`;
- `research/benincasa/check_unsplit_relative_horizontal_saturation.py`;
- allocator claim `seqclaim-685d0c92dce370e7bcac001c`.

## Next falsifier

Extract a basis for the twenty-one-dimensional horizontal orbit together
with the two connection matrices induced by the retained-pivot reduction.
Compute their common invariant subspaces and the occurrence-reflection
action. Only a source-derived invariant quotient may be compared with the
Tate/elliptic extension

\[
0\to\mathbb V_{\rm ell}(-1)\to\mathbb V_\triangle\to\mathcal T\to0.
\]
