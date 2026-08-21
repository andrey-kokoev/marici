# Scalar Stieltjes positivity is reflection positivity of the time-addition kernel

Fix `t_0>0` and define, for small nonnegative time increments,

```
K_(t_0)(s,u)=Theta(t_0+s+u),                           (1)

K_(t_0)^+(s,u)=-partial_t Theta(t_0+s+u).              (2)
```

If

```
Theta(t)=integral_[0,infinity)e^(-t lambda)dnu(lambda), (3)
```

then

```
K_(t_0)(s,u)
=integral [e^(-s lambda)][e^(-u lambda)]
          e^(-t_0 lambda)dnu(lambda),                  (4)

K_(t_0)^+(s,u)
=integral lambda[e^(-s lambda)][e^(-u lambda)]
          e^(-t_0 lambda)dnu(lambda).                  (5)
```

Both kernels are positive semidefinite. Equation (4) is reflection positivity
for the additive heat semigroup; equation (5) says its infinitesimal generator
is positive.

## Equivalence with the one-time Hankel hierarchy

Differentiate (1) at `s=u=0`. After canceling row and column signs,

```
partial_s^i partial_u^j K(0,0)
=Theta^(i+j)(t_0)
```

produces the ordinary moment matrix `(D_(i+j))`. Differentiating (2) produces
the shifted matrix `(D_(i+j+1))`. Therefore local analytic reflection
positivity of both kernels implies the complete one-time Stieltjes hierarchy.

Conversely, the hierarchy plus right-half-plane holomorphy reconstructs the
measure by the one-time moment theorem, and (4)--(5) follow. In the completed
Xi analytic class,

```
RH
<=> K_(t_0)>=0 and K_(t_0)^+>=0 locally
    for one t_0>0.                                     (6)
```

Here positivity means every finite matrix obtained from time increments is
positive semidefinite.

## Why this is a better construction target

The derivative formulation is an infinite list of nonlinear determinant
inequalities. The kernel formulation asks for two coherent Gram
factorizations:

```
K(s,u)=<V_s,V_u>,
K^+(s,u)=<A^(1/2)V_s,A^(1/2)V_u>,                     (7)
```

with `V_s=e^(-sA)V_0` and `A>=0`. Such a factorization simultaneously proves
every Hankel minor and directly produces the positive generator whose Jacobi
model was constructed previously.

This is the scalar analogue of the desired correspondence/Mackey object:
time addition is composition, reflection exchanges the two legs, and the
positive generator is the source-derived boundary operator. A source proof
must build (7) from the completed endpoint--gamma--prime system, not infer it
from zeros.

## Smallest falsifiers

For two increments `s_0,s_1`, reflection positivity requires

```
Theta(t_0+2s_0)Theta(t_0+2s_1)
-Theta(t_0+s_0+s_1)^2>=0.                             (8)
```

The infinitesimal limit is the log-convexity determinant
`D_0D_2-D_1^2>=0`. The analogous determinant for `-Theta'` is the first
shifted constraint. A negative two-time determinant is therefore the smallest
coupled scalar falsifier.
