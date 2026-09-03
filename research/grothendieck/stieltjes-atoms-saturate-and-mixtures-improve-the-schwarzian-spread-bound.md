# Stieltjes atoms saturate and mixtures improve the Schwarzian spread bound

## From the squared logarithmic derivative to the angular response

Let

\[
S(w)=\frac{C'(w)}{C(w)},
\qquad
H(w)=(w-c)S(w),
\qquad c=\frac14.
\]

Under a positive Stieltjes representation

\[
S(w)=\int_0^\infty\frac{d\rho(a)}{w+a},
\]

we obtain

\[
H'(w)=\int_0^\infty\frac{a+c}{(w+a)^2}\,d\rho(a).
\]

Writing `y=w-c` and `lambda=a+c`, each atom has the Bernstein representation

\[
\frac{\lambda}{(y+\lambda)^2}
=\int_0^\infty e^{-yt}\lambda t e^{-\lambda t}\,dt.
\]

Thus the Bernstein measure sought for `H'` is not a new object: it is the positive Stieltjes measure of the centered xi logarithmic derivative transported by the gamma-shape-two kernel `lambda t exp(-lambda t)`.

## Exact conditional-spread theorem

For one spectral rate `lambda`, two independent Bernstein variables have density proportional on the fiber `t+u=v` to

\[
t(v-t),\qquad 0<t<v.
\]

After scaling by `v`, this is the beta distribution with parameters `(2,2)`, so

\[
\operatorname{Var}(t\mid t+u=v)=\frac{v^2}{20}.
\]

A pair of unequal rates `lambda,mu`, symmetrized under exchange, multiplies this fiber density by

\[
\cosh\!\left((\lambda-\mu)(t-v/2)\right).
\]

This factor is increasing in `|t-v/2|`. Chebyshev covariance for two increasing functions of `|t-v/2|` therefore shows that it cannot decrease the conditional second moment. Hence every positive mixture of spectral rates satisfies

\[
\operatorname{Var}(t\mid t+u=v)\ge\frac{v^2}{20}.
\]

Equality holds for a single rate or for equal-rate pairs; spectral-rate mixing only improves the spread.

## Consequence

Once `S` is Stieltjes, the conditional-spread criterion is automatic and the Schwarzian numerator

\[
2H'H'''-3(H'')^2
\]

is nonnegative. The previously proposed spread inequality is therefore not an independent arithmetic gate.

The unresolved gate is exactly the source derivation of the positive Stieltjes measure `rho`. For centered xi, existence of that measure with the required pole residues is RH-equivalent. Reconstructing it from critical-line zero ordinates is circular.

## Disposition

Close the conditional-spread branch as a general consequence of a positive Stieltjes representation. Do not search for a separate theta concentration proof of the `v^2/20` bound. The only nonredundant construction is the positive Stieltjes or Gram representation from the completed arithmetic source without assuming zero locations.
