# The integral norm relation defines a two-periodic complex

Epistemic-graph event: 1369.

## Construction

Let `G` be a nontrivial finite group of order `d`, let `R` be a commutative
ring, and put `A=R[G]`.  Write `T` for multiplication by
`nu_G=sum_(g in G)g`.  The universal identity

`T^2=dT`

implies

`T(d-T)=0=(d-T)T`.

Thus `A` carries the canonical two-periodic complex

`... -> A --(d-T)--> A --T--> A --(d-T)--> A --T--> A -> ...`.

This exists integrally; it does not require `d` to vanish or be invertible.

## The norm-side homology

Let `epsilon:A -> R` be augmentation and `I=ker(epsilon)`.  Since
`Tx=epsilon(x)nu_G` and the coefficient embedding `R nu_G -> A` is
injective,

`ker(T)=I`.

Every `x` has the canonical expression `x=epsilon(x)1+i`, with `i in I`,
and hence

`(d-T)x=d i+epsilon(x)(d1-nu_G)`.

Therefore the homology at the target of `d-T` is exactly

`H_T=I/(dI+R(d1-nu_G))`.

This quotient is annihilated by `d`.  It is the integral object whose
bad-characteristic fibers produce the modular norm obstruction.

## Specializations

- After inverting `d`, multiplication by `d-T` maps onto `I`, so `H_T=0`.
- Over a field `k` with `char(k)` dividing `d`, `d-T=-T`, and
  `H_T=I/(k nu_G)`, of dimension `d-2`.
- For `G=C2`, `d1-nu_G=1-g` generates `I`, so the integral quotient is zero.
- For `G=C3`, reduction gives `I/(3I+R(3-g^0-g-g^2))`; over `Z` this is
  `Z/3`, recovering the one-dimensional characteristic-three residual.

## Scope

This is a canonical algebraic two-periodic correspondence on the regular
group ring.  It does not supply the missing physical relative-chain
pushforward.  A physical interpretation would require a source-derived pair
of chain maps realizing both `T` and `d-T` and respecting the physical
boundary operator.
