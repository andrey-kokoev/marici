# Newman window entropy has an exact exterior-flux obstruction

Let `r_1,...,r_N` be distinct real roots in a finite observation window and
write

```
A_i = sum_(j != i) 1/(r_i-r_j),
R^2 = sum_i r_i^2,
p = N(N-1)/2,
c = p/R^2.
```

After centering the window, suppose its roots obey the forced Calogero law

```
r_i' = 2 A_i + b_i,
```

where `b_i` is the force exerted by roots excluded from the window (together
with any centering correction). For

```
widehatDelta = product_(i<j)(r_i-r_j)^2 / (R^2)^p,
q_i = A_i-c r_i,
```

direct differentiation gives the exact identity

```
d/dlambda log(widehatDelta)
  = 4 sum_i q_i^2 + 2 sum_i b_i q_i.                 (1)
```

Consequently the Hermite-relative entropy satisfies

```
E_N' = -4 sum_i q_i^2 - 2 sum_i b_i q_i.             (2)
```

The first term is intrinsic dissipation. The second is exterior entropy
flux and has no universal sign. Thus a finite Xi window does not inherit the
closed finite-rank Lyapunov theorem merely by containing real roots.

## Exact threshold

Monotonicity survives whenever

```
sum_i b_i q_i >= -2 sum_i q_i^2.
```

A sufficient, deliberately stronger condition is

```
||b||_2 <= 2 ||q||_2
```

together with non-adverse alignment; a norm bound alone cannot prevent the
worst alignment unless it is strict in the corresponding direction. The
right quantity to estimate is therefore the scalar boundary flux, not just
the magnitude of the omitted-root force.

## Consequence for the program

Any infinite-rank passage needs one of the following:

1. windows for which `sum b_i q_i` has a controlled lower bound;
2. an added exterior counterterm whose derivative cancels the flux and is
   defined canonically from the full Xi divisor; or
3. a global renormalized discriminant avoiding windows altogether.

Equation (1) is also a falsifier: a proposed truncation principle fails if
its measured exterior flux overwhelms intrinsic dissipation. No claim about
RH follows from the finite theorem until this gate is crossed.

