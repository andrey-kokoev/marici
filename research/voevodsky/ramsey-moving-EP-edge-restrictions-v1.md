# Actual edge restrictions of the moving E/P choice family

Connections: `face-chart-transition-descent` overlap/law-domain acceptance and `joint44-native-source-selection` retained-family/independent-reader acceptance.

## Result

For the moving-preparation U(2) family:

- the actual retained paired edge traces have exact geometric covariance;
- their full PN pullback square passes;
- collapsing the two parent-face traces to one scalar fails on five edges, for every U;
- the tested single-edge neutron instrument cannot recover even the paired CD observation, for every U;
- an explicitly nonlocal three-sector-edge instrument recovers the prepared data. All three of those sector edges are necessary within that instrument family.

These tests do not select U. They distinguish retained/contextual observations from stronger scalar/locality claims. Neither stronger claim is silently imposed on the parent.

## 1. The observations were not redefined to make the square commute

The checker loads the existing geometric proton readout H:12 tangent traces, two per geometric edge, each retaining its parent face and directed patch.

It uses the preceding geometric comparison G and the saved signed edge action W, checking on all36 inputs:

    H G = W H,       W* W = W² = I12.

For every one of the12 trace occurrences it also checks the edge, directed patch, parent-face label and orientation sign under the ABCD -> BADC chart change. Thus parent-face provenance is not erased.

This is coordinate covariance of the geometric observations. It does not turn a PN-ineligible face into an eligible one or supply a native role-changing operation.

With the unchanged PN map S and its metric inverse, the saved pullback observation is H_N = H S^-1. The checker verifies

    H_N S = H

and its restriction to the new preparation. These are the actual saved rows, not a newly chosen scalar readout.

## 2. Scalar collapse fails uniformly over the choice family

Using the reference compatible member

    T x = (x3,x4,x2,x0,x1),

compute the12 prepared traces H B'_P. Exact two-by-two minors and explicit kernel witnesses show:

| Edge | Rank of its two parent-face traces |
|---|---|
| AB, AC, AD, BC, BD | 2 |
| CD | 1, with opposite-sign agreement |

On each rank2 edge, there is a coefficient vector invisible to either chosen trace but visible to the other. Hence neither scalar determines its companion on the full prepared domain.

Changing U right-multiplies both rows by the same invertible five-coordinate matrix. It cannot change their joint rank, equality, or existence of a factorization from one row through the other. This proves the same conclusion for arbitrary U, not merely the two permutation examples.

It does not refute retaining both traces as separate, parent-indexed observations.

## 3. A single native-edge locality witness survives every U

The native instrument tested is the earlier sector0 uv-edge restriction, with intrinsic slots

    [0,1,6,7].

Take neutron coefficient basis vector e2 in the moving preparation. Its full prepared norm is1, but all four local instrument coordinates vanish. The required paired CD traces are nonzero; their exact multiradical values are retained in the receipt.

Thus no function of this local observation can recover the required CD observation on the full prepared domain: zero input and this unit input give the same local data and different required outputs.

This counterexample is uniform over U. The family acts on neutron context slots0,4; active slot2 is unchanged. The freedom left in the two contexts cannot repair this loss of an active mode.

The full PN pullback rows have support on all36 native neutron coordinates. Their exact transport equation must not be reported as evidence of a four-coordinate edge-local detector.

## 4. An explicit prepared-domain repair, with support disclosed

The existing enlarged instrument retains the two uv patches in each of three different sector edges:12 intrinsic coordinates in total.

Let E be its12-by5 restriction matrix on the new neutron preparation and M its restricted metric. The checker computes

    K = E* M E

and verifies det(K) != 0. Therefore

    D = adjugate(K) E* M / det(K)

satisfies D E = I5. The exact numerator, nonzero denominator and multiplication identity are saved, avoiding any floating-point inversion.

This recovers all five prepared coefficients for the reference member, hence all12 paired traces. For another U, retain the known context basis change when decoding coefficients. The physical trace factorization remains valid: the observation and the preparation acquire the same right-unitary change.

The old diagonal-Gram decoder was **not** reused: the moving context modes introduce nonzero restricted cross terms. That shortcut fails; the exact adjugate decoder passes.

Omitting any one sector edge leaves an active coefficient invisible to the other two while the required CD observation still detects it. Thus all three edges are necessary **within this declared three-sector instrument family**. This is not a lower bound for every conceivable detector or every alternative local field interpretation.

## 5. Interpretation for the parent

The retained higher-incidence reading survives these numerical restriction tests. The stronger one-scalar-per-edge and tested one-native-edge interpretations do not. A nonlocal prepared-domain observation is available and explicitly typed by its larger support.

Because the parent asks for a higher incidence object retaining full references and law domains, these scalar/locality failures are not automatically parent obstructions. Conversely, the positive trace equations do not themselves instantiate the actual native edge/triple composition witnesses or authorize a different support policy.

The remaining task is now precise: bind the retained paired/nonlocal observation to those native restriction types, keeping its parent faces, context choice and support. Do not continue searching U for a scalar-local repair; the uniform counterexamples already rule that out at this scope.

No unique context choice, active E->P operation, native-policy admission, parent verdict or graph publication is claimed.

## Reproduction and verification

    python research/voevodsky/checkers/check_ramsey_moving_EP_edge_restrictions.py

Fresh exact execution passes. Receipt: `results/ramsey-moving-EP-edge-restrictions-v1.json`.

The receipt contains12 face/edge/orientation bindings, prepared trace rows, both-direction nonfactorization witnesses, the uniform active-mode locality counterexample, exact three-edge decoder and each omitted-sector control. Existing source pins are checked.

Verification level: exact multiradical computation plus written arbitrary-U arguments by invertible basis change and fixed active column. No new formal-kernel proof or all-native-policy theorem is claimed.
