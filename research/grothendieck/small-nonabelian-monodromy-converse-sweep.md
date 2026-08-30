# Small nonabelian-monodromy converse sweep

## Falsifier search

Ledger 1275 leaves open whether every visible monodromy prime is necessary
for power--Mackey compatibility when the kernel is nonabelian.  The smallest
direct falsifier is a faithful cyclic automorphism action and a prime `p`
dividing its order for which every `p`-th power fiber map remains bijective.

The checker enumerates every automorphism of:

- `S3` (6 automorphisms);
- `D8` (8 automorphisms);
- `Q8` (24 automorphisms).

For every nonidentity automorphism, it forms the corresponding cyclic
semidirect product, tests every quotient fiber for indices `1..12`, and
compares the result with

`gcd(n,exp(K)*order(alpha))=1`.

## Result

No counterexample occurs.  Every visible action prime produces a failed
fiber, and every coprime index passes, across the complete 38-automorphism
census.  Thus the product-exponent converse survives all nonabelian groups of
this bounded family.

## Scope

This is exhaustive for the three named automorphism groups, not a proof for
arbitrary nonabelian kernels.  It upgrades the open converse from one
quaternion control to a bounded hostile census and supplies a precise future
falsifier.  No ring Adams operation or physical chain transfer is asserted.

