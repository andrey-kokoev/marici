# Euler-ray adjacency resums exactly and diverges at the common zero phase

For one prime `p`, put `r=p^(-1/2)`. Retaining its entire prime-power tower,
the paired translation symbol is

```
a_p(theta)=2 log(p) sum_(k>=1) r^k cos(k theta).        (1)
```

The Adams harmonics resum geometrically:

```
a_p(theta)
 =2 log(p) Re[ r e^(i theta)/(1-r e^(i theta)) ]
 =2 log(p) [r cos(theta)-r^2]
              /[1-2r cos(theta)+r^2].                 (2)
```

Since this is increasing in `cos(theta)`, its extrema are

```
max a_p =  2 log(p) r/(1-r)     at theta=0,
min a_p = -2 log(p) r/(1+r)     at theta=pi.           (3)
```

Thus higher prime powers make the positive and negative extrema asymmetric.
The squarefree `C2` model correctly detects the first-power edge budget but
cannot encode this full Adams tower by treating all powers as the same odd
edge.

## Finite global cutoff

For a finite set of prime powers on `L2(R)`, the Fourier multiplier is

```
a_Y(t)=2 sum_(p^k<=Y) log(p)p^(-k/2) cos(t k log p).   (4)
```

Every cosine equals one at `t=0`, so the triangle bound is attained:

```
||A_Y|| = a_Y(0)
        =2 sum_(p^k<=Y) log(p)p^(-k/2).                (5)
```

As the cutoff grows, even the first-prime-power subseries is not summable.
Consequently the raw infinite adjacency is not a bounded operator and its
pointwise zero-phase symbol is divergent. A claim of
`H_arch(t)-a_prime(t)>=0` using the unsmoothed separate symbols is therefore
ill-typed.

## Correct global gate

The explicit formula pairs the prime distribution only with admissible test
autocorrelations. Gamma, endpoint, and prime terms must be combined before
removing the cutoff. The appropriate object is a common quadratic-form limit
or a relative resolvent/Schur operator, not a difference of two independently
defined bounded multipliers.

This leaves a precise falsifier protocol:

1. choose an admissible compactly supported smooth log-time test family;
2. evaluate the completed gamma/endpoint and prime-power terms with one common
   cutoff convention;
3. search for a negative finite Gram eigenvalue;
4. prove cutoff independence before interpreting a positive sweep.

The zero-phase divergence explains why local prime contractions and finite
cube completions cannot be promoted by a naive norm limit.
