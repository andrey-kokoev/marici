# Replay terminal summary versus source interpretation

Offline replay now returns terminal={word,observations} derived solely from the validated final graph when completion is claimed; partial traces return terminal=None. The ordered values retain Boolean/scan tags. No claimed terminal payload from the artifact is trusted.

Added `source_interpreter.py`, a direct finite-list algorithm with no graph/rule-manifest/reducer imports. It shares input normalization but implements operation semantics directly, including pre-update ifadd snapshots and fuel-first scan exhaustion. Four literal witnesses distinguish last-fuel insertion, FOUND on the next permitted test, zero-fuel behavior and conditional pre-update results.

Fresh93 serialized/deserialized mixed traces totaling2296 replay steps have terminal summaries exactly equal to the source interpreter. The updated27-suite closure passes. This establishes bounded differential evidence between two algorithms, not independent authorship or formal semantic equivalence. It tests terminal semantics, not intermediate publication timing.

Next assurance priority is a mutation of the declarative rule manifest itself: current certificates and replay agree by construction on that manifest. In an isolated copy, introduce a linear, type-correct semantic defect shared by production and manifest, then check that the direct-source comparison rejects it. This tests the new independent semantic layer rather than merely rechecking a production/manifest mismatch. Keep baseline and changed-source isolation explicit.
