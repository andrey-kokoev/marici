# Minimal tail cut interfaces can be piecewise, not linear

## Frozen structural test

Use a rational analytical control, not the actual fixed-hat kernel. The
prefix coordinates p,q,t and suffix y lie in [0,1]. Freeze the crossing rows

    p+y <= 1,
    q+2y <= 2,
    p+q+3y <= 3,
    2p+2y <= 2,
    p+y <= 2.

The terminal objective is F=t-y. Declared continuations choose a rational
y and observe admission and, when admitted, the objective. Future finite
linear constraints on y may also be accumulated. New reads of p or q are
NOT in this continuation language.

This finite rational family is a controlled instance of analytical cut
compression. It supplies a continuum proof and exact finite checks, not a
new claim about the prime-tail midpoint.

## Exact continuation equivalence

The third row is the sum of the first two, the fourth duplicates twice the
first, and the fifth weakens the first. Nonnegative implication certificates
prove their redundancy for every real prefix, not just sampled points.
The residual feasible suffix set is exactly

    0 <= y <= h,       h=min(1-p,1-q/2).

Therefore the interface (h,t) preserves every declared completion's admission
and terminal value. It also determines the effect of every future conjunction
of constraints on y.

Conversely, if two h values differ, a rational y strictly between them is
admitted by only one prefix. If h agrees but t differs, y=0 is admitted by
both and gives different objective values. Thus

    prefixes are continuation-equivalent iff their (h,t) agree.

This characterizes the coarsest equivalence over the whole real prefix cube.
No particular future extremum was used to define the interface.

## Why a fixed linear basis is not minimal

Suppose a linear summary L(p,q,t) is sufficient. For any v in its kernel,
small perturbations by v preserve L inside either active open region.

- On p>q/2, h=1-p; sufficiency forces v_p=v_t=0.
- On p<q/2, h=1-q/2; sufficiency forces v_q=v_t=0.

Both regions have nonempty interior. Hence ker L is zero and rank L=3.
A two-field PIECEWISE interface is sufficient, but no rank-two linear
summary is sufficient. Eliminating algebraically dependent rows alone would
miss this compression: the relevant residual constraint depends on which
bound dominates at the current prefix.

There is also a precise continuous minimality statement. The section
(p,q,t)=(1-h,0,t) realizes every (h,t) in [0,1]^2. Any sufficient continuous
real-valued scalar would restrict to a continuous injection of this square
into the line. This is impossible: its boundary circle would embed into a
compact interval, but removing a point from a circle leaves it connected,
whereas removing an interior point of an interval disconnects it. Thus two
Euclidean coordinates are minimal among continuous sufficient summaries.
This is not a lower bound on arbitrary discontinuous encodings into reals.

## Objective-only compression fails

Compare prefixes

    (p,q,t)=(1/2,0,1/2) and (0,0,1).

Their present minima t-h are both zero, but y=3/4 is rejected by the first
and admitted by the second. Preserving the current extremum does not preserve
future refinement admission or its effect on that extremum.

Conversely, (1/2,0,1/2) and (0,1,1/2) have different p,q values and different
active crossing rows, but identical (h,t)=(1/2,1/2). They genuinely merge for
the declared language. An added historical audit p<=1/4 would distinguish
them; admitting that extension would require additional retained information.

## Composition of further evidence

After suffix-bound refinements, retain the residual interval [ell,u] and t.
A new lower or upper bound intersects that interval; an empty interval remains
empty. This is persistent constraint intersection, not a reset to the original
fiber. The interval carries the shared suffix witness through refinements.

The two-field result is for the ORIGINAL cut where ell=0. After arbitrary
lower-bound frames, the current residual representation can require the
additional ell coordinate. No fixed two-field budget for every enriched
language or later cut is claimed. Retrospective marked-cut queries would
also require retaining their cut relations or frame history.

## Exact checks

The producer and independent Fraction verifier establish:

- 125 rational-grid prefixes and 35 continuation classes;
- 240 equivalent pairs;
- explicit separating completions for all 7,510 inequivalent pairs;
- 6,860 quotient two-frame checks;
- direct concrete-prefix checks for the same refinement language;
- exact nonnegative certificates for all three redundant rows;
- omission witnesses for both retained fields;
- the optimum-only compression counterexample;
- the rank-three linear obstruction's independent coefficient directions.

Finite enumeration checks the implementation. The residual-interval formula,
necessity argument and rank obstruction prove the continuum claims. The
continuous dimension lower bound uses the elementary topological argument
above; it is not inferred from a finite grid or mechanically checked topology.

## Structural synthesis

Dependency completeness says which quantities may matter. Continuation
minimality asks which combinations actually matter at the current cut.
The latter can be piecewise because inequalities can mask one another.
Thus a dependency-complete carrier is a sound starting point, but its
smallest behavioral view need not be a fixed linear projection of that carrier.

For our lane, a productive future reduction should preserve the residual
feasible suffix relation and objective offset, not merely row rank or the
current optimized value. This result establishes the mechanism on a frozen
control; applying it to the actual prime-tail constraint family remains open.

## Reproduction

    python research/grothendieck/checkers/construct_minimal_tail_cut_interface.py
    python research/grothendieck/checkers/verify_minimal_tail_cut_interface.py

Contract: `results/minimal-tail-cut-interface-contract.json`.
Packet: `results/minimal-tail-cut-interface.json`.

The verifier imports neither the constructor nor an optimization package.
