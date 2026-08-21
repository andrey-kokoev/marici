# Arbitrary finite-surjection conjugation spectrum

## Intrinsic theorem

Let `q:G->H` be an arbitrary finite group surjection with kernel `K`, and
let

`A_q = image(G -> Aut(K))`

be the conjugation image.  The `n`-th power correspondence commutes with
every coefficient fiber sum and basis-level fiber lift if and only if

`gcd(n,exp(K)*exp(A_q))=1`.

This includes split, nonsplit, central, and noncentral extensions.

## Fiber reduction

For `g in G`, conjugation by `g` restricts to an automorphism `alpha_g` of
`K`.  After translating source and target fibers, the restricted power map
is the twisted word

`k -> k alpha_g(k) ... alpha_g^(n-1)(k)`

up to reversing the harmless convention for left versus right cosets.  The
fiber problem therefore depends on the actual conjugation action, while the
extension cocycle contributes only the target translation `g^n`.

If `n` is coprime to `exp(K)*exp(A_q)`, the cyclic semidirect argument makes
every such twisted word bijective.

If a prime divides `n` and `exp(K)`, the identity fiber fails.  If it divides
`n` and `exp(A_q)`, choose a conjugation automorphism `alpha` of that prime
order and a moved element `x`.  The coboundary `x^-1 alpha(x)` has telescoping
twisted norm equal to one, so the corresponding fiber is not injective.

## Nonsplit noncentral control

The generalized quaternion extension `Q16 -> C2` has kernel `C8`, inversion
conjugation, and no complement, while the dihedral extension `D16 -> C2` is
the split control with the same kernel action.  Both have exactly the odd
survivor indices through 24.  The nonsplit cocycle changes the group but not
the fiber spectrum.

## Scope

This completes the algebraic finite-surjection classification.  For
nonabelian groups the power correspondence is basis-linear and not generally
a ring Adams operation.  No physical relative-chain pushforward is supplied.

