# A second elementary anchor reaches complex Pick radius seventeen halves

At `t=81`, the centered coordinate is `s=19/2`. Log-convexity and the gamma
recurrence give

\[
 \Gamma(19/4)<\frac{10395}{512}.
\]

Together with `pi^(-19/4)<1/162` and `zeta(19/2)<21/20`, the completed source
formula proves an explicit upper bound for `Xi(19/2)`. Dividing by the directed
lower bound for `Xi(1/2)` yields

\[
 C(81)<13.                                               \tag{1}
\]

This bounds every unknown normalized theta coefficient from degree seven
onward by a tail carrying the factor `13/81^7`. Combining it with the first
six directed coefficients and preserving the logarithmic denominator proves

\[
 \boxed{\operatorname{Re}F'(t)>0.008
 \qquad (|t|\le17/2).}                                  \tag{2}
\]

The independently certified `C(9)<2` inequality keeps the source zero-free on
the larger disk `|t|<=9`. Vertical integration therefore gives

\[
 \boxed{|t|\le17/2,\quad\operatorname{Im}t>0
 \Longrightarrow\operatorname{Im}F(t)>0.}               \tag{3}
\]

No zero locations are used. The remaining uncertified part of the current
zero-free source disk is the thin annulus `17/2<|t|<=9`. RH is not proved.

## Durable verification

- Checker: `checkers/central_complex_pick_radius_seventeen_halves_certificate.py`
- Result: `results/central-complex-pick-radius-seventeen-halves-certificate.json`
