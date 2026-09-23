# Audit-conditioned reconstruction can be worse conditioned

## Fixed pins, fixed norms

Retain the source and norms of Grothendieck's conditioning theorem: source L1 and observable |delta U|+|delta V|. Fix the audited values exactly; they are parameters, not perturbed inputs. Only unpinned coordinates vary. Subtracting fixed contributions translates the observable domain without changing its metric.

For two free indices p<q with slopes r_p>r_q, the conditional observation is invertible:

    x_p=(V'-r_q U')/(r_p-r_q),
    x_q=(r_p U'-V')/(r_p-r_q).

Its matrix columns have L1 norms

    (r_p+r_q)/(r_p-r_q), 2/(r_p-r_q).

Since both slopes are at most one, the induced L1 operator norm is exactly 2/(r_p-r_q). This is also the Lipschitz constant on the residual polygon: at a strictly interior residual source point, a sufficiently small pure V perturbation with U fixed is feasible and attains the column norm. Every conditional section is this inverse, so this sensitivity is unavoidable.

## An exponential example inside the same owning family

Audit and fix every coordinate except the final two. For m>=3,

    p=m-2, q=m-1,
    r_p-r_q=127*128^(-(m-1)),
    Lip(s_A)=2*128^(m-1)/127.

The pins may be any admissible exact values; they only translate the residual image. This is exponential in m, whereas the unpinned two-moment section has global conditioning Theta(m^2) in the same source and observable norms.

There is no contradiction with the statement that visible restriction cannot worsen a fixed section's Lipschitz constant. Pinning source coordinates generally removes the original section points from the allowed fibers. The conditional section is a different map on a different residual image, not merely the restriction of the original map. The original section can use larger-slope coordinates to produce a stable representative; fixed audits forbid that freedom.

Thus retaining more exact information can make the remaining inverse problem worse conditioned, even while reducing the number of possible witnesses. Uncertainty size and reconstruction sensitivity are distinct quantities.

## One and zero free coordinates

With one free coordinate j, observable differences are (delta x,r_j delta x), so the exact inverse Lipschitz constant on its segment is 1/(1+r_j). With no free coordinates the domain is a singleton and the least constant is zero. Conditioning therefore need not vary monotonically with the number of audits: leaving two close slopes can be unstable, while pinning one more coordinate leaves a stable one-dimensional inverse.

## General residual boxes

With at least two free slopes, the endpoint uniqueness argument and greedy-section derivative bound apply to the residual ordered box. Define R_free as the supremum of the free greedy-profile L1 difference divided by its weighted moment gap. Then

    R_free <= optimal residual section constant <= Lip(greedy residual section) <= 1+R_free.

The derivative bound uses free slopes in [0,1] and is under the same fixed-pin norm convention. The two-free case above has an exact inverse formula and a sharper exact constant. No claim of a uniform polynomial bound over arbitrary audit sets follows from the unpinned all-m theorem.

## Noisy audits are a different contract

If retained pin values themselves vary, the input includes their differences and their affine contributions to U',V'. The norm must assign weights to those additional coordinates. The fixed-pin theorem supplies no complete bound for that enlarged-input problem. Nor does numerical stability of a selected witness identify the actual source or make membership decisions uniformly robust at a boundary.

## Verification

    python research/voevodsky/checkers/check_audit_conditioning.py

The exact checker calls the owning audit-aware section on midpoint controls and a pure-V perturbation, verifies all pins, reconstructs both moments, and matches the exact ratio against the inverse formula. It also checks one-free-coordinate controls. The continuum and all-m claims follow from the displayed affine inverse, not finite extrapolation.

Artifact: `results/audit-conditioning.json`. This is an implementation control, not a separate independent verifier or a fresh upstream admission replay.
