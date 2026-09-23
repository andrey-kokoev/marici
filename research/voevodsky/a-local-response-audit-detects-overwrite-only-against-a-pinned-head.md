# A local response audit detects overwrite only against a pinned head

A SYNTHETIC event sequence prepared -> receipt -> proof-use denial -> later revision is hash-linked through exact parent IDs and request digest. Fresh `check_synthetic_response_audit.py` rejects changing the denial to allow against a pinned original head (`AUDIT_PINNED_HEAD_MISMATCH`) and rejects removing the denial while leaving the revision parent unchanged (`AUDIT_PARENT_MISMATCH`). The original event list remains intact in this local test; no real owner response was received.

If an adversary can rewrite BOTH the chain and its locally stored head, this checker cannot detect the rewrite. Durable tamper evidence needs an independently anchored head, trusted timestamp/signature and admissible source-event chain. Even an anchored log would prove record integrity, not by itself that the fictional response signer owns the Farkas primitive rows or grants proof use. Epistemic graph transitions remain coordination evidence, not issuer signatures.

Next test an AUDIT FORK where two children share the same denial parent: separate pinned branch heads cannot establish which policy branch is source-owned. Require explicit authorized merge or conflict state rather than interpreting append-only log order as publication permission. Analytic S,A,R,C,G correspondence remains deferred.
