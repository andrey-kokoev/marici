# The direct Sonin Euler orientation forces a meromorphic determinant line beyond the Euler half-plane

## Question

Can the direct inverse-Euler Sonin multiplier continue toward the critical strip as one holomorphic Fredholm determinant?

## Claim boundary

Not across a zero of the completed zeta function. The direct Euler orientation continues as a reciprocal completed-zeta section, which is meromorphic and has poles at zeta zeros. A Fredholm determinant of a holomorphic Schatten-family is holomorphic. Therefore the global compiler must be meromorphic, a ratio of determinant-line sections, or use a different orientation. This is a typing obstruction, not a zero-location claim.

## Direct orientation

The primary-source Sonin multiplier fixes

$$
M(s)=M_\infty(s)\prod_p(1-p^{-s}).
$$

On \(\operatorname{Re}s>1\), this is the archimedean completion factor times

$$
\zeta(s)^{-1}.
$$

The local return convention is \(K_p=-p^{-s}\), so finite stages are ordinary direct determinants.

## Continuation obstruction

Let \(K(s)\) be holomorphic with values in a Schatten ideal supporting \(\det_3\). Then

$$
\det_3(I+K(s))
$$

is holomorphic. Multiplication by holomorphic nonvanishing counterterm exponentials preserves holomorphy. Such a compiler can have zeros but cannot have poles.

By contrast, after the standard endpoint and gamma completion, the continuation of the direct inverse-Euler product is proportional to

$$
\Xi(s)^{-1}
$$

up to explicitly declared elementary factors. It has poles at zeros of \(\Xi\). No holomorphic Fredholm determinant can equal this meromorphic function on a connected domain containing one of those poles.

Equality on the Euler half-plane does not remove the obstruction: analytic continuation would force equality wherever both sides exist.

## Correct global types

There are three mathematically consistent options:

1. **Meromorphic determinant section:** retain the direct Sonin orientation and allow the compiler to be meromorphic.
2. **Ratio of determinant sections:** write
   $$
   M(s)=\frac{D_+(s)}{D_-(s)},
   $$
   so poles arise as zeros of \(D_-\). This matches the already constructed reflected scattering ratio \(M/M^\#\).
3. **Inverse determinant:** represent the Euler zeta factor by \(\det(I+K)^{-1}\), explicitly declaring that the compiler is an inverse section rather than a determinant.

Changing to \(K_p=+p^{-s}\) does not solve the problem because it produces \(1+p^{-s}\), not the zeta local factor.

## Consequence for multiplicities

In the ratio model, zero and pole multiplicities are divisor multiplicities of the two determinant sections. This is the correct line-bundle setting for preserving multiplicity under reciprocal reflection; a single everywhere-holomorphic scalar determinant is the wrong target type for the direct Sonin multiplier.

## Disposition

The requested global continuation cannot be a single holomorphic determinant in the source-fixed direct Euler orientation. The next constructive object is a meromorphic/reflected determinant-line ratio, with numerator and denominator separately holomorphic where their Schatten families are defined.