# One-to-one witnesses for the hidden 44-item layer

## Question and rule

Can the 126-item outer layer assign a distinct shared-face witness to each of
44 hidden inner items, leaving 82 available outer items?

User layers 3 and 4 correspond to construction layers 2 and 3 (zero-based).
An item is one regular tetrahedron or one four-tetrahedron octahedral group.
Each outer item has capacity ONE regardless of constituent count. This is a
stated modeling assumption, not a consequence of equal physical capacities.

## Test

`checkers/check_surface_witness_matching.mjs` derives item adjacency directly
from exact shared triangular faces of the constituent cells, discarding faces
internal to an octahedral group. It solves bipartite maximum matching and
independently checks cardinality using unit-capacity augmenting-path max flow.
The saved assignment includes the shared-face coordinates for every pair.

## Result

- 44 inner items; 126 outer items.
- 52 outer items share an eligible face with the inner layer.
- Inner degrees: six items have 2 eligible neighbors, sixteen have 3, twenty-two
  have 4.
- Matching cardinality: **44**, independently confirmed by max flow.
- All inner items have distinct witnesses. No Hall obstruction exists.
- **82 outer items remain unused**: 74 regular tetrahedra and 8 octahedral groups.
  The 44 assigned witnesses are octahedral groups.

This proves feasibility of the specified finite incidence/capacity rule. It
neither establishes a unique witness assignment nor proves that witnesses
must consume capacity in a physical realization. In particular, it does not
derive protons, neutrons, a nuclear binding mechanism, or a lead-208 limit.
A different witness relation or capacity per constituent tetrahedron would be
a different model and would require a separate calculation.

## Evidence

Run `node research/strominger/checkers/check_surface_witness_matching.mjs`.
The complete matching, adjacency, unused items, and geometry source hashes are
in `results/surface-witness-matching/verification.json`.
