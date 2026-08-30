# Higher Weil contacts unfold by Hermite profiles

Suppose the first nonzero spatial jet of a threshold contact has even order
`2m`:

```
U(sigma_*,xi_*+x)=c x^(2m)+O(x^(2m+1)),       c>0.    (1)
```

All lower spatial derivatives vanish. Since the variance flow is the heat
equation, sharpening by `delta=sigma_*-sigma>0` applies the backward heat
operator. On the leading jet,

```
e^(-delta partial_x^2) x^(2m)
=delta^m H_(2m)(x/(2sqrt(delta))),                     (2)
```

where `H_(2m)` is the physicists' Hermite polynomial.

Therefore the local sharp-side profile is

```
U(sigma_*-delta,xi_*+x)
=c delta^m H_(2m)(x/(2sqrt(delta)))
 +o(delta^m)                                           (3)
```

on the parabolic scale `x=O(sqrt(delta))`.

## Universal entropy exponent

Every even Hermite polynomial of positive degree has negative intervals.
Changing variables `x=2sqrt(delta)z` in the negative-mass integral gives

```
N_local(sigma_*-delta)
=C_m c delta^(m+1/2)+o(delta^(m+1/2)),                 (4)

C_m=2 integral_R [-H_(2m)(z)]_+ dz >0.                (5)
```

For `m=1`, `H_2(z)=4z^2-2`, and (4) recovers the generic `3/2` law
`C_1=8sqrt(2)/3`. A quartic contact has exponent `5/2`, a sextic contact
exponent `7/2`, and so on.

## Contact multiplicity is observable

The logarithmic slope

```
d log N / d log delta -> m+1/2                         (6)
```

determines the order of the first nonzero contact jet. Thus negative-mass
scaling distinguishes generic tangency from a finely tuned higher-order
event. The latter requires vanishing of additional archimedean--prime jet
equations and must survive correspondingly deeper levels of the prime phase
block-Hankel hierarchy.

## Relation to Newman/Hermite geometry

This Hermite appearance is forced by the local heat semigroup and is not an
identification of Weil variance with the de Bruijn--Newman deformation. It
does show that both lanes share the same universal collision normal forms:
Hermite polynomials govern how multiple contact jets resolve under heat.

The result is local and conditional on a finite analytic contact with leading
jet (1). It classifies failure onset; it does not exclude such contacts.
