# The norm detects fiber-invariant boundary defects away from degree torsion

Epistemic-graph event: 1336.

## Conditional detection theorem

Let `S:C(H)->C(J)` be the formal quotient pushforward for a fiber of size
`d`, and let `T:C(J)->C(H)` be the fiber-trace map.  On deck bases,

`S T=d id`.

Assume multiplication by `d` is injective on `C(J)`.  Then `S` is injective
on `im(T)`.  Indeed, if `v=T y` and `S v=0`, then `d y=0`, hence `y=0` and
`v=0`.

Consequently, in a quotient tower, an earlier boundary defect cannot be
annihilated by the next quotient if its image is fiber-invariant in the
strong sense

`im(Omega_q) subset im(T_r)`

and the target chain module has no `d_r`-torsion.  Under this hypothesis,
`S_r Omega_q=0` implies `Omega_q=0`.  Combined with separated transported
supports and surjectivity of `S_q`, Ledger 1319's terminal test certifies both
stages.

## Bad-prime failure

The torsion condition is essential.  For `C2->1` over `F_2`,

`T(1)=(1,1)` and `S(x,y)=x+y`,

so `S T=2 id=0`.  The nonzero invariant trace vector `(1,1)` lies in
`ker(S)`.  A boundary defect supported on it is invisible after the quotient.
More generally, degree primes are precisely where norm-based detection can
collapse.

## Scope

This is an algebraic detection theorem for a supplied trace map.  The frozen
five-site evidence does not yet supply a physical relative-chain `T` or `S`.
It therefore cannot activate the physical Mackey object.  It does specify a
useful audit: once physical maps exist, test whether each defect image is in
the trace submodule and whether the relevant coefficient module has degree
torsion.
