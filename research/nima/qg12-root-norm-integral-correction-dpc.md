# Integral root norm correction: correction cycle 3

## Problem

The quotient map sends the invariant generator `e_-+e_+` to twice the coinvariant generator. This index-two composite might imply that invariants and coinvariants can only be compared after inverting two.

## Bold conjecture

The cokernel of inclusion followed by quotient obstructs an integral comparison between the invariant and coinvariant root lattices.

## Named rivals

1. index two obstructs every integral comparison;
2. the reverse norm is an integral isomorphism in natural generators even though it is not a section of the quotient;
3. target comparison is integral, but it does not determine which source correspondence is physical.

## Risky consequences

If the bold conjecture is correct, no integral map can send the primitive coinvariant generator to the primitive invariant generator.

## Strongest falsification attempt and residual

For the transitive permutation lattice,

\[
N([e_-])=e_-+e_+
\]

is integral and sends generator to generator. Hence `N` is an isomorphism between the rank-one coinvariant and invariant lattices. The quotient composite satisfies

\[
q\circ N=2,
\]

so `N` is not a section of `q`; that fact does not obstruct the integral comparison. Corrected execution `structured_command_execution:e_31668_1788304651008845000_9` records both statements separately. The bold conjecture is falsified.

## Disposition and residual conjecture

No inversion of two is required on the target side. The remaining gate is entirely arrow-typed: a source contour may induce a projection-like correspondence, the norm-like correspondence, or another allocation in the augmentation fiber. The target's canonical norm does not decide which source arrow exists.

Residual conjecture: a source-derived correspondence that is explicitly norm-like selects the even primitive class with the exact conductor normalization already verified. Reopening still requires the oriented contour, specialization matrix, or source equivariance theorem.

## Evidence

- `research/nima/checkers/check_qg12_root_invariants_coinvariants.py`
- `research/nima/qg12-root-invariants-coinvariants-dpc.md`
- `research/benincasa/results/qg12_root_pair_norm_transfer_correction.json`
- `research/nima/qg12-conductor-augmentation-fiber-dpc.md`
