# 3259 — The Rank-Twelve Final Block Passes an Exact Generic-Fiber Source-Normalization Gate

## Frozen question

The reconstructed characteristic-zero candidate for the final (4\times3) blocks of the marked-relative connection had passed multiprime held-out evaluations, flatness, infinity-Gysin, and generic quartic-regularity tests. It had not been compared directly with the characteristic-zero source equations.

The bounded gate is:

> At one generic rational base point, do the 24 candidate coordinates equal the coordinates forced by the complete source-normalized Laurent reduction, without selecting a primitive section?

This is a generic-fiber normalization test. It is not a substitute for the uncompleted global polynomial identity in (u,v).

## Exact source presentation

The reduction engine now exports its sparse pre-elimination system

\[
M_{\mu}(u,v)z=r_{\mu,k}(u,v)
\]

before modular row reduction. At

\[
(u,v)=(7,11),
\]

the presentation has 132 rows, 372 primitive coefficients, and rank 117 for both derivatives. Every nonzero coefficient was rationally reconstructed independently modulo

\[
2305843009213693951
\quad\text{and}\quad
2305843009213693921.
\]

The two reconstructed sparse matrices and all six right-hand sides agree exactly after forgetting the prime label.

## Section-independent reduction

Exact row reduction over \(\mathbb Q\) was applied to the three right-hand sides simultaneously for each derivative. The four final-master coordinates

\[
z_8,z_9,z_{10},z_{11}
\]

are fixed by the source system: their reduced rows have no dependence on any of the 255 free primitive coordinates. Thus the test does not choose a sparse, convenient, or quartic-adapted primitive witness.

The resulting 24 rational values agree entrywise with the evaluation of the reconstructed characteristic-zero candidate. The durable packet records all values and the two-prime provenance.

## Narrow result

The candidate final block passes an exact characteristic-zero source-normalization gate on a generic fiber:

\[
B^{\mathrm{candidate}}_{\mu,\mathrm{final}}(7,11)
=
B^{\mathrm{source}}_{\mu,\mathrm{final}}(7,11),
\qquad \mu\in\{u,v\}.
\]

This removes the immediate possibility that the modular candidate arose from an incompatible primitive convention or from the wrong source quotient.

It does not prove the rational-function identity globally. A single fiber cannot determine a bivariate rational matrix without an independently derived uniqueness theorem. Accordingly, prior conclusions that generic \(\mathcal Q\)-support is absent continue to rest on their separate indicial and regularity arguments, not on this gate.

## Artifacts

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`
- `research/benincasa/checkers/certify_marked_extension_exact_point.py`
- `research/benincasa/results/marked_extension_exact_point_certificate.json`

## Next falsifier

Repeat the exact gate at independently chosen generic fibers and derive a finite uniqueness set from source-fixed degree bounds. Only after that derivation may finitely many fiber equalities certify the global candidate. If a new fiber disagrees, reject the candidate immediately; do not change its reconstruction degrees or primitive convention.
