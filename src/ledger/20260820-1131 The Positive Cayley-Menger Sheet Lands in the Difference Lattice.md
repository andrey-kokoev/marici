---
title: "The Positive Cayley-Menger Sheet Lands in the Difference Lattice"
date: 2026-08-20
entry: 1131
status: established-local-betti
sector: cosmology
---

# 1131 — The Positive Cayley–Menger Sheet Lands in the Difference Lattice

Sequence claim: `seqclaim-7f8ae5fc97d6e347443a2588`.

## Frozen physical chain

At the second-center exceptional node,

\[
W^2=4T^2.
\]

The source positive Cayley–Menger prescription fixes

\[
W=2|T|.
\]

Thus its real chamber lies on the normalization sheet (e_-), where
(W=-2T), for (T<0), and on (e_+), where (W=+2T), for (T>0).

## Oriented boundary

Orient the (T)-axis increasingly.  Splitting it at the node gives

\[
[-R,0]\quad\text{and}\quad[0,R].
\]

Their endpoint coefficients at zero are respectively (+1) and (-1).
Consequently the normalization boundary of the physical chamber is

\[
\boxed{\partial\gamma_{CM}=e_- - e_+.}
\]

It is primitive in the anti-invariant sheet-difference lattice

\[
N^-=\mathbb Z(e_+-e_-),
\]

but Entry 1130's canonical map sends it to

\[
-2[e_+]
\]

in the primitive odd coinvariant lattice.

## Consequence

The physical source resolves one half of the integral ambiguity: it selects
the difference lattice, not an arbitrary primitive odd coinvariant.  The
factor two is therefore a real normalization-cover boundary multiplicity,
not a freely chosen regulator hierarchy.

This does **not** yet fix the (e_6) Betti lattice.  Hence it still does not
turn Entry 1127's rational scalar into a complete integral index theorem.
The remaining datum is now only on the target side: determine the saturated
Betti lattice in the (e_6) period line.

## Classification

The result uses the existing positive Cayley–Menger chain, normalization
cover, and conductor.  It supplies no new carrier stratum.  It identifies a
sector-specific integral coefficient boundary inside the shared calculus.

## Evidence

- `research/benincasa/checkers/rank12_positive_sheet_node_boundary.py`;
- `research/benincasa/results/rank12-positive-sheet-node-boundary.json`;
- Entries 180, 791, and 1127--1130.

