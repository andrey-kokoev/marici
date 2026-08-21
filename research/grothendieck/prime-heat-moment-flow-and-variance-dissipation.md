# The smoothed prime moments form a completely monotone heat hierarchy

Use Gaussian variance `sigma=1/(4t)` and write

```
c_n(sigma)=Lambda(n)n^(-1/2)e^[-sigma(log n)^2].       (1)
```

Define ordinary and twisted moments

```
M_k(sigma)=sum_n c_n(sigma)(log n)^k,
Z_k(sigma,xi)=sum_n c_n(sigma)(log n)^k e^(i xi log n). (2)
```

Termwise differentiation is justified at every positive `sigma` and gives

```
partial_sigma M_k=-M_(k+2),
partial_sigma Z_k=-Z_(k+2),
partial_xi Z_k=i Z_(k+1).                              (3)
```

In particular,

```
partial_sigma Z_0=partial_xi^2 Z_0,                   (4)
```

so the prime character sum itself obeys the forward heat equation.

## Complete monotonicity

Every even moment is a derivative of the scalar prime load:

```
(-1)^j partial_sigma^j M_0=M_(2j)>0.                  (5)
```

Thus `M_0` is completely monotone: it is the Laplace transform of the
positive measure obtained by pushing von Mangoldt mass along
`log n -> (log n)^2`. The all-order moment data are already encoded in one
zero-character function.

## Exact variance dissipation

Let

```
E(sigma)=M_2/M_0                                    (6)
```

be the mean squared log displacement under the normalized damped prime
measure. Then

```
E'(sigma)
=-[M_4/M_0-(M_2/M_0)^2]
=-Var_sigma((log n)^2) <= 0.                           (7)
```

Equivalently,

```
partial_sigma^2 log M_0=Var_sigma((log n)^2)>=0.       (8)
```

Broadening the Gaussian therefore decreases the effective arithmetic
displacement at a rate exactly equal to its variance. Equality can occur only
when the damped measure is supported on a single displacement.

## Block-flow consequence

For any polynomial coefficient vector `v`,

```
partial_sigma [v^* H_r v]
=-integral a^2 |p_v(a)|^2 dmu_sigma(a) <=0.            (9)
```

Hence every ordinary Hankel block decreases in Loewner order as smoothing
variance increases. The full phase Gram has the analogous negative shifted
Gram derivative. Sharpening the kernel reverses this direction and loads
larger prime displacements monotonically into the contact constraints.

This does not prove completed positivity because the archimedean block evolves
simultaneously. It supplies an exact dynamic invariant for continuation from
the broad-positive regime and replaces unrelated cutoff comparisons by one
common heat flow.
