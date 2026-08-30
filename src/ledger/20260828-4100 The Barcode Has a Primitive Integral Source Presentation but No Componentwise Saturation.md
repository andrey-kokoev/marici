# 4100 — The Barcode Has a Primitive Integral Source Presentation but No Componentwise Saturation

## Question

Can the characteristic-zero interaction-net barcode be derived by lifting its
source complex over the integers, rather than reconstructing finite-field
row-reduced basis vectors?

## Frozen input

Use the source-labelled \(G_{12}\) depth-three product-pole presentation at

\[
(x,y,z)=(2,3,4),
\qquad
\gamma=-\frac12,
\]

with \(K\)-depth \(3\), denominator depth \(2\), and ambient monomial degree
\(14\). Retain all labelled de Rham, \(K\)-multiplication, and five
denominator-multiplication relations before quotient reduction or pivot
selection.

Normalize each rational relation by:

1. clearing its denominator;
2. dividing by its integer content;
3. orienting it by the first labelled nonzero coefficient.

No modular pivot or barcode basis is used in this normalization.

## Result

The frozen presentation has:

\[
\begin{aligned}
720&\text{ de Rham rows},\\
6336&\text{ }K\text{-multiplication rows},\\
5\cdot6720&\text{ labelled denominator-multiplication rows},
\end{aligned}
\]

for a total of \(40656\) primitive integral relations on \(15496\) labelled
coordinates.

Every row has width at most \(7\), and the largest absolute coefficient is
\(109440\). The canonical serialized presentation has SHA-256

9e35bf07ebd20182e5ce52efe7bd76b2955818b273f5182429a48e2e628a8679.

Reduction modulo each barcode prime

\[
31991,\qquad 32003,\qquad 32009
\]

preserves every row and every row support. Thus the three finite-field
computations are reductions of one source-normalized integral presentation.

However, the bipartite relation hypergraph is connected: all \(15496\)
coordinates lie in one component. Therefore the integral saturation problem
cannot be decomposed into independent combinatorial components merely by
following relation incidence.

## Narrow conclusion

The failure of coefficientwise CRT does not imply that no integral barcode
exists. It shows that modular row-reduced representatives are not the object to
lift. The correctly typed candidate is a saturated subquotient of the complete
primitive integral source presentation.

The connectedness result removes the cheapest possible implementation:
componentwise Smith/Hermite reduction is unavailable. Any exact lift must use a
global sparse-lattice method or a source-derived filtration finer than raw
relation connectivity.

## Next finite falsifier

Construct the depth filtration over this primitive integral presentation and
test whether fraction-free elimination, modular Smith reconstruction, or a
source-derived block filtration produces saturated kernels whose reductions
have dimensions

\[
20,\qquad 6,\qquad 27
\]

and depth-four emergence rank \(1353\) at all three good primes.

If no source-derived block filtration exists and the global saturated
calculation produces prime-dependent torsion, then the stable finite-field
skeleton does not descend to a free integral barcode lattice.

## Artifacts

- research/benincasa/checkers/check_interaction_net_integral_source_presentation.py
- research/benincasa/results/interaction-net-integral-source-presentation.json
