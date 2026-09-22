# Single-valley compatibility makes the Abel relaxation sharp

## DPC disposition: corroborated

For the fixed N=1e6 combined kernel K=K_plus+K_minus, the checker certifies
37 negative-derivative whole cells and 400 positive-derivative whole cells.
The only remaining box is

    [4369568624007/274877906944, 8739137248015/549755813888],

approximately [15.896398050270363,15.896398050272182]. K'' is strictly positive
on this entire box, and K' has opposite strict signs at its endpoints.
There is exactly one critical point there. The cells exhaust the domain
from an outward enclosure of log(1e6) through 64. Beyond 64,
K=(B0-J64)exp(-7u/2), with B0-J64<0, so K'>0 forever.
Thus K decreases to one minimum and then increases to zero.

## Matching primal and dual

The pointwise Abel bound for any 0<=A<=M is

    -integral K' A >= -integral_{u_*}^infinity K' M.

The schedule A=0 below u_* and A=M at and above u_* is nondecreasing,
because M is positive and increasing. It has A(log N)=0 and obeys the
capacity constraint. Its jump at u_* is a permitted positive atom.
It attains the bound exactly. This gives a feasible continuum primal and
a matching pointwise dual, not merely overlapping numerical estimates.

Closed exponential-polynomial antiderivatives, evaluated with the certified
root box, enclose the shared sharp extremum by approximately

    [-3.075338645573230e-7, -3.0753386455607574e-7].

The finite cumulative primal/dual sandwich is separately checked to contain
this interval. This is a proof for the continuous Chebyshev relaxation,
not a claim that its extremizer can be a prime-power measure.

## What has been resolved together

1. The separate kernels' transition and critical boxes do not imply an
   incompatible combined mass schedule. The combined objective has a simple
   single-valley shape.
2. Independent pointwise freedom in A does not lower this objective beyond
   what a genuine cumulative measure already achieves.
3. A strict coupling gap for this lower-bound objective is ruled out under
   the frozen Chebyshev relaxation. Finer cumulative optimization cannot
   improve its exact minimum.
4. This does not rule out tighter interval quadrature or other evidence.
   It specifically closes the proposed recovery of a missing cumulative
   compatibility constraint as the source of improvement here.

## Secondary threshold test

At the admissible relaxed extremizer, the unchanged finite pairing and
other C contributions give approximately

    C in [1.9721821213657262, 1.9721821321902966].

Using the unchanged theta/H/L intervals, the exact upper gain at this
extremizer is below the frozen midpoint threshold. Consequently no universal
lower bound over THIS admissible-measure family can certify that threshold.
Additional restrictions excluding this measure are needed to resolve the
midpoint through this route. This is NOT a source-infeasibility certificate:
the actual prime tail is not shown to realize the relaxed extremizer.
The existing actual-source midpoint disposition is not changed.

## Structural synthesis

Preserving a dependency improves an extremum only when the relaxed
extremizing behavior violates that dependency. Here it does not: all the
budget can be held until the valley and then released without any forbidden
reset. In the operational observer examples, a provenance bit is likewise
unnecessary when the relevant distinction already survives in observable
continuations. Structural necessity for a model and quantitative relevance
for a particular objective are different claims.

## Reproduction

    uv run --with python-flint python research/grothendieck/checkers/check_combined_tail_single_valley.py

Artifact: `results/combined-tail-single-valley.json`.
The command first freshly replays the cumulative primal/dual checker, checks
its owning input hashes, proves the shape using whole-cell Arb evaluation,
uses an interval Taylor coefficient for K'', computes the closed integral,
and performs exact rational threshold comparisons. Numerical kernel code
is shared with the cumulative checker; no independent implementation is
claimed. No pre-existing calibration branch is overwritten by this test.
