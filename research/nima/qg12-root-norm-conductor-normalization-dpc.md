# Root norm versus conductor normalization: new cycle 4

## Problem

The root norm sends one coinvariant generator to the even root pair and introduces a factor of two after augmentation. This factor might conflict with the exact conductor coefficient.

## Bold conjecture

The norm/transfer factor of two obstructs the established `q_g2` conductor normalization.

## Named rivals

1. norm doubles the coefficient incorrectly;
2. the two equal conductor residues supply exactly the required factor of two;
3. scalar agreement holds but does not establish a chain-level norm factorization.

## Risky consequences

Starting from one oriented occurrence residue and the inverse Euler class, norm followed by augmentation must fail to reproduce the exact connecting coefficient if the bold conjecture is correct.

## Strongest falsification attempt and residual

The individual residue and inverse Euler factor give the oriented coinvariant scalar

\[
c=-\frac{1}{64p^4(\kappa-1)^2}.
\]

The norm gives `(c,c)`, and augmentation gives

\[
2c=-\frac{1}{32p^4(\kappa-1)^2},
\]

exactly the established conductor connecting coefficient. Execution `structured_command_execution:e_31668_1788304350720308200_7` verifies the equality symbolically. The bold conjecture is falsified.

## Disposition and residual conjecture

The algebraic coefficient is exactly compatible with norm transfer of one oriented coinvariant scalar. This is stronger than parity compatibility but weaker than a physical-chain theorem: equality after augmentation does not prove that the source specialization factors through the norm.

The residual conjecture is that the exact scalar normalization uniquely selects the norm pair `(c,c)` over odd allocations such as `(2c,0)`. The next falsifier computes the fiber of augmentation at the established coefficient. If odd allocations remain, a source-derived equivariance or chain map is still indispensable.

## Evidence

- `research/nima/checkers/check_qg12_root_norm_conductor_normalization.py`
- `research/nima/qg12-root-invariants-coinvariants-dpc.md`
- `research/nima/qg2-conductor-connecting-morphism-dpc.md`
- `research/benincasa/results/qg2_inverse_euler_gysin_dpc.json`
