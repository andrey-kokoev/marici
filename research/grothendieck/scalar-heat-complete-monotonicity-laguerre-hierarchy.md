# Scalar Stieltjes positivity becomes an endpoint--gamma--prime Laguerre hierarchy

Let

```
Theta(t)=K_endpoint(t)+K_gamma(t)+K_prime(t)            (1)
```

be the corrected scalar completed heat kernel. The RH-equivalent Stieltjes
gate requires

```
D_k(t)=(-1)^k partial_t^k Theta(t)>=0                  (2)
```

for every integer `k>=0` and every `t>0`, together with the completed
meromorphic normalization and residue conditions.

## Prime derivative theorem

For a displacement `a=log n`, put

```
g_a(t)=t^(-1/2)exp[-a^2/(4t)],
y=a^2/(4t).                                            (3)
```

Then

```
(-1)^k partial_t^k g_a(t)
=t^(-k-1/2)e^(-y) P_k(y),                             (4)

P_k(y)=k! L_k^(-1/2)(y),                              (5)
```

where `L_k^(-1/2)` is a generalized Laguerre polynomial. Starting from
`P_0=1`, the source-derived recurrence is

```
P_(k+1)(y)=(k+1/2-y)P_k(y)+y P_k'(y).                 (6)
```

Therefore

```
D_k^prime(t)= -k!/[2sqrt(pi)t^(k+1/2)] sum_(n>=2)
 Lambda(n)/sqrt(n) e^(-y_n)L_k^(-1/2)(y_n),           (7)

y_n=(log n)^2/(4t).                                   (8)
```

This sum converges absolutely at every fixed positive `t` and order `k`.

## Completed hierarchy

The endpoint contribution is elementary:

```
D_k^endpoint(t)=(-1)^k 4^(-k)e^(t/4).                 (9)
```

The gamma contribution is obtained by differentiating its convergent
integral with the same recurrence after the required constant terms are kept.
The corrected scalar source conjecture is

```
D_k^endpoint+D_k^gamma+D_k^prime >=0
                 for all k>=0,t>0.                    (10)
```

Order zero is the earlier pointwise inequality. It is only the first member
of (10), not the RH-equivalent statement by itself.

## Structural consequences

Laguerre polynomials change sign. Hence even a single negative prime sector
does not contribute with one fixed sign throughout the derivative hierarchy.
The alternating endpoint term also fails complete monotonicity separately.
All orders require completed gamma--endpoint--prime cancellation; sectorwise
positivity is structurally impossible.

An off-axis squared pole produces an oscillatory exponential in `t`, which
must fail (10) at some order even if its order-zero contribution is hidden by
a positive background. The hierarchy therefore has the correct sensitivity
that the scalar sign test lacked.

## Falsifier protocol

For a chosen `(k,t)`, truncate the prime sum with a certified Laguerre-weighted
tail, enclose the differentiated gamma integral, and combine it with (9). A
strictly negative interval disproves complete monotonicity and RH. Finite
positive checks remain diagnostics only; a proof needs one all-order mechanism
or a direct Stieltjes representation.
