# Equal ordered row math does not identify the same row occurrences

Fresh `check_row_matrix_vs_identity_digest.py` holds exact ordered row normals and bounds fixed while renaming each synthetic row occurrence ID. Its matrix-math digest stays equal; a separately versioned row-identity commitment changes. Reordering rows changes even the matrix digest because multiplier coordinates index positions. Thus mathematical proof reuse may be possible across renamed rows, but an occurrence-bound source claim cannot silently reuse the old row identities.

Neither synthetic row ID nor hash authenticates an owner-issued source. Analytic S,A,R,C,G correspondence remains deferred.

Next test DUPLICATE ROWS with distinct IDs: two identical inequalities at different positions yield same mathematics under some multipliers but swapping their row IDs changes a provenance-aware packet. Bind packet multiplier slots to ordered row identities when reporting proof history.
