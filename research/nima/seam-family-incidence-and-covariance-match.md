# Legitimate reuse of family covariance on the actual seam

## Typed match and limit

The seam supplies two forward paths x0=AB, x1=AD DB:A->B and two returns y0=BA, y1=BC CA:B->A. Their Cartesian pairing is entirely endpoint-compatible.

The existing bilinear mean/fluctuation identity therefore applies in the formal linear path span, and under any separately justified bilinear response realization. No inverse reference is needed to form y_j x_i.

But the full prior residual operation A_i+B_i+B_i r A_i expects parallel maps with a supplied reference return. It cannot be imported unchanged: forward and return paths here have opposite Hom types, so X+Y is not typed. The reused result is the bilinear covariance identity, not the complete same-slot dynamics or its physical interpretation.

## Two source-visible incidence relations

The full endpoint pullback has all four corners. The ORIGINAL TWO TRIANGLE RECORDS form a different, already identifiable relation:

    ABC = y1 x0,
    ADB = y0 x1.

This is the off-diagonal pair {(0,1),(1,0)} in the direct/indirect indexing. The complementary diagonal corners are the shared two-cycle and the four-cycle. These corners are not new fabricated paths; all are in the actual seed.

Thus there is a real candidate source of correlated context: keeping the two supplied triangles as the admitted comparison family, rather than taking every composable forward/return pair. The seed exposes this distinction. It does not require every later constructor to choose one of those operations.

## Exact covariance calculation

With explicitly equal weights within each two-element marginal, write

    Xbar=(x0+x1)/2, Ybar=(y0+y1)/2,
    Delta=C11-C10-C01+C00, Cij=yj xi.

Independent pairing gives the four-corner average and zero covariance. Equal-weight composition of the supplied triangle relation instead gives

    (C01+C10)/2 - Ybar Xbar = -Delta/4.

The complementary cycle relation gives +Delta/4. The difference between those two joint responses is -Delta/2.

More generally, all equal-marginal two-by-two joint weight laws have diagonal entries t and off-diagonal entries 1/2-t, for 0<=t<=1/2. Their correction is

    (t-1/4)*Delta.

The formulas follow symbolically by coefficient expansion in the four independent retained words. The checker confirms the corner coefficients and representative rational t values. Equal weights are declared for this calculation, not physical probabilities or an energy normalization inferred from endpoint incidence.

## What this resolves

It is legitimate to reuse the prior family-covariance algebra at these ports. It does NOT automatically produce a nonzero correction: the full independently weighted product gives zero. A nonzero formal correction can follow from retaining the actual two-triangle incidence instead of freely combining its marginal path families.

This is not adding nonlinear preparation to rescue v2. It changes the operation being compared: composition over an explicitly retained joint family versus composition of its separate means. The corresponding numerical response still requires an admitted reader that does not annihilate Delta. Additive primitive cost continues to give zero in all these cases.

The triangle relation is available from the input. The source question is now narrower and concrete: does the intended comparison constructor preserve that joint two-triangle relation, or generate the full endpoint-pullback family? A retention requirement should preserve the original relation as provenance in either case; preservation as provenance is not a rule for which terms enter the active response.

## Formal constructor-level distinction

`agda/SeedTriangleJointContext.agda` now instantiates the existing table kernel with the actual two triangle contexts. The row type has constructors ABC and ADB. Its forward/return projections are (direct,indirect) and (indirect,direct), and its execution maps recover the exact typed seed paths from `SeedSeamPathComparisonBoundary`.

Source grouping and the existing four-step presentation cycle recover the COMPLETE joint table, not merely its marginals. Formal negative proofs show that neither (direct,direct) nor (indirect,indirect) has a row witness in that table. A separately declared product table contains all four combinations and evaluates them as valid endpoint paths. It is a different input domain, not an equivalent reindexing of the two supplied triangles.

This matches the inspected native rule signatures: dependent family operations use supplied index types; componentwise congruence preserves that index; distribution reorganizes supplied dependent choices. No inspected signature instructs a retained family to discard its joint relation and freely cross its marginal projections. An independent-product or path-pullback expansion is an additional operation.

Therefore, for the task 're-present and compose the supplied triangle contexts', the correlated incidence is already the correct source domain. Calling its independent four-corner replacement mere retention would be incorrect. This does NOT establish that the physical successor is that task rather than an explicitly expanded comparison family. It also supplies no averaging weights, matrix response or physical preference for the display endpoint A.

The formal result settles the provenance/constructor distinction while leaving active physical operation selection explicit. The four-step table presentation theorem is not an identification with the confirmed rung schedule.

## Verification

The existing seed mixed-boundary checker was extended, not replaced:

    python research/nima/checkers/check_seed_seam_mixed_boundary.py

Exact checks pass for typed corners, the original-triangle relation, independent/product pairing, general joint-weight coefficient identity, and both signed covariance corrections. Existing retained-word and additive-cost controls remain intact.

The constructor follow-up was freshly verified with:

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedTriangleJointContext -Fresh

Safe/cubical/guardedness closure passes. Receipt: `results/agda-SeedTriangleJointContext.json`. No numerical response values or physical law were introduced.
