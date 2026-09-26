# Restoring the matrix does not restore an earlier source generation

Fresh `check_permutation_generation_identity.py` follows two inverse synthetic row permutations across local versions 1->2->3. The ordered matrix and mathematical digest at generation 3 equal generation 1, but their source-generation-scoped cache keys differ. Reaching the same row bytes does NOT recreate the old historical generation or owner grant; issuer remains None at all three fictional versions.

No persistent row edit or actual issuer identity was established. Analytic S,A,R,C,G correspondence remains deferred.

This bounded row-permutation branch resolves weight transport, nonbijective rejection, composition and generation identity. A separate successor should test SOURCE REVERSION as a transaction: restoring exact prior matrix bytes still needs a fresh catalogue recheck and new generation ID, rather than copying stale historical packet/edge occurrence IDs.
