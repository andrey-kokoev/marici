# An identical Farkas packet can have two distinct occurrence IDs

Two FICTIONAL proof occurrences use exactly the same four-row square x<=2 packet (x-upper multiplier 1, surplus 1). Their canonical packet SHA-256 matches, but their occurrence IDs differ. An edge whose source is occurrence 001 refuses replay with occurrence 002 as `OCCURRENCE_ID_MISMATCH`, even though its math packet digest is equal. Fresh `check_packet_vs_occurrence_id.py` verifies this distinction.

Content addressing identifies a proof MATRIX under a chosen manifest/encoding, not that a particular check actually happened or that two recorded checks are one history. The fixture statuses remain TEST_ONLY_NOT_OBSERVED. Neither synthetic occurrence carries row-source publisher authority, and analytic S,A,R,C,G correspondence remains deferred.

Next test an event DEDUPLICATION cache: reuse packet arithmetic across equal packet digests without deduplicating occurrence-level audit entries or their parent-event dependencies. Reject cached proof math if the source manifest generation changes, even when packet multipliers are identical.
