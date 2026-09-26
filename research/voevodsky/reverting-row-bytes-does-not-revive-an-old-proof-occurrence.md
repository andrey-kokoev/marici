# Reverting row bytes does not revive an old proof occurrence

Fresh `check_source_reversion_catalogue.py` stages three IN-MEMORY square row generations: g1 y-upper1, g2 y-upper2, g3 y-upper1 restored. The exact ordered matrix digest at g3 equals g1, and the simple x<=2 x-upper packet is freshly checked at g3, but generation and packet/edge occurrence IDs differ. No issuer is present at ANY generation, so restoring bytes inherits no publication grant.

Important scope: this checker RECHECKS a proof packet, but merely gives fresh edge IDs; it does NOT validate edge semantics or establish complete catalogue closure. No persistent source edit occurred. Analytic S,A,R,C,G remains deferred.

Next test the REVERTED CATALOGUE edge: create two fresh g3 valid target packets and validate the new same-target comparison under g3. Reject copying the g1 edge endpoints even when their mathematical packets are byte-identical.
