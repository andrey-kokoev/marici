# The relative difference quotient repairs volume but arithmetic weights do not descend

Let an abelian group `G` act diagonally on `G x G` by

```
c.(a,b)=(a+c,b+c).
```

The difference is invariant, and the induced map

```
d_bar:(G x G)/diag(G) -> G,
d_bar([a,b])=a-b                                      (1)
```

is a group isomorphism. If quotient Haar measure is chosen as the pullback
of Haar measure under `d_bar`, then

```
U_rel:L2(G)->L2((GxG)/diag G),
(U_rel f)([a,b])=f(a-b)                                (2)
```

is unitary. This removes the infinite center-of-mass volume rather than
dividing by a formal infinity.

For finite `G`, the full incidence map has `I*I=|G|I`, while passing to one
diagonal orbit representative per difference gives exactly `I`. Thus the
relative quotient is the canonical normalized version of the finite
pull--push correspondence.

## Arithmetic coefficient obstruction

The unweighted geometry descends, but a coefficient system descends only if
its pair weight `w(a,b)` is invariant under simultaneous translation:

```
w(a+c,b+c)=w(a,b).                                    (3)
```

In multiplicative arithmetic coordinates, diagonal translation corresponds
to common scaling `(m,n)->(cm,cn)`, and the quotient remembers only the ratio
`m/n`. Von Mangoldt-type product weights are not invariant. For example,

```
(m,n)=(2,3),        weight=log 2 log 3,
(cm,cn)=(10,15),   weight=0,
```

although both pairs represent the same ratio `2/3`; `10` and `15` are not
prime powers. Hence the ordinary prime coefficient does not descend to the
relative difference quotient.

This is exactly where a coefficient--Betti system is needed: the geometric
relative quotient can carry the difference class, while a separate
coefficient object must transport arithmetic weight with a cocycle or
correspondence law.

## Theorem versus unavailable physical map

Equations (1)--(2) are an exact group/Haar theorem. They construct the
abstract relative Hilbert space, not a physical relative-chain pushforward
for the Marici/Xi source. The coefficient descent failure prevents claiming
that the prime explicit formula already lives on this quotient.

## Falsifier

A proposed relative source model fails if it identifies pairs with the same
ratio while retaining a weight that changes under common scaling, unless it
also supplies an explicit coefficient cocycle and proves independence of
representative.

