# The zeta pole canonically Abel-renormalizes every transported prime kernel

## Abel family

For `epsilon>0`, define

`F(epsilon)=-zeta'(1+epsilon)/zeta(1+epsilon)`

`          =sum_(n>=2) Lambda(n)n^(-1-epsilon)`.

The basis-`k` prime sum is

`P_k(epsilon)=(-1)^(k-1)/(k-1)! partial_epsilon^(k-1)F(epsilon)`

` =sum_n Lambda(n)n^(-1-epsilon)(log n)^(k-1)/(k-1)!`.

Since `F(epsilon)=epsilon^(-1)+` an analytic germ, differentiation shows

`P_k(epsilon)=epsilon^(-k)+` a finite germ.

There are no intermediate negative powers. The same degree-independent rule
renormalizes every basis index:

`P_k^ren=FP_(epsilon=0)[P_k(epsilon)-epsilon^(-k)]`.

## Completed prime germ

More invariantly, define

`J(epsilon)=epsilon^(-1)-F(epsilon)`

` =epsilon^(-1)+zeta'(1+epsilon)/zeta(1+epsilon)`.

The pole of zeta makes `J` analytic at zero, with `J(0)=EulerGamma`. Its
derivatives package all renormalized prime basis values. This is not an
optional subtraction: it is exactly the pole--zeta cancellation already
present in the completed logarithmic derivative.

## Full completed germ at one

The completed logarithmic derivative can be written near `s=1+epsilon` as

`xi'/xi(1+epsilon)`

` =1/(1+epsilon)-log(pi)/2+psi((1+epsilon)/2)/2+J(epsilon)`.

Every term on the right is now analytic at zero. This gives a universal
source decomposition into endpoint, archimedean, and Abel-renormalized prime
germs without splitting a cancelling singular pair.

## What this solves

- It replaces the divergent raw von Mangoldt kernels by a canonical Abel
  finite part.
- The subtraction rule is common to all polynomial degrees and basis indices.
- It reproduces the Stieltjes-constant jets used in the finite Toeplitz
  channels.

## What remains

The analytic germ is not manifestly positive. The next problem is to prove
that the quadratic combinations selected by the coefficients `A_k(p)` are
nonnegative after endpoint, gamma, and `J` are coupled. Individual Taylor
coefficients of `J` may have either sign and are not Gram blocks.

A later comparison with sharp cutoffs must prove that its contour-derived
finite part agrees with this Abel prescription; that equivalence is not
assumed here.
