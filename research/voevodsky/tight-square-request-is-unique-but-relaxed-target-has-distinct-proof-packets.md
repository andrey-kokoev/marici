# Tight square request is unique but relaxed target has distinct proof packets

The prior frozen request uses the TIGHT target `x<=1`. On the four square rows, any nonnegative Farkas packet for normal (1,0) has x-upper multiplier `1+a` when x-lower multiplier is a, and paired y multipliers d. Exact bound 1 forces `a+d+surplus=0`, hence a=d=surplus=0. Thus that original target has ONE exact nonnegative packet; inventing a different certificate for it would be false.

A DIFFERENT, relaxed local target `x<=2` does exhibit two packets: P=(0,1,0,0;surplus1) and Q=(1,2,0,0;surplus0). Both prove normal (1,0), bound 2, but hash differently. Fresh `check_equivalent_packet_request_scope.py` refuses Q against a separate exact-P request as `EQUIVALENT_PACKET_NOT_COVERED`. A hypothetical `EXPLICIT_TARGET_ONLY` rule could match Q mathematically, but yields only TEST-ONLY target match and is not a real grant. The original frozen request remains unchanged and unauthorized.

Next test a target-scoped request's QUANTIFIER boundary: authorizing one target statement does not automatically authorize all stronger/weaker bounds or arbitrary proof derivations under source edits; state a precise predicate for a future hypothetical target-only grant and refuse changed normal, bound and source manifest. Source owner and analytic S,A,R,C,G correspondence remain unresolved.
