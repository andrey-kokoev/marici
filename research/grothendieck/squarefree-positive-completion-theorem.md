# Squarefree positive completion from individual prime contractions

Fix a diagonal energy `D>0` and prescribed real single-prime correlations
`r_1,...,r_d` on `G=(C2)^d`. Ask whether the unspecified correlations on
subsets of size at least two can be chosen so that the translation-invariant
kernel is positive semidefinite.

There is such a completion if and only if

```
|r_j| <= D                    for every j.              (1)
```

Necessity is already visible in each principal two-point block
`[[D,r_j],[r_j,D]]`. For sufficiency, set

```
f(S) = D product_(j in S) (r_j/D).                     (2)
```

This preserves `f(emptyset)=D` and `f({j})=r_j`. Its Walsh eigenvalues are

```
lambda_eta = D product_j [1+(-1)^(eta_j) r_j/D],       (3)
```

which are all nonnegative under (1). Thus arbitrary squarefree cubes admit a
positive completion exactly when every prime edge is individually
contractive.

## Relation to von Mangoldt support

Formula (2) is not an arithmetic identity. For distinct primes it inserts a
mixed coefficient `r_p r_q/D`, whereas the von Mangoldt coefficient at `pq`
is zero. The theorem instead specifies the exact burden on a *completed*
source: gamma/endpoint or mapping-cone correlations must provide mixed terms
that complete the sparse arithmetic edge data without being mislabeled as
prime atoms.

The contrast is sharp:

```
sparse arithmetic kernel PSD    iff  sum_j |r_j| <= D;
some completed kernel exists    iff  max_j |r_j| <= D. (4)
```

The gap between `l1` and `l-infinity` is the required completion resource.
For example, edges `(1/2,-1/3,1/5)` with `D=1` make the sparse cube negative
(`-1/30`) but the product completion strictly positive.

## Next source gate

Existence is only linear algebra. The RH program needs a canonical source
construction whose mixed correlations obey (or dominate) this completion
while retaining `Lambda(pq)=0` in the arithmetic summand. Failure on any
finite cube is an explicit negative completed Weil square; success on abstract
edge data alone is not evidence that the actual Weil distribution supplies
the completion.
