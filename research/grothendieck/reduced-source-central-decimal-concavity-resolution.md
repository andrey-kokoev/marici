# High precision resolves the apparent central-boundary concavity failures

The binary64 broad scan produced unstable negative reciprocal-slope chord gaps
near `t=0`. A new evaluator keeps the coupled completed expression intact in
the central coordinate

\[
 s=\frac12+\sqrt t
\]

and performs all real eta, digamma, logarithmic-derivative, and finite-
difference arithmetic with 70--80 decimal digits.

Twenty-one arithmetic-midpoint chords with endpoints from `10^-8` through
`10^-2` were tested. Every gap is positive in both runs. The smallest is

\[
 3.6497\ldots\times10^{-20}
\]

on the chord from `10^-8` to `10^-7`. A control simultaneously changes decimal
precision from 70 to 80 digits, Euler-transform depth from 120 to 132, and
relative differentiation step from `10^-3` to `5*10^-4`. The maximum change
over all chords is only about `1.84e-26`, leaving a conservative positive
margin about `3.6497e-20`. This value uses exact rational Bernoulli
coefficients and is superseded by the directed interval certificate in
`central-reciprocal-slope-interval-certificate.md`.

## Interpretation

The small negative values in the binary64 boundary scan were numerical
cancellation. No central-boundary counterexample survives high precision. In
combination with the previous middle and tail scans, reciprocal-square-root
concavity has now survived controlled numerical attacks from `10^-8` through
`10^8`.

This remains an arbitrary-precision numerical result, not directed interval
arithmetic: the Euler-transform and digamma truncation errors are controlled by
cross-run stability rather than rigorous outward-rounded remainders. The next
upgrade is to attach explicit remainder bounds to this same central evaluator.
It does not prove global concavity, full Loewner positivity, or RH.

## Durable verification

- Checker: `checkers/reduced_source_central_decimal_concavity.py`
- Result: `results/reduced-source-central-decimal-concavity.json`
