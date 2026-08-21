# RH is a compact Hausdorff moment problem at the reduced quarter point

Let

```
S(x)=xi'/xi(1/2+sqrt(x))/(2sqrt(x)),
x_0=1/4,                                                (1)
```

where the endpoint pole pair has already been canceled. Define the Taylor
jet

```
A_k=(-1)^k S^(k)(x_0)/k!,       k>=0.                  (2)
```

Under the Stieltjes/RH representation,

```
A_k=integral_[0,infinity)dnu(lambda)/(x_0+lambda)^(k+1). (3)
```

Put

```
u=1/(x_0+lambda),          0<=u<=4,
dmu(u)=u dnu(lambda).                                  (4)
```

Then

```
A_k=integral_[0,4]u^k dmu(u).                          (5)
```

Thus one canonical Taylor jet is a compact Hausdorff moment sequence.

## Exact positivity hierarchy

A sequence `(A_k)` is represented by a positive measure on `[0,4]` if and
only if, at every order, the following three Hankel/localizing matrices are
positive semidefinite:

```
H_r       =(A_(i+j)),
H_r^u     =(A_(i+j+1)),
H_r^(4-u) =(4A_(i+j)-A_(i+j+1)).                      (6)
```

They are the polynomial Grams with multipliers `1`, `u`, and `4-u`. Compact
support makes the moment problem determinate automatically; no separate
Carleman or exponential-growth condition is required.

## Reconstruction

For `|h|<1/4`, the Taylor series and (5) give

```
S(x_0+h)=sum_k (-h)^k A_k
        =integral_[0,4] dmu(u)/(1+h u).                (7)
```

Returning to `lambda=u^(-1)-x_0` recovers

```
S(x)=integral_[0,infinity)dnu(lambda)/(x+lambda).      (8)
```

Analytic continuation identifies this with the completed meromorphic Xi
resolvent globally. Its poles lie on the nonpositive real `x` axis, forcing
the Xi zeros onto the critical line. Conversely RH supplies (3)--(6).

Therefore, in the completed Xi analytic class,

```
RH <=> the quarter-point jet (A_k) is a [0,4]
       Hausdorff moment sequence.                      (9)
```

## Why this target is attractive

- It uses the canonical no-counterterm point left by endpoint reduction.
- It needs one local Taylor jet rather than all heat times.
- The representing coordinate is compact, so determinacy and growth are
  automatic.
- The upper-support localizer `4H-H^u` records the fact that squared spectral
  energy is nonnegative; ordinary Hankel positivity alone would allow poles
  on the wrong side of `x_0`.
- The moments are source-explicit through the Laurent/Taylor jets of
  `zeta'/zeta`, gamma polygamma values, and elementary factors at `s=1`.

The first value is already fixed:

```
A_0=1+EulerGamma/2-log(2sqrt(pi))>0.                   (10)
```

The next attack is to derive the general quarter-point jets in a common
completed recurrence and seek a Gram factorization proving all three matrix
families. This remains RH-equivalent, not a proof.
