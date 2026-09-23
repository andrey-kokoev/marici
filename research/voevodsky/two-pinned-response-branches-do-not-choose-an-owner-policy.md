# Two pinned response branches do not choose an owner policy

A FICTIONAL denial has two hypothetical direct child records, one allowing proof use and the other denying it. Their separately pinned child hashes are distinct and both bind the same prior denial. Fresh `check_response_audit_fork.py` reports `PINNED_FORK_UNRESOLVED` irrespective of child order. A synthetic merge object must cite BOTH child IDs; even then matching bytes produce only `TEST_ONLY_MERGE_BYTES_NOT_AUTHORIZED`, not an independently authenticated source-owner resolution.

Append-only integrity and multiple preserved heads are valuable audit properties, but do not answer which issuer action governs. The actual Farkas owner remains unassigned, no request was sent, and no owner response or signed merge exists. Graph chronology or local hash anchoring must not manufacture source policy precedence.

The bounded synthetic-response audit branch is complete: a pinned head detects ordinary overwrites, full local rewrite needs an external anchor, and anchored forks still require source-owned resolution. A nonredundant successor should test MINIMAL MATHEMATICAL CONTINUATION independent of owner: check whether local Farkas proof packets stay verifiable after removal of all fictional communication/audit artifacts, while publication and analytic correspondence remain explicitly blocked.
