# WG retained-history congruence under fixed nested/flattened presentation

## Versioned scope

This supplements, rather than silently broadens, `history-to-state-congruence-v1.md`. Fix exactly F and G from `Composite` in `ComposableWitnessSpecialization.agda`. N=compile G and K=compile(compose F G) share these actual input sources. The candidate relation and allowed continuations below are explicit. No arbitrary equivalence, quotient by endpoint, relation-algebra/WG identification, physical actuation or runtime-resource model is introduced.

## Relation on histories

For generated histories with the same number of events, relate hN and hK iff their initial states are connected by flatten and every recorded state and actual witness is carried by flatten and flatten-edge. Retain the initial input source pair and generator policy unchanged. This is the graph of an invertible history presentation map, not a quotient deleting provenance. Disjoint-union histories in the two presentations may be identified only through this supplied map (and its inverse); histories within either presentation remain identical at the retained record level.

An admitted next generated event is exactly the source's `generate` output. A witnessed edge package can also be recorded if supplied at the Step type; it is not thereby an executable generated intervention. Keep these two vocabularies distinct.

## Finite continuation theorem

Let α=Composite.flatten and β its inverse. Let E be the `Realization.steps` isomorphism from `Composite.correct`. Its endpoints field identifies the transported target with α of the source target; its generated field identifies transported generated events.

Base: α takes the initial state of hN to hK, preserving fixed source records.

Induction: suppose current states correspond. Apply the generated field to the next generated event. Its state and actual witness are the transported ones; endpoint compatibility gives the induction hypothesis at the extended histories. Therefore every finite generated suffix transports in both directions and replay commutes. For supplied full-step histories, use E and its endpoint path at each extension. This latter theorem is about dependent history records, not automatic scheduling or generation of arbitrary steps.

Concatenation follows by induction on the second history, preserving the matching boundary; empty history is preserved. Observers on K pull back through α (and through E for edge observations). Thus all explicitly chosen retained-state/edge observations, including proof payload observations, match on related histories. Success relations pull back in exactly the same way.

A further fixed refinement H on N has its admission family transported by `Composite.rebase`: `Admit'(x)=Admit_H(βx)`. Its extra witness indices use unflatten-edge. Hence enabled dependent admissions, their actual payloads and certification obligations correspond. This is the permitted proof-sensitive continuation family; no broader refinement transport is claimed.

Resource convention: only existing admission/witness obligations and fixed source data are compared. There is no numeric resource cost in this WG instance. Adding costs requires a compatible cost map and is a successor candidate.

## Attachment boundary

The marked path-algebra module attachment is not a field of this `Composite` interface. It is therefore NOT transported here by assertion. For the separate relation-module task, retain the actual module/action/connecting map and use identity transport until a genuine comparison is supplied. The previous nonsplit-attachment counterexample remains valid against an erasing candidate. This division prevents an unsupported identification between the two source models.

## Evidence

Freshly inspected `ComposableWitnessSpecialization.agda` definitions: Refinement, compile, compose, Step, Realization, Composite.correct/rebase and ProofDependentFixture. Existing dependent certificates are reused; no fresh Agda run is claimed.

`checkers/wg_retained_history_transport_v1.py` transcribes the finite Boolean fixture. Eight checks pass across eight initial states and generated histories of lengths 0 through 8, including full witness-record transport, concatenation and rejection of the wrong first-layer payload at unchanged endpoints. Boolean certificate tokens are checked against their propositions; this is not an independent proof of arbitrary dependent types.

Disposition: a precise bounded WG history relation and finite continuation theorem are now available alongside the energy/context subcases. This is suitable for a scope-explicit owner review of the congruence gate, not an automatic resolution of its broadest reading. Mathematical assembly must use precisely these same vocabularies and relation; attachment-preserving comparisons remain a separate obligation if included in assembly scope.
