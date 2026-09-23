# An unsent owner payload must be refreshed if evidence bytes drift

The prepared local Farkas handoff payload's frozen request digest and three evidence file hashes currently match the files in `research/voevodsky/results/`. Fresh `check_unsent_payload_evidence_drift.py` then simulates a one-byte change to ONE evidence item, without changing any physical evidence file, and rejects it as `EVIDENCE_DIGEST_DRIFT`; a simulated change to the frozen request yields `FROZEN_REQUEST_DRIFT`. Current hashes alone give `LOCAL_REFERENCES_CURRENT_STILL_UNSENDABLE`, since the owner route is unassigned.

A future exact evidence-bearing request must regenerate or explicitly reapprove its payload after any byte drift. A hash verifies local integrity against frozen bytes, not source truth, trustworthy ownership or atomic storage. Even with current hashes, no authorized recipient, source event or generation is present and no owner message is sent.

Next test PATH REBIND: a payload containing only relative evidence paths and byte hashes may be copied to a different workspace or mapped through a symlink. Require fixed project-root/scope identity and resolve paths without traversal before using the payload; do not treat file-path safety as publication authority. Analytic S,A,R,C,G remains deferred.
