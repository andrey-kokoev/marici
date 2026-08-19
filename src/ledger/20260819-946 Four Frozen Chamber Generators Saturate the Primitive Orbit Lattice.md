# 946 — Four Frozen Chamber Generators Saturate the Primitive Orbit Lattice

## Source provenance

Entry 929 established that the frozen six-point packet contains six labelled
word/chamber generators.  It lacks their parameter connection, but the
labelled combinatorial lattice itself is source data.

Entry 945's finite quotient therefore asks whether these pre-existing chamber
generators saturate the two-sheet shift-orbit sublattice.

## Exact augmentation census

Adjoin subsets of the six standard labelled chamber columns to the primitive
two-seed orbit matrix and recompute all determinantal divisors.

No subset of at most three chamber columns makes every Smith invariant a
unit.  Several subsets of four do.  Therefore

\[
\boxed{
\min\#\{\text{labelled chamber lifts needed for saturation}\}=4.
}
\]

After adjoining any of the recorded saturating four-subsets, the Smith form
is

\[
(1,1,1,1,1,1).
\]

## Interpretation

The quotient

\[
(\mathbb Z/2)^3\oplus\mathbb Z/4

\]

is not intrinsic torsion of the full frozen algebraic source lattice.  It is
the finite failure of the two physical sheet seeds and their shift orbits to
generate the already available chamber lattice.

Thus the corrected architecture is

\[
\boxed{
L_{\rm orbit}\subsetneq L_{\rm chamber},
\qquad
[L_{\rm chamber}:L_{\rm orbit}]=32
}
\]

for the primitive normalized model, with four independently labelled chamber
directions required to witness saturation.

This does not provide the missing parameter connection from Entry 929, and it
does not identify the chamber lattice with a physical integral Betti local
system.  It establishes only the source-normalized algebraic lattice.

## Consequence for carrier versus coefficients

No new carrier or new coefficient torsion is required by the two-primary
quotient.  The necessary saturation vectors are already frozen source labels.
What remains coefficient-theoretic is their transport and comparison with
actual twisted cycles.

## Next falsifier

Construct the logarithmic-insertion enlargement required by Entry 929 and
test whether its connection preserves (L_{\rm chamber}) over the integral
group ring.  Independently compare the six labelled chambers with a twisted
Betti basis; failure of integral comparison would relocate the defect from
the algebraic source lattice to the de Rham--Betti comparison.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_orbit_two_primary.rs`;
- packet:
  `research/benincasa/string-six-point-orbit-two-primary.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_orbit_two_primary`;
- allocator claim:
  `seqclaim-78dc9919acb99237f009a26a`.
- epistemic event:
  `ev-000000000563-7b20bbfe-1eaa-4abe-ad7a-ba9eeb6b8db5`.
