# 968 — The Loaded Corner Determinant Defines an Integral Gauge Class

## Gauge questions from Entry 967

The loaded comparison representative contains two choices that must not be
mistaken for physical data:

1. residue orientations of its six source columns;
2. the coefficient of the already-hit endpoint added to either circuit
   column.

It also admits apparently longer paths in the active chamber graph.  Test
these three ambiguities separately.

## Orientations and endpoint additions

Changing a source-column orientation is right multiplication by a diagonal
matrix with entries \(\pm1\).  It is therefore an integral unimodular source
gauge.

For a circuit column

\[
e_{m missing}-e_{m hit},
\]

changing the hit-endpoint coefficient by any \(k\in\mathbb Z\) is left
multiplication by an integral target-row shear.  The row being added is zero
on every other relevant pivot column, so the operation has determinant one.

Consequently every integral orientation and endpoint choice has the same
determinant up to sign.  The checker verifies all \(64\) source orientations
and endpoint coefficients \(-4\leq k_{24},k_{34}\leq4\), totaling \(5184\)
independent cases; every skeleton determinant has absolute value one.

## Path selection by frozen support

On the \(X=1\) branch, the direct loaded paths are

\[
123456\to124356
\quad\leadsto\quad A_3B_{34}/Z,
\]

\[
132456\to134256
\quad\leadsto\quad ZA_2B_{24}.
\]

The only longer active alternatives continue to an additional occupied
chamber and carry

\[
A_3B_{34}B_{24}/Z,
\qquad
ZA_2B_{24}B_{34}.
\]

Neither monomial occurs in the frozen composite Fitting support.  Such paths
would introduce new resonance divisors and are therefore excluded by the
predeclared source-support test.

## Narrow conclusion

\[
\boxed{
\text{Entry 967's determinant is an integral gauge-class invariant, and
source support uniquely selects its two direct circuit paths.}
}
\]

The comparison remains a gauge class rather than a distinguished matrix,
which is the correct type.  No new carrier cell and no fitted support summand
has been used.

## Next falsifier

Compare this loaded gauge class with the frozen dense-to-block source
transition.  Work through invariant data:

- determinant divisor and valuations;
- localization at each composite wall;
- rank-one residue/image lines;
- compatibility with the pair-shift character blocks.

Do not compare raw matrix entries until a common basis gauge has been
derived.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_loaded_corner_gauge.rs`;
- packet:
  `research/benincasa/string-six-point-loaded-corner-gauge.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_loaded_corner_gauge`;
- allocator claim:
  `seqclaim-fdf3877c9008007969c0cb6f`.
- epistemic event:
  `ev-000000000585-c056293e-a15d-42c1-9eef-91ff3c934163`.
