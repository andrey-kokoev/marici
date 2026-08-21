# Prime phases generate an all-order block Hankel contact hierarchy

At fixed `t>0`, retain the positive damped von Mangoldt measure

```
mu_t=sum_(n>=2)c_n(t) delta_(log n),
c_n(t)=Lambda(n)n^(-1/2)e^[-(log n)^2/(4t)].           (1)
```

Its ordinary and character-twisted moments are

```
M_k=sum_n c_n(log n)^k,
Z_k(xi)=sum_n c_n(log n)^k e^(i xi log n).             (2)
```

For an order `r`, form the Hankel matrices

```
H_r=(M_(i+j))_(0<=i,j<=r),
Z_r=(Z_(i+j))_(0<=i,j<=r).                            (3)
```

## Block positivity theorem

The matrix

```
B_r(xi)=[[H_r, conjugate(Z_r)],
         [Z_r, H_r]]                                  (4)
```

is positive semidefinite for every real `xi`. It is the Gram matrix in
`L2(mu_t)` of the `2(r+1)` functions

```
1,a,...,a^r,
e^(i xi a),a e^(i xi a),...,a^r e^(i xi a).           (5)
```

When `H_r` is nonsingular, (4) is equivalently the contraction condition

```
||H_r^(-1/2) Z_r H_r^(-1/2)|| <= 1.                  (6)
```

Thus the prime translation character is a contraction simultaneously in
every polynomial moment metric.

## Contact derivatives

Writing `R=Re Z_0`, differentiation alternates the twisted moments:

```
partial_xi^(2j) R = (-1)^j Re Z_(2j),
partial_xi^(2j+1) R = (-1)^(j+1) Im Z_(2j+1).         (7)
```

The completed contact equations prescribe `Re Z_0` and `Im Z_1` from the
archimedean value and slope. First-contact curvature constrains `Re Z_2`;
higher tangency or heat derivatives constrain subsequent entries. Requiring
the partially specified block (4) to admit a positive completion gives a
nested semidefinite exclusion hierarchy.

The earlier value--slope ellipse and fourth-moment curvature covariance bound
are low-order scalar consequences of this Gram positivity. The block form
retains correlations between all moments and can be strictly stronger.

## Correct scope

Every actual prime character passes every level automatically. Therefore a
failed semidefinite feasibility test rigorously excludes a proposed contact.
Passing finitely many levels does not construct the phases, prove contact, or
prove RH. Even passage at all abstract moment levels may describe a
contractive dilation unless the fixed support and multiplicative phase
relations are also enforced.

This is nevertheless a practical source-only program: compute certified
enclosures for `M_k` and the archimedean contact jets, then solve small exact
or interval semidefinite feasibility problems in increasing order until the
candidate region is excluded or survives for deeper arithmetic analysis.
