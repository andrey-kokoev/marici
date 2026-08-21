# Weil Gaussian positivity has a one-sided smoothing threshold

Replace inverse heat time `t` by Gaussian variance

```
sigma=1/(4t),
q_sigma(x)=1/sqrt(4pi sigma) exp[-x^2/(4sigma)].        (1)
```

Up to a positive scalar normalization, the two-variable completed kernel is

```
U(sigma,xi)=(W_hat*q_sigma)(xi).                       (2)
```

It obeys the ordinary forward heat equation

```
partial_sigma U = partial_xi^2 U                       (3)
```

and the Gaussian semigroup law

```
U(sigma_2)=q_(sigma_2-sigma_1)*U(sigma_1),
                         sigma_2>sigma_1.              (4)
```

Therefore positivity at one variance propagates to every larger variance.
In the earlier parameter `t`, positivity at `t_1` propagates to all
`0<t<t_1`. It does not propagate toward larger `t`, where the Gaussian narrows
and resolves finer spectral sign structure.

## A sharp hostile model

Take the signed spectral distribution

```
mu=delta_(-1)+delta_(1)-delta_0.                       (5)
```

Its Gaussian smoothing factors as

```
(mu*q_sigma)(x)
=q_sigma(x)[2e^(-1/(4sigma))cosh(x/(2sigma))-1].       (6)
```

The bracket is minimized at `x=0`. Hence the smoothed distribution is
nonnegative everywhere exactly when

```
sigma >= 1/(4 log 2),
```

or equivalently

```
t <= log 2.                                            (7)
```

Broad Gaussian positivity can therefore hide a genuine negative spectral
atom. Positive short-time heat scans do not control the sharp large-`t`
limit.

## Weil smoothing threshold

When the completed convolution is well defined, introduce

```
sigma_W = inf {sigma_0:
  U(sigma,xi)>=0 for all sigma>=sigma_0 and all xi}.    (8)
```

The semigroup theorem makes the positivity set an upper ray whenever it is
nonempty. RH is equivalent to positivity at every variance and therefore to
`sigma_W=0`, together with positivity in the distributional zero-variance
limit. A positive `sigma_W` would quantify how much smoothing is required to
hide a failure of Weil positivity.

This threshold resembles the de Bruijn--Newman constant only at a structural
level. Here the heat flow convolves a fixed spectral distribution; Newman
flow deforms the entire function and moves its zeros. No equality between the
two parameters is asserted.

## Research consequence

The source attack can be organized monotonically:

1. prove positivity in a broad-smoothing regime;
2. lower `sigma` until the first possible contact `U=0`;
3. derive a source-side maximum-principle, zero-contact rigidity, or entropy
   estimate that forbids a positive threshold;
4. otherwise extract the first contact as a finite `(sigma,xi)` falsifier.

The hard direction is necessarily backward heat. This explains why ordinary
PNT estimates settle coarse smoothing but lose the exponentially delicate
large-`t` regime.
