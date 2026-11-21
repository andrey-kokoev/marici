# Why triple-born rules are redundant in the regular candidate systems

The singleton/pair rule systems do more than repair triple-born defects later: they prevent the relevant triples from being selected at all.

ramsey_triple_defect_implication.py takes the already compiled support-conflict and singleton/pair-born repair implications. For each disjoint triple, it assumes its three switches selected, then applies ordinary logical unit propagation, including contraposition: if all repairers are forbidden and all but one triggering switch are selected, that last switch is forbidden. Selecting a switch also forbids all overlapping supports.

Across all ten regular candidate systems:
-46,720 disjoint triples tested.
-46,692 assumptions produce contradiction by unit propagation alone.
-Only28 triples remain unexcluded.
-NONE of those28 has a genuinely triple-born independent seven. Every seven it contains was already independent after one of its proper subcollections.

Survivors by source:182 two;183 one;185 one;186 four;191 twenty;all others zero. The twenty at191 are the ten valid triples plus the ten triples inside the irreducible quintuple. The latter can have blue defects, but those defects have singleton/pair birth and are repaired when the full quintuple is selected. JSON records every surviving triple and its total/genuinely-new seven counts.

## Finite sufficiency proof, not just final-output prediction

Suppose a disjoint selected coalition satisfies all compiled lower-order rules but has a final independent seven I. By the general bounded-birth lemma, I is born in a minimal selected subcollection of at most three switches.
-If born in one or two, its compiled rule requires a selected added edge inside I, contradicting final independence.
-If born in three, that triple either was ruled out by a sound unit-propagation contradiction, or is one of the28 surviving triples. In the second case no such genuinely triple-born I exists.
Contradiction. Thus the compiled systems are sufficient for ALL disjoint coalitions in this finite candidate domain, without enumerating their larger final graphs.

This answers the redundancy mechanism: lower-order repair requirements plus support incompatibilities PREEMPT higher-order defect formation. It is not that every triple-born obstruction has a nearby individually visible cousin (that earlier conjecture was refuted), nor that a separate triple repair law has been added.

Scope remains explicit: compilation of lower-order defects and verification of the28 survivors are finite computations on the ten regular catalogue types, and the candidates are individually invalid triangle-free switches. We have not derived the whole rule system from order/degree hypotheses alone. The next structural proof target is why dangerous triples always force contradictory repair demands, ideally by a bounded set of reusable implication patterns rather than46,692 individual propagation checks.
