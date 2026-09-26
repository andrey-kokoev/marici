# Source oracle detects a shared manifest/runtime defect

Fresh isolated-copy experiment swaps GS's fuel/cursor boundary roles in both `scanning_set_program.py` and the hand-declared GS template. The swap preserves every port, kind and allocation witness. The trace producer recomputes the changed contract digest, so this is not a stale-hash or production/template mismatch test.

The clean source-comparison baseline passes. Under the shared mutation, all57 complete certificate fixtures still pass, demonstrating why certificate consistency alone is insufficient semantic evidence. The replay/source comparison then fails precisely at `result['terminal']==interpret(bits,ops)`, after replay has accepted the trace. The traceback was freshly read and identifies that oracle assertion, not a syntax/import failure. Temporary sources/results are isolated; all production source hashes remain unchanged.

This is one representative semantic fault, not exhaustive sensitivity or an independently reviewed interpreter. It validates the purpose of the separate direct source semantics layer and makes the trust boundary concrete: a consistent declarative rule system may implement the wrong source language.

Next consolidate the audit chain into a review-ready assurance statement distinguishing structural recognition, legal trace replay, source-result agreement, confluence and authenticated provenance. Include reproducible commands and explicitly mark that the semantic oracle comparison is currently a checker, not a default replay acceptance condition. Decide whether to offer a separate semantic replay command rather than silently strengthening structural replay. No new instruction feature is needed.
