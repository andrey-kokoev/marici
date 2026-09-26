# Path-commitment JSON must reject duplicate claim-kind keys

Fresh `check_strict_path_json_keys.py` passes a JSON object with TWO `kind` keys, `original-identity@1` and `derived-reduction@1`. A permissive last-value parser sees only the latter; a strict duplicate-key hook rejects `DUPLICATE_JSON_KEY` before commitment. Two uniquely keyed, reordered encodings of the same typed original-identity record produce the same canonical digest after strict parsing and sorted-key serialization.

This is a local parsing safety illustration; it does not validate a signature, prove a path occurred or identify a row issuer. Analytic S,A,R,C,G mapping deferred.

Next test UNKNOWN-FIELD smuggling: one verifier ignores an extra `issuer` or `origin` field while another hashes it. Require exact typed field set per claim kind or explicitly versioned extension handling; no implicit authorization from a JSON field.
