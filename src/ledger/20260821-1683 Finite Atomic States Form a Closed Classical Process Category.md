# 1683 — Finite Atomic States Form a Closed Classical Process Category

## Process-closure test

Entry 1682 finds finite-dimensional invariant atomic families under classical
scalar-cubic dynamics. Test simultaneous closure under Cut, independent product,
and convex mixture.

For finite supports (A,B) of sizes (N,M):

1. deterministic Hamiltonian evolution is an invertible flow and preserves the
   number of distinct atoms;
2. the independent product has support (A\times B) and at most (NM) atoms;
3. cardinality-weighted linear Cut pushforward maps each product atom to one
   output atom and therefore has at most (NM) atoms;
4. convex mixture has support in (A\cup B) and therefore at most (N+M)
   atoms.

Coincident atoms or coincident Cut images reduce the count.

The exact checker verifies 64 generic product/Cut cases with

\[
1{,}296
\]

distinct product atoms, 64 disjoint convex-mixture cases, and a collision case
in which four product atoms map to three output atoms.

## Narrow result

\[
\boxed{
\text{the union of all finite atomic positive states is closed under the classical process operations.}
}

A fixed-(N) stratum is not monoidally closed:

\[
N\otimes M\leadsto NM,
\qquad
N\oplus M\leadsto N+M
\]

generically. Atom count is a coefficient-complexity grading with collision
specializations, not a fixed carrier arity.

This closure remains classical. Quantum-positive states cannot be identified
with phase-space atoms without an independently defined quantization map.

## Durable artifacts

- `research/benincasa/checkers/finite_atomic_process_category.rs`
- `research/benincasa/results/finite-atomic-process-category.json`
- `research/benincasa/finite-atomic-process-category.md`

## Next falsifier

Test quantization. Determine whether a source-declared finite family of quantum
positive states—coherent-state mixtures, finite-rank density operators, or
another admissible class—is closed under the cubic unitary, Cut channel, and
convex mixture. Do not treat classical atoms as quantum states.
