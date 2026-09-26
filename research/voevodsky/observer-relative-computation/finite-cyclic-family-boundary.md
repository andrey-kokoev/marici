# Uniform finite-family boundary on positive-power residue observations

`agda/ObserverFiniteCyclicBoundary.agda` replaces isolated numerical examples with a uniform theorem for any finite list of positive-period probe codes. Code n denotes period suc(n); no arbitrary observer callback is stored.

An integer cover of the actual comparison loop supplies a semantic winding readout. Freshly checked transport computes winding(power n)=pos(n). The probe reads abs(winding) modulo its period, and a checked bound places every result below that period. These are finite-output observers; no finite-memory or resource-cost claim follows from the output bound.

## Checked result

For every finite family, the product of its periods is positive (the empty product is1). Every listed period divides this product, so all probes give identical readings on that many turns and on zero turns. The integer cover proves that the two actual paths are unequal. Consequently no decoder of the joint readings faithfully reconstructs every positive-power comparison path.

This is semantic path separation, not merely inequality of syntax or modular integers. The proof covers arbitrary positive periods and arbitrary finite lists, including duplicates and the empty list. It does not say that every conceivable observer loses this information: the integer diagnostic itself detects it.

## Important scoped boundary

These probes use ABSOLUTE winding. They agree with cyclic residue counting on the positive-power fragment, which suffices for the invisibility counterexample, but they are not yet a construction of signed finite cyclic monodromy on arbitrary inverse paths. In particular abs deliberately loses orientation on negative winding. The current leaf establishes this precisely scoped finite-output boundary; the signed finite-state bridge remains active work rather than an implicit assumption.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-finite-cyclic-boundary.log. The new membership eliminator was written at general indices to satisfy the strict transport gate. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Construct actual finite cyclic state spaces/permutation covers uniformly in their positive period, with signed forward/backward transport. Relate their observations to these positive-power residue probes and carry the finite-family obstruction across that bridge. Do not substitute absolute winding for a signed action or assume a monodromy theorem merely from a numerical remainder computation.
