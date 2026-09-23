# Incremental proof invalidation must index endpoint supports, not just signed deltas

For chosen packets P, Q, single and comparison edge P->Q, index each row to its incident PACKET supports and each comparison edge to the UNION of its endpoint supports. Fresh `check_mixed_row_dependency_index.py` reports x-low -> P and edge; x-high -> P,Q,single and edge; y-low/y-high -> Q and edge. Editing both upper rows invalidates all three packets and the comparison for RECHECK, even though the signed comparison's aggregate bound perturbation is zero. Invalidation is conservative: it does not say every rechecked packet ultimately fails, only that a cached answer cannot be reused without checking.

Separately, a complete source-manifest publication scope changes on ANY row edit, including edits of rows unused by a selected packet. There is no real issuer grant now, and the local support index cannot mint one. This closes the bounded incremental row-checking audit: row-local math dependencies and all-row authority scope are separate.

A nonredundant successor should test a SOURCE-EDIT TRANSACTION with one allowed and one rejected changed row: when one mathematical packet fails, rollback must preserve the old manifest/proof catalogue as a coherent frozen version rather than mixing old cached rows with new proof checks. Publication stays blocked; analytic S,A,R,C,G deferred.
