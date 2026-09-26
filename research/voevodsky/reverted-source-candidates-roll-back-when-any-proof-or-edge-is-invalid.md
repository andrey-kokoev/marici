# Reverted source candidates roll back when any proof or edge is invalid

Fresh `check_reversion_atomic_rollback.py` stages an IN-MEMORY g3 return to y-upper1 from current g2 y-upper2. If Q has invalid negative surplus or the edge still carries generation2, the whole candidate is rejected; the exact original g2 state/digest, source rows, packet IDs and edge IDs remain unchanged. A candidate with locally consistent g3 packet arithmetic and fresh edge generation produces a separate g3 state without overwriting g2.

This checker is a simplified atomicity fixture, NOT a full standalone Farkas proof checker or actual persisted edit. It neither validates a historical comparison event nor supplies an issuer grant. Analytic S,A,R,C,G deferred.

Next test IDEMPOTENT REVERSION CANDIDATE IDs: retrying an accepted local g3 candidate should return the same generation and catalogue without accidentally advancing g4; reusing its ID with different candidate content must fail as a conflict.
