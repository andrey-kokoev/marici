# Adjoint-denominator composition cancellation: Lean packet

Source: `research/grothendieck/adjoint-denominator-composition-cancellation.md`
(epistemic-graph event 1355).

The formal coefficient type is `ℚ`; clearing denominators are integers. Lean
defines `ClearsRationalDenominator L q` by the existence of an integer `z`
with `L*q=z`. `LeastRationalDenominator L q` explicitly carries positivity,
clearing, and the universal property that `L` divides every integer clearer.
No rational-normal-form implementation is silently identified with this
mathematical specification.

`clearsRationalDenominator_mul` proves that clearers multiply under scalar
composition. `leastRationalDenominator_mul_dvd` then proves that the least
denominator of a composite divides the product of the two stage denominators.

The executable rank-one fixture sets

\[
S_q=\frac23,\qquad S_r=\frac32.
\]

It proves that `3` clears `S_q`, `2` clears `S_r`, neither is cleared by `1`,
and proves directly from the universal divisibility specification that their
least positive denominators are respectively `3` and `2`. But `S_r S_q=1`
has least denominator `1`. Thus terminal integrality cannot reconstruct stage
integrality.

This does not yet formalize higher-rank pairing lattices, uniqueness of the
adjoint from nondegenerate pairings, least common denominators of rational
matrices, Smith normal form, localization-prime support, or the independent
boundary-defect channel. Those require the named lattice maps and matrices
from each five-site specialization. The scalar theorem is arithmetic and
does not manufacture those source objects.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans are run, and this module remains outside
`MariciFormal.lean`.
