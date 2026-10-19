# Iteration17: the missing context-composition filler and coherence

## Fresh obligation and explicit result

The54-node net left source binding open because the chosen half-gain/drift DG base-witness substitutions differed by a47-term degree-one cycle. The new checker constructs an18-term degree-two chain whose boundary is EXACTLY that cycle. Its complete coefficients are serialized in the receipt, not replaced by a boundary-zero assertion.

All basis elements and differentials come from the existing shared-leg DG owner construction. No new source generator, unspecified filler or free-seed tetrahedron face is introduced.

## Existence and uniqueness mechanism

The owner's degree-two basis consists of109 paths h_i k_j (100 arrow-block and9 state-block paths). Each boundary contains a unique pivot -x_i k_j with nonroot i,j, and no other degree-two basis boundary uses that pivot. The checker verifies all109 pivots explicitly. Thus the degree-two boundary is injective.

For a degree-one cycle z, candidate filler coefficients are simply

    coefficient(h_i k_j) = -coefficient_z(x_i k_j).

The checker then verifies delta(filler)=z, rejecting a cycle not filled by that candidate. For the actual owner complex, the freshly reused rank facts give

    dim C1=246, rank delta1=137, rank delta2=109,
    H1 dimension =246-137-109=0.

Thus every degree-one cycle in this fixed complex has a unique degree-two filler. The displayed cycle is not merely homologous to zero by an unprovided assumption: its actual18-term filler is computed and checked.

## Context comparison and coherence

Write F_M=T_M for the explicit substitution from iteration16, and define K(M,N) on abase by

    delta K(M,N)=F_M(F_N(abase))-F_(N M)(abase).

It vanishes on other generators. The checker confirms strict composition on all non-base generators and that the coefficient of abase in every F_N(abase) is1. All25 pairs from the five declared test contexts have checked fillers; comparisons involving identity have zero filler.

For each of125 triples, the following equality holds as an ACTUAL degree-two chain:

    K(L,N M)+F_L(K(M,N)) = K(M L,N)+K(L,M).

The final term represents K(L,M) applied to F_N(abase), whose base coefficient is1. These are the two comparison routes from F_L F_M F_N to F_(N M L).

The general algebraic explanation is explicit: their boundaries are equal by associativity of substitution and matrix composition; their difference is a degree-two cycle; injectivity of delta2 forces it to vanish. Likewise uniqueness forces the unit comparisons. This argument is conditional on the declared row-sum-one DG substitution laws and strict non-base composition. Finite tests are not misreported as a new universally quantified Agda proof.

A CoherentStep now retains the original context packet, updated packet and the exact Comparison record containing both defect and filler. Zero and sign-reversed replacements of the nonzero actual filler fail its boundary equation. The previous source/context history is not identified with a flattened matrix product.

## Scoped source-binding closure

Together with the prior checks, the retained joint source now has:

- explicit marked-path generator assignments into actual shared-leg paths;
- the actual nonzero product, balanced products and local right-b action;
- retained original raw cuts and source seam certificates;
- explicit gain/drift context updates tied to the same schedule/energy leg assignments;
- actual DG comparison witnesses and their context-composition fillers;
- unit/triple coherence at the stated complex and policy scope.

`relation-assembly-source-binding` is therefore constructed at this conditional joint-source scope. It does not assert that the noninjective evaluation reconstructs the source, that numerical detection is faithful after every gain, or that the source recorder-balanced seam complex is identified with the target DG complex. The source remains explicitly retained and checked. Matrix cancellation at q=1/4 remains a valid hostile against dropping that source/symbolic layer.

This is a justified graph-of-evaluation/context construction, not an independent appended relation certificate: source, symbolic target, numerical assignment and context update satisfy the checked equations. No physical normalization or additional actuator is inferred.

## Verification and next root turn

    uv run --with sympy python research/strominger/checkers/check_context_composition_fillers.py

Eight checks pass;109 pivots,25 context pairs and125 triples are checked. Receipt: `research/strominger/results/context-composition-fillers-v1.json` includes the18-term actual filler. Prerequisite source checks rerun. No new Agda closure is claimed.

The root remains OPEN pending its final common-witness assembly review. Next compose the now-compatible schedule, relation-context and energy task interfaces, retain their distinct observers and verification boundaries, and explicitly test witness/provenance erasure at the resulting package boundary. Do not promote input readiness alone to a root theorem.
