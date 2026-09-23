# A staged source edit must rollback unless its whole proof catalogue validates

Stage the y-upper bound edit from 1 to 2 IN MEMORY. If the required catalogue still contains original P,Q,single packets, Q fails the x<=2 target, so the entire candidate is rejected and the old immutable row version, catalogue and digest remain intact. If the candidate explicitly REBUILDS Q with a new x-upper one-row proof plus surplus 1, all staged packets pass local mathematics and a new in-memory version can be committed; the old version is not overwritten. Repeating the same accepted candidate ID is idempotent. Fresh `check_local_source_edit_transaction.py` verifies each case.

This is NOT an authorized source edit or publication: the checker persists only a result report, not a modified row source or real grant. An accepted mathematical catalogue at version 2 cannot inherit a version-1 source issuer identity, and comparison histories must be explicitly rebuilt rather than copied. Actual Farkas owner still unknown, analytic S,A,R,C,G map deferred.

Next test two concurrent staged candidates from the SAME old math generation with conflicting row changes. A version-compare-and-swap must accept at most one; retry of the losing candidate needs a new proof validation on the winner's source, not silent last-writer-wins.
