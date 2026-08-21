# One heat-time moment sequence reconstructs the scalar Stieltjes measure

Let `Theta` be real analytic on `(0,infinity)`, fix `t_0>0`, and define

```
D_k=(-1)^k Theta^(k)(t_0).                             (1)
```

Assume:

1. every ordinary and shifted Hankel matrix

   ```
   (D_(i+j))_(0<=i,j<=r),
   (D_(i+j+1))_(0<=i,j<=r)                            (2)
   ```

   is positive semidefinite;
2. for every `0<r<t_0`,

   ```
   sum_(k>=0) D_k r^k/k! < infinity.                  (3)
   ```

Then `Theta` is completely monotone on `(0,infinity)` and has a unique
positive Laplace representation

```
Theta(t)=integral_[0,infinity)e^(-t lambda)dnu(lambda). (4)
```

## Proof

The Stieltjes moment theorem applied to (2) gives a positive measure `mu_0`
on `[0,infinity)` with

```
D_k=integral lambda^k dmu_0(lambda).                   (5)
```

Condition (3) is exactly the finite exponential-moment condition

```
integral e^(r lambda)dmu_0(lambda)<infinity,
                         0<r<t_0.                     (6)
```

It also makes the moment problem determinate. For `|s|<r`, Taylor expansion
and absolute interchange give

```
Theta(t_0+s)
=sum_k (-s)^kD_k/k!
=integral e^(-s lambda)dmu_0(lambda).                  (7)
```

Define `dnu(lambda)=e^(t_0 lambda)dmu_0(lambda)`. By (6), its Laplace
transform exists for every positive `t`, and (7) becomes (4) first near
`t_0`, then everywhere on `(0,infinity)` by analytic continuation. Complete
monotonicity follows.

## Converse and RH target

Any positive squared-spectral measure immediately supplies (2)--(3) at every
`t_0>0`. Therefore, with the completed Xi analytic and residue data fixed, RH
is equivalent to the one-time conditions above for any chosen `t_0`.

This removes one continuous quantifier from the scalar program:

```
all derivative orders at one t_0
       + exponential moment control
<=> complete monotonicity at every t>0.                (8)
```

## Source-side formulation

Each `D_k` at `t_0` is the explicit completed Laguerre sum already derived.
The research target can therefore choose a convenient time, form its
ordinary and shifted source Hankel matrices, and seek one all-order positive
Gram construction plus the growth estimate (3).

Finite Hankel positivity remains diagnostic. Dropping (3) is also unsafe:
an indeterminate moment sequence need not reconstruct the analytic heat germ
far enough backward to reach all positive times.

The theorem does not make the all-order problem easy, but it turns a
two-parameter sign hierarchy `(k,t)` into a single moment sequence with a
clear algebraic positivity structure.

## Right-half-plane holomorphy removes the separate growth gate

For the completed Xi source kernel, `Theta(t)` is holomorphic on
`Re(t)>0` once the standard sum--integral interchanges are justified. The
prime log-Gaussians converge there because `Re(1/t)>0`; endpoint and gamma
terms have the same domain under their completed formula.

The open disk centered at `t_0` with radius `t_0` lies in this half-plane.
Therefore the Taylor series of `Theta` at `t_0` converges absolutely for every
`|s|<t_0`. Hankel positivity makes every `D_k` nonnegative (even entries from
`H_r`, odd entries from `H_r^+`), so absolute Taylor convergence is exactly
condition (3).

Consequently, in the admitted Xi analytic class,

```
all H_r(t_0)>=0 and H_r^+(t_0)>=0, for every r,
```

at one arbitrary chosen `t_0>0` is already the full scalar Stieltjes/RH gate.
No additional growth conjecture remains beyond proving the declared
right-half-plane holomorphy of the source formula.
