# Flavor robustness-normalization no-go

## Question

Is WP994's joint radius \(1/24697\) an intrinsic physical tolerance?

## Claim boundary

The calculation varies only the formal target scale. It does not authorize
larger actuator ranges, assign a control cost, or infer detector resolution.

## Scale family

Replace WP993's three targets by

\[
(-L,0),\qquad (L,0),\qquad (0,L),\qquad L>0.
\]

They remain inside the same three strict preparation regions. The exact
symmetric error radii become

\[
r_{\rm commuting}(L)=\frac{3087L}{3088},\qquad
r_{\rm rank\text{-}two}(L)=\frac{24696L}{24697},\qquad
r_{\rm full\text{-}rank}(L)=\frac{L}{24697}.
\]

Thus

\[
r_*(L)=\frac{L}{24697}.
\]

There is no scale-independent finite maximum: increasing \(L\) increases the
formal margin without changing the region geometry. The case \(L=2\) is the
smallest exact hostile to treating WP994's unit-target value as intrinsic.

## Disposition

WP994 remains correct conditional on its unit-target normalization, but its
numerical radius is not a physical apparatus threshold. A robustness claim
requires a source-derived actuator normalization, admissible control range, or
cost/support constraint that fixes \(L\). Without that constructor, enlarging
the formal margin is algebraic rescaling rather than improved experimental
control.

## Verification

- `research/flavor/checkers/wp995_robustness_normalization_no_go.py`
- `research/flavor/results/wp995_robustness_normalization_no_go.json`
