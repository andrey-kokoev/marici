# Von Mangoldt coefficients descend after divisor pushforward to a logarithmic cocycle

On the positive-integer divisibility poset, define the divisor pushforward

```
(B Lambda)(n)=sum_(d|n) Lambda(d).                      (1)
```

The classical exact identity is

```
(B Lambda)(n)=log n.                                   (2)
```

Thus the pair coefficient

```
c(m,n)=(B Lambda)(m)-(B Lambda)(n)
      =log(m/n)                                        (3)
```

is invariant under common scaling:

```
c(am,an)=c(m,n).                                       (4)
```

It therefore descends to the multiplicative relative quotient whose points
are rational ratios.

## Prime information is recoverable only with divisor incidence retained

Möbius inversion gives

```
Lambda(n)=sum_(d|n) mu(d) log(n/d).                    (5)
```

Hence passing from `Lambda` to `log` need not lose prime coefficients if the
integer divisibility correspondence and its Möbius inverse remain part of
the object. If one retains only the real coordinate `log n`, however, the
discrete divisor incidence is forgotten and (5) is unavailable.

This yields a concrete paired coefficient--Betti pattern:

```
von Mangoldt coefficient --divisor pushforward--> logarithmic potential
                                              |
                                              v
                              relative difference log(m/n).
```

The logarithmic potential is the quotient-compatible component; the
von Mangoldt function is the primitive coefficient recovered by Möbius
pullback/inversion.

## What survives

The following conclusions are exact:

1. prime coefficients admit a canonical divisor-poset pushforward;
2. the pushed coefficient has an additive common-scaling cocycle;
3. its antisymmetric pair difference descends to the ratio quotient; and
4. the original coefficient is recoverable when divisor incidence is kept.

What does not follow is that the quadratic Hermitian Xi defect equals a norm
of this cocycle. Establishing that equality requires a compatible transform,
adjoint, and graph/difference correspondence.

## Physical limitation

The divisor zeta/Möbius transforms are arithmetic incidence operations, not
the unavailable physical relative-chain pushforward. Any physical reading
must construct the corresponding chain maps independently.

