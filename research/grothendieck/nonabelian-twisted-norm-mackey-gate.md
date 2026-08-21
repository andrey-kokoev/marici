# Nonabelian twisted-norm Mackey gate

## Question

Does the prime-to-kernel-exponent criterion of Ledger 1258 remain valid for a
surjection of finite groups whose source is not abelian?

## Fiber criterion

Let `q:G -> H` be a surjection of finite groups and let `P_n(x)=x^n`.  On
integer-valued coefficient functions define `P_n^* f=f o P_n` and let `q_!`
be unnormalized fiber sum.  Then

`q_! P_n^* = P_n^* q_!`

if and only if, for every `h in H`, the power map sends the fiber `q^-1(h)`
bijectively onto `q^-1(h^n)`.

Choose `g in q^-1(h)` and write the source fiber as `gK`, where `K=ker q`.
The criterion is equivalently bijectivity of the twisted norm

`N_{g,n}:K -> K`,

defined by the unique factorization

`(gk)^n = g^n N_{g,n}(k)`.

When `G` is abelian this is multiplication by `n` on `K`, recovering the
criterion `gcd(n, exp K)=1`.  Without commutativity, the kernel exponent alone
does not control the twisted norms.

## Smallest hostile test

For the sign quotient `S3 -> C2`, the kernel is `A3 ~= C3`.  At `n=2`,
`gcd(2,3)=1`; nevertheless every transposition squares to the identity.  The
odd fiber of three elements therefore maps with multiplicity three to one
point of `A3`, rather than bijectively onto `A3`.  Both coefficient push-pull
compatibility and the corresponding basis-level fiber-lift compatibility
fail.

The abelian control `C6 -> C2` with kernel `C3` passes at `n=2`, proving that
the failure is caused by the nontrivial conjugation action, not by the kernel
or quotient orders.

## Scope

This is an algebraic correspondence result.  It neither supplies nor assumes
a physical relative-chain pushforward.  It also shows that Ledger 1258 must
retain its finite-abelian-source hypothesis; a nonabelian extension requires
the fiberwise twisted-norm criterion.

## Falsifier

The theorem is false if a tested fiber-sum square commutes while its power map
is not a bijection of fibers, or conversely.  The diagnosis is false if the
`S3 -> C2`, `n=2` square commutes, or if the `C6 -> C2`, `n=2` control fails.

