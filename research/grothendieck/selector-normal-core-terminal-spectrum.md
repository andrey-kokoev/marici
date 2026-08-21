# Selector normal core and terminal spectrum

## Terminal quotient theorem

For a finite group `G` and selector `c:G->R`, put

`S=Stab_R(c)` and `K_c=Core_G(S)=intersection_{g in G} gSg^-1`.

Then `K_c` is the unique largest normal kernel through which `c` descends.
Indeed, selector descent through `G->G/K` is equivalent to `K normal in G`
and `K subset S`, while the normal core is the largest normal subgroup of
`G` contained in `S`.

Decorate an admitted kernel by

`R(K)=rad(exp(K) exp(im(G->Aut(K))))`

and let `U(K)` be the corresponding prime-to-`R(K)` operation monoid. By
the monotonicity theorem,

`intersection_{K admitted} U(K) = U(K_c)`.

So one terminal quotient computes the power indices compatible with every
coefficient-admissible quotient. There is no need to intersect the spectra
kernel by kernel.

## Nonnormal hostile control

Let `G=S3`, let `H=< (12) >`, and let `c` distinguish the three right
cosets of `H`. Its right stabilizer is exactly `H`, which is not normal.
Its normal core is trivial. Therefore the selector is invariant under a
nontrivial subgroup but admits no nontrivial group quotient kernel.

The exact checker enumerates all six permutations, all subgroups, normality,
the selector stabilizer, and the normal core. The normal subgroup orders are
`1,3,6`, while the only admissible kernel has order `1`.

## Scope

The terminal object is terminal only in the coefficient quotient poset. It
does not create a relative-chain pushforward or certify a physical quotient.
