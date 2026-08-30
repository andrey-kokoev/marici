# Quark-slot port descent (WP321)

## Proposed physical labels

The most immediate attempt to physicalize the six binary slots of WP320 is to
name them as three up-sector and three down-sector quark generations. This does
not by itself create source ports. Before Yukawa symmetry breaking, generation
labels are weak-basis coordinates.

WP321 first audits the exact permutation subgroup. Independent generation
permutations reduce 64 literal binary words to the 16 pairs of sector Hamming
weights

\[
(w_u,w_d),\qquad 0\leq w_u,w_d\leq3.
\]

If up/down exchange is also admitted, these reduce further to 10 unordered
pairs. A binary address assigned to individual generation slots does not
descend even under this finite subgroup, hence cannot descend under the full
weak-basis group without additional structure.

## Hostile pair

The words `100|000` and `010|000` are related by an up-generation permutation.
They have the same quotient label ((1,0)) but different binary addresses.
This is an exact failure of presentation-independent descent.

## Instrument gate

Generation-resolving source ports would require source-derived projectors that
transform covariantly under the full weak-basis group. Defining those
projectors by diagonalizing and ordering the Yukawa matrices uses the flavor
readout to construct the source labels, so it cannot authorize a selector.

Run `uv run python research/flavor/checkers/wp321_quark_slot_port_descent.py`
to regenerate the exact quotient audit.
