# The unweighted prime tail does not have a vanishing finite-section remainder

## Correction to the finite-tail plan

Finite Dirichlet sections converge strongly to a bounded zero-extension translation, but not in operator norm. A nonzero translation is not compact. Consequently the remainder

`Q_M T_a Q_M`

need not tend to zero in norm as `M` grows. The increasing finite-tail norms in the `L=1` scout are consistent with this structural fact.

Thus no proof may certify the infinite prime tail by claiming that the unweighted beyond-cutoff translation matrix becomes small. Entrywise off-diagonal decay is insufficient: sharp interval boundaries produce long matrix tails, and norm convergence would incorrectly imply compactness of the translation operator.

## Correct weighted object

Let the positive tail reserve be diagonal in the Dirichlet basis,

`D_N=Q_N[log(1+sqrt(-Delta_D))-C_L]Q_N`,

where `N` is large enough that `D_N` is strictly positive. Let `B_L` collect the bounded prime, endpoint, and order-zero remainders. Positivity on the tail is equivalent to positivity of

`I+K_N`,

where

`K_N=D_N^(-1/2) Q_N B_L Q_N D_N^(-1/2)`.

Because the diagonal entries of `D_N^(-1/2)` tend to zero, this diagonal operator is compact. Hence `K_N` is compact for bounded `B_L`. Finite-section norm approximation becomes valid only after this logarithmic weighting.

## Explicit remainder bounds

Write

`d_m=log(1+m pi/(2L))-C_L`.

For `m>M` and positive `d_m`,

`||Q_M K_N Q_M|| <= ||B_L||/d_(M+1)`.

For the coupling between modes `N<m<=M` and `m>M`,

`||E_(N,M) K_N Q_M||`

`<=||B_L||/sqrt(d_(N+1)d_(M+1))`,

where `E_(N,M)=E_M-E_N`.

These bounds decay logarithmically. They recover the absolute-norm threshold as a fallback, but they also permit explicit finite matrices of the weighted operator to capture favorable cancellation before applying the remainder bound.

## Birman--Schwinger-style certificate

A valid tail computation should:

1. choose `N` so `D_N>0`;
2. form the finite weighted matrix `E_(N,M) K_N E_(N,M)`;
3. interval-enclose its smallest eigenvalue;
4. subtract the weighted coupling and beyond-cutoff bounds;
5. conclude `I+K_N>=0` only if the resulting margin remains nonnegative.

The low block and its coupling to the positive tail then enter the separate Schur complement.

## Disposition

The requested unweighted beyond-cutoff remainder is structurally unavailable and is withdrawn. The logarithmically weighted compact Birman--Schwinger operator is the correct finite-section object. The next checker should weight the existing translation matrix by `d_m^(-1/2)` and measure whether its finite spectrum plus rigorous absolute remainder can beat the direct absolute prime bound.
