# Directed C-tail branch: quantitative enclosure, midpoint unresolved

The fixed N=1,000,000 calculation now has a separate, hash-bound C-only branch,
merged with unchanged theta/H/L data and replayed against the frozen midpoint.
It does not overwrite the old pairing or midpoint-ladder calibration.

## Bound

Let a=log(N), A(u)=psi(exp(u))-psi(N). Positivity of the Mangoldt measure and
the owning binomial Chebyshev proof imply

    0 <= A(u) <= M(u) = 2 log(2) exp(u) + u + log(2) - psi(N).

For either continuous kernel, integration by parts on the entire tail gives

    sum_{n>N} Lambda(n) K(log(n)) = -integral_a^infinity K'(u) A(u) du.

There is no initial boundary term: A(a)=0. The boundary at infinity vanishes
because both kernels are constant multiples of exp(-7u/2) beyond 64.
Knot boundary terms cancel by continuity. No local monotonicity or unproved
prime-distribution cancellation is assumed.

Every finite cell encloses -K' over its WHOLE interval, multiplied by
[0,M(right)] and the exact rational cell width. Thus positive derivative
contributions are one-sided nonnegative, negative contributions one-sided
nonpositive, and ambiguous cells retain both sides. Arb may widen these
one-sided intervals during accumulation; this is conservative. The mesh is
at most 1/512 and includes outward rational endpoints of all retained sign
and derivative boxes. The three critical boxes are charged absolutely.
The tiny outward rounding strip below log(N) uses the zero extension of A.

For c=B0 or -J(64), the suffix is enclosed by [s c W,0], where s=7/2 and

    W = 2 log(2) exp((1-s)64)/(s-1)
        + exp(-s64) ((64+log(2)-psi(N))/s + 1/s^2).

Both c are proved negative. This is an analytic infinite-suffix bound.

This is a global Abel variation enclosure, not a claim that each positive
kernel sector has a strictly positive guaranteed mass. The Chebyshev
majorant alone gives no such lower mass. Shared cumulative mass is not
charged once per sign cell; it enters through the derivative integral.

## Result

Approximately:

- C in [1.97218206008525, 1.97218306645693].
- Gain in [6.280451053885102e-193, 6.280456250665598e-193].
- Frozen threshold 6.280452051525288e-193.
- Status: UNRESOLVED.

Exact rational endpoints, finite pairing evidence, critical-box charges and
input/code hashes are in `results/directed-C-only-Abel-branch.json`.
The existing symmetric C enclosure is intersected with the new enclosure;
an empty intersection would fail, not certify source infeasibility.
`results/directed-Abel-midpoint-replay.json` records the actual task-engine
replay using `three-channel-source-task-calibration-directed-Abel.json`.

## Verification

    uv run --with python-flint python research/grothendieck/checkers/check_directed_C_tail_branch.py

Passes fresh numerical reconstruction, input hash checks, separate exact
endpoint intersection checks, exact theta gain reconstruction and threshold
classification. Numerical reconstruction shares the producer implementation;
this is NOT an independent analytic implementation of Abel integration.

The directed-tail branch is now quantitative, not another work ledger.
It improves the enclosure but does not resolve the midpoint. This does not
prove no stronger signed-tail method at N=1e6 can succeed. In particular,
using A as an arbitrary pointwise value in [0,M] loses its cumulative-measure
constraints and can overestimate its signed variation contribution.
