# Tetrahedral mirror-orientation experiment

## Question

Can two optical frames that are exactly indistinguishable to every pairwise HOM measurement be separated by a phase-sensitive ternary observable?

## Frozen preparation

Prepare the four pure qubit states whose Bloch vectors are the tetrahedral vertices

`(+++)`, `(+--)`, `(-+-)`, and `(--+)`, with each component divided by `sqrt(3)`. Frame M is the componentwise complex conjugate of frame A. This is a reflection of the Bloch sphere, not a proper rotation.

Every diagonal fidelity is 1 and every off-diagonal fidelity is 1/3 in both frames. The complete pairwise record must agree within 0.01.

## Orientation observable

For the preregistered ordered triple `(0,1,2)`, measure the complex Bargmann loop

`B012 = Tr(P0 P1 P2)`.

Compile it independently as a sequential projector loop and as the expectation of the three-copy cyclic shift. The ideal values are `+i/(3 sqrt(3))` for A and `-i/(3 sqrt(3))` for M. Thus the Y-quadrature contrast is `2/(3 sqrt(3))`, approximately 0.384900, while the pairwise records remain equal.

## Acceptance gate

- Pairwise absolute error and cross-frame discrepancy are at most 0.01.
- The two complex compilers agree within 0.02.
- Each real quadrature has absolute value at most 0.02.
- A has positive Y, M has negative Y, and their Y contrast is at least 0.34.
- Reversing the cyclic order conjugates the result.
- Dephased, real-coplanar, pairwise-only, same-sign mirror, and compiler-mismatch controls are rejected where appropriate.
- An identity-cycle phase fixture fixes the X/Y sign convention before the primary contrast is unblinded.

There are at most 64 preregistered bounded estimands. With 100000 effective trials per estimand and tolerance 0.02, the Hoeffding union bound is `128 exp(-20)`, below 0.01.

## Claim boundary

This packet freezes an executable mathematical and statistical test. It does not claim that a controlled three-copy cyclic shift, a sequential projector loop, source-labelled interaction-net amplitudes, or physical data already exist. Benincasa's finite-field barcode export is an algebraic source packet, not an optical lift.

