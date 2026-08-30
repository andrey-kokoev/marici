# Visible-monodromy exponent Adams spectrum

## Corrected theorem

Let a finite group `H` act, not necessarily faithfully, on `K=F_p^r` via
`rho`, and form `G=K semidirect H -> H`.  The `n`-th power correspondence
commutes with every coefficient fiber sum and basis-level fiber lift exactly
when

`gcd(n,p*exp(im rho))=1`.

The proof factors the action through the faithful visible quotient
`H/ker(rho)`.  Every fiber norm depends only on `rho(h)`, so an invisible
factor in `H` cannot add a resonance prime.  Ledger 1268 is the faithful
special case.

## Hostile controls

Let `C15` act on `F_2^2` through its quotient `C3` and the irreducible
order-three matrix.  At `n=5`, the full quotient exponent would incorrectly
predict failure, while the visible exponent criterion predicts survival.
Exact fiber enumeration passes.

For the entirely trivial action `C3` on `F_2`, index `n=3` likewise survives:
the quotient power map changes the fiber label, but the fiber-linear norm is
`3I=I`.  Thus quotient torsion invisible to the kernel action is not a Mackey
obstruction.

## Scope and falsifier

This concerns an elementary-abelian kernel and algebraic power
correspondences.  It does not assert a ring Adams operation for nonabelian
total groups or supply a physical chain pushforward.  A nonfaithful example
disagreeing with the image-exponent criterion falsifies the theorem.

