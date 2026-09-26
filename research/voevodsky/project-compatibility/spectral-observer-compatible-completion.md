# Reusing the spectral observer: faithful recovery and the correctly typed completion

## Fresh source evidence

Read ledger Entries2276,2283,2288,2295 and `research/benincasa/checkers/gram_wall_smith_nearby_cone.rs`. They retain the frozen spectral Gaussian contact source, not our continued loop-collision patch. Entry2288's checker verifies a local determinant2c, a unit minor and the direct-score determinant-6; it prints zero completed-cone homology without computing a differential or that homology.

This audit preserves the demonstrated recovery while separating it from the stronger, insufficiently typed cone claim. No owner artifact is changed.

## Orientation and actual retained matrices

The printed matrices have occurrences as rows and ports as columns. Thus column occurrence vectors are observed by their transposes. Write

    T(c)=[[1,0,0],[1,1,-c],[1,1,c]],
    Q=[[1,2,0],[1,-1,-1],[1,-1,1]],
    A=T(c)^T, B=Q^T.

T is the existing local Smith representative, not a newly derived global finite-q tensor matrix. At c0, ker(A) is spanned by k=(0,1,-1). Bk=(0,0,-2), agreeing with Entry2283's cross-score value. det(T)=2c and det(Q)=-6.

Therefore the direct source port really does distinguish the tensor-dark class. No singular tensor inverse is needed.

## Correct the cone statement, not the physical recovery

The stacked observer

    F: x -> (Ax,Bx)

maps a rank3 source to a rank6 ambient output. It is injective because B is invertible. Its ordinary two-term mapping cone nevertheless has a rank3 cokernel; it is NOT acyclic. This remains true at and away from the Gram wall. The analogous direct-sum map on two independent source copies would also not establish the claimed contraction of the tensor defect.

An explicit compatibility complex is instead

    0 -> V --F--> Y_tensor direct_sum Y_score --H--> Y_tensor -> 0,
    H(y,z)=y-A B^(-1) z.

Then HF=0, H is surjective via y, and ker(H)=im(F): if H(y,z)=0, the unique source is x=B^(-1)z. The compatible output object is ker(H), NOT all independently arbitrary tensor/score pairs. Equivalently F is an isomorphism onto that declared compatible target.

This split exact sequence explains precisely how an augmented observer complex can be acyclic. It does not silently redefine the ordinary cone as that three-term complex. The existing physical compatibility relation between two readings of the same occurrence packet supplies the equation; the owner must confirm whether this is the complex intended by Entries2283/2288.

## Quantitative noncollapse in a declared norm

For real coefficients with Euclidean norms, Q's columns are orthogonal, with squared lengths3,6,2. Hence B has least singular value sqrt(2), and

    ||(Ax,Bx)|| >= ||Bx|| >= sqrt(2)||x||.

Recovery x=B^(-1)z has norm at most1/sqrt(2), uniformly in c. Unlike the scalar degenerating-unit example, this bound does not divide by the Gram normal. This supplies a genuine finite-dimensional stability statement for the retained normalized port coordinates.

## Restore the source contact weights

Entry2295 retains W=-8 diag(C12,C23,C31) on occurrence rows. Thus the actual column readouts are

    A_C=T^T W, B_C=Q^T W.

On a domain where every C_e is nonzero,

    A_C B_C^(-1)=T^T (Q^T)^(-1),
    ||(A_C x,B_C x)|| >= 8 sqrt(2) min_e|C_e| ||x||.

In particular, a uniform lower bound on the contact magnitudes gives uniform recovery through the Gram wall. On a compact positive-energy domain avoiding poles, continuity and the source's no-finite-zero result provide such a lower bound. Contact infinity is NOT covered: C_e may tend to zero, and the estimate degenerates. The prior Cartier-grade treatment there must be inspected separately, not replaced by division by vanishing contact weights.

This norm is explicitly the Euclidean norm on the finite retained coefficient/port packets. It is not a proof that an experimental measurement norm, an infinite score tower, or an unrestricted physical completion is equivalent to it. The direct score is a boundary-state susceptibility; operational preparation was already excluded by Entry2283.

## Decision

Reuse this existing spectral contact observer as a scoped physical-source realization of the comparison/readout contract. The concrete result is stronger and more precise than another toy singular matrix: a pre-existing admitted alternate port recovers the physical-source packet with a c-independent bound on bounded contact domains.

Retain three distinct claims:

1. faithful finite-packet recovery: established by the exact source matrices;
2. exact compatible-output complex: established by the explicit H above;
3. physical/global completion and the owner's intended complex: not discharged merely by either finite calculation.

Next inspect the already existing contact-infinity Cartier-grade construction (Entries2224–2225) and whether its topology preserves this readout bound. Send the cone-typing discrepancy and explicit candidate repair to the source owner; no owner acknowledgment or change is presumed.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_spectral_observer_completion.py` recomputes the exact symbolic matrices, kernel recovery, compatibility differential, dimensions, contact-weight cancellation and singular-value data. These checks support the written general argument; they do not recompute the global spectral-weight positivity theorem or physical continuation.
