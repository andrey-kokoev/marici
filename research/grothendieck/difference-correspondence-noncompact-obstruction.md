# Difference correspondences are isometric only after finite-volume normalization

Let `G` be a locally compact abelian group with Haar measure and consider
the source difference pullback

```
(D f)(a,b)=f(a-b).                                     (1)
```

Formally, Tonelli and translation invariance give

```
||Df||_(L2(GxG))^2
 = integral_G integral_G |f(a-b)|^2 da db
 = vol(G) ||f||_(L2(G))^2.                             (2)
```

This is the continuous form of the finite pull--push law
`I_diff*I_diff=|G|I`.

## Compact case

If `G` is compact and Haar measure is normalized to total mass one, `D` is
an isometry. Fourier duality with the discrete character group then realizes
the conjugation-twisted spectral copy map without further divergence.

## Noncompact obstruction

If `G` is noncompact with infinite Haar volume, every nonzero `f` gives

```
||Df||=infinity.                                       (3)
```

Thus (1) is not a bounded map from `L2(G)` to `L2(GxG)`. For the discrete
hostile model `G=Z`, take `f=delta_0`. Then `Df(a,b)=1` precisely on the
infinite diagonal `a=b`, which is not square-summable. In the window
`[-M,M]^2`, its squared norm is exactly `2M+1`.

The logarithmic prime coordinate is naturally noncompact, so the finite
abelian theorem cannot be transferred by writing the same incidence map and
dividing by a nonexistent `sqrt(vol(G))`.

## Admissible repair classes

A legitimate infinite source model must specify one of:

1. a compact quotient or finite-volume arithmetic quotient;
2. a relative tensor product that divides out center-of-mass translation;
3. a semifinite trace per unit Haar volume;
4. a weighted correspondence with a proved compatible adjoint; or
5. a projective family of finite quotients with controlled normalization.

These choices are not automatically equivalent. In particular, a trace per
unit volume may recover the norm identity but can erase the absolute prime
scale needed by the explicit formula.

## Separation from the physical claim

The compact and finite identities are algebraic theorems. No canonical
relative-chain pushforward for the noncompact arithmetic source has been
constructed. Any physical or topological interpretation must provide the
quotient/trace data explicitly before using the difference correspondence.

