# Discriminating the proposed higher-homotopy interpretation

## Question

Operator asks whether the quartic-source quadratic weight defect should be replaced by a higher homotopy, with a subsequent coherence obstruction. Test this against the rival explanation of independent contact data omitted by the triangulation presentation. This direction is non-evidential until its differential and evaluation maps are constructed.

## Claim boundary

The test constructs a combinatorial complex from the actual six-point source valences, not a BRST/BV or physical differential. C0 has the 14 cubic trees. C1 has the 21 one-quartic diagrams; an oriented edge boundary is the difference of its two cubic refinements. C2 has the three two-quartic diagrams; each has four refinements and an oriented square boundary. Exact incidence arithmetic verifies d1 d2=0.

Ranks over Q are rank(d1)=13 and rank(d2)=3. Thus H1 has dimension 21-13-3=5. Commuting two independent quartic refinements does have a square coherence, but these squares do not fill all cycles.

### Evaluation test

Map a cubic basis tree to its actual source contribution g^4 divided by its propagator product. This map does not annihilate the ordinary edge differential. The first tested edge evaluates to -g^4(s04-s35)/(s02 s03 s04 s35), which is generically nonzero. Hence this unweighted refinement complex does not make physically equal contributions into boundaries under the proposed evaluation to rational amplitudes with zero differential.

Multiplying the two refinement terms by their respective canceled channel variables does make their evaluations equal. This is the algebraic propagator-cancellation identity, not by itself a physical differential. Their common evaluation carries coupling g^4; matching it to the actual one-quartic coefficient g^2 lambda requires the independent multiplier lambda/g^2, on g nonzero. The operation is singular as a prescription at g=0, where the quartic theory still exists. Contact normalization has not been derived from the cubic vertices.

### Strongest attempted completion

Add the six pentagon cells corresponding to a triangle and a pentagon dissection. The combined two-boundary rank is eight, so these extra cells kill the five remaining H1 classes (with one relation among the nine square/pentagon boundaries). This is an exact combinatorial completion test. A pentagon cell is not an interaction present in the declared cubic-plus-quartic source. Such a cell could conceivably arise as coherence rather than as a physical quintic vertex, but the source has not supplied that interpretation or an amplitude-compatible map for it.

## Disposition

The naive higher-homotopy interpretation fails its first evaluation test. Weighted refinement cancellation and square coherence exist, but neither identifies the measured quadratic-in-weights residual with dH. In particular that residual is a product of coefficient functions, whereas the tested differential acts on graph chains: a source-derived multiplicative comparison map is missing. Do not promote the five combinatorial H1 classes to physical obstructions or call the pentagon completion a cubic polynomial failure.

The tested evidence supports keeping contact data explicit rather than treating this defect as already explained by higher homotopy. It does not rule out a separately derived homotopy-algebra description of the scalar theory. Reopening that interpretation requires a declared graded source complex, its differential and product, and an evaluation/comparison carrying the specific residual into its boundary image. This branch stops at that missing map; the previously admitted face-specific allocation test remains an independent executable rival.

Checker: checkers/check_source_refinement_complex.py. Results: results/source_refinement_complex.json. Tests use exact rational/symbolic arithmetic and preserve the nonzero evaluation control. Git prohibition remains active; no Git operation occurred.
