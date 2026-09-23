# A local source candidate needs proof and edge catalogue closure

Fresh `check_candidate_catalogue_closure.py` checks a synthetic generation-2 square with x-upper=2 and y-upper=2. New P proves x<=2 with surplus0; new Q proves x<=3 with surplus1; an explicit typed P->Q bound-weakening edge checks the same source/generation, endpoint IDs, common normal and surplus increment. Together these form `LOCAL_CLOSED_CANDIDATE_NOT_AUTHORIZED`. Omit Q and the edge has a missing endpoint; set Q surplus0 and its packet is invalid; carry an old-generation edge and it is stale. Each invalid candidate is refused as a whole.

This models in-memory catalogue closure only, not an owner-issued migration or historical occurrence. Analytic S,A,R,C,G remains deferred.

Next test a COMPARISON edge in the same catalogue where both proof endpoints are valid on the new source but target bounds differ: generic endpoint closure cannot replace edge-specific type checks. Require comparison equality of exact targets rather than weakening's ordered bounds.
