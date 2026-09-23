# A mixed opened trace has only partial occurrence replay

For a synthetic three-edge chain A->B->C->D, the B occurrence commitment is correctly opened and the C commitment is merely repeated across adjacent edge fields. Fresh `check_mixed_opened_trace_chain.py` returns `LOCAL_OCCURRENCE_CHECKED` for the B join and `COMMITMENT_LINK_ONLY` for C; a wrong B-as-C opening fails. The full occurrence-level chain therefore remains `UNVERIFIABLE_TRACE` at C. Mathematical packet signed deltas still telescope all the way back to zero for A=D: that endpoint equation cannot disclose C.

This is deliberately a VECTOR of local statuses, not one misleading global 'verified' bit. Local digest checking is weaker still than attested historical execution: neither B's disclosed ID nor C's opaque commitment authenticates source/effect issuer authority. Only actual separately authorized event evidence could make a publication or replay claim.

Next test selective disclosure across TWO alternative paths sharing the same C commitment but differing at an earlier opaque event. Check whether a common commitment entails common path identity (no), and require each path's source/target trace hashes before comparing observational histories. Analytic S,A,R,C,G remains deferred.
