# Reverted row math requires new comparison edge endpoints

Fresh `check_reversion_comparison_edge.py` rechecks on hypothetical restored g3 rows two exact x<=2 packets: P-g3=(0,1,0,0),surplus1 and Q-g3=(1,2,0,0),surplus0. A newly labelled `comparison@1` edge between these fresh g3 IDs passes local endpoint validity, exact same target, and generation. Carrying g1 endpoint IDs into a g3 edge fails `STALE_ENDPOINT_ID`; carrying an edge labelled generation1 fails `STALE_EDGE_GENERATION`, even though g1/g3 row bytes coincide.

The edge is only a local mathematical recheck; no actual source edit, observed comparison event or issuer grant. Analytic S,A,R,C,G mapping deferred.

Next test TRANSACTION ROLLBACK when a reversion candidate correctly rechecks P-g3 but includes an invalid Q-g3 or stale edge: none of its new g3 catalogue should be partially admitted, and the pre-reversion g2 state must stay intact.
