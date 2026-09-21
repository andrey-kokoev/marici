# Theta parity squares and the permutohedral three-cell

## Constructed and checked

The actual 24 four-prime route words form the vertices of the three-dimensional permutohedron P4. Its 36 edges exchange adjacent positions. Its 14 facets are indexed by ordered nonempty bipartitions A|A^c:

- six square facets with block sizes 2|2;
- four hexagons with block sizes 1|3;
- four hexagons with block sizes 3|1.

This extends the earlier abstract permutohedral fixtures to the actual event-segmented theta route source and its observations. The six square alternating vertex vectors coincide, with the recorded orientations, with all six existing parity columns K.

The new checker is `checkers/check_theta_permutohedral_three_cell.py`; its complete incidence matrices, orientations, route labels, and subdivision data are in `results/theta-permutohedral-three-cell.json`.

## The common higher cell

Orient each edge from the smaller route index to the larger. Orient each facet by its cyclic traversal beginning at the smallest route index and proceeding to its smallest adjacent route index. With these explicit conventions, the cellular chain complex is

    0 -> Q -> Q^14 -> Q^36 -> Q^24 -> 0
          d3    d2      d1

and the exact checks give

    d1 d2 = 0,       d2 d3 = 0,
    rank(d1)=23,    rank(d2)=13,    rank(d3)=1.

Every entry of the single d3 column is +1 or -1. Hence the oriented boundary of the three-cell uses every square and every hexagon exactly once. The boundary sphere has Betti numbers (1,0,1), and attaching the three-cell gives (1,0,0,0).

Squares encode the commuting relation s1 s3=s3 s1. The two hexagon families encode s1 s2 s1=s2 s1 s2 and s2 s3 s2=s3 s2 s3. These are all checked against the actual adjacent-swap edge labels.

Thus the common coherence is an explicit three-ball with six square and eight hexagonal boundary comparisons. A sequential comparison involving only three squares would require additional cuts and matching boundaries; the closed cellular boundary already supplies the canonical common object.

## Three opposite pairs and reversal

In the earlier parity-column order, route reversal pairs columns

    (0,5), (1,4), (2,3).

The checker constructs reversal on vertices, oriented edges, and oriented faces, verifies both chain-map squares, and verifies

    reversal_2 d3 = -d3.

On the six-dimensional parity space reversal has three +1 directions and three -1 directions. The three opposite-face pairs therefore have a precise even/odd decomposition. They are symmetry pairs at the same cellular dimension; no tower successor has been inferred from their count.

## Boundary chains and alternating vertices have different types

For a square with cyclic vertices v0,v1,v2,v3, define its observation mode by

    a_square = e_v0 - e_v1 + e_v2 - e_v3.

For a hexagon use the six-term alternating vertex sum. These lie in the route source C0=Q^24. The cellular boundary of a face instead lies in C1=Q^36 and sums oriented edges.

The identity d2 d3=0 relates face boundaries. It is not an assertion that the six square vertex modes are linearly dependent. All six remain independent.

The eight hexagon vertex modes span dimension seven. Together the fourteen facet vertex modes span dimension twelve. Thus the square-mode span and the hexagon-mode span intersect in exactly one dimension.

That shared mode is the global alternating route vector

    a = sum_w sign(w) e_w.

It has three exact decompositions: the signed sum over the six squares, the signed sum over the four 1|3 hexagons, and the signed sum over the four 3|1 hexagons. For the stored parity columns,

    a = K_0 - K_1 + K_2 + K_3 - K_4 + K_5.

The face signs and both hexagonal decompositions are stored and checked. These are vertex-space identities, separate from the cellular three-boundary identity.

## Exact signature observations

For the full event-segmented degree-d coordinate map K_d, the ranks of the observed facet vertex families are:

| d | six squares | eight hexagons | all facets |
|---|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 6 | 6 |
| 3 | 0 | 6 | 6 |
| 4 | 6 | 7 | 12 |

All entries were computed with exact rational arithmetic. The theta atom map H is injective on the finite atom span by the previously imported independence theorem, so H^(tensor d) preserves these finite ranks.

The lower-degree observer detects six combinations in the hexagonal vertex family while missing every square mode and the shared global alternating mode. Degree four detects the complete twelve-dimensional combined facet-mode span.

These are ranks of alternating vertex observations, not ranks of cellular boundaries or homotopy groups. Every face edge loop closes under every observation: K_d d1 d2=0.

## What a square means analytically

For a square with commuting swap coordinates s,t in [0,1], the bilinear source mixture is

    c(s,t)=(1-s)(1-t)e_v0 + s(1-t)e_v1 + st e_v2 + (1-s)t e_v3.

Its mixed derivative is the square parity vector:

    partial_s partial_t c = e_v0-e_v1+e_v2-e_v3.

Consequently the two- and three-point theta observations of this mixture have zero mixed derivative, whereas the four-point observation has the nonzero mixed derivative H^(tensor 4) K_4 a_square.

This gives a direct analytical interpretation: the square mode is the interaction between two commuting route deformations. Vanishing of that interaction does not force either individual edge deformation to vanish. This bilinear square filling is an additional convenient parametrization; the global filling below uses barycentric piecewise-affine maps.

## An explicit continuous analytical filling

Use the barycentric subdivision of P4. For each nonempty cell sigma, assign its barycenter the uniform source mixture

    c_sigma = (1/|vertices(sigma)|) sum_(w in vertices(sigma)) e_w.

For every maximal flag vertex < edge < face < body, interpolate these four vectors affinely. There are 144 tetrahedra. The checker enumerates every flag and verifies its incidence. Shared simplex faces agree because their vertex assignments are global. All images are probability mixtures.

This constructs a continuous piecewise-affine map

    c:P4 -> X=C^24

whose vertex values are the original route basis vectors. Applying the bounded finite theta map gives

    F c:P4 -> L2(R_+^2) direct-sum L2(R_+^4).

It is an explicit analytical three-cell whose boundary contains all the observed square and hexagonal comparisons. The same construction works for the bordered lift by replacing F with F_border. On every tetrahedron the observation is the affine combination of four known source responses, so the common domains and boundary agreement are explicit.

This construction realizes the route coherence in the linear observation carrier. That carrier is contractible, so the filling is not evidence of a nontrivial third homotopy class. It also does not identify the interpolation with an independently defined arithmetic successor or prove preservation of an earlier signed Green form.

## Verification and conclusion

Fresh command:

    uv run --with sympy python research/voevodsky/checkers/check_theta_permutohedral_three_cell.py

All assertions passed: oriented chain identities, boundary ranks, square-to-parity identification, braid/commutation labels, global antisymmetry decompositions, reversal chain naturality and top-cell sign, exact observation ranks, and all 144 barycentric flags.

The proposed higher connection is now concrete: three opposite pairs of square modes belong to one permutohedral three-cell, with eight braid hexagons providing its remaining boundary. The actual theta observations extend over that cell. Their information content changes at degree four exactly as the table records.
