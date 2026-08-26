# Exact candidate block zeros

Work package: WP531  
Owner: marici.Figueiredo

## Question

Are the eight sub-cutoff vector channels reported provisionally in WP529
physical couplings, or numerical leakage between exact WP508 support blocks?

## Admitted domain

The domain is limited to the eight WP529 triples re-evaluated by WP530. The
canonical gauge coordinates are the WP508 four-generator blocks

\[
B_0=(F_1,F_6,P_1,E_1),\qquad
B_1=(F_2,F_7,P_2,E_2),\qquad
B_2=(F_3,F_8,P_3,E_3).
\]

No conclusion is asserted here for the fivefold-degenerate quintet or for an
unclassified numerical-zero channel.

## Exact restriction

The checker constructs the Yang--Mills cubic tensor directly from the
Gell-Mann commutators, with \(g_F=\sqrt 2\), and adds the two declared
three-vector Levi-Civita tensors with exact rational couplings. The eight
ordered candidate triples occupy four support signatures:

\[
(0,0,2),\quad(0,2,0),\quad(1,1,2),\quad(1,2,1).
\]

Every one of the 64 canonical entries in each restricted tensor is exactly
zero. Equivalently,

\[
\lVert G|_{B_0\otimes B_0\otimes B_2}\rVert^2
=
\lVert G|_{B_0\otimes B_2\otimes B_0}\rVert^2
=
\lVert G|_{B_1\otimes B_1\otimes B_2}\rVert^2
=
\lVert G|_{B_1\otimes B_2\otimes B_1}\rVert^2
=0.
\]

## Theorem and interpretation

The WP508 mass operator preserves each \(B_i\). Therefore every relevant mass
eigenvector remains inside its declared block, and arbitrary changes of basis
within any block cannot turn a zero restricted trilinear form into a nonzero
one. All eight WP529 candidate mass-basis couplings vanish identically.

This upgrades WP530's multiprecision collapse from numerical evidence to an
exact block-support theorem. WP529's provisional candidate interpretation is
superseded: those entries are eigensolver leakage, not physical decay support.
This is a rigidification of the vector self-energy bookkeeping, not a flavor
selector and not a new instrument.

## Falsifier and remaining gate

The smallest exact falsifier is one nonzero canonical entry in any of the four
restricted tensors, or one alleged candidate eigenvector with support outside
its WP508 block.

The theorem does not yet authorize calling WP517's 34-channel list a complete
total width. That requires the exact five-dimensional quintet spectral
projector, a basis-invariant classification of every remaining
threshold-open numerical-zero class, and degenerate-subspace coupling sums.

## Reproduction

Run uv run --offline --with sympy python
research/flavor/checkers/wp531_exact_candidate_block_zeros.py.

The generated result is
research/flavor/results/wp531_exact_candidate_block_zeros.json.
