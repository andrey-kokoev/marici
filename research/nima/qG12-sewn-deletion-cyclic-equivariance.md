# Sewn deletion-face cyclic equivariance

## Question

Do the `q_G12` sewn deletion-face residues transport equivariantly to the `q_G23` and `q_G31` sectors under the frozen source cycle?

## Source cycle

The source relabelling is

\[
(a,b,c;X_1,X_2,X_3)\mapsto(b,c,a;X_2,X_3,X_1).
\]

It preserves all ten pole rows and has four orbits: the total pole, the three one-site walls, the three two-site walls, and the three occurrence walls. It sends

\[
q_{G12}\mapsto q_{G23}\mapsto q_{G31}\mapsto q_{G12}
\]

and

\[
q_{g23}\mapsto q_{g31}\mapsto q_{g12}\mapsto q_{g23}.
\]

The six-link source cycle rotates by four positions, and its ordered residue-sign sequence is preserved.

## Transported deletion faces

A `q_G12` deletion-face row is determined by:

1. the selected shared wall `q_gi`;
2. the two remaining shared walls;
3. both occurrence walls as the unsplit sum;
4. the inherited residue orientation.

The source cycle permutes each item within its corresponding orbit. Because it is a three-cycle on both ambient edge variables and site energies, its Jacobian has sign `+1`; the ambient orientation is preserved. The already-frozen ordered residue signs therefore transport without an additional global sign.

The occurrence identity

\[
\frac1u+\frac1v=\frac{u+v}{uv}
\]

is functorial under relabelling. Hence every transported sector retains the source-unsplit occurrence numerator and product. Three applications return every labelled denominator and orientation to its starting value.

Pairwise Čech closure is also preserved: the cyclic map is an invertible relabelling of the affine wall arrangement, so opposite iterated-residue Jacobians remain opposite and the mixed occurrence double-residue numerator remains zero.

## Exact scope

The following are cyclic-equivariant at source/incidence level:

- all pole coefficients;
- deletion-face denominator sets;
- occurrence sewing;
- ordered residue signs;
- pairwise Čech closure.

The conductor-normalized cohomology classes are not yet proved cyclic-equivariant. Reduced Cayley–Menger factors and analytic normalization were frozen explicitly only in the `q_G12` chart. No transported square-root branch or comparison of conductor finite parts is materialized for `q_G23` and `q_G31`.

## Strongest falsification attempt

Apply a noncyclic swap rather than the source three-cycle. The frozen hostile test produces six pole-row defects, including two-site and occurrence labels. Thus the equivariance is specific to the sourced cyclic action, not arbitrary permutation symmetry.

## Acceptance test for normalized equivariance

1. construct reduced Cayley–Menger factors in all three two-site charts;
2. transport a declared square-root branch around the three-cycle;
3. compute conductor residues and normalized finite parts in each chart;
4. verify equality after labelled cyclic pullback;
5. apply the hostile noncyclic swap and require a mismatch.

## Disposition

Sewn deletion-face localization is exactly cyclic-equivariant through Čech closure. The remaining cyclic gate is normalization-level transport of the square-root branch and conductor finite parts.

## Evidence

- `research/benincasa/generic_lower_positive_chain_census_result.json`
- `research/benincasa/three-site-physical-residue-link.json`
- `research/nima/results/three-site-q-cyclic-completion.json`
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
