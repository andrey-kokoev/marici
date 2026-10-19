# Common internal corner: pairwise naturality, nonzero three-cell sum

Iteration 19, 2026-10-13. Freshly read the mutable work net's common-corner task. This deliberately distinguishes two verified internal gluings from a complete chain or weighted descent.

## One actual common positive source corner

Reference the A/history8 source matrix at alpha1=alpha5=0, with ordered surviving variables

    (alpha2,alpha3,alpha4,alpha6,alpha7,alpha8).

The active labels are {1,2,3,5,6,8}, with parallel pairs (3,5) and (6,8). Source dimension is six. These same matrices occur as boundary closures in H5's Y1268 facet and H9's Y1235 facet.

The checker reconstructs all three positive cyclic closure frames symbolically and derives their six-dimensional logarithmic transitions to the reference generator. The six active Z rows are a basis, giving an actual boundary fiber inverse. At both pinned positive external fixtures, all three source points map to exactly the same rank-six target point; all three full source-chart target germs have rank eight.

## Ordered normals and signs

Fix the common target normal order

    Y1268 first, Y1235 second.

The source deletion order is aligned to these target normals in each history. For H9 this reverses its natural shared-facet-first order. Both target functions have actual symbolic source pullbacks by their corresponding deleted coordinates and nonzero units; neither is a fitted tangent plane.

On the common reference six-dlog generator the resulting coefficients are

    History5: -1,
    History8: +1,
    History9: -1.

These are derived from the generic intrinsic log coefficients, source deletion parity and actual six-coordinate transition Jacobians. Their source sum is symbolically -1, not zero.

For each chart and each external fixture, source iterated residue then pushforward, first source residue/pushforward then second target residue, and top pushforward then both target residues agree. Reverse both normal and source deletion orders: the density changes sign. Swapping normal rows without aligning the deleted coordinates would conceal this anticommutation in a misleading determinant ratio, so that shortcut is explicitly avoided.

All twelve chart/fixture/order three-route comparisons pass.

## Pairwise naturality versus three-cell sum

The completed Y1268 gluing gives H5+history8=0 after the second residue. The completed Y1235 gluing gives history8+H9=0 in its natural normal order; reversing both routes preserves that zero in the declared common order.

The selected three-composite unit-weight sum, however, is minus the reference density at both fixtures:

    -298135937212587264659 / 447463355364480000,
    -5003804216711260406760623657 / 2986785549733078114560000.

Both exact residuals are retained. Pairwise boundary naturality does not make this three-cell chain complete. Reversing one orientation gives a nonzero paired residual.

A hostile independently doubles history8's coefficient. That fits the corner sum to zero but leaves a nonzero internal-pair boundary residual and violates the frozen source normalization/gluing. It is recorded as a rejected shortcut, not a candidate source-derived weighted coefficient.

## Scope and next executable continuation

This establishes one actual common positive source/target corner, ordered iterated residue squares, pairwise gluing naturality and a nonzero selected three-composite sum. It does not refute the original weighted nine-form conjecture or the historical complete BCFW chain: neither has been instantiated by these three unit-weight forms alone. Component/sector maps, remaining terms and global chain attachment remain missing. Scientific gate verdicts are unchanged.

Next: identify a possible fourth six-active-label top cell on support {1,2,3,5,6,8} using the owning source seed/history matcher. Test whether transported history6 supplies that cell, and derive its intrinsic orientation and corner residue independently of the desired residual. A transported representative must not be admitted as untransported K0 by this test. If the matcher rejects the candidate, retain that disposition rather than inventing a compensating form or choosing its sign from the corner sum.

## Implementation and reproduction

An initial zero was a Python integer inside the symbolic coordinate mapping; the `.subs` evaluation failed. It was converted to a SymPy zero without changing the chart or criterion. The subsequent fresh headless run passes.

    python research/benincasa/checkers/check_three_composite_common_corner.py

Receipt: `research/benincasa/results/three_composite_common_corner.json`.

Eight grouped checks pass; predecessor source/checker hashes are verified. Evidence is exact source/normal/order and local differential algebra, not a kernel proof or complete weighted theorem.
