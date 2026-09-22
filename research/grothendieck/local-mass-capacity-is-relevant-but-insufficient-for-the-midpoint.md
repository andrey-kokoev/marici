# Local mass capacity is relevant but insufficient for the midpoint

## DPC result

The strict-improvement prediction is corroborated. Adding integer support
and the elementary atom bound 0<=mass(log n)<=log n raises the infimum above
the sharp continuous Chebyshev relaxation by at least

    2.0518686562692935e-11.

A support-only admissible measure comes within

    7.403055424949447e-15

of that continuous optimum. Thus the certified gap is genuinely a local
capacity effect, not merely the displacement of the minimum from the integer
lattice. The gap applies uniformly to every capped measure and excludes
approaching sequences, not just the old extremizing atom.

A separate explicit infinite capped measure still has gain below the frozen
midpoint threshold. Consequently these elementary arithmetic constraints,
although relevant, are insufficient to resolve the midpoint by a universal
lower bound over this relaxed family.

No prime enumeration beyond N=1e6, new prime-distribution hypothesis, or
actual-source infeasibility conclusion is used.

## Finite cut dual: why the gap is strict

Let u_* be the certified single minimum of K=K_plus+K_minus, with root box
[u_-,u_+]. Retain M=U(exp u)-psi(N). The exact excess over the old optimum is

    integral_a^{u_*} (-K') A + integral_{u_*}^infinity K' (M-A).

Every term is nonnegative. Freeze L=7,800,000 and R=8,200,000, with
log L<u_-<u_+<log R. Integer support and atom caps give

    A(log R)-A(log L) <= B = (R-L) log R.

Set t=A(log L), and define

    alpha = K(log L)-K(u_-)>0,
    beta  = K(log R)-K(u_+)>0,
    D     = M(u_+)-B>0.

Restrict the first slack integral to [log L,u_-] and the second to
[u_+,log R]. Monotonicity of A and M implies

    excess >= alpha*t + beta*max(0,D-t)
           >= min(alpha,beta)*D > 0.

This is a finite cut certificate with exact rational lower coefficients.
It says there is not enough local arrival capacity to avoid BOTH premature
mass before the valley and missing mass after it. All other regions,
including the infinite suffix, contribute nonnegative slack and need no
numerical truncation in this dual proof.

## Support-only control

The minimum satisfies ceil(exp u_*)=8,011,576. Put no mass before that integer,
and thereafter set A(u)=M(log floor(exp u)). This is an admissible uncapped
integer-supported measure over the entire infinite tail.

The initial delay costs at most M(log n0)[K(log n0)-K(u_*)]. Subsequently the
capacity missed by rounding down is at most 2log(2)+1/n0. Since K'>0 there,
the remaining cost is bounded by

    (2log(2)+1/n0) (-K(log n0)).

These bounds include the infinite suffix analytically. Their sum is far
smaller than the capped-family gap, even accounting for the root enclosure
and the old optimum's interval width.

## Capped feasible primal and the secondary threshold test

Use the integer cumulative schedule

    B_n=0                              for n<=L,
    B_n=min(M(log n),15(n-L))           for n>L.

Both branches are increasing and have increments at most 15; min preserves
this bound. Since log n>15 for n>L, each atom is legal. B_n<=M(log n) by
construction. The ramp catches up with M before n=9,000,000 and remains
above it thereafter, so B_n follows the capacity branch forever afterward.
These guards are checked with interval arithmetic.

Comparison with the continuous extremizer gives a total excess upper bound
1.5588922903801495e-9. The infinite lattice-rounding contribution is bounded
by 15*(-K(u_*)). No infinite sum is truncated without a bound.

Together, the primal and dual enclose the capped infimum approximately by

    [-3.075133458707603e-7, -3.0597497226569556e-7].

They are NOT matching sharp optimality certificates for the capped problem.
The exact capped optimum is not computed. They do settle strict separation
and exhibit a feasible witness relevant to the task.

Using upper endpoints for every unchanged finite pairing and theta/H/L
contribution, this capped witness has

    C <= 1.972182133749189,

and its exact upper gain is below the frozen midpoint threshold. This is a
counterexample to universal certification over the NEW RELAXED family, not
a claim that the actual primes realize this measure. The actual-source
status remains unchanged.

## Structural synthesis

Three information levels are now separated:

1. Independent pointwise capacity and cumulative compatibility have the same
   minimum for the single-valley objective: the extra dependency is redundant.
2. Local arrival capacity changes that minimum: it prevents immediate release
   of all stored cumulative budget at the optimum location.
3. The elementary local capacity still admits a task-defeating measure.
   Relevance of a dependency is not the same as sufficiency for a decision.

The useful observer distinction is therefore not another memory of the
past. It is a constraint on which mass schedules can actually be developed
from that past. The finite cut inequality detects its relevance without
solving every microscopic scheduling choice.

## Reproduction and boundaries

    uv run --with python-flint python research/grothendieck/checkers/check_local_tail_capacity_gap.py
    uv run --with python-flint python research/grothendieck/checkers/verify_local_tail_capacity_gap.py

Artifact: `results/local-tail-capacity-gap.json`.

The producer freshly replays the single-valley and cumulative certificates.
The separate verifier checks hash bindings, rational dual inequalities,
separation from the support-only control, capped-primal guards, exact gain
comparison, and rejection of a corrupted gap. It does not independently
reimplement the owning interval kernel evaluation. Existing calibration
branches are not overwritten with a purported actual-source verdict.
