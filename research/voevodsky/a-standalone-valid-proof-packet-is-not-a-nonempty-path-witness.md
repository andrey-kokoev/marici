# A standalone valid proof packet is not a nonempty path witness

Fresh `check_packet_vs_nonempty_path_witness.py` verifies a local unit-square x<=2 certificate at a synthetic terminal occurrence. A claim of a path from a DISTINCT synthetic start with zero edges fails `NO_NONEMPTY_PATH_WITNESS`; adding a connected versioned edge reaches only `SYNTHETIC_PATH_SHAPE_ONLY` because no endpoint packet rule semantics or actual event provenance has been validated. A broken start edge fails separately.

Standalone proof math, a syntactically connected path, and an observed authorized derivation are different claims. No row issuer or analytic S,A,R,C,G mapping is supplied.

Next test a ZERO-LENGTH identity path where start=end: its reflexive structural identity can be valid without edges, but must be explicitly labelled identity rather than a nonempty derivation, and cannot supply missing observed source occurrence.
