# Verified scalar bands now return original-atom approximate lifts

## Composition delivered

Nima's independent whole-polygon scalar verifier now gates a process-local approximate-section service. The caller supplies an expected n/eta contract independently of the candidate packet. Bootstrap checks all scalar cells, coverage, continuity and envelope bounds, then checks the admitted source cube and exact original-metric direction.

The expected contract fixes the owning m=4 moment-curve two-history family, epsilon=16513*128^-4*eta, exact public moments and atom caps, approximate lifting only, and no archival re-exposure. This is a fixed-family composition, NOT an arbitrary migration compiler or an added backend language in Nima's checkpoint service.

## Original-atom answers

For an admitted point the service locates all containing verified cells and requires their affine values to agree. It clamps that value to [0,1] and applies the source inverse. The answer also contains one witness from each ORIGINAL history fiber at the same public point: the nearest scalar point in [f,1] and in [0,g].

A separate answer verifier imports no section adapter or candidate constructor. It directly checks the independently expected state and point, original source caps, exact original public moments, both history witnesses, and infinity-norm distance from the returned source vector to EACH witness. It reconstructs the scalar envelopes using Nima's independent envelope code. Thus approximate compatibility is not inferred from a producer's distance claim or mistaken for an exact common filling.

## Checkpoint reuse

The session owns an immutable copy of the successfully checked whole-polygon section. Only append-public restrictions are supported. The successor is reconstructed internally from the expected predecessor and supplied operation; there is no candidate section replacement, serialized-checkpoint import or tolerance-changing operation.

Restriction preserves the same section on the domain intersection. No old plane/vertex arithmetic or pairwise cell geometry needs replay: coverage and continuity restrict automatically. Query-time domain, new-frame and cell-location checks still run. The service reuses the admitted whole section, not independently addressable local blocks. A future coefficient change would require fresh bootstrap in a new session.

Caller mutations to the original candidate and returned receipt do not affect the trusted snapshot. Stale handles, fine refinements and archive requests fail. This remains a trusted-process service, not a hostile-memory security boundary.

## Results

Two n=18 packets, eta=1/1000 and eta=1/100, pass bootstrap and public restriction. They retain eight and three verified cells respectively. Fresh whole-polygon replay checks 1024 and 704 plane/vertex obligations; successor restriction replays zero such obligations. These counters do not include scalar geometry work, envelope reconstruction, point location, hashes or per-answer arithmetic.

Original-atom answers pass the independent checker at all eighteen original public vertices, an interior centroid, and that centroid after restriction. Fourteen refusals cover corrupted scalar coefficients, stale handles, excluded points, hidden fine refinements, archive requests, corrupted atom answers and stale answer statements.

Nima's independent archived verifier was also freshly rerun: all thirty whole-polygon certificates passed.

## Costs and remaining limits

Receipts record live state and full section encodings separately. They are not a complete heap or restart-archive ledger. Per-answer history witnesses are additional proof data in the result, and the implementation currently reconstructs scalar envelopes to produce them; that work has NOT been optimized away by the checkpoint.

This closes the scalar-to-source answer composition for the fixed family and makes safe restriction reuse executable. It does not deliver an exact fiber archive, arbitrary-policy transitions, a general migration-bound approximate section attachment, or optimal verification complexity. Nima's matching-order cell bound and our lower bound still concern representation complexity, not total storage or runtime.

## Reproduction

    python research/voevodsky/checkers/check_approximate_section_checkpoint.py
    python research/nima/checkers/verify_scalar_envelope_band.py

Implementation: `checkers/approximate_section_checkpoint.py`.

Independent answer verifier: `checkers/verify_approximate_atom_lift.py`.

Artifact: `results/approximate-section-checkpoint.json`.
