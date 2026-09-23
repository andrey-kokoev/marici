# Typed path edges must bind row manifests and exact targets

Fresh `check_path_edge_manifest_target_binding.py` compares synthetic weakening edges with the same from/to occurrence IDs and rule but (a) changed x-upper source row or (b) changed destination bound x<=3 rather than x<=2. A vertex-plus-rule digest collides in both cases. A full digest over source-row manifest and both exact endpoint normal/bound records distinguishes all three. Replay on changed rows fails `SOURCE_MANIFEST_MISMATCH`; replay on changed bound fails `EXACT_TARGET_MISMATCH`.

A matching structural commitment is necessary but NOT sufficient: the endpoint proof packets, admissible weakening arithmetic, and actual event provenance must still be validated. None of these fixtures supplies a row issuer or analytic S,A,R,C,G correspondence.

Next check a MIXED-MANIFEST path: each edge individually has a complete commitment, but concatenation tries to cross from one row manifest into another without an explicitly typed source migration. Require composability at the middle occurrence and source generation, not only two individually valid edge digests.
