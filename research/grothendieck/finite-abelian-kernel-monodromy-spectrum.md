# Finite-abelian-kernel monodromy spectrum

## Theorem

Let a finite group `H` act on a finite abelian group `K`, let `M` be the
image of this action in `Aut(K)`, and form `G=K semidirect H -> H`.  The
`n`-th power correspondence commutes with every coefficient fiber sum and
basis-level fiber lift if and only if

`gcd(n, exp(K)*exp(M))=1`.

For each prime `p` dividing `|K|`, reduce the twisted norm on the
`p`-primary component modulo `p`.  An endomorphism of a finite abelian
`p`-group is invertible exactly when its reduction on `K_p/pK_p` is
invertible.  Ledger 1269 then applies to this Frattini quotient.  The identity
fiber detects the primes in `exp(K)`; nontrivial visible monodromy detects the
remaining primes in `exp(M)`.

## Exact controls

- `C4 semidirect C2` with inversion;
- `C9 semidirect C2` with inversion;
- `(C4)^2 semidirect C3` with the lifted order-three matrix
  `[[0,-1],[1,-1]]`.

Exhaustive fiber tests through index 24 agree with the product-exponent
criterion in every case.

## Scope and falsifier

The kernel is finite abelian, while the total group may be nonabelian.  The
power correspondence is basis-linear and need not be a ring Adams operation.
No physical chain pushforward is supplied.  Any exact fiber disagreement
with the product-exponent criterion falsifies the theorem.

