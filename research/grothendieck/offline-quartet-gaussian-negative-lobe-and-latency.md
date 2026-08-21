# An off-line zero quartet creates an amplified negative Gaussian lobe

Let an off-critical zero be

```
rho=1/2+alpha+i beta,          alpha>0, beta>0.
```

In the real spectral coordinate `gamma=(rho-1/2)/i`, the functional and real
symmetries produce the four complex ordinates

```
+/-beta +/- i alpha.                                   (1)
```

Their contribution to the half-signed Gaussian divisor kernel is

```
Q_(alpha,beta)(t,xi)=e^(t alpha^2) [
 e^(-t(xi-beta)^2) cos(2t alpha(xi-beta))
 +e^(-t(xi+beta)^2) cos(2t alpha(xi+beta))].           (2)
```

This expression is real and even in `xi`, but not nonnegative.

## Exact negative lobe

Set

```
xi_k=beta+(2k+1)pi/(2t alpha),       k>=0.             (3)
```

The first cosine in (2) equals `-1`. The absolute size of the second Gaussian
relative to the first is

```
exp[-4t beta xi_k] < 1.                               (4)
```

Regardless of the second cosine's sign, (4) implies

```
Q_(alpha,beta)(t,xi_k)<0                              (5)
```

for every `t>0`. Thus an isolated off-line quartet is detected by every
Gaussian scale if the character variable is allowed to move sufficiently far.
A positive arithmetic background can hide this lobe at broad smoothing, but
cannot change its oscillatory source.

## Inverse-time amplification scale

At the first lobe `k=0`, the dominant negative magnitude is

```
exp[t alpha^2-pi^2/(4t alpha^2)].                     (6)
```

It ceases to be exponentially suppressed when

```
t alpha^2 approximately pi/2.                         (7)
```

Against a background of local Weyl size roughly `log(beta)/sqrt(t)`, a more
realistic visibility condition is

```
t alpha^2 - pi^2/(4t alpha^2)
  greater than or comparable to log log(beta) - (1/2)log(t). (8)
```

Hence the Gaussian inverse-time latency is governed primarily by
`alpha^(-2)` with a slowly varying height correction. This differs from the
Li-rank latency `|rho|^2/alpha`; the two probes amplify off-line defects by
different mechanisms.

## Contact interpretation

Start in the unconditional broad-positive regime and increase `t` (decrease
variance). If an off-line quartet exists, its factor (6) eventually overwhelms
any fixed-scale positive background near its moving lobe under the usual
tempered zero-density bounds. Continuity and character coercivity then force
a first finite double contact before negativity appears.

This supplies the spectral anatomy of the source-side contact conjecture. It
does not locate a zeta quartet or prove a uniform arithmetic domination bound;
those remain on opposite sides of the RH equivalence.
