# The von Mangoldt term is a self-adjoint translation adjacency, not a penalty norm

Let `S_a` denote translation by `a` on additive log-time test functions. For a
finite prime-power cutoff `Y`, define

```
A_Y = sum_(p^k<=Y) w_(p^k) (S_(k log p)+S_(k log p)^*),
w_(p^k)=log(p)/p^(k/2).                                (1)
```

Every summand is bounded and self-adjoint, hence so is `A_Y`. Under the
Fourier transform it is multiplication by

```
a_Y(t)=2 sum_(p^k<=Y) w_(p^k) cos(t k log p).          (2)
```

The arithmetic contribution to the centered explicit-formula quadratic form
is `-<g,A_Y g>` (up to the chosen common normalization). It is generally
sign-indefinite. It is not of the form `-||Bg||^2`, and replacing it by
independent negative diagonal prime costs changes its operator type.

## Exact squarefree first-power sector

Retain only the first powers of `d` distinct primes and quotient their
translation labels mod two. On `(C2)^d`, the adjacency is

```
A = sum_j w_j T_(e_j).                                 (3)
```

Its Walsh eigenvalues are

```
alpha_eta = sum_j (-1)^(eta_j) w_j.                   (4)
```

Thus

```
||A|| = sum_j |w_j|.                                  (5)
```

Adding diagonal energy `D I` gives positivity exactly when
`D>=sum_j |w_j|`. This is precisely the additive edge-budget theorem, now
derived as the spectral norm of the source-typed prime adjacency rather than
as an abstract correlation rule.

## Prime towers and Adams harmonics

For one prime, all powers remain on one translation circle and give the
trigonometric polynomial

```
a_p(theta)=2 sum_(k:p^k<=Y) log(p)p^(-k/2) cos(k theta). (6)
```

The powers are harmonics of one phase, not independent prime coordinates.
This is the operator version of the Adams identity: the `k`th prime-power
channel is obtained by the power map `theta -> k theta`. Any model assigning
orthogonal coordinates to `p,p^2,...` destroys this source relation.

## Revised positivity gate

The completed problem should be posed on the common Fourier/log-time space:

```
H_arch - A_prime >= 0,                                 (7)
```

or as a source-derived Schur dilation of that difference. The comparison is
pointwise in the translation spectral variable only after both operators are
placed in the same representation. Comparing von Mangoldt weights to norms
of separately chosen gamma defect vectors is not invariant and has now been
discarded.

At finite cutoff the falsifier is explicit: find a Fourier/Walsh character
for which the archimedean symbol is smaller than the prime adjacency symbol.
Passing to the completed, unbounded limit remains the hard analytic gate and
must retain endpoint terms.
