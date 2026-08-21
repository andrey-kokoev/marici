# The diagonal Loewner slope stays positive in the first boundary scan

For positive real `x`, the Pick condition implies the diagonal Loewner
inequality

\[
 F'(x)=K_F(x,x)\ge0.
\]

Numerically this can be approached without differentiating the source formula:

\[
 F'(x)=\lim_{y\downarrow0}\frac{\operatorname{Im}F(x+iy)}y.
\]

The zero-free eta/digamma evaluator was scanned at 57 logarithmically spaced
points from `x=10^-3` to `10^4`, using three imaginary steps. Every normalized
slope was positive. This removes the trivial small-`y` factor that made the
first raw Pick margin appear weakest near the real boundary.

The test is still numerical and weaker than full Loewner positivity. Positive
diagonal entries do not imply positive semidefiniteness of arbitrary Loewner
matrices, and transform-depth error is not enclosed.

## Next hostile test

Evaluate `2x2` Loewner determinants

\[
 F'(x)F'(y)-\left(\frac{F(y)-F(x)}{y-x}\right)^2
\]

over widely separated positive points. This is the first genuinely coupled
Pick constraint beyond monotonicity.

## Durable verification

- Checker: `checkers/reduced_source_pick_boundary_slope.py`
- Result: `results/reduced-source-pick-boundary-slope.json`

The subsequent `2x2` scan is robustly positive for widely separated points but
hits an unresolved cancellation floor near the diagonal. See
`reduced-source-loewner-two-point-conditioning.md`.
