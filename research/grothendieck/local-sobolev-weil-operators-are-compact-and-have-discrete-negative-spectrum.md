# Local Sobolev Weil operators are compact and have discrete negative spectrum

## Question

What additional structure follows after representing the fixed-support Weil form on `H_0^s((-L,L))`, with `s>0`?

## Compactness mechanism

Use the zero-extension Sobolev norm on the bounded logarithmic interval. The representing operator is measured relative to the positive multiplier `(1+u^2)^s`.

The archimedean form has multiplier growth `O(log(1+|u|))`. Relative to the `H^s` inner product, its effective symbol has order

`log(1+|u|)/(1+u^2)^s`,

which tends to zero as `|u|` tends to infinity. The corresponding localized pseudodifferential operator is compact.

The endpoint contribution is finite rank because it is assembled from finitely many weighted linear functionals. The fixed-support prime contribution is a finite sum of translated `L^2` pairings. Each such form factors through the compact Rellich embedding

`H_0^s((-L,L)) -> L^2((-L,L))`

for `s>0`, followed by bounded translation/restriction maps. Its representing operator on `H_0^s` is therefore compact.

Hence the complete local Weil operator `A_(L,s)` is compact and self-adjoint.

## Spectral consequence

The nonzero spectrum of `A_(L,s)` consists of real eigenvalues of finite multiplicity accumulating only at zero. In particular, any negative spectrum is discrete.

A negative eigenvalue has a finite-dimensional witness: for a dense nested Galerkin sequence, sufficiently accurate compressions contain a negative Rayleigh quotient. Thus a certified finite Galerkin calculation can falsify local Weil positivity.

The converse requires more. Positive compressions at finitely many dimensions do not exclude a later negative eigenvalue. To certify positivity one needs lower enclosures controlling the unresolved orthogonal complement and the off-diagonal coupling to it.

## No coercive proof on this scale

Because `A_(L,s)` is compact on an infinite-dimensional space, it cannot satisfy a strictly positive lower bound

`A_(L,s) >= c I`

with `c>0` unless the space is finite-dimensional. Zero is necessarily in its spectrum. This independently explains why a uniform coercivity strategy is mismatched to the completed Weil problem.

Positivity, if true, must be semidefinite with spectral accumulation at zero.

## Certified Galerkin gate

Let `P_M` be an orthogonal projection onto a finite trial space and decompose

`A=[[A_MM,B_M],[B_M^*,C_M]]`.

A sufficient lower certificate is

`lambda_min(A_MM) >= epsilon_M`,

`||B_M|| <= beta_M`,

`C_M >= -gamma_M I`,

with a Schur or block estimate proving the full operator nonnegative. Merely showing `A_MM>=0` is insufficient. Since the unresolved tail tends to zero in operator norm for a compact operator, explicit approximation-number bounds could make this programme effective.

## Scope

The compactness claim uses standard localized pseudodifferential and Rellich facts plus the previously established logarithmic digamma growth. Publication use requires fixing the extension convention at fractional `s` and writing the prime translation/restriction factorization explicitly.

## Disposition

The local RH problem is a compact self-adjoint semidefinite problem, not a coercive one. The next executable target is a basis with computable operator-norm tail bounds, enabling certified negative-eigenvalue searches and, potentially, positivity enclosures.
