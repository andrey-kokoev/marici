# qRB microstep 133: rank-two Gaussian Gram gate

For two Gaussian translates `a<b`, positivity of the heat-regularized Gram is equivalent to

$$
\Theta(t,a)\Theta(t,b)
\ge
 e^{-t(a-b)^2/2}
\Theta\left(t,\frac{a+b}{2}\right)^2.
$$

Equivalently, wherever `Theta` is positive,

$$
\log\Theta(t,\xi)+t\xi^2
$$

must be midpoint-convex in `xi`.

This is the first genuinely coupled spectral-observer test. Diagonal positivity alone is insufficient. It remains independent of the relative carrier construction and is the first positivity gate for an ordinary Gaussian Gram realization.

Status: rank-two gate explicitly reduced to midpoint convexity; no global positivity claim.
