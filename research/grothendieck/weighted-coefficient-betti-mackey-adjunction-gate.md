# Weighted Hilbert adjunction preserves the Mackey norm only under fiber balance

Let `q:G->H` be a finite surjection and give coefficient functions weighted
Hilbert products

```
<a,b>_G=sum_(g in G) mu_G(g) conjugate(a(g))b(g),
<c,d>_H=sum_(h in H) mu_H(h) conjugate(c(h))d(h),       (1)
```

with positive weights. Pullback remains `(q^*c)(g)=c(q(g))`. Its Hilbert
adjoint is forced to be

```
(q_*^mu a)(h)
 =mu_H(h)^(-1) sum_(q(g)=h)mu_G(g)a(g).                (2)
```

Therefore

```
q_*^mu q^*
 =diag_h d_mu(h),
d_mu(h)=sum_(q(g)=h)mu_G(g)/mu_H(h).                   (3)
```

The original Mackey norm `d I`, with `d=|q^(-1)(h)|`, survives exactly when

```
sum_(q(g)=h)mu_G(g)=d mu_H(h)                          (4)
```

for every fiber. This is the weighted fiber-balance condition.

The coefficient--Betti evaluation pairing can remain algebraically perfect
if the dual Betti basis receives reciprocal weights. But the Hilbert adjoints
of pullback and transfer still obey (2); algebraic duality does not make an
arbitrary metric invisible.

## C2 hostile normalization

For `q:{0,1}->*`, write upstairs weights `mu_0,mu_1` and downstairs weight
`nu`. Then

```
q_*^mu q^*=(mu_0+mu_1)/nu.                            (5)
```

Degree-two Mackey normalization requires `nu=(mu_0+mu_1)/2`. If the selected
delta vector at zero must still transfer with coefficient one, (2) requires
`nu=mu_0`. Both hold exactly when

```
mu_0=mu_1.                                             (6)
```

Thus a nonconstant fiber weight recreates the original normalization
conflict. Weighted averaging cannot simultaneously preserve arbitrary local
metrics, the degree norm, and the frozen selected-vector normalization.

## Consequence for the reciprocal von Mangoldt metric

The candidate prime-power metric

```
mu(n)=1/Lambda(n)^2                                   (7)
```

is compatible with a given Mackey quotient only if its fiber averages define
the downstairs metric as in (4). It preserves the old unweighted degree and
selected-vector normalization only when `Lambda(n)^2` is constant on the
relevant fibers.

That constancy is not automatic. Difference/ratio correspondences generally
place distinct prime powers in one geometric fiber, and von Mangoldt weights
do not descend through common-scaling quotients without the previously
constructed divisor cocycle. Therefore (7) cannot simply be installed as a
Hilbert metric on the existing Mackey object.

## Surviving options

There are three logically distinct repairs:

1. derive fibers on which the reciprocal von Mangoldt metric is balanced;
2. accept the weighted degree `d_mu(h)` as a new modular function and rebuild
   the Mackey norm theorem with it;
3. keep the integral Mackey pairing unweighted and introduce the reciprocal
   factors only in a separate analytic comparison operator, whose adjoint is
   audited explicitly.

The third option preserves the algebraic correspondence but no longer claims
that the analytic Hilbert adjoint is the original transfer.

## Falsifiers and next target

A proposal fails if it changes the source metric while retaining the old
adjoint formulas by assertion, or if it uses (7) without checking fiber
balance. The smallest decisive calculation is (5)--(6).

The next target is to test the divisor-pushforward/logarithmic-cocycle module
for a canonical modular density whose weighted transfer retains the exact
linear Euler cross functional. If its modular degree is nonconstant, the
relative Gaussian completion must be formulated as a measured groupoid or
Hilbert correspondence, not an ordinary finite-degree Mackey functor.

This is an exact weighted-adjunction theorem. It does not supply the needed
balanced prime-power fibers or prove RH.
