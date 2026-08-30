# Surjective preimage adds exactly the kernel resonance surcharge

## Extension theorem

Let `phi:G->H` be a surjection of finite groups, put `N=ker(phi)`, and let
`K` be normal in `H`. For `P=phi^-1(K)`,

`R_G(P)=lcm(R_G(N),R_H(K))`.

The primes in `P` are exactly those in `N` or `K`, by the exact sequence

`1 -> N -> P -> K -> 1`.

For conjugation images, restriction and passage to the quotient give

`A_P -> A_N x A_K`

with surjective projections. Its kernel consists of automorphisms fixing `N`
pointwise and `P/N` pointwise. Such automorphisms are extension derivations
with values in `Z(N)`, so their orders introduce only primes already dividing
`|N|`. Hence the total kernel-plus-action prime support is precisely the
union of the supports defining `R_G(N)` and `R_H(K)`.

Therefore

`U_G(P)=U_G(N) intersection U_H(K)`.

Combined with Ledger 1297, selector pullback adds exactly the resonance sieve
of the map kernel.

## Exact controls

- `(S3 x C5)->S3` over `A3`: labels `5`, `6`, and `30`.
- `Q8->C2 x C2` over an order-two subgroup: labels `2`, `2`, and `2`;
  the preimage is cyclic of order four and conjugation inversion adds no new
  prime.

Both spectra equal the intersection through index 60.

## Scope

This is an algebraic extension law. It does not construct a Betti transfer or
turn coefficient pullback into a physical pushforward.
