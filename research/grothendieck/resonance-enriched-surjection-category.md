# Finite surjections form a resonance-enriched coefficient category

## Resonance cost

For a finite-group surjection `phi:G->H`, define its squarefree resonance
cost by

`rho(phi)=R_G(ker(phi))`.

The identity has trivial kernel, hence `rho(id)=1`. For composable
surjections `G--phi->H--psi->J`, Ledger 1299 applied to `ker(psi)` gives

`rho(psi phi)=lcm(rho(phi),rho(psi))`.

Thus finite surjections carry a strict enrichment in the join-semilattice of
squarefree positive integers ordered by divisibility, with join `lcm` and
unit `1`.

Passing to compatible indices gives the equivalent contravariant law

`U(psi phi)=U(phi) intersection U(psi)`.

## Selector objects

A selector `c` contributes an object cost `R(K_c)`. Pullback along `phi`
combines the arrow and object costs:

`R(K_(phi^*c))=lcm(rho(phi),R(K_c))`.

This packages Ledgers 1297--1300 as one strict coefficient correspondence
system. It supplies pullback, composition, selector kernels, and the exact
power--Mackey admissibility sieve.

## Exact cyclic control

For `C60->C30->C6`, the two arrow costs are `2` and `5`, while the composite
cost is `10`. Through index 60 the spectra have sizes `30`, `48`, and `24`,
and the composite spectrum is exactly their intersection. Identity laws also
hold.

## Missing enrichment

No corresponding covariant relative-chain functor has been constructed.
Therefore this is the coefficient half of a paired Mackey/correspondence
object, not the physical object itself.
