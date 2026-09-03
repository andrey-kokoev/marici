# Maximal local three-site factorization-incidence audit

## Question

How much of the smallest physical divisor/residue category is already materialized locally, and what is its first absent field?

## Claim boundary

The strongest existing physical object is the three-site connected-subgraph link in `three-site-physical-residue-link.json`. It provides ten named divisor vertices:

- four common vertices `q_G`, `q_g1`, `q_g2`, `q_g3`;
- six cyclic link vertices `q_G12`, `q_g23`, `q_G31`, `q_g12`, `q_G23`, `q_g31`.

It also provides the complete six-cycle of maximal compatible pairs, the source-order residue signs `(-1,+1,-1,+1,-1,+1)`, an oriented fundamental cycle with zero boundary, and the distinction between the contractible full nerve and normal link `C6`. Unlike the two-site spurious corner, this incidence object is compiled from physical connected-subgraph denominators.

`physical_positive_chamber_q_wall_gate.py` supplies exact coefficient vectors for six forms: `q_g1`, `q_g2`, `q_g3`, `q_G12`, `q_g23`, and `q_g31`. It proves these forms are strictly positive on the declared physical chamber, so that chamber's contour does not intersect their divisors.

The bubble packets add exact but different data: eight source arrangement divisors, rank-six residue matrices, exact Kohno flatness on eleven rank-two flats, and a three-dimensional regular boundary space. Their last three walls are source-designated spurious divisors. These data cannot be merged with the three-site physical link merely because both use residues.

## Maximal source-side category

The currently materialized category has:

- objects: ten named three-site physical divisors;
- incidence: six maximal compatible link pairs plus the four common cone vertices;
- one-cells: source-ordered residue operations for the six link edges;
- coherence evidence: the alternating sign cycle has zero simplicial boundary;
- chamber data: coefficient vectors and nonintersection for only six named forms.

It does not yet contain actual residue morphisms as rational forms or period maps. The zero-boundary cycle certifies incidence coherence, not equality of iterated residues or factorization of an integrated observable.

## First missing field

Subsequent local discovery found the complete source-derived linear-form table in `generic_lower_positive_chain_census_result.json`. `check_three_site_q_cyclic_completion.py` verifies all ten rows under the sourced relabelling `a→b→c→a`, `X1→X2→X3→X1`; the physical link rotates by four positions and preserves its residue-sign sequence. The earlier claim that four rows were absent is retracted.

The first missing data are now:

1. exact single-residue maps and their normalization;
2. both sequential residues for every compatible pair;
3. a commuting-order or signed-coherence statement;
4. an explicit incompatible-pair failure;
5. pairing of the physical `C6` residue cycle with the source integration contour or relative chain.

The last item is the existing integrated-observable gate.

## Strongest falsification attempt

The bubble residue matrices might supply the missing residue morphisms. This fails because their eight-divisor arrangement includes three spurious parameter walls and their physical boundary conditions land in degree zero, whereas the three-site physical link is a degree-one `C6` built from connected-subgraph denominators. No source map identifies their objects, residue matrices, or contour classes.

## Disposition

A nontrivial physical incidence category is frozen: all ten three-site divisor rows, the complete `C6` compatibility graph, its cyclic action, and its oriented cycle. Exact factorization remains unproved. The low-point census should resume from normalized residue maps, not from a new abstract Carrier or a rank comparison.

## Evidence

- `research/benincasa/three-site-physical-residue-link.json`
- `research/benincasa/physical_positive_chamber_q_wall_gate.py`
- `research/benincasa/bubble-arrangement-provenance.json`
- `research/benincasa/bubble-residue-flatness.json`
- `research/benincasa/bubble-physical-boundary-factorization.json`
- `research/benincasa/generic_lower_positive_chain_census_result.json`
- `research/nima/results/three-site-q-cyclic-completion.json`
