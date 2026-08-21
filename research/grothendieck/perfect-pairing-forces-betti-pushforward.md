# Perfect pairing forces the only possible Betti pushforward

## Uniqueness theorem

Let coefficient modules `C_G,C_H` and Betti modules `B_G,B_H` carry perfect
pairings, and let `q^*:C_H->C_G` be coefficient pullback. A Betti map

`sp_q:B_G->B_H`

satisfying

`<q^*c,Gamma>_G=<c,sp_q Gamma>_H`

for every `c,Gamma` is unique, because the pairing on `H` is nondegenerate.
It is the adjoint transpose of `q^*`.

For deck-labelled dual bases this forces

`sp_q(Gamma_g)=Gamma_(q(g))`

with coefficient one. No averaging, sign, or multiplicity remains free once
the pairing normalization is fixed.

## Strict composition and norm

For composable quotients, transpose reverses products, so the forced maps
satisfy

`sp_(r q)=sp_r sp_q`.

Moreover, the same matrix identity gives the degree norm on the paired basis.
For `C4->C2->1`, the checker obtains norms two and four and strict
composition exactly.

## Remaining existence problem

This theorem is conditional on perfect pairings and on the existence of a
map on the actual Betti relative complexes. It determines the only possible
map on deck-labelled generators, but does not prove that this assignment
commutes with relative boundaries, respects support, or comes from source
geometry. Those are now the entire remaining physical obstruction.
