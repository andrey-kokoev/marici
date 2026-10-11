# Internal preparation is possible if the bank mean may change

## Question

Must the history-sensitive preparation use an added reservoir? Test that
without changing the original return U or creating quadratic budget.

There is an important distinction: the prior encoded target
`(u+beta*d,-beta*d)` has a zero-mean bank and costs more than the baseline.
A different payload-preserving encoding may redistribute the existing
common-mode budget. This note tests that alternative explicitly, not as
an unnoticed replacement of the previous target.

## Internal resource already present

The baseline (u,0) decomposes into

    symmetric component: (u/2,u/2),
    antisymmetric allocation: a=(u/2,-u/2).

Both have squared norm 6. The decoder x+r sees the symmetric component but
annihilates a. The contrast mode b=(d,-d) also lies in the decoder kernel,
has squared norm 4 and is orthogonal to a.

Thus the full existing 24-coordinate carrier/bank space contains an internal
allocation degree of freedom. It is not an extra reservoir mode. It was
excluded by the earlier imposed zero-mean-bank sector.

## Conditional preparation map

Use a metric-preserving rotation on span(a,b), fixing its orthogonal
complement. A rational parametrization is

    c=(3-2t²)/(3+2t²), beta=6t/(3+2t²),
    3c²+2beta²=3.

Applied to the baseline, it gives

    x=(1+c)u/2+beta*d,
    r=(1-c)u/2-beta*d.

Exactly:

    x+r=u,
    total model budget=80.

The original U fixes a and negates b. Therefore the preparation E_t satisfies
`U E_t = E_-t U`, matching the sign reversal of the native history contrast
if the declared controller uses opposite t for the exchanged records.
The magnitude t remains supplied; this covariance does not select it.

For t=+/-1:

    x=3u/5 +/- 6d/5,
    r=2u/5 -/+ 6d/5.

The active budget is 48 and bank budget 32, totaling the original 80.
The old return swaps these two contrast signs without changing either mean.
The internal budget bounds |beta| by sqrt(3/2) in this family.

## Exact assumption boundary

This is NOT the previous preparation: the carrier common coefficient is
3/5 instead of 1, and the bank mean is 2/5 instead of zero. Its spatial
readouts must be computed afresh before importing any earlier values.

If mean(r)=0 and x+r=u are retained, then

    budget=80+(40/3)||r||².

Hence a nonzero bank in THAT sector necessarily needs added budget.
The previous reservoir accounting was correct for that target. The present
internal construction changes the allowed bank sector rather than refuting
that calculation.

It also introduces a PREPARATION operation. The original U still fixes
(u,0) and cannot generate either prepared contrast from it. No source rule
has been found selecting this rotation, its magnitude, or its physical
implementation. Norm preservation establishes model accounting, not absence
of apparatus/control costs or a calibrated physical energy law.

## Disposition

An external extra mode is not mathematically necessary if common allocation
between the existing carrier and bank is permitted to change. A source-selected
preparation coupling is still necessary. The precise next source question is
whether the intended retained-record interface admits a nonzero bank mean
and this common-to-contrast conversion—not another unconstrained gain fit.

## Verification

    uv run --with sympy python research/nima/checkers/check_internal_history_preparation.py

20 exact symbolic checks pass: full isometry, inverse, decoder preservation,
control covariance, the original budget, explicit fixture allocations, and
the zero-mean-bank obstruction. Receipt:
`results/internal-history-preparation.json`.
