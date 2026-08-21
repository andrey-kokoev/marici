# Explicit source formula for the two-variable Weil Gaussian kernel

Use the even completed Xi divisor and count positive ordinates once. For
`t>0` and real `xi`, the Gaussian test in the spectral variable is

```
h_(t,xi)(u)=exp[-t(u-xi)^2].                            (1)
```

Applying the centered explicit formula and dividing the signed divisor by
two gives

```
Theta(t,xi)=K_endpoint(t,xi)+K_gamma(t,xi)+K_prime(t,xi), (2)
```

where

```
K_endpoint(t,xi)=e^(t/4-t xi^2) cos(t xi),             (3)

K_gamma(t,xi)= -log(pi)/(4 sqrt(pi t))
 +1/(4pi) integral_R e^[-t(u-xi)^2]
             Re psi(1/4+iu/2) du,                     (4)

K_prime(t,xi)= -1/(2 sqrt(pi t)) sum_(n>=2)
 Lambda(n)/sqrt(n) e^[-(log n)^2/(4t)] cos(xi log n). (5)
```

The endpoint identity follows exactly from the two polar evaluations:

```
[h(i/2)+h(-i/2)]/2=e^(t/4-t xi^2)cos(t xi).            (6)
```

The Fourier transform of (1) gives the damped cosine in (5). At `xi=0`,
equation (4) is equivalent to the previously derived one-sided digamma
integral, and (2) reduces to the reconciled scalar heat kernel.

## Spectral interpretation

Under RH,

```
Theta(t,xi)=(1/2) sum_(gamma signed) m_gamma
             e^[-t(xi-gamma)^2]                       (7)
```

and is strictly positive. At `xi=0`, reflection turns (7) into the heat trace
over positive ordinates only. Formulae (2)--(5), however, are source-side and
contain no zero input.

## Why the endpoint oscillation matters

Away from the zero character, the endpoint is not the positive scalar
`e^(t/4)`: it oscillates through `cos(t xi)` and is Gaussian-damped in `xi`.
Therefore neither endpoint nor prime term is separately positive. Any
nonzero-character test that reuses the scalar endpoint is incorrectly
normalized.

The new RH-equivalent source target is the explicit inequality

```
K_endpoint(t,xi)+K_gamma(t,xi)+K_prime(t,xi)>=0        (8)
```

for every `t>0` and real `xi`, with the usual convergence and common-cutoff
requirements. A certified negative pair `(t,xi)` would be a finite-smearing
Weil falsifier. A proof would directly supply positive Gaussian
approximations to the Weil/GNS spectral measure.

## Scope

The formula is the classical explicit formula specialized to a shifted
Gaussian. Publication use still requires declaring the Fourier convention
and justifying the Schwartz-test substitution and prime summation. It is an
identity and a sharpened target, not a proof of (8).
