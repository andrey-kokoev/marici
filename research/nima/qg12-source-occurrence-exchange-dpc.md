# Source occurrence exchange: new cycle 2

## Problem

An equivariant specialization to the unordered root-pair lattice would have even image. Such equivariance might descend from exchanging the two occurrence summands of the source-sewn canonical form.

## Bold conjecture

The source-sewn equality `eta_31+eta_23=eta_unsplit` carries a canonical involution exchanging `eta_31` and `eta_23` while preserving their coefficient data.

## Named rivals

1. commutativity of the sum supplies an exchange symmetry of the summands;
2. the sum is invariant, but the ordered unequal summand data are not;
3. an exchange exists only after forgetting the Tate/Kummer coefficients and endpoint jets.

## Risky consequences

Writing the coefficient vector as `(c_31,c_23)`, exchange must preserve it. Therefore the bold conjecture requires `c_31=c_23`.

## Strongest falsification attempt and residual

The frozen source audit explicitly identifies the two Tate/Kummer classes `c_i[dn/w]` as unequal. For the exchange matrix `S`, execution `structured_command_execution:e_31668_1788304174058573500_5` computes

\[
S(c_{31},c_{23})-(c_{31},c_{23})
=(c_{23}-c_{31},c_{31}-c_{23}).
\]

This vanishes exactly when `c_31=c_23`, contrary to the source condition. Commutativity makes the total sum invariant but does not construct an involution preserving the typed summands. The bold conjecture is falsified.

## Disposition and residual conjecture

Root-transposition equivariance cannot be derived from occurrence exchange. It can only be a property of a separately constructed specialization from the already-sewn unsplit total to the unordered root target. If such a map is source-canonical, descent would force its image into the even invariant submodule; existence, nonzero value, primitivity, and orientation remain unconstructed.

The next falsifier is to test whether source canonicity plus unordered-target descent alone excludes the previously admissible projection maps. This is conditional map classification, not construction of the missing physical chain.

## Evidence

- `research/nima/checkers/check_qg12_source_occurrence_exchange.py`
- `research/benincasa/occurrence-resolved-physical-period-no-go.md`
- `research/nima/qg12-equivariant-root-target-dpc.md`
