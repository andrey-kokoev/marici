# The valuation Dirichlet metric detects height but has the wrong zero set

For one prime `p`, put

```
r=p^(-1/2-iT)
```

and consider the prime-power potential vector

```
f=(1,r,r^2,...).
```

The incidence-derived one-prime metric is the first-difference energy. On
the infinite chain its convergent energy is

```
E_p(T)
 =|f_0|^2+sum_(k>=1)|f_k-f_(k-1)|^2
 =1+|1-r|^2/(1-|r|^2)
 =2[1-p^(-1/2)cos(T log p)]/(1-p^(-1)).                (1)
```

Subtracting the height-independent reference at `T=0` gives

```
D_p(T)=E_p(T)-E_p(0)
 =2p^(-1/2)[1-cos(T log p)]/(1-p^(-1)) >=0.            (2)
```

Thus the non-diagonal valuation metric repairs the phase blindness of the
ordinary diagonal norm. It detects the logarithmic prime phase locally and
positively.

## Heat-smoothed global energy

For `tau>0`, define

```
D_tau(T)=sum_p exp[-tau(log p)^2] D_p(T).               (3)
```

The Gaussian makes this absolutely convergent. Every term is nonnegative.
Moreover, simultaneous vanishing requires

```
T log p in 2pi Z       for every prime p.              (4)
```

Already `p=2,3` force `T=0`, since a nonzero solution would make
`log 2/log 3` rational and hence imply `2^m=3^n` for nonzero integers.
Therefore

```
D_tau(T)=0 iff T=0.                                    (5)
```

## Consequence

The valuation Dirichlet metric supplies positive, height-sensitive prime
geometry—but it has the wrong zero set for a spectral determinant. Riemann
zeros occur at nonzero heights, whereas (5) vanishes only at the origin.

This rules out identifying a raw phase-distance energy with the Xi
reflection defect or with `|xi(1/2+iT)|`. A zero-producing construction needs
signed interference, a determinant, or coupling to the archimedean sector;
termwise positive prime energies cannot generate nonzero spectral zeros.

## What survives

The calculation still validates the incidence metric as the correct carrier
of off-diagonal phase information. It should enter as a control norm or
quadratic form for the prime interaction, not as the spectral equation
itself.

