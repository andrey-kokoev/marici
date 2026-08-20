---
title: "The Four-Cycle Node Hessians Introduce No New Carrier Divisor"
date: 2026-08-20
entry: 1165
status: active
sector: cosmology
---

# 1165 — The Four-Cycle Node Hessians Introduce No New Carrier Divisor

Sequence claim: `seqclaim-9a8f91f4b96047834cdc9013`.

## Frozen question

Entry 1164 identifies 296 labelled forced infinity incidences whose generic
branch enhancement is an \(A_1\) node. The first finite falsifier is whether
degeneration of those nodes defines a new irreducible carrier divisor.

Let

\[
H=\operatorname{adj}(G)=
\begin{pmatrix}
A&D&F\\ D&B&G\\ F&G&C
\end{pmatrix}.
\]

For each labelled incidence, restrict

\[
4B_4=-\Delta^TH\Delta
\]

to the two-dimensional projective tangent plane, impose the corresponding
branch-activation equation, and take the exact Hessian determinant.

## Exact census

An occurrence-preserving rational derivation reduces the 296 records to 28
labelled polynomial types. Independent characteristic-zero factorization in
Rust/Symbolica gives:

- 152 coordinate-point occurrences: every Hessian is a product or square
  of linear Gram-cofactor forms in the entries of \(H\);
- 144 alternating-point occurrences: the four labelled Hessians are
  two-plane minors of \(H\), including
  \[
  AB-D^2,\qquad AC-F^2,\qquad BC-G^2.
  \]

The fourth is the same determinant in the remaining labelled tangent plane.
By Jacobi's complementary-minor identity,

\[
\operatorname{minor}_2(\operatorname{adj}G)
=
\det(G)\,operatorname{minor}_1(G)
\]

up to the labelled basis unit. Hence the deeper degeneration support is a
union of the already frozen Gram-determinant and complementary Gram-minor
supports. No irreducible quartic-only divisor remains.

## Narrow result

\[
\boxed{
\text{The forced C4 node Hessians introduce no new carrier divisor.}
}
\]

The generic nodes and their deeper degenerations are organized by existing
Gram-minor/triangle support. Their nontrivial content remains coefficient
data: the mixed-Tate node arrangement and its quadratic deck character.

This is an algebraic support statement. It does not prove that the physical
Bunch--Davies relative chain activates the anti-invariant node classes.

## Next falsifier

Construct the source-relative specialization map to one labelled normalized
node arrangement, retain its deck character and orientation, and test whether
the anti-invariant classes pair nontrivially. Failure to obtain a
source-derived map means the algebraic coefficient class is physically
unselected, not that a new carrier cell should be added.

## Evidence

- `research/benincasa/checkers/derive_four_cycle_node_hessian_polynomials.py`
- `research/benincasa/marici-gm/src/bin/four_cycle_node_hessian_factor.rs`
- `research/benincasa/checkers/audit_four_cycle_node_hessian_carrier.py`
- `research/benincasa/results/four-cycle-node-hessian-polynomials.json`
- `research/benincasa/results/four-cycle-node-hessian-factors.json`
- `research/benincasa/results/four-cycle-node-hessian-carrier.json`
- Entry 1164.
