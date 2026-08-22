# The proposed unit-disk bound has a numerical safety factor above 200

A 96-point scan of `F'` on `|t|=1` uses the zero-free eta/digamma evaluator and
central differences in the complex `t` plane. Independent runs change Euler
depth and halve the differentiation step.

Both runs attain their largest sampled modulus at `t=-1`:

\[
 \max|F'(t)|\approx0.0927565572.
\]

The maximum pointwise discrepancy between controls is about `4.45e-10`. Thus
the proposed rigorous bound `|F'|<=20` has a sampled safety factor above 215.
Even a bound of one would have more than a factor-ten numerical margin and
would make the quarter-disk Taylor tail much smaller than required.

The scan also crosses the principal-square-root seam at the negative real
point without a visible discontinuity in the completed source. Nevertheless,
this is not proof of analyticity or a modulus bound between samples. The next
rigorous implementation should use the reflection-even centered Xi series or
complex interval boxes, so branch cancellation is structural rather than
numerical.

This reconnaissance uses no zero locations and does not prove the unit-disk
gate, continuum concavity, or RH.

## Durable verification

- Checker: `checkers/reduced_source_F_prime_unit_circle_scan.py`
- Result: `results/reduced-source-F-prime-unit-circle-scan.json`
