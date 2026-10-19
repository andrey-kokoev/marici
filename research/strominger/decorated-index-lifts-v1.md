# Sector-index lifts and directed blocks

## Frozen classification

The carrier is the checked direct sum of four continuous joint-sector spaces,
not a four-value compression. Its complex projector algebra is C^4. Abstract
complex unital algebra automorphisms permute its four primitive idempotents,
giving S4. The present task asks which permutations lift to the represented
36-dimensional field, not whether S4 exists abstractly.

For every permutation sigma of the four indices, require an invertible linear
T with T E_i=E_sigma(i) T. Metric preservation may additionally be required;
identity supplies it in a fixed field. Similarity preserves projector rank.
Check all24 permutations for P and N separately. Since each field's four ranks
are distinct, identity is the only candidate and is realized. This classifies
index images, not all transformations acting within the sectors.

For P-to-N maps, use F_sigma(i) T=T E_i and the same fixed rank test. The only
rank-compatible index matching exchanges10 and01. The previously constructed
metric-unitary PN map realizes it after exchanging L/G roles, as freshly
checked through its exact factor certificate. Requiring the independently
specified geometric C3 action as well excludes that remaining candidate by
the existing universal obstruction. None of these statements identifies P and
N as one fixed decorated object.

## Relation of the two fours

For the P involutions R_L=2L-I and R_G=2G-I, verify

    E_ab = (I+(2a-1)R_L)(I+(2b-1)R_G)/4.

The four sectors are the four character spaces of the represented Klein group;
their multiplicities are1,11,2,22. Group elements and characters are different
types, even though both sets have four members. The geometric A4 and the two
reflections preserve these sectors, so their previously checked48-element
field action induces identity on this index set. Faithful field action need
not give faithful action on the sector indices.

## Directed blocks versus reversibility

Use the actual ordered corner-cycle matrix C, not a new transition rule.
Extract all E_i C E_j blocks (source j, target i), then repeat for C^2. Check
C^3=I and compare the metric adjoint with its inverse. A nonzero off-diagonal
block does not define an invertible whole-sector permutation or a stochastic
transition probability. Directional coarse incidence can coexist with an
invertible full linear map. Do not infer physical unitary evolution from
linear invertibility.

## Scope and next obligation

This classifies the declared index lifts and one source operation's blocks.
It is not a census of every physical symmetry or a proof of external sewing.
A future transition grammar must retain full block amplitudes and composition,
rather than replacing a field operator by an unlabelled reachability graph.

Replay: `python research/strominger/checkers/check_decorated_index_lifts.py`.
Receipt: `results/decorated-index-lifts/verification.json`.
