# Fixed policy and equal results do not erase history multiplicity

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverNonuniqueHistory.agda`; log: `results/agda-nonunique-history.log`. The older whole-programme receipt predates this fixture.

## Actual operational fixture

There is one fixed forward policy and two rule witnesses, red and blue, each from initial to terminal. Terminal has no outgoing step. The two resulting one-step histories have identical endpoints, length and Unit-valued semantic output, but are provably distinct.

The module checks a full equivalence History≃Bool: the rule observer returns the rule's label, and replay reconstructs the full history with both inverse laws. This proves exact sufficiency of a one-bit observer for THIS two-history fixture; it is not an information-theoretic bound for arbitrary systems.

Both histories have equal mere-admissibility observations. Faithful recovery of the supplied history from that truncation is impossible by the preceding general reconstruction criterion. Faithful recovery from their common Unit result is likewise impossible. A constant procedure can still choose the red history; choosing an admissible history is not recovering the one that was supplied.

## Foundational consequence

Even with fixed orientation, positivity of admissibility and knowledge of the result do not identify a retained witness. Access to the rule label does. Thus an existing history space and merely knowing that it is inhabited are different mathematical objects, with different observational content.

This does not refute a definition of execution as access to existing witness-bearing structure. It does rule out silently replacing that structure by its mere existence proposition while claiming to preserve which history occurred. No temporal clock, probabilistic choice, physical nondeterminism or external occurrence is asserted by this small formal example.

## Next

Consolidate the current operational/observational and higher-descent results in a fresh source-bound closure audit. The previous checkpoint predates named-endpoint coherence, groupoid reconstruction/equivalence, witness-sensitive readouts, the operational bridge, orientation policies and history reconstruction. Record the precise surviving interpretation boundary rather than reusing that old receipt or treating the iteration budget as programme completion.
