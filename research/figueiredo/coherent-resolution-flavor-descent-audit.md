# Coherent Resolution flavor-descent audit

## Question

Does the admitted finite A3 Coherent Resolution determine a chain-level flavor quotient or a faithful `physical16` readout?

## Source package and typed data

The authoritative package used here is `research/nima/a3-coherent-resolution.md`, checked by `research/nima/checkers/check_a3_coherent_resolution.py` with result `research/nima/results/a3-coherent-resolution.json`.

Its generators are the 14 triangulations in degree zero, the 21 flips in degree one, the nine square or pentagon relation cells in degree two, and one oriented associahedral cell in degree three. The differentials are signed incidence, oriented face boundary, and the primitive integral boundary of the polytope. The augmentation sends every degree-zero generator to 1. The ranks are 13, 8, and 1, and the augmented complex is exact.

The arbitrary-rank source package `research/nima/arbitrary-m-coherent-resolution.md` instead uses strict chains of partial triangulations with alternating-deletion differential and contraction obtained by adjoining the empty partial triangulation. Its theorem is quantified separately at every finite rank.

## Descent test

A physical descent requires a target chain complex, a map on every source generator, admissible equivalences defining the target quotient, and a chain identity. None of those flavor-target data occur in either Coherent Resolution package. In particular, the augmentation is not a flavor map: it identifies all 14 cluster vertices and carries no flavor label, weak-basis orbit, support convention, or readout authority.

The only admitted coefficient audit is `research/nima/a3-physical-weight-resolution-gate.md`. Six positive-root coordinates determine 7 of 21 mutation-edge ratios. The other 14 ratios depend on three absent negative-simple coordinates. Assigning those coordinates arbitrarily gives a closed exact coboundary, but the source explicitly denies that this establishes physical content.

Therefore no source-derived map

\[
F:CR_3\longrightarrow S_{\rm flavor}
\]

is currently typed. Consequently the equation \(d_SF=Fd_{CR}\), descent of the Carrier contraction, kernels, obstruction classes in a flavor target, and fiber multiplicities are not defined rather than failed numerical tests.

## `physical16` and `physical10`

The flavor programme records `physical16` as a faithful tested coordinate on the quark-Yukawa physical quotient and `physical10` as a non-faithful measured projection. Coherent Resolution supplies no map from its generators to either coordinate object. Thus prior flavor-sector faithfulness does not compose with this Carrier package. No claim about a `physical16` or `physical10` fiber of a Coherent Resolution generator follows.

## Strongest falsification attempt

Conjecture: the Coherent Resolution plus canonical weights already determines flavor descent.

Rivals: the resolution is only a combinatorial presentation; missing boundary coordinates prevent coefficient transport; or a flavor map exists independently but has not been linked to these generators.

Risky consequence: all 21 mutation edges must have source-derived transport before any weighted chain map can be tested. The exact audit finds only 7 determined edges and a residual of 14. This falsifies determination by the currently admitted weights. The residual cannot discriminate the first and third rivals because the target flavor complex and generator map are absent.

## Claim boundary

This is a finite-source no-go audit. It does not refute the existence of a future flavor descent, alter the independent `physical16` faithfulness result, or promote finite A3 data to an unbounded theorem. The first missing typed object is a labeled map from the 14 triangulations and 21 flips to a declared flavor target complex, including target differential, quotient conventions, and physical readout authority. Acceptance requires explicit generator images and exact verification of \(d_SF=Fd_{CR}\); only then can contraction descent and fibers be computed.

## Disposition

The requested positive derivation is blocked at the first missing typed object. The surviving theorem is that the A3 Carrier complex is exact while its admitted physical weights leave 14 of 21 edge transports undetermined. `physical10` cannot repair this, and `physical16` cannot be invoked without a source-derived comparison map.

Verification:

- `research/figueiredo/checkers/check_coherent_resolution_flavor_descent_audit.py`
- `research/figueiredo/results/coherent-resolution-flavor-descent-audit.json`
