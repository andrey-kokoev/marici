# Initiality forces Frobenius rigidity on conditional pi_0

Epistemic-graph event: 1379.

## Rigidity theorem

Let `M` be the conditional initial commutative semiring derived from the
pointed additive Carrier.  Every unital semiring endomorphism

`F:M -> M`

is the identity.  This follows immediately from initiality: there is exactly
one unital semiring map from the initial object to itself, and the identity is
one such map.

The additive endomorphisms `f_n` used to define multiplication satisfy

`f_m composed f_n=f_(mn)`,

but `f_n(U)=nU`.  Hence `f_n` preserves the multiplicative unit `U` only for
`n=1`.  The nontrivial power-indexed additive maps are not semiring
Frobenius endomorphisms.

## Frobenius-congruence control

The identity does satisfy

`F(x)=x congruent x^p mod p`

for every intrinsic prime `p`, by the ordinary Frobenius congruence in the
initial semiring.  But the same operator occurs at every prime.  It therefore
contains no prime-dependent spectral information and cannot distinguish
local places.

A rank-one determinant of the identity would be `1-u`.  Substituting
`u=p^(-s)` would reproduce the denominator of the zeta function of a point
over `F_p`, but neither the rank-one cohomology object, the prime-indexed
specialization, nor the spectral weight `p^(-s)` is supplied by `M` itself.
Using that expression now would insert the desired Euler factor.

## Consequence

Intrinsic primes do emerge conditionally on `pi_0`, but nontrivial Frobenius
cannot live as a unital endomorphism of the initial semiring itself.  Any
successful next object must enlarge `M` while retaining its prime classes,
for example through independently derived symmetric powers, a Burnside-type
category, a Witt object, or graded cohomology.  Those structures are targets,
not present conclusions.

## Scope

This is a categorical rigidity theorem at conditional `pi_0`.  It asserts no
full-Carrier lift, physical chain operation, Witt construction, or Euler
product.
