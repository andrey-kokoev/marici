# Negative Weil mass is a monotone defect entropy with universal contact onset

For a completed Gaussian character kernel `U(sigma,xi)` that is coercive in
`xi`, define

```
N(sigma)=integral_R [-U(sigma,xi)]_+ dxi.              (1)
```

The negative set is compact at every positive variance, so `N` is finite even
though `U` itself grows logarithmically at character infinity.

Since `partial_sigma U=partial_xi^2 U`, the convex-function/Kato inequality
for `r -> [-r]_+` gives

```
N(sigma_2)<=N(sigma_1),       sigma_2>sigma_1.         (2)
```

For a smooth negative interval `(a,b)`, this follows directly from

```
d/dsigma integral_a^b (-U) dxi
=-[partial_xi U(b)-partial_xi U(a)] <=0.               (3)
```

The left crossing has negative slope and the right crossing positive slope.
Approximation handles tangencies.

Thus `N` is an exact monotone defect entropy. It vanishes throughout the
broad-positive regime. RH is equivalent to its vanishing at every positive
variance, subject to the established Gaussian limit to the Weil distribution.

## Universal generic onset

Suppose a first contact at `(sigma_*,xi_*)` is nondegenerate, with

```
kappa=(1/2)partial_xi^2 U(sigma_*,xi_*)>0.             (4)
```

The heat equation gives `partial_sigma U=2kappa` there. Locally,

```
U=2kappa(sigma-sigma_*)+kappa(xi-xi_*)^2+higher order. (5)
```

On the sharper side `delta=sigma_*-sigma>0`, the newborn negative island has
width `2sqrt(2delta)` and mass

```
N_local=(8sqrt(2)/3)kappa delta^(3/2)+o(delta^(3/2)). (6)
```

The exponent `3/2` is universal for generic heat tangency. Higher-order
contacts have different exponents and require additional vanishing jets,
which the prime block-Hankel hierarchy can test.

The contact program can now monitor the minimum, the simultaneous
value--slope zero, and this integrated negative mass. The last distinguishes
a genuine negative island from numerical point noise and supplies a predicted
local scaling law. It quantifies failure; it does not reverse heat smoothing
or prove RH.
