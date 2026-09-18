# Physical-weight gate for the finite A3 Coherent Resolution

## Question

Do the six exact positive-root canonical weights determine a coefficient transport on the full A3 resolution?

## Result

The A3 cluster carrier has nine almost-positive roots. Under the polygon model, the six physical interval labels are

\[
[i,j]\longmapsto(i,j+2),\qquad 1\le i\le j\le3.
\]

The remaining three diagonals are the negative simple roots. The current canonical-form kernel supplies no weights for them.

Given nonzero coordinates `x_d` on all nine diagonals, define a cluster-vertex product

\[
W(C)=\prod_{d\in C}x_d
\]

and mutation transport along an oriented edge `C -> C'` by

\[
r(C,C')=\frac{W(C')}{W(C)}.
\]

Every square and pentagon holonomy is then exactly one by telescoping. This is an exact coboundary coefficient system.

For the physical input, only 7 of 21 mutation edges have ratios determined by the six positive-root weights. The remaining 14 require at least one of the three missing negative-simple coordinates.

## Consequence

The signed physical exchange residual does not determine a mutation cocycle. A full coefficient system requires three additional boundary coordinates and a source-derived rule relating cluster-vertex products to canonical-form weights. Arbitrary assignments produce a closed but cohomologically trivial transport and therefore cannot establish physical content.

## Claim boundary

This is a finite A3 coefficient-completion theorem. It neither chooses the missing coordinates nor identifies product weights with canonical forms.

Verification:

- `research/nima/checkers/check_a3_physical_weight_transport.py`
- `research/nima/results/a3-physical-weight-transport.json`
