# Source quadratic composition is multidimensional before a Clifford quotient

## Question

Can the actual source ideal support a rank-one symmetric law ab+ba=2B(a,b)omega in I^2/I^3? Freeze the source recorder ideal and typed path multiplication independently of this candidate.

## Exact obstruction

Use zero-mark two-event recorder relations r_ij=[i,j]-[j,i]. For the three pair partitions of events {0,1,2,3}, form

    r_01 r_23, r_02 r_13, r_03 r_12.

Each relation is anchored at the appropriate corner for its position in the product. These three four-event products are linearly independent. All six ordered products (including exchanged blocks, reanchored at their new corners) are bound to columns of the actual exported J1 source-I^2 presentation by exact rational coordinate reconstruction.

The explicitly reanchored symmetric sums

    r_01 r_23 + r_23 r_01,
    r_02 r_13 + r_13 r_02,
    r_03 r_12 + r_12 r_03

also have exact rank three. Their path supports are independent; the checker verifies rank directly.

The independent recorder confirms absence of zero- and one-event ideal components. Thus I^3 has minimum event length six and vanishes on this four-event corner. The rank-three witnesses remain independent in I^2/I^3. No single omega spans them.

## Typed meaning of symmetry and square

For fixed typed arrows x:0->3 and y:3->15, xy is nonzero while yx is zero in the total path algebra because endpoints mismatch. Already these typed anticommutators, using the three intermediate corners above, give independent second-degree outputs. Exchanging event blocks requires explicitly reanchored copies, as used in the symmetric test; it is not an untyped interchange of the same arrows.

A single off-diagonal homogeneous corner element squares to zero. A sum of compatible corner elements can have a nonzero square: a=x+y satisfies a^2=xy and a^3=0. These identities are checked using typed multiplication. Therefore a square can represent an element of I^2 without identifying that element with the whole ideal square.

## Structural result

The source's quadratic layer records several distinct compositions, even within one outer corner. A vector-valued symmetric pairing is natural at this level. A scalar Clifford law would require an additional quotient or representation justified by the source/observer contract.

The test refutes the proposed fixed-line law in the source associated graded. It does not rule out all Clifford representations, a central-valued generalized quadratic form, or an observer that intentionally collapses some of these distinctions. Nor does it identify source nilpotence with a physical time quantum.

## Reproduction

    python research/voevodsky/checkers/check_source_quadratic_clifford_candidate.py

Artifacts:

- `results/source-quadratic-clifford-contract.json`
- `results/source-quadratic-clifford.json`

The checker verifies input bindings and exact product membership using the existing full presentation; it does not rebuild that entire presentation.
