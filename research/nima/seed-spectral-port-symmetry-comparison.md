# Spectral ports admit seed-symmetry comparison, not yet interaction

## Recovered constructions

`record4-spectral-promotion.md` constructs complete promoted records with eigenphase and history window. `spectral-promotion-nine-cycles.md` explicitly says repeated promotion adds provenance, not a next-level composition law. `two-triangles-shared-edge-half-phase.md` has a genuine overlapping coefficient model, but its BA=-AB cochain gluing is an additional convention, as audited in `shared-edge-native-reversal-and-gluing-audit.md`.

There is nonetheless a source-tied representation comparison available without that gluing: the seed automorphism already established in `seed-cycle-response-through-retained-rungs.md` exchanges its two triangle families.

## Exact specialization to existing spectral records

The only nonidentity automorphism of the six directed-edge graph is s=(AB)(CD). It sends the ordered triangle occurrences

    (AB,BC,CA) -> (BA,AD,DB)

and back. These are separate three-dimensional occurrence coefficient spaces. The induced slot bijection J is the identity matrix IN THEIR CORRESPONDING ORDERED BASES; it is not an identification of the original occurrence IDs.

Reusing the existing ledger and spectral projector constructor, the checker verifies

    J C_left = C_right J,
    J E_left,lambda = E_right,lambda J.

All three modes are retained. Eigenphases agree under this orientation-preserving transport; conjugation is not inserted. After transport, same-mode projector overlap is that projector and distinct-mode overlap is zero. These are linear algebra identities in the declared counting-metric representation, not transition probabilities or detector signals.

Every promoted identity keeps its own fresh label and root. Deconstructing the two windows recovers their respective original three occurrences. The comparison transports provenance instead of replacing one history by the other.

## Scope

This is a newly checked specialization of existing seed symmetry and spectral-promotion machinery. It is NOT a newly recovered physical law, a native pointed filler/admission proof, or an assignment of transport to the six primitive arrows. No inverse identification of AB and BA values, coherent amplitude, preparation, selected mode or coupling parameter is added.

It answers a limited version of the next-port question positively: the two spectral families can be compared covariantly as labelled representations. It does not supply a process in which one changes the other's state. Applying this relabelling repeatedly would not produce binding or a new response.

The matrix-domain gate for the seam covariance remains unresolved and should not be declared closed by this different, whole-record comparison. Any further claim of cross-port interaction requires an actual operation beyond spectral equivalence, together with its retained inputs and observation.

## Verification

    python research/nima/checkers/check_seed_spectral_port_transport.py

Fresh exact checks pass: exhaustive graph automorphisms, typed occurrence relabelling in both directions, cyclic intertwining, all three promoted modes, distinct fresh identities and roots, history recovery, and same/different-mode transported overlaps. Existing ledger/projector functions are imported directly; their full standalone regression suite was not rerun in this turn.
