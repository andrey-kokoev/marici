# Full-state admissibility of the readable bank product

## Fresh verdict

The preceding bank composition recipe matches the desired response algebra, but it CANNOT be identified with a conservative linear update of the two original banks on their direct-sum coefficient space.

There are two exact obstructions:

1. its output is bilinear in two operand banks, whereas compositions of the prior linear orthogonal source updates are linear;
2. even with a prepared tensor-product joint bank, its unscaled product readout can exceed the input's positive coefficient budget.

A constructive normalized full-state exchange is available, but needs an explicitly PREPARED joint bank and a distinct gain-bearing response reader. It is not an already admitted physical interaction.

## Readable product on a prepared joint bank

Each operand has16 bank coefficients. On a PREPARED256-coordinate joint bank define M by

    M(t_b tensor t_a)=(C t_b)*(C t_a),

extended linearly to all256 coordinates. The actual Clifford multiplication and source coisometric C are reused.

Direct basis construction gives

    M M^T=4I,
    rank(M)=4,
    dim ker(M)=252.

Thus D=M/2 is coisometric. The denominator follows from the source coefficient metric; it is not a fitted gain.

Tensor preparation itself is additional data. On an unrestricted direct-sum coefficient state the tensor map is nonlinear; the normalized joint exchange does not construct that joint input from two separate resources.

## Exact norm hostiles

Choose x=unit+e1 and operand banks C^T x. The prepared joint bank has coefficient norm squared4, but its unscaled product M(tensor) has norm squared8. This is a SEPARABLE preparation, not a hostile requiring arbitrary entangled joint data.

A generic joint-readable unit bank D^T(unit) has norm squared1 and M-readout norm squared4, attaining the operator gain2.

Neither output can be treated as an unscaled conservatively transferred carrier with a nonnegative residual budget under the same metric.

## Constructive full-state completion

For an explicit4-coordinate carrier x and256-coordinate joint bank t, use the generalized existing exchange formula

    E(x,t)=(D t,D^T x+(I-D^T D)t).

The checker verifies the actual260-coordinate matrix is symmetric and its square is identity on every basis vector. Hence E^T E=I on the full space. The complete252-dimensional kernel remains in the bank.

This closes a mathematical full-state conservation/inverse obligation for a DECLARED larger carrier. It is not the original20-coordinate source schedule, and its unitary/orthogonal existence does not establish source admission, a clock or apparatus.

## Response conversion remains explicit

The original comparison recipe reads

    raw_response=matrix(2 M(t)).

The conservative extraction carrier is

    x_out=D t=M(t)/2.

Therefore reproducing the old raw response requires the explicit observation

    raw_response=matrix(4 x_out).

That is a gain-bearing port convention, NOT the conserved output state itself. Several actual fixture pairs are checked through this conversion with full resource retention.

The pinned T9 values and J4 are not changed. Nor is the factor4 declared as physical amplifier gain or free resource creation. Detector calibration, measurement back-action and energy interpretation still need their own source contract.

## What has and has not advanced

Advanced:

- ruled out the old unscaled recipe as a conservative linear source update;
- computed the exact joint readout normalization and hidden dimension;
- constructed a full-state inverse/conservative extraction retaining the kernel;
- preserved the distinction between state resource and response gain.

Still required:

- source-admitted preparation of the256-coordinate joint bank;
- selection/implementation of the260-coordinate interaction;
- physical interrogation realizing the gain-bearing response;
- storage, reset/reuse/degradation and timing.

No further response fit can substitute for those missing operations. The next decision is whether this larger prepared-joint-bank task is intended, or whether another existing physical interaction should replace the bilinear recipe.

## Verification

    uv run research/strominger/checkers/check_joint_bank_extraction.py

820 exact checks pass. Dependencies freshly rerun the single-reader fixture/response and reference-port chains. New checks cover source product/readout Gram, rank/kernel, coisometric lift, bilinear and separable norm hostiles, the full260-coordinate inverse/symmetry/conservation identities, kernel retention and explicit response conversion.

No new Agda closure, experimental calibration or physical instrument realization is claimed.

Artifacts:

- `research/strominger/checkers/joint_bank_extraction.py`
- `research/strominger/checkers/check_joint_bank_extraction.py`
- `research/strominger/results/joint-bank-extraction.json`
