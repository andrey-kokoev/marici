# One Cauchy bound controls eta Euler tails through the fifth-jet order

For

\[
 d_k(s)=\Delta^k(n^{-s})|_{n=1}
 =\frac1{\Gamma(s)}\int_0^\infty
 t^{s-1}e^{-t}(1-e^{-t})^k\,dt,
\]

take real `s` in `[0.5,0.6]` and the complex Cauchy circle of radius `0.1`.
It stays in the rectangle `0.4<=Re(z)<=0.7`, `|Im(z)|<=0.1`.

On this rectangle a deliberately crude Weierstrass-product estimate gives
`|1/Gamma(z)|<4`. Indeed, separate the `n=1` factor in the reciprocal-gamma
product and use

\[
 \log|1+w|\le\Re w+
 \frac{|w|^2}{2(1-|w|)}
\]

for the remaining `|w|<=0.35` factors. Bounding `gamma<1`, `|z|<0.71`, and
the residual inverse-square sum by its integral gives a product bound below
four.

For `sigma=Re(z)<1`, the substitution `u=e^-t` and
`-log(u)>=1-u` imply

\[
 \int_0^\infty t^{\sigma-1}e^{-t}(1-e^{-t})^kdt
 \le\frac1{k+\sigma}\le\frac1{k+0.4}.
\]

Thus Cauchy's estimate gives, for every derivative order `j`,

\[
 |d_k^{(j)}(s)|\le
 \frac{4j!10^j}{k+0.4}.
\]

After Euler depth `N`, summing the geometric weights yields

\[
 \boxed{|R_{N,j}(s)|\le
 \frac{4j!10^j}{N+0.4}\,2^{-N}.}
\]

At `N=300`, every bound through `j=6` is below `5e-83`. This single theorem
replaces separate hand-derived eta, eta-prime, and eta-double-prime estimates
and supplies the derivatives needed by the interval fifth-jet computation.

This is a transform-tail theorem only. Directed jet propagation and gamma-
sector derivative remainders remain before continuum certification; RH is not
proved.

## Durable verification

- Checker: `checkers/eta_high_jet_cauchy_tail.py`
- Result: `results/eta-high-jet-cauchy-tail.json`
