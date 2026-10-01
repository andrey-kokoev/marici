# Schedule mixing reaches equal comparison response

## Declared schedule

Use the closed comparison/record exchanges H_i from
[137-closed-record-equilibrium.md](137-closed-record-equilibrium.md). At each
step wait with probability1/2; otherwise choose comparison i with probability
p_i, where every p_i>0 and sum p_i=1. Choice is independent of the current state.
Each realized operation is orthogonal and preserves the full budget. The
schedule-averaged zero-mean covariance evolves by

    T(C) = C/2 + sum_i p_i H_i C H_i^T/2.

No additive amplitude noise, reset, or external quadratic-budget injection
is used. Scheduling randomness and averaging are explicit model assumptions.
Their physical implementation and thermodynamic costs are not calculated here.

## Convergence argument

On real symmetric matrices with the Frobenius inner product, conjugation by
an orthogonal reflection is a self-adjoint involution. Each half-identity plus
half-conjugation is therefore an orthogonal projector. T is their positive
weighted average, with spectrum in[0,1]. Its1-eigenspace is the intersection
of their fixed spaces: covariances invariant under every comparison. Every
other eigenvalue is strictly below1 in this finite-dimensional space, so T^n
converges to the orthogonal projector onto that common fixed space. The idle
probability removes possible period-two eigenvalues.

The prior connected-normal argument identifies that space. Let F project
onto the16-dimensional common fixed state space and A=I-F onto the137-dimensional
span of comparison normals. For initial covariance C0,

    C_infinity = F C0 F + [tr(A C0)/137] A.

Cross terms decay. The fixed-state covariance is retained; the active covariance
becomes isotropic. The limit does not depend on the positive probabilities p_i,
although convergence rates do. This requires all comparisons to remain enabled
and choices to be state-independent.

For positive active budget, each mismatch w_i-u_i^T q has limiting variance

    2 tr(A C0)/137.

Its fraction of the sum of all137 mismatch variances is1/137. If the active
budget is zero, all those responses vanish and the normalized ratio is undefined.
Unequal event sampling can still weight measured event averages differently;
equality of per-comparison response is distinct from frequency of observation.

## Test from empty records

Start with unit covariance on the16 carrier coordinates and zero records.
The total budget is16. For uniform comparison choice:

| Random-schedule steps | Frobenius distance to predicted covariance | Carrier budget |
|---:|---:|---:|
| 1 | 3.5295776834 | 15.5 |
| 137 | 0.849347774148 | 4.42200697293 |
| 1000 | 0.0630778780132 | 2.61592990566 |
| 2000 | 0.00555106224965 | 2.57316344058 |
| Limit | 0 | 2.56918462188 |

Initial active budget is12.2306345439. Limiting mismatch variance per slot is
0.178549409401. The checker also verifies that the predicted limit is stationary
for unequal probabilities proportional to1,...,137. The2000-step computation
checks convergence progress, not exact arrival at the limit; the limit follows
from the finite-dimensional spectral argument.

## Structural meaning and physical scope

Strong comparison-invariant equilibrium can arise from mixing among closed
record exchanges instead of imposing isotropy at preparation or continually
injecting independent noise. Individual histories remain reversible; the
covariance convergence is an ensemble statement after averaging over schedules.
No deterministic trajectory is asserted to settle to a single state.

This supplies a dynamical route to equal normalized mismatch response for the
specified operation family. It leaves open whether the carrier implements that
family and scheduling law, and whether electromagnetic coupling measures this
normalized response. It does not derive the observed decimal correction or a
physical time/energy scale.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_137_random_schedule_equilibrium.py

The checker verifies the candidate limit, uniform response, trace conservation,
monotone covariance error over2000 steps, preservation of fixed covariance,
and stationarity with an unequal positive comparison distribution. NumPy uses
explicit tolerances. The convergence proof and its assumptions are stated above.
