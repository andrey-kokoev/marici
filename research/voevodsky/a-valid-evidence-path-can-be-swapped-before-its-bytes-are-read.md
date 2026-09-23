# A valid evidence path can be swapped before its bytes are read

A local synthetic two-stage model validates an evidence path, then reads its bytes. If the file contents change between these steps, path validation alone cannot guarantee the attachment; fresh `check_evidence_file_swap_model.py` detects the changed bytes as a hash mismatch against the frozen payload. Attaching an already-captured immutable byte snapshot and verifying its digest avoids THIS local content-change race. No physical evidence files were altered.

A same-byte copy from a different physical origin has the SAME digest, so content addressing alone cannot prove path/source provenance; a production implementation needs trusted root binding plus an atomic safe-open/descriptor or immutable object store. This checker does not implement OS-level race freedom and does not authenticate any row publisher. The unsent owner payload remains `LOCAL_PREPARED_UNSENDABLE`.

The bounded unsent-handoff payload branch is complete: exact request/evidence hashes, route-null status, path binding and content-swap limits are explicit. A nonredundant successor can examine a HANDOFF ACKNOWLEDGEMENT state machine with synthetic acknowledgements: mere delivery or receipt must not be mistaken for owner attestation, and current absent recipient keeps all transitions unsendable. Analytic S,A,R,C,G remains deferred.
