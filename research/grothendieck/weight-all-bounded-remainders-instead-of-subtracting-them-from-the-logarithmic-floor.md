# Weight all bounded remainders instead of subtracting them from the logarithmic floor

## Problem

The conservative tail argument first forms

`D=log(1+sqrt(-Delta_D))-C I`

and then waits until `D` is positive. Any large localization constant forces the starting mode to scale like `exp(C)`. This turns an analytic bounded-remainder estimate into an artificial low-block explosion.

## Unshifted factorization

Let

`A=log(1+sqrt(-Delta_D))`.

It is strictly positive on every Dirichlet mode. Write the local Weil operator as

`W_L=A+B_L`,

where `B_L` contains all bounded terms: the exact archimedean-minus-log remainder, Carleman boundary difference, endpoint cells, localization cells, and prime translations with their declared signs and prefactors.

Then

`W_L=A^(1/2)(I+K_L)A^(1/2)`,

where

`K_L=A^(-1/2) B_L A^(-1/2)`.

The diagonal operator `A^(-1/2)` is compact because its Dirichlet eigenvalues tend to zero. Therefore `K_L` is compact and self-adjoint whenever `B_L` is bounded and self-adjoint.

Positivity of `W_L` is equivalent to

`I+K_L>=0`.

No preliminary mode threshold of order `exp(||B_L||)` is needed to define this test.

## Finite certification

Let `E_M` be the first `M` Dirichlet modes and `Q_M=1-E_M`. The finite matrix

`E_M K_L E_M`

contains the actual cancellation among all bounded remainders. The absolute fallback gives

`||Q_M K_L Q_M|| <= ||B_L||/log(1+(M+1)pi/(2L))`

and

`||E_M K_L Q_M||`

`<=||B_L||/sqrt(log(1+pi/(2L)) log(1+(M+1)pi/(2L)))`.

These generic bounds still decay only logarithmically and can remain impractical. But the large localization constant no longer enters by being subtracted wholesale from the principal floor; it enters through the computed finite weighted matrix and only through the residual norm estimate beyond `M`.

## Stronger structure-specific route

Each component of `B_L` should receive its own tail estimate:

- multiplication and endpoint terms through their Dirichlet matrix decay;
- commutator localization cells through Fourier-moment structure;
- Carleman boundary difference through its explicit kernel;
- prime translations through shifted-sine overlaps and resonance bounds.

Summing componentwise weighted remainder bounds can be substantially sharper than applying `||B_L||` once. A finite calculation may then capture low-mode cancellation without requiring that the raw logarithmic floor dominate every bounded term separately.

## Claim boundary

Compactness proves existence of norm-convergent weighted finite sections, not a practical cutoff. A usable RH certificate still needs directed finite matrices and quantitative componentwise tail bounds. No positivity has been established.

## Disposition

The shifted-positive-tail architecture is retained only as a conservative existence proof. The executable architecture is the unshifted compact factorization `I+K_L`, with every bounded remainder inserted before truncation. Directed integration of the angular window improves one component but is not a prerequisite for defining this factorization.
