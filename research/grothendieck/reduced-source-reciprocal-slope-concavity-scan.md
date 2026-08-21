# A derivative-light source scan survives the first concavity attack

The curvature theorem replaces unstable third differentiation by the chord
condition

\[
 \frac1{\sqrt{F'((x+y)/2)}}\ge
 \frac12\left(\frac1{\sqrt{F'(x)}}+\frac1{\sqrt{F'(y)}}\right).
\]

This requires only first derivatives, estimated through normalized imaginary
boundary values of the zero-free eta/digamma source evaluator.

On nine endpoints from `0.01` through `100`, all 36 arithmetic-midpoint chord
tests are positive in two runs using different transform depths and boundary
heights. The smallest gap occurs on `[0.01,0.03]`:

- baseline gap: about `1.797e-9`;
- control gap: about `1.770e-9`;
- maximum baseline/control discrepancy over the entire scan: about `6.08e-11`.

Even subtracting that global discrepancy leaves a positive margin of about
`1.71e-9`. Unlike the third-derivative scan, this test is numerically stable
under its stated controls.

## Meaning and scope

No sampled chord violates the first coupled local consequence of Loewner
positivity. This is stronger evidence than pointwise `F'>0` because it compares
three source locations and tests the covariance curvature without explicitly
differentiating it three times.

It is still a finite, non-interval scan. It neither proves concavity between
the sampled points nor establishes the full matrix-valued Loewner hierarchy.
It does not prove RH.

## Durable verification

- Checker: `checkers/reduced_source_reciprocal_slope_concavity_scan.py`
- Result: `results/reduced-source-reciprocal-slope-concavity-scan.json`
