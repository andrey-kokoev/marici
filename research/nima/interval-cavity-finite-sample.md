# Fixed-sample interval certification: conditional theorem

## Result and frozen scope

The workbench's `interval-cavity-finite-sample-certification` task is constructed. Under the frozen independent-Bernoulli, static shared-factor model, **40,000 trials per arm**, six arms total (**240,000 trials**), suffice for correct unique interval identification with probability greater than 0.99. This is conservative, not sample-optimal.

The arms are reference and validation at each of three ports. Their probabilities are b_k=a_k and c_k=a_k*t_k, with a_k>=1/5 and t the signature of one of the six canonical intervals, entries 9/25 or 1. Trials within each arm are independent with that fixed probability. Cross-arm independence is not required for the union bound. Hardware and acquired-data claims are excluded.

The classifier returns an interval only when exactly one canonical signature is compatible with its confidence region. It otherwise returns no interval, distinguishing ambiguity from model inconsistency. Its error bound is an **unconditional repeated-design probability**, not a posterior or an error bound conditioned on the event of certification.

## Simultaneous rate bounds without floating-point rounding

For n=40,000 and epsilon=1/100, the two-sided Hoeffding inequality for each arm is

    P(|p_hat-p|>epsilon) <= 2 exp(-2 n epsilon^2).

There are six arms, so the probability that any rate bound fails is at most 12 exp(-8). The checker avoids evaluating a rounded logarithm or exponential: the positive Taylor sum S=sum_(k=0)^8 8^k/k! is strictly less than exp(8), hence

    12 exp(-8) < 12/S = 3780/556403 < 1/100.

Thus all six exact rational boxes [p_hat-epsilon,p_hat+epsilon], clipped to [0,1], contain their true probabilities simultaneously with probability greater than 0.99. This analytic inequality, not simulations, establishes coverage. The fixed design does not allow outcome-dependent continuation, arm sizes or epsilon selection.

## Exact classifier

For each port form

    B_k=[max(1/5,b_hat-epsilon), min(1,b_hat+epsilon)],
    C_k=[max(0,c_hat-epsilon), min(1,c_hat+epsilon)].

An empty B_k means no model-compatible signature. Otherwise a candidate t_k>0 is compatible precisely when

    B_k intersection [C_k.lower/t_k, C_k.upper/t_k]

is nonempty. This is an exact existential test for a shared factor a_k with a_k in B_k and a_k*t_k in C_k. A three-coordinate candidate is retained only if all three tests succeed. The code uses rational arithmetic throughout and never divides by a reference count.

The input API validates all six distinct arms, integer click/no-click counts summing to exactly n, fixed attempted counts and complete port coverage. These are mathematical record checks, not provenance verification of an experiment.

## Why the good event always yields the correct unique interval

On the simultaneous good event the true factors satisfy all six boxes, so the true signature is retained. Any other compatible b',c' differs from the true b,c by at most 2 epsilon. Since b>=a_min=1/5 and c=b*t,

    |c'/b'-t| <= 2 epsilon (1+t)/(a_min-2 epsilon)
                <= 4 epsilon/(a_min-2 epsilon)
                =2/9.

The distinct canonical coordinate values differ by 16/25, greater than 2/9. Thus no compatible candidate can have a different value in any coordinate. Every distinct interval differs in at least one coordinate, proving uniqueness. Therefore both an incorrect certification and a failure to certify the correct interval imply failure of the simultaneous good event, and each has probability less than 0.01 under the model.

This extends the earlier point-ratio bound correctly: confidence-region candidates can be another epsilon away from the estimates, so the old single-epsilon bound cannot simply be reused unchanged.

## Ambiguity and model inconsistency

At these tight fixed bounds, even arbitrary valid count packets cannot have two compatible canonical signatures. Indeed each B has width at most 2 epsilon and lower endpoint >=a_min. The gap between possible high and low response ranges is at least

    (1-9/25)*a_min - (9/25)*2 epsilon > 2 epsilon,

larger than the width of C. Each coordinate can fit at most one canonical value. A production packet therefore either uniquely certifies an interval or reports model inconsistency with no interval.

The requested ambiguous-region test uses the generic region engine with a wider diagnostic radius 1/5; all six intervals are then compatible and the engine abstains. That diagnostic is explicitly **not** a certificate issued under the fixed epsilon=1/100 protocol. Zero reference counts give an empty B and model-inconsistent abstention. Neither inconsistency nor abstention alone proves the model false: the confidence event can fail.

## Exact verification and drift limit

The checker compares the signatures against the completed instrument response receipt. It checks 1,536 exact good-event corner packets covering every interval, minimum factors, mixed factors and the unit boundary. These regress, rather than replace, the analytic uniform proof.

Hostiles include incomplete/duplicate arms, negative or boolean counts, wrong attempted counts, missing no-clicks, zero references, a noninterval mask and a broad ambiguous region.

A separate distributional alias shows why the static shared-factor premise matters. True interval [1,2] with reference factors

    (1/4,1/2,3/4)

and changed validation factors

    (25/36,1/2,27/100)

has exactly the same six reference/validation probabilities as stationary interval [2,3] with the original reference factors. Every factor remains in [1/5,1]. The classifier can therefore identify [2,3] even though the drifted process is [1,2]. This refutes extending the theorem to unrestricted between-arm factor drift. No classifier using only these six count distributions can uniformly distinguish the aliased pair; collecting more trials does not remove this alias.

## Reproduction

    python research/nima/checkers/check_interval_cavity_finite_sample.py

Receipt: `results/interval-cavity-finite-sample.json`.

Completed within the frozen mathematical scope. A bound on factor drift would be a separately specified model extension, not a hardware prerequisite and not automatically selected as the next task. No causal-geometry claim is promoted.
