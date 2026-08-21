# Split-section ambiguity is a derivation torsor

## Torsor theorem

For abelian groups `K,H`, consider the split projection

`q:K x H -> H`.

Every group-homomorphic section is

`s_u(h)=(u(h),h)`

for a unique `u in Hom(H,K)`. Every base-preserving shear is

`alpha_v(k,h)=(k+v(h),h)`

for `v in Hom(H,K)`, and it acts on sections by

`alpha_v s_u=s_(u+v)`.

Thus the section set is a torsor under the derivation group `Hom(H,K)`, and
the shear action is simply transitive. If `Hom(H,K)` is nontrivial, no section
is invariant under all base-preserving shears.

## Exact prime controls

For `C_p x C_p -> C_p` at `p=2,3,5`, there are exactly `p` homomorphic
sections and `p` shears. The orbit of any section is the full section set,
and the fixed-section count is zero.

## Relation to resonance

The derivation ambiguity adds no new resonance prime: its primes already lie
in the kernel, as used in Ledger 1299. Yet it obstructs choosing a natural
selection-preserving split. Therefore the norm--resonance bidegree is complete
for coefficient arithmetic composition but not for canonical lift data.

## Scope

A source-derived marking can select a torsor point, but none is supplied by
the abstract quotient. No physical chain lift is constructed here.
