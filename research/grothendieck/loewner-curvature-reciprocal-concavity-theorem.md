# Loewner curvature is reciprocal-square-root concavity

Put `g(x)=F'(x)>0`. The first nontrivial diagonal Loewner contact is

\[
 C(x)=\frac{g(x)g''(x)}6-\frac{g'(x)^2}4.
\]

For `h(x)=g(x)^(-1/2)`, direct differentiation gives

\[
 C(x)=-\frac13 g(x)^{5/2}h''(x).
\]

Consequently

\[
 \boxed{C(x)\ge0\quad\Longleftrightarrow\quad
 (F'(x)^{-1/2})''\le0.}
\]

Thus the first coupled local condition says that the reciprocal square root of
the source slope is concave. This is a simpler hostile falsifier than a
near-diagonal determinant: any positive-axis point where this curvature is
strictly convex disproves global Loewner positivity.

## Spectral covariance identity

Under the proposed positive spectral representation, write

\[
 g(x)=\sum_a \frac{c_a}{(x+\lambda_a)^2},\qquad c_a>0,
\]

and `M_r=sum_a c_a/(x+lambda_a)^r`. Then

\[
 C=M_2M_4-M_3^2
 =\frac12\sum_{a,b}c_ac_b p_a^2p_b^2(p_a-p_b)^2\ge0,
 \qquad p_a=(x+\lambda_a)^{-1}.
\]

This makes the curvature a literal variance/covariance determinant. It is
strict when the positive measure sees at least two distinct spectral points.
At `x=1/4` it reduces to the already certified
`16(A_0A_2-A_1^2)`.

## A useful separation

Complete monotonicity of `F'` is not sufficient. The completely monotone
function `g(x)=exp(-x)` has

\[
 \frac{gg''}{6}-\frac{g'^2}{4}=-\frac{g^2}{12}<0.
\]

The missing property is specifically Stieltjes order two, not merely alternating
derivative signs. This prevents the research program from confusing easy
one-variable positivity with the genuinely coupled spectral constraint.

## Status

The equivalence and finite positive-measure identity are algebraic theorems.
Their application to the completed Riemann source away from the quarter point
remains conjectural. They do not prove RH.

## Durable verification

- Checker: `checkers/loewner_curvature_concavity_identity.py`
- Result: `results/loewner-curvature-concavity-identity.json`
