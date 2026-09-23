# A rule-version label is part of the edge commitment

Fresh `check_rule_version_edge_replay.py` constructs synthetic same-target comparison endpoints. Relabelling their edge from `comparison@1` to hypothetical `comparison@2` leaves the local target-equality Boolean unchanged, but changes its complete edge digest; replay of the old commitment under the new label fails `EXACT_RULE_VERSION_OR_EDGE_MISMATCH`. Equal current output is not evidence that future/changed rule semantics are equivalent or that an observed event used the new rule.

The fixture defines NO real `comparison@2` semantics, version migration, signature or owner authorization. A matching structural digest is still not observed history. Analytic S,A,R,C,G correspondence remains deferred.

The bounded candidate-catalogue closure branch now tests packet/edge closure, edge-type dispatch, and versioned commitment. A distinct successor can test a NONEMPTY PATH-ENDPOINT invariant: an isolated valid packet and zero edges must not be represented as a witnessed derivation path from a source occurrence, although it remains a valid standalone math packet.
