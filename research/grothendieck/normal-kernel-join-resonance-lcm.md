# Normal-kernel joins carry least-common-multiple resonance

## Join theorem

For normal subgroups `K,L` of a finite group `G`, their join is `KL`. With

`R(K)=rad(exp(K) exp(A_K))`, `A_K=im(G->Aut(K))`,

one has

`R(KL)=lcm(R(K),R(L))`.

For the kernel factor, the primes in the exponent of a finite group are the
primes dividing its order, and the prime support of `|KL|` is the union of
the supports of `|K|` and `|L|`.

For the action factor, restriction gives a homomorphism

`A_KL -> A_K x A_L`.

It is injective because an action trivial on both `K` and `L` is trivial on
their generated subgroup `KL`; both projections are surjective by definition.
Hence the prime support of `A_KL` is exactly the union of those of `A_K` and
`A_L`. Combining the two factors proves the radical lcm identity.

Therefore

`U(KL)=U(K) intersection U(L)`.

This identifies simultaneous coarse-quotient compatibility with the normal
join, while paired-selector refinement from Ledger 1288 uses the meet.

## Nonabelian control

In `G=S3 x C5`, take `K=A3 x 1` and `L=1 x C5`. Their labels are `6` and
`5`; the join `A3 x C5` has label `30`. Exact action enumeration verifies
that its spectrum through 60 is the intersection of the two input spectra.

## Scope

The join theorem classifies coefficient correspondences. It does not supply
the physical constructor that would simultaneously realize two quotient
systems or any relative-chain pushforward.
