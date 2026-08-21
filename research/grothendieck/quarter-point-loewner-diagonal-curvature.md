# The first coupled Loewner contact is certified at the quarter point

Let

\[
 D(x,y)=F'(x)F'(y)-\left(\frac{F(y)-F(x)}{y-x}\right)^2,
 \qquad F(t)=(4t-1)S(t).
\]

Writing `y=x+delta` and expanding gives

\[
 D(x,x+\delta)=\delta^2\left(
 \frac{F'(x)F'''(x)}6-\frac{F''(x)^2}4
 \right)+O(\delta^3).
\]

At the distinguished point `c=1/4`, the quarter-point moments
`A_k=(-1)^k S^(k)(c)/k!` give

\[
 F'(c)=4A_0,\qquad F''(c)=-8A_1,\qquad F'''(c)=24A_2.
\]

Therefore

\[
 \boxed{\lim_{\delta\to0}\frac{D(c,c+\delta)}{\delta^2}
 =16(A_0A_2-A_1^2)>0.}
\]

The strict inequality is unconditional at this finite order: it follows by
directed interval propagation from the already certified eta-derived boxes for
`A_0,A_1,A_2`. No Riemann-zero location is used.

This resolves the apparent near-diagonal sign problem at the quarter point.
The raw two-point scan was subtracting quantities whose determinant vanishes
quadratically; its tiny negative values were below that evaluator's error.
More importantly, the calculation identifies a structural bridge: the first
nontrivial local `2 by 2` Loewner condition is exactly the first Hankel
determinant. The coupled kernel hierarchy and the moment hierarchy are two
coordinate views of the same positivity obstruction.

## Scope

This certifies only the second-order diagonal contact at `x=1/4`. It does not
establish positivity away from that point, higher contact orders, the global
Pick property, or RH.

## Durable verification

- Checker: `checkers/quarter_point_loewner_diagonal_curvature.py`
- Result: `results/quarter-point-loewner-diagonal-curvature.json`
