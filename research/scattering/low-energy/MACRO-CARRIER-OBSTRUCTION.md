# C8 — exact spectral obstruction for the fixed two-tick controller

## Fixed controller, independently of C10

Reconstruct D on the twelve labelled displayed occurrences by the same-support endpoint-extension rule of `C8-MACRO-CONTROLLER.md`. Its primitive-clock controller is F=[[0,D],[I12,0]]. Exact multiplication gives F²=diag(D,D), so the phase-zero synchronized return is precisely D, not a selected submatrix or a fitted operator.

Fresh rational elimination gives

    det(D-I12)=9.

Thus 1 is not an eigenvalue of D. This fact does not follow merely from C10's noncontraction result: a globally noncontractive matrix could still have a reducing isometric carrier on a smaller subspace. Here the relevant target eigenvalue is actually absent.

## Target and contradiction

The declared target is U=T tensor T with

    T=[[-1/2,1/2],[-3/2,-1/2]],
    H=diag(3,1) tensor diag(3,1)=diag(9,3,3,1).

Take v=(1,0,0,3)^T. Direct rational multiplication gives

    Uv=v,       v*Hv=18.

If DJ=JU, then (D-I)Jv=J(U-I)v=0. Since D-I is invertible, Jv=0. But J*J=H would give ||Jv||²=v*Hv=18, a contradiction. Consequently no J in the declared class exists, even before checking the reducing-complement equation. A rank-four intertwiner also fails simply because its nonzero target eigenvector would be killed.

The checker reconstructs all displayed records and primitive expansions through the separately replayable macro-map builder, verifies F², computes det(D-I) by exact Gaussian elimination, and verifies the target invariant vector and its positive metric norm. No floating spectral tolerance is used.

## Scope

Only the fixed twenty-four-record two-tick controller and its twelve-record phase-zero return are excluded. The complementary records are not dropped. A different clock, amplitudes, comparison package or source-authorized controller is a different conjecture. Neither physical photon production nor the existence of every possible retained tensor construction is decided.

C3's one-primitive-tick obstruction, C8's synchronized-return obstruction and C10's raw-readout norm obstruction are distinct results. No one is substituted for another, and no failed existence assertion becomes a positive prerequisite elsewhere in the net.
