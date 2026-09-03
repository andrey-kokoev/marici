# The prime form linearizes as an indefinite multiplier, not a Gram map

## Question

Can the quadratic order-space encoding be replaced by a map linear in the Hankel polynomial?

## Exact finite-cutoff linearization

Fix `t,h>0` and define

\[
d\rho_{t,h}(u)=\frac1{2\pi}e^{-tu^2}(1-e^{-hu^2})du.
\]

The evaluation map

\[
(V_hp)(u)=p(e^{-hu^2})
\]

is linear. At prime-power cutoff `N`, define the real bounded multiplier

\[
W_{P,N}(u)
=-\sum_{2\le n\le N}\Lambda(n)n^{-1/2}\cos(u\log n).
\]

Then the truncated prime form has the exact representation

\[
Q_{P,N}(t,h;p)
=\langle V_hp,M_{W_{P,N}}V_hp\rangle_{L^2(\rho_{t,h})}.
\]

Thus the desired linearization already exists at every finite cutoff.

## Why it is not a Hilbert Gram factorization

The multiplier `W_(P,N)` changes sign. The representation is therefore an indefinite quadratic form, equivalently a Krein-space factorization after writing

\[
W_{P,N}=|W_{P,N}|^{1/2}
\operatorname{sgn}(W_{P,N})
|W_{P,N}|^{1/2}.
\]

It is not a positive norm square. Replacing the sign operator by the identity changes the form and erases the prime oscillation.

This is the linear counterpart of the earlier quadraticization obstruction: direct Hilbert norms create positive diagonal contributions or cross-prime terms, whereas the exact single-prime cosine sum is retained by an indefinite multiplier.

## Infinite-cutoff obstruction

The coefficients do not have finite total variation:

\[
\sum_{n\ge2}\Lambda(n)n^{-1/2}=\infty.
\]

Hence `W_(P,N)` does not converge by absolute summation to a bounded multiplier or finite signed measure. Gaussian integration against each polynomial matrix coefficient can converge because Fourier transforms decay in `log n`, but weak convergence on the polynomial core does not establish a closable multiplication operator.

The completed gamma contribution must be added before asking for semiboundedness. Sectorwise prime positivity is already false, so no closure argument may take an absolute value or close the prime form independently and then infer the completed lower bound.

## Exact remaining operator problem

Let `q_(Gamma+P)` denote the coupled form on the polynomial image of `V_h`. The required theorem is now one of the following:

1. `q_(Gamma+P)` is represented by an order-zero signed measure absolutely continuous with respect to a positive reference measure, with density bounded below; or
2. it is a genuinely nonlocal closable form whose closure is semibounded on the original moment norm.

The order completion and Gaussian graph-domain embedding may provide a form core or auxiliary estimate, but they do not change the sign multiplier into a positive Gram operator.

## Strongest falsification attempt

Finite cutoffs prove neither closability nor a cutoff-uniform lower bound. Indeed `||W_(P,N)||_infinity` is bounded above only by the divergent coefficient sum. Any proposed limiting operator must exploit cancellation jointly with the gamma term and cannot follow from uniform multiplier norms.

## Disposition

The linear-map blocker is resolved at finite cutoff: `V_h` is the canonical linear map. The obstruction is not linearity but the existence and semibounded closure of the coupled infinite multiplier/form. Further Gram-map searches that omit the sign operator are mis-typed.