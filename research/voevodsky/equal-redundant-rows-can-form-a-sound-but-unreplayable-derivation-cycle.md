# Equal redundant rows can form a sound but unreplayable derivation cycle

Take syntactically distinct row IDs z,w for the same square inequality `x+y<=2`. Individually, a packet 'z from w' and a packet 'w from z', both with multiplier one, have the correct normal and bound. But their combined dependency graph has a cycle and NO primitive-root base: recursively expanding either certificate never reaches the original square rows. Fresh `check_redundant_row_dependency_cycle.py` validates both equations and rejects the mutual derivation as `DERIVATION_CYCLE`.

An acyclic alternative DOES exist: derive z from primitive x-high and y-high, then derive w from z. The cycle rejection concerns the CHOSEN derivation graph, not mathematical validity of either redundant inequality. Endpoint row equality and retraction-kernel rank do not detect dependency nontermination. Historical replay needs a finite acyclic, primitive-rooted derivation DAG plus introduction edge IDs and manifest generations; even such mathematical anchoring does not authenticate a source publisher.

Next test a DAG with SHARED subproofs and two equivalent topological traversals: distinguish structural dependency identity from temporal execution order, and check whether a retained DAG alone is enough to replay a recorded sequential proof path. Keep analytic correspondence deferred.
