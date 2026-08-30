# 3261 — Three Exact Fibers Support the Rank-Twelve Candidate but Do Not Prove It Globally

## Hostile replication

Entry 3259 established exact source normalization of the final (4\times3) marked-relative extension block at one generic fiber. The same section-independent calculation has now been repeated at

\[
(u,v)=(7,11),\qquad(8,13),\qquad(11,7).
\]

For each point and each derivative direction, the complete 132-row, 372-column pre-elimination source presentation was evaluated at two independent primes. The residues were combined by the Chinese remainder theorem before rational reconstruction. This is necessary because some exact integer coefficients at the new fibers exceed the single-prime square-root reconstruction window.

Exact row reduction over \(\mathbb Q\) then showed at every fiber that coordinates

\[
z_8,z_9,z_{10},z_{11}
\]

are independent of all free primitive coordinates. All 72 resulting values agree with the characteristic-zero candidate.

## Degree-bound audit

The existing source-derived Cramer bounds are

\[
\deg D\le1063,
\qquad
\deg N\le1070.
\]

They are valid formal bounds, but they make naive bivariate uniqueness interpolation computationally and conceptually poor. Three exact fibers are strong hostile replication; they do not determine a rational function within that enormous class.

## Narrow conclusion

The candidate has survived three independent exact characteristic-zero source fibers, including asymmetric points and both derivative directions. No primitive-section ambiguity appears in the final block at any tested fiber.

The global source identity remains unproved. It must not be inferred from the 72 agreements.

## Next falsifier

Derive a sharper uniqueness mechanism from the structure of the source module. Admissible routes include:

1. a source-derived low-degree dual certificate for the four fixed coordinates;
2. a minimal-minor or determinantal cancellation theorem reducing the Cramer bounds;
3. a rigidity theorem for the extension cocycle modulo regular triangular gauge.

Do not replace this missing theorem by accumulating an arbitrary number of fibers.

## Artifacts

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`
- `research/benincasa/checkers/certify_marked_extension_exact_point.py`
- `research/benincasa/results/marked_extension_exact_point_certificate.json`
