# Binary resource separation is now checked, not only tested

The new safe Cubical module ResolutionNetFootprints.agda uses the original Resolve operator unchanged. A world assigns each token one of absent/free/spent. Unary rule data permit staying put or consuming free→spent. Binary rule data require pointwise ownership separation: one side must be absent. In particular spent is still owned.

For arbitrary token types and every admitted finite resolution history, Agda proves:

* uses(history,t) = spent-count(endpoint(t));
* origins(history,t) = owned-count(endpoint(t));
* each count is at most one;
* two owned statuses cannot inhabit a separation rule.

Here origins counts seed ownership occurrences across the entire branching derivation. Thus the theorem excludes not just repeated use along a path, but duplicated origin claims merged through different branches. It rejects the subtle spent/free overlap that would reintroduce an unused copy of an already-spent ticket.

Nonvacuity is explicit: a two-token example starts from separately owned resources, consumes each, and combines the histories via a binary rule. Both per-token use counts are exactly one. A separate function eliminates any claimed separation of spent and free for the same token.

Fresh `python research/voevodsky/resolution-net-v1/check_agda_footprints.py` passes Agda2.8.0.1 with --ignore-interfaces under --safe --cubical --guardedness. No new postulates or holes. Result/log: results/agda-footprints.json and agda-footprints.log.

Scope qualifications: the theorem is pointwise for arbitrary Token:Type, so it includes finite token universes but does not assert finite support or a finite TOTAL cardinality. Unary rules may consume several distinct tokens pointwise in one witnessed step; the Python single-token operation is a narrower case. The signature does not create resources or split one world into multiple output ports. The theorem is about one derivation, not selection of an authoritative external commit among alternate derivations. Python-to-Agda representation refinement is still open.

Architectural conclusion: binary resource linearity can be carried by the admitted rule signature; it does not require new internal flattening agents. This is a genuine instance of the proposed simplification, with the side condition made explicit rather than hidden. Next return to the operational proof gap: all-schedule termination and concrete port-to-term refinement, now with resource-indexed examples available as regression cases.
