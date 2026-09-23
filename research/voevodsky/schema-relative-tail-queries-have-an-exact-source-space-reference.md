# Schema-relative tail queries have an exact source-space reference

## Delivered gate

A separate research reference backend now handles variable audit coordinates, not only fixed pins. Its schema is (U,V,(x_j) for j in A). Retained rational linear frames and objectives in those coordinates are pulled back to the original finite atom-cap box. The backend supports state-relative point membership, optimization and emptiness with exact rational source-space certificates.

It does not modify the owning Nima API, authenticate observations or introduce a scalable generator optimizer. Source admission is inherited as a mathematical assumption from the owning tail model; this run does not freshly replay its upstream admission proof.

## Schema extension and evidence

Extending A to B containing A inserts zero coefficients for newly exposed coordinates in every old frame. Thus every old source-space inequality is exactly unchanged. Merely extending the schema does not narrow the source set. Additional accepted linear frames may then constrain variable audited coordinates and mix them with U,V.

Controls retain U<=5, extend from the two-moment schema to audits {0,m-1}, then append x_0>=2 and U+x_(m-1)<=6. These are variable audits, not externally fixed values. A final frame x_0<=1 makes the state inconsistent. Tests optimize U, V and x_0-x_(m-1), and test both a feasible and an excluded joint point. Pure schema extension preserves the old objective values.

## Exact solver and certificates

The reference solver enumerates all full-rank active sets of size m, solves them by rational Gaussian elimination, and checks source feasibility. Bounded nonempty rational polytopes have vertices even when the feasible affine dimension is smaller than m; active source rows still span the ambient dimension at a vertex.

For an optimum it enumerates conic combinations of active normals with at most m nonzero weights until it obtains the objective, returning the source point and matching bound. For an empty system it enumerates augmented-row combinations with at most m+1 weights giving (0,...,0,-1), an exact Farkas certificate. Membership appends both inequality orientations for each specified observable equality and solves with zero objective. An empty membership intersection excludes the point; it does not claim the original state is empty.

The executable reference assumes well-formed internal inputs. It is not a validated public API or hardened service. Enumeration is deliberately exponential/combinatorial and limited here to m=3,4. All source caps and translated frame rows are materialized; no visible-image facet projection is needed. This is the correctness reference against which a later generative backend can be compared, not a constant-memory achievement.

## Independent verification

The verifier imports neither the producer nor its solver. It independently constructs the expected schemas, histories and requests, translates source rows, checks every primal coordinate and row, and verifies dual/Farkas sums exactly. State and request are compared against those independent expected statements, not accepted from the response as their own authority.

All 22 certificates passed. Deliberate altered-history, changed-query, invalid-source-witness and corrupted-dual attacks were rejected. Known feasibility statuses are independently asserted for the controlled workload. Assertions must remain enabled; the verifier rejects optimized Python execution.

## Structural significance

The refinement-closure theorem now has an executable source-space instance beyond the original two-observable API. Richer linear audits do not destroy exact certified query completeness. They increase source-space solving and verification costs and require schema-aware statement binding.

The outstanding target is representation efficiency: replace exhaustive source-space enumeration with a verified generative or other scalable backend while preserving precisely the same denotation, expected-history boundary and certificate semantics. The existence of this reference does not establish a 2m projected-cut bound for the enlarged observation or permit arbitrary witness transport.

## Reproduction

    python research/voevodsky/checkers/check_schema_relative_tail_lp.py
    python research/voevodsky/checkers/verify_schema_relative_tail_lp.py

Artifacts:

- `results/schema-relative-tail-lp.json`
- `results/schema-relative-tail-lp-verification.json`
