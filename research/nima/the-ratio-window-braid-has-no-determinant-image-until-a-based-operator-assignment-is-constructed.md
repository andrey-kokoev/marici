# The ratio-window braid has no determinant image until a based operator assignment is constructed

## Question

Can the coherent interval-refinement packet be sent to the normalized third-determinant line using the currently available source operations?

## Available determinant structure

For relative operators with product law `star`, the third-determinant anomaly is the exact trace-class cocycle

\[
\alpha_3(A,B)
=-\operatorname{Tr}(A^2B)
-\operatorname{Tr}(AB^2)
+\frac12\operatorname{Tr}((AB)^2).
\]

It satisfies the two-cocycle identity and reciprocal dagger order reversal. After the source-derived low-grade coboundary normalization, the determinant line is a strict one-dimensional module. Rank-two normalized faces then force all higher scalar path coherence.

The exact rational anomaly checker confirms nonzero strict-multiplicativity hostiles, the cocycle identity, and dagger reversal.

## First missing typed object

The refined seam packet contains based interval windows and signed ratio faces. To apply the determinant character it needs a source assignment

\[
\kappa_G:Q_a\longmapsto K_{G,a}
\]

such that

\[
K_{G,a+b}=K_{G,a}\star K_{S_aG,b}.
\]

The same operator packet must satisfy:

- first trace equals the primitive endpoint current;
- half the square trace equals the square endpoint current;
- the connected coordinate is the retained third-determinant tail;
- adjacent ratio-window faces map to the computed anomaly cell;
- reciprocal transport reverses order and conjugates the anomaly.

No current source operation constructs this assignment from the interval Stein attachment.

## Why no determinant formula may be fitted

The interval partition and its Stein Gram determine boundary energies, not a unique Schatten-three operator. Equal primitive and square traces admit unequal connected determinants. Assigning an operator to reproduce the desired determinant section would reconstruct the source backward from its scalar readout.

The normalized determinant module theorem is conditional on `kappa_G`; it does not construct `kappa_G`.

## Finite falsifier and acceptance test

Any candidate assignment is rejected if either:

1. two source packets with equal first two trace coordinates receive the same connected determinant despite the exact unequal-determinant hostile; or
2. an adjacent ratio face fails the displayed anomaly formula or the three-factor cocycle identity.

Acceptance requires an operator assignment derived before determinant evaluation and satisfying the based composition law on every reachable rank-two face.

## Disposition

The determinant anomaly and all coherence laws after operator assignment are verified. The functor from the refined interval packet to that operator groupoid is absent. This branch stops at `kappa_G`; completion and scalar determinant readout are not executable before it is constructed.

Verification:

- `research/nima/checkers/check_det3_multiplicative_anomaly.py`
- `research/nima/results/det3-multiplicative-anomaly.json`
- `research/nima/results/low-cumulants-do-not-select-det3-operator.json`
