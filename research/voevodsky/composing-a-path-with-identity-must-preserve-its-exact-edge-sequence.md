# Composing a path with identity must preserve its exact edge sequence

Fresh `check_path_identity_unit_law.py` composes the synthetic one-edge typed path P->Q with identity at P on the left and identity at Q on the right. Both compositions reproduce EXACTLY the same P/Q endpoints and one-edge tuple; neither adds or removes an event. Identity at R on either side fails `COMPOSITION_MIDDLE_ID_MISMATCH`.

This unit law is structural. It does not establish that the edge was observed, its Farkas endpoints verified or its source issued. Analytic S,A,R,C,G remains deferred.

Next test associativity for THREE composable typed edges while retaining their exact ordered edge sequence; mixing a stale source generation in the middle must fail the scoped composition check BEFORE associativity is claimed.
