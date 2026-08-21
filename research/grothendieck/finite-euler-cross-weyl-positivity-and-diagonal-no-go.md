# The finite Euler cross-resolvent is positive, but its source diagonal diverges

Let `H_0=-d^2/du^2` on the logarithmic line. For `y>0`, its resolvent kernel is

```
G_y(u,v)=exp(-y|u-v|)/(2y).                            (1)
```

For two boundary points `0` and `a>0`, the Weyl/Green matrix is

```
M_a(y)=(1/(2y))[1 exp(-ya); exp(-ya) 1].              (2)
```

It is positive definite because its determinant is

```
det M_a(y)=(1-exp(-2ya))/(4y^2)>0.                    (3)
```

Thus a signed off-diagonal propagator is fully compatible with a positive
coupled matrix. Reversing the orientation of the second boundary vector
changes the cross-entry sign without changing positivity or the determinant.

## Exact finite Euler realization

At finite prime-power cutoff `N`, define the source distribution

```
q_N=sum_(2<=n<=N)Lambda(n)n^(-1/2) delta_(log n).      (4)
```

Then

```
<delta_0,(H_0+y^2)^(-1)q_N>
 =(1/(2y))sum_(n<=N)Lambda(n)n^(-1/2-y).               (5)
```

Choosing the negative coefficient--Betti orientation gives exactly the sign
of the Euler term in `xi'/xi`. Unlike a Schur correction, (5) is linear in
the source and includes every prime power with the correct multiplicity.

The full finite Green Gram matrix

```
W_N(y)=
[ <delta_0,R_y delta_0>  <delta_0,R_y q_N> ]
[ <q_N,R_y delta_0>      <q_N,R_y q_N>     ]           (6)
```

is positive semidefinite because `R_y=(H_0+y^2)^(-1)` is positive. Its
determinant is the Cauchy--Schwarz defect

```
||R_y^(1/2)delta_0||^2 ||R_y^(1/2)q_N||^2
-|<R_y^(1/2)delta_0,R_y^(1/2)q_N>|^2 >=0.             (7)
```

This is the first universal coupled positivity theorem containing the exact
finite Euler cross term.

## Infinite diagonal obstruction

The same-point part of the source diagonal contains

```
(1/(2y))sum_n Lambda(n)^2/n.                           (8)
```

Already its prime subseries is `sum_p (log p)^2/p`, which diverges. Spatial
propagation does not suppress this diagonal because `G_y(u,u)=1/(2y)` is
translation invariant. Therefore `q_N` does not converge to a vector in the
positive resolvent Hilbert space, even though the cross entry (5) converges
for `y>1/2`.

This proves that the desired infinite `2x2` positive Weyl matrix cannot be
obtained by the naïve raw-source limit. The diagonal must be defined
relatively—through gamma/endpoint subtraction, a changed source metric, or a
renormalized quadratic form—while the off-diagonal entry remains the exact
linear Euler trace.

## Consequence for zero production

Finite positivity alone does not identify Xi. In fact `det W_N(y)` is
nonnegative for real `y>0`; its zeros express linear dependence of two
resolvent boundary vectors, not yet Riemann zeros. The completed conjecture
must prove that a relative limit of (6), augmented by gamma and endpoint
channels, equals the RH-equivalent Herglotz/Weyl matrix after continuation.

The diagonal counterterm is constrained by (7): arbitrary subtraction can
destroy positivity. It must arise from enlarging the indefinite source space
and then taking a positive quotient, not from subtracting a scalar after the
Gram matrix is formed.

## Falsifiers and next target

A proposal fails if it:

1. replaces the linear cross entry by a quadratic norm;
2. omits prime powers or von Mangoldt weights;
3. takes `N->infinity` in the source diagonal without renormalization;
4. subtracts the diagonal divergence without proving positivity of the
   completed quotient;
5. identifies finite Gram-determinant zeros with Xi zeros.

The next target is a relative/Krein enlargement of (6) whose gamma-oscillator
negative sector cancels (8) at the form level and whose positive quotient
retains (5). This theorem supplies its exact finite boundary condition.
