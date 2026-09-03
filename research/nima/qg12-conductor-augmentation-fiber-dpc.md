# Conductor augmentation fiber: new cycle 5

## Problem

Norm transfer reproduces the exact connecting coefficient. The scalar normalization might uniquely determine the equal root allocation and hence the even cycle.

## Bold conjecture

The exact conductor coefficient uniquely selects the even norm pair over all ordered-root allocations.

## Named rivals

1. total normalization forces equal root coefficients;
2. normalization fixes only their sum and admits single-root or asymmetric allocations;
3. integrality or primitivity removes the asymmetric allocations.

## Risky consequences

The augmentation fiber over the exact coefficient must contain only the equal pair if the bold conjecture is correct.

## Strongest falsification attempt and residual

Let

\[
C=-\frac{1}{32p^4(\kappa-1)^2}.
\]

Every pair

\[
(\lambda C,(1-\lambda)C)
\]

has augmentation `C`. Execution `structured_command_execution:e_31668_1788304433384759700_8` verifies the full one-parameter fiber. It contains the norm pair at `lambda=1/2`, both single-root projections at `lambda=0,1`, and asymmetric allocations. Exact normalization therefore does not select parity. The bold conjecture is falsified.

## Disposition and residual conjecture

The algebraic conductor calculation fixes only the augmented coefficient. It is compatible with the even norm pair but also with single-root and asymmetric lifts. Choosing `lambda=1/2` requires a source-derived root-transposition-equivariant specialization or an oriented relative-chain map.

No current source object supplies that map. Reopening requires one of:

- an oriented physical contour with endpoint/root trivialization;
- an integral specialization matrix to the root pair;
- a source-derived equivariance theorem for the sewn total.

Without one of these objects, further scalar, parity, or denominator manipulations cannot discriminate points in the augmentation fiber.

## Evidence

- `research/nima/checkers/check_qg12_conductor_augmentation_fiber.py`
- `research/nima/qg12-root-norm-conductor-normalization-dpc.md`
- `research/nima/qg12-unsplit-contour-root-pair-no-go-dpc.md`
