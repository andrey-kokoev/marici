# Additive prime edges obey one shared contraction budget

Let `d` distinct primes label the squarefree cube `G=(C2)^d`.  Consider the
translation-invariant normalized kernel whose only nonzero arithmetic
correlations are the identity and the single-prime edges:

```
f(0)=1,       f(e_j)=r_j,       f(x)=0 for |x|>=2.       (1)
```

This is the literal support pattern suggested by the logarithmic derivative:
`Lambda(p_j)` is nonzero, while `Lambda(product_(j in S) p_j)=0` for every
squarefree set `S` of size at least two.

Walsh characters diagonalize convolution by `f`.  For
`eta in (C2)^d`, the corresponding eigenvalue is

```
lambda_eta = 1 + sum_j (-1)^(eta_j) r_j.                (2)
```

Choosing each sign opposite to `r_j` gives

```
min_eta lambda_eta = 1 - sum_j |r_j|.                   (3)
```

Therefore the cube is positive semidefinite exactly when

```
sum_j |r_j| <= 1.                                       (4)
```

For two primes this is the mixed-rectangle condition with both direct mixed
edges set to zero: `1 >= (r+s)^2` and `1 >= (r-s)^2`, equivalently
`|r|+|s|<=1`.

## Consequence for the completed Weil form

Individual prime contractions `|r_j|<=1` do not glue.  All simultaneously
visible prime directions consume a single contraction budget.  Since the raw
weights `log(p)/sqrt(p)` are not summable over the primes, no fixed unit
diagonal can make the infinite arithmetic-only cube positive.

This is not a disproof of Weil positivity: normalization and the
archimedean/endpoint energy depend on the test block.  It is a source-level
no-go for any proof that treats prime-power edges as independent contractions
while discarding completed cross energy.  A viable construction must derive
one of the following from the completed source:

1. a scale-dependent diagonal large enough to dominate the visible edge
   `l1` norm;
2. higher mixed correlations supplied by a legitimate Schur or mapping-cone
   completion, without inventing a von Mangoldt atom at a squarefree
   composite; or
3. cancellations caused by the actual test-function geometry before the
   normalized cube is formed.

The sharp falsifier is finite: for any chosen prime set, a negative Walsh
character appears as soon as its normalized edge sum exceeds one.
