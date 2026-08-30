# Exact open-channel partition

Work package: WP533  
Owner: marici.Figueiredo

## Question

Can every one of the 173 threshold-open vector coordinate triples in the
WP516 witness be classified without a numerical coupling cutoff?

## Exact representation partition

The canonical fourteen-dimensional gauge space decomposes orthogonally as

\[
\mathcal H_{\mathrm{gauge}}=Q\oplus C_0\oplus C_1\oplus C_2,
\]

where \(Q\) is the exact rank-five mass-six quintet projector from WP532 and
each \(C_i\) is the rank-three complement of the embedded quintet line in one
WP508 four-generator block. The checker constructs explicit exact
orthonormal frames and verifies that their projectors are pairwise orthogonal
and resolve the identity.

For every ordered signature

\[
A\otimes B\otimes C,\qquad
A,B,C\in\{Q,C_0,C_1,C_2\},
\]

the exact Yang--Mills tensor is restricted to the corresponding frames. Of
the 64 signatures, 49 have zero squared tensor norm and 15 have nonzero norm.
Zero restriction is invariant under every change of basis within the four
subspaces.

## Complete threshold-open census

The independently replayed WP529 threshold test contains 173 open coordinate
triples. Their exact support partition is:

- 139 forbidden coordinates in zero tensor restrictions;
- 34 allowed coordinates in nonzero tensor restrictions.

The 139 forbidden coordinates consist exactly of:

- all 131 entries previously called numerical zeros;
- all eight provisional WP529 sub-cutoff candidates.

There are no unresolved numerical zeros inside a nonzero restriction class.
The 34-coordinate complement is exactly the list retained by WP516 and used
by WP517.

This resolves the apparent contradiction in WP529's terminology:
“resolved” there meant only larger than \(10^{-12}\). Eight such entries were
still numerical eigensolver leakage. Exact representation support, not a
floating-point threshold, supplies channel-presence authority.

## Classification

WP533 is a complete rigidification of the on-shell vector channel support at
the frozen WP516 existence witness. It is not a selector and adds no physical
instrument.

The smallest exact falsifier is one WP516 retained channel in a zero tensor
restriction, or one of the 139 excluded coordinates in a nonzero restriction.

The next gate is no longer channel discovery. It is to replace the 34
coordinate rows by invariant parent-level width sums, combine those with
quark residues on the common WP527 source domain, and insert the resulting
self-energies through the WP525 complex-mass Ward completion. Pole
production, lineshape and detector calibration remain separate.

## Reproduction

Run uv run --offline --with sympy --with numpy python
research/flavor/checkers/wp533_exact_open_zero_classification.py.

The generated result is
research/flavor/results/wp533_exact_open_zero_classification.json.
