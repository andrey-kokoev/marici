# Gamma cancellation forces a reciprocal-square von Mangoldt source metric

The exact Euler cross source has prime coefficients

```
a_p=Lambda(p)p^(-1/2)=(log p)p^(-1/2).                 (1)
```

With the counting metric, its same-point Green diagonal through `p<=P`
contains

```
D_0(P)=sum_(p<=P)(log p)^2/p
      ~ (1/2)(log P)^2.                                (2)
```

The canonical gamma oscillator covariance with the logarithmically matched
cutoff `K=floor(log P)` grows only as

```
G(P)=sum_(k<K)1/(k+1/4)
    ~ log log P.                                       (3)
```

Therefore the gamma oscillator cannot cancel the raw positive Euler-source
diagonal. The earlier `log log P` cancellation applied to unweighted critical
prime amplitudes; inserting the exact von Mangoldt cross coefficients changes
the diagonal divergence by two logarithmic powers.

## Unique log-power metric match

Give the prime basis a local squared norm

```
||e_p||^2_alpha=(log p)^(-alpha).                      (4)
```

Then the weighted source diagonal behaves, by the prime number theorem, as

```
D_alpha(P)
 =sum_(p<=P)(log p)^(2-alpha)/p
 ~ integral^(log P) u^(1-alpha)du.                    (5)
```

Hence:

```
alpha<2:  power growth (log P)^(2-alpha),
alpha=2:  logarithmic growth log log P,
alpha>2:  finite limit.                               (6)
```

Among this natural family, `alpha=2` is uniquely compatible with the gamma
oscillator divergence. Equivalently,

```
||e_p||^2=1/Lambda(p)^2                               (7)
```

on prime support. The von Mangoldt factors then remain in the linear cross
functional but cancel from the quadratic norm:

```
||a_p e_p||^2=(Lambda(p)^2/p)/Lambda(p)^2=1/p.         (8)
```

For the full prime-power module the same metric is defined on support where
`Lambda(n)>0`; higher powers contribute a convergent correction to
`sum 1/n`, leaving the prime `log log P` divergence.

## Pairing obligation

Equation (7) is not yet admitted geometry. It changes the Hilbert adjoint of
incidence and transfer maps and is nonintegral because `Lambda(p)=log p`.
The coefficient--Betti evaluation pairing must derive this metric—or an
equivalent placement of reciprocal von Mangoldt weights on the dual leg—while
preserving the linear cross coefficient in (1).

This is possible in type: coefficients may live on one leg and reciprocal
metric weights on the dual Betti leg. But simply declaring the metric after
observing the divergence is a renormalization fit. A valid source theorem
must derive it from the logarithmic Jacobian, divisor pushforward, or a
unitary incidence normalization.

## Consequences

The relative prime--gamma Weyl target now has three ordered stages:

1. derive the reciprocal-square von Mangoldt Hilbert metric from the paired
   source structure;
2. use it to reduce the exact Euler source diagonal to harmonic-prime size;
3. cancel that `log log P` divergence against the quarter-shift oscillator
   under `K=floor(log P)` before taking the positive quotient.

Skipping stage 1 leaves an uncancellable `(log P)^2` divergence. Performing
stage 1 without rechecking adjunction may destroy the exact Euler cross term.

## Falsifiers

A proposal fails if it:

1. claims that the gamma harmonic trace cancels the raw von Mangoldt-square
   diagonal;
2. uses a log-power metric with `alpha!=2` while claiming matched divergence;
3. inserts `1/Lambda^2` without deriving the changed coefficient--Betti
   adjunction;
4. loses the linear `Lambda(n)` coefficient in the cross-resolvent;
5. extends the reciprocal weight to integers with `Lambda(n)=0` rather than
   restricting to intrinsic prime-power support.

The next target is an exact weighted adjunction theorem for the prime-power
coefficient--Betti module. This gate fixes its only log-power metric candidate
but does not construct it or prove RH.
