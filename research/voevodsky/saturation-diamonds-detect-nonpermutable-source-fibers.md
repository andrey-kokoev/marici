# Saturation diamonds detect nonpermutable source fibers

## Actual source-bound test

Use the independently replayed four-state primitive-evidence carrier P,A,B,AB. The A-only observer L has fibers {P,A},{B},{AB}; the B-only observer M has fibers {P,B},{A},{AB}. Define S_L(C)=L^-1(L(C)), relative to the fixed carrier, and likewise S_M.

The saturation diamond fails on C={A}:

    S_M S_L({A})={P,A,B},
    S_L S_M({A})={P,A}.

Its source witness is A --L--> P --M--> B. There is no reverse-order intermediate state: the M-fiber of A is {A}, and its L-fiber does not contain B.

## Exact criterion and exhaustive checks

Let K_L and K_M be the equivalence relations given by equal observer values. Saturation is relational image under the corresponding kernel. Therefore the closures commute on every subset exactly when K_L and K_M commute under relational composition. Singleton subsets already detect every difference.

The checker verifies this equivalence for all sixteen source restrictions and all their subsets (81 carrier/subset cases). Noncommutation occurs exactly when the restricted carrier contains P,A,B together. Restricting the carrier changes the relative closure operator; this must be distinguished from intersecting evidence while leaving the source carrier fixed.

The criterion concerns existence of a reverse-order middle witness. A coherent bijection of middle-witness types is a stronger proof-relevant statement and is not inferred here.

## Joint retention versus alternating forgetting

The paired observation (L,M) is injective on the four-state carrier, so its saturation is identity. By contrast, alternating the two separate saturations to a fixed point sends {A} to {P,A,B}. Retaining both observations and repeatedly forgetting through them are different operations.

The former preserves their intersecting distinctions. The latter closes under the join of their kernel equivalences. Neither operation should be confused with the primitive-evidence merge A meet B=AB.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_saturation_diamond.py

Artifact: `results/continuation-quotient/saturation-diamond.json`.
