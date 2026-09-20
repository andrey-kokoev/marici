# Two-sided extension of the admitted source axis gives support obstructions, not returning corrections

## Question

Does compatibility with a larger two-sided neighborhood impose genuinely new central-seam constraints, or merely reproduce inclusion/restriction laws?

The operator proposed that residual data of a central comparison might extend in both realization directions and admit corrections constrained by distant levels. The discriminating test was a four-level extension fiber, followed by one extra level on each side.

This test uses an existing source direction, not a new conjectural feedback law. In `research/voevodsky/source-authorized-successor-assembles-on-the-relative-rigged-subsystem-and-stops-at-the-physical-prolate-sonin-seam.md`, initial edge cutoffs form an admitted directed source axis. Its full identification with the intended realization-dimension or cycle counter remains unproved.

## Source, variance, and retained data

Use the ordered prime-labelled edges of the arithmetic {2,3,5} cube beginning at label 2. Let E_n be the rational coefficient space on the first n edges. The source maps are coordinate inclusions I_nm:E_n->E_m for n<m. Their dual maps are restrictions I_nm*:E_m*->E_n*.

These are two differently typed constructions. A dual restriction is not an inverse source successor. The test retains every edge coefficient; source cycles are not quotiented by interval or theta history.

The central seam is 5->6. The first neighborhood has levels (4,5,6,7); the enlarged neighborhood has (3,4,5,6,7,8). Thus the experiment concerns an initial-edge cutoff, not all conductor, radial, or domain directions of the analytic tower.

All coefficients are treated as rational sets, or 0-types. Their identity types are propositions. A nonsingleton affine fiber is therefore noncontractible as this set-level type. This statement is not an assertion about the contractibility of a topologized real affine space or about higher analytical mapping spaces.

## Extension types and pullback

For the covariant system, admissible tuples satisfy x_(n+1)=I_n,n+1 x_n. For the contravariant system, admissible dual tuples satisfy lambda_n=I_n,n+1* lambda_(n+1).

Define the left partial extension type using levels (4,5,6), and the right partial extension type using (5,6,7). Both restrict by forgetting outer coordinates to the corresponding central seam type. Their pullback is exactly the set of compatible four-level tuples. Fixing a central datum gives the extension fiber computed by exact rational linear equations.

Thus both restriction maps to the seam are supplied by restriction of diagrams. No reverse source map is invented. In the set-level model the homotopy pullback reduces to the ordinary pullback because agreement witnesses have no higher ambiguity.

## Covariant result: empty or singleton

Let a fixed central pair satisfy x_6=I_56 x_5. It extends to the four-level neighborhood exactly when x_5 belongs to the image of E_4. When it does, the extension is unique: injectivity determines the lower value and the successor determines the upper value.

Three exact cases were tested:

- x_5=(1,0,0,0,0) extends uniquely to both neighborhoods.
- x_5=(0,0,0,0,1) has no extension to level 4, despite being a legal central source state.
- x_5=(0,0,0,1,0) extends uniquely to level 4 but not to the additional level 3.

Therefore enlarging the lower side can impose a new condition on the central datum. The condition is earlier support membership. It does not supply a correction to that datum. Enlarging the upper side adds no choices or constraints in this strict covariant system.

The general finite statement is immediate: the extension fiber over x_k is empty unless x_k lies in the earliest retained source image, and is singleton otherwise.

## Contravariant result: exterior freedom, no new central constraint

Fix lambda_6=(1,2,3,4,5,6) and lambda_5 equal to its first five coordinates. The four-level extension fiber has one free rational coordinate, the seventh dual coordinate. The enlarged fiber has two free coordinates, the seventh and eighth.

The comparison from the enlarged fiber to the first is the surjection (a,b)->a. Every central covector still extends. Further lower restriction is determined and introduces no extra condition.

These extension fibers are nonunique because the source has gained new directions, not because a higher coherence witness has been discovered.

## Pairing test

Two exterior covectors differing only on a newly added coordinate restrict to the same central covector. They also pair identically with every covariant source vector included from the center: the included source has zero coefficient in that new direction.

Thus pairing the admitted co/contra systems does not create a returning correction. Evaluation naturality makes the exterior freedom invisible to the centrally included source. Source inclusion followed by restriction is identity on the smaller source; the opposite composite is a proper projection, not identity on the larger one.

## Noncollapse control

At level 6 the retained source has the nonzero cycle (1,-1,0,1,0,-1), using the tested edge ordering. Its interval synthesis is zero. The full source record retains it.

This ensures the preceding findings were not produced by silently dropping cycle information. It does not assert that all analytical boundary conditions of the completed source have been imposed; the experiment isolates the edge-source axis and its actual maps.

## What the test decides

On this admitted source axis:

- larger neighborhoods can reject central data through support constraints;
- dual extension permits free outer data but does not constrain the central covector;
- no selected correction, stabilizing law, or return mechanism is generated by inclusion, restriction, and pairing alone.

The proposed full mechanism therefore cannot be inferred from these maps. A source-defined coupled extension relation would have to connect the added directions to the central seam beyond their coordinate inclusion/restriction. That relation might come from the independently defined Green or boundary operator, but it has not been supplied in this experiment.

This is not a refutation of every two-sided analytical extension model. It identifies which elementary operations do not suffice and prevents their being renamed as feedback. No passage to infinity is made. The edge index is bounded below, and an inverse limit of unrestricted dual coefficients would additionally require the declared source topology and admissibility conditions.

## Disposition and verification

The finite test has a definite answer: the available edge-cutoff maps yield support obstruction on the covariant side and unconstrained exterior freedom on the dual side, not corrective influence from distant levels. We should not extrapolate a seven- or eight-simplex, or an infinite stabilization law, from this result.

`uv run --with sympy python research/nima/checkers/check_two_sided_source_extension_fibers.py` exits 0 with eleven exact checks. Result: `research/nima/results/two-sided-source-extension-fibers.json`. The test is degree zero; higher coherence and full analytic extension fibers were not computed.
