# 945 — The Primitive Two-Seed Orbit Model Has Smith Index Thirty-Two

## Exact finite calculation

Entry 944 proves the basis-independent lower bound (16mid[L_{\rm
sat}:L_{\rm orbit}]).  To sharpen it, take the primitive normalized two-seed
model with character multiplicities

\[
(2,1,1,2)
\]

and all four ((\mathbb Z/2)^2) translates of each seed.

The gcds of every (k\times k) minor give the Smith invariants

\[
\boxed{(1,1,2,2,2,4).}
\]

Hence the primitive model has finite quotient

\[
\boxed{
L_{\rm sat}/L_{\rm orbit}
\simeq
(\mathbb Z/2)^3\oplus\mathbb Z/4,
\qquad
[L_{\rm sat}:L_{\rm orbit}]=32.
}
\]

The computation enumerates all minors; it does not infer the Smith form from
the mod-two rank alone.  A rejected provisional guess of index (64) was
removed after the exact minor calculation returned the displayed form.

## Scope qualification

This is exact for the primitive normalized abstract orbit model after
localization away from Entry 943's nonunit kinematic factors.  The explicit
source formulas carry an additional even normalization.  Therefore this
entry does not assert that (32) is the final index of the physical integral
Betti lattice.

What is established is that the two source sheet seeds and their shift orbits
cannot themselves provide an integral saturation.  Additional source-derived
integral cycles would have to kill three order-two classes and one order-four
class.

## Next falsifier

Search the frozen residue and Poincaré-dual source basis for four independent
integral lifts with the required reductions.  Test their images in

\[
(\mathbb Z/2)^3\oplus\mathbb Z/4.
\]

If no such lifts are source-derived, retain this finite quotient as genuine
two-primary coefficient data rather than adjoining saturation vectors.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_orbit_two_primary.rs`;
- packet:
  `research/benincasa/string-six-point-orbit-two-primary.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_orbit_two_primary`;
- allocator claim:
  `seqclaim-189cd3c3730e1a4b083227da`.
- epistemic event:
  `ev-000000000562-64b632e2-9030-43c4-90a3-d57cef8b35c8`.
