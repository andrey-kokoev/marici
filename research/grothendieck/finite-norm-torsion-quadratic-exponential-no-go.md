# Finite norm-complex torsion cannot equal the quadratic Euler exponential

At one prime write `x=p^(-s)`. The quadratic channel removed by the third
regularized determinant contributes the local factor

```
E_2(x)=exp(+-x^2/2),                                    (1)
```

with the sign determined by whether one writes zeta or its reciprocal.

Suppose a finite based chain complex has differentials whose entries are
polynomial or rational functions of `x`. Whenever its Reidemeister torsion is
defined and acyclic, that torsion is a finite alternating product of minors.
It is therefore a rational function of `x`.

But `exp(x^2/2)` is not rational. If `exp(x^2/2)=P(x)/Q(x)` with nonzero
polynomials `P,Q`, logarithmic differentiation gives

```
P'Q-PQ' = x P Q.                                       (2)
```

The left side has degree at most `deg(P)+deg(Q)-1`; the right side has degree
`deg(P)+deg(Q)+1`. This is impossible. The same argument applies to the
negative exponential.

Therefore the finite two-periodic norm complex `(N,2-N)`, even after an
algebraic `x`-twist, cannot have ordinary finite torsion equal to the exact
quadratic Euler counterterm.

## What the norm complex still explains

The norm complex remains relevant as the algebraic carrier of the failure of
second-Adams descent:

```
N^2=2N,
N(2-N)=0=(2-N)N.                                      (3)
```

It locates the anomaly at degree two and records the bad-prime normalization.
What it does not provide is the analytic exponentiation of the quadratic
trace. Algebraic anomaly type and analytic determinant value are separate
obligations.

## Minimal analytic enlargement

The exponential is naturally produced by an infinite or regularized
construction. Three candidate types remain:

1. a Gaussian/Fock space whose connected quadratic cumulant exponentiates;
2. a determinant regularization that subtracts or restores
   `Tr(P_s^2)/2` as an anomaly functional;
3. an infinite relative complex with zeta/heat-regularized torsion.

Each must be coupled to gamma and endpoint channels before scalarization.
Simply declaring its regularized torsion to be (1) is circular; the
regularization law and its coefficient `1/2` must follow from the source
pairing.

## Stronger local falsifier

Any proposal using a uniformly finite-dimensional local complex at each
prime, with algebraic dependence on `p^(-s)`, fails to reproduce the isolated
quadratic exponential exactly. A product over primes does not repair the
local mismatch. The proposal must identify the infinite/regularized degree
of freedom responsible for exponentiation.

This no-go does not exclude a completed infinite norm complex, nor does it
construct one or prove RH.
