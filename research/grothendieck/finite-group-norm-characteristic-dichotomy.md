# The finite-group norm has a sharp characteristic dichotomy

Epistemic-graph event: 1368.

## Universal identity

Let `G` be any nontrivial finite group, `k` any field, `A=k[G]`, and
`epsilon:A -> k` the augmentation.  Put

`nu_G=sum_(g in G) g`.

For every `x in A`, left or right multiplication permutes the elements of
`G`, so

`x nu_G=epsilon(x)nu_G=nu_G x`,

and therefore `nu_G^2=|G|nu_G`.  Neither commutativity nor the `p`-group
hypothesis enters this identity.

## The two regimes

If `char(k)` does not divide `|G|`, then

`e_G=nu_G/|G|`

is a central idempotent.  Multiplication by `e_G` projects `A` onto its
one-dimensional invariant trivial summand, with kernel the augmentation
ideal.  This is the split, normalized transfer regime.

If `char(k)` divides `|G|`, multiplication `m_nu` is square-zero and

`ker(m_nu)=I=ker(epsilon)`, `im(m_nu)=k nu_G subset I`.

Hence

`H(A,m_nu)=I/(k nu_G)`, `dim_k H=|G|-2`.

For `m` regular fibers the homology dimension is `m(|G|-2)`.  Thus the
rank formula of Ledger 1345 holds for every finite group at every bad
characteristic, not merely for finite `p`-groups.  What is lost outside the
`p`-group case is the identification of the augmentation ideal with the
Jacobson radical and of the norm line with the entire regular-module socle.

## Hostile controls

- `S3` in characteristic two or three has four residual dimensions per
  regular fiber.
- A group whose order is prime to the characteristic has no square-zero
  norm complex: its normalized norm is instead an idempotent projector.
- The only nontrivial bad-characteristic regular fiber with zero norm
  homology remains the order-two group in characteristic two.

## Scope

This is the algebraic norm correspondence on a regular group-algebra fiber.
It does not construct a physical relative-chain pushforward or establish
that a physical branch quotient realizes the regular representation.
