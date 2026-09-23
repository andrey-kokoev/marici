# A closed proof catalogue needs explicit versioned edge-rule labels

Fresh `check_closed_catalogue_rule_versions.py` recognizes ONLY `comparison@1` and `bound-weakening@1`, dispatching respectively to exact same-target and same-normal/weights/surplus-increment checks. Missing, unversioned, unknown future, array-valued or compound labels fail closed as `UNKNOWN_OR_AMBIGUOUS_RULE_VERSION`. Thus a valid packet pair cannot be silently interpreted under a convenient fallback rule.

This fixture verifies rule-label dispatch only, not Farkas endpoint proof correctness, actual audit occurrence, owner-issued source, or analytic S,A,R,C,G map.

Next test a VERSION-UPGRADE attempt: an edge signed/scoped under rule `comparison@1` must not be replayed as `comparison@2` even if implementation currently produces the same Boolean result. Bind exact rule version into the edge digest and require separate explicitly authorized migration when semantics change.
