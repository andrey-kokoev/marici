# The canonical primary filtration is not a Frobenius theory

Epistemic-graph event: 1375.

## Canonical operations on norm homology

Let `H_d=(Z/d)^(d-2)` and write `d=product p^a_p`.  Without choosing a
Chinese-remainder splitting, each primary subgroup is intrinsically

`H_(p)={x in H_d : p^r x=0 for some r}`

and is isomorphic to `(Z/p^a_p)^(d-2)`.  On it, scalar multiplication

`P_p(x)=p x`

is canonical and satisfies the exact composition law

`P_p^r=P_(p^r)`.

Its kernel and image filtrations recover the valuation `a_p`:

`ker(P_p^r) congruent (Z/p^min(r,a_p))^(d-2)`,

and `P_p^a_p=0` while `P_p^(a_p-1)` is nonzero when `a_p>1` and `d>2`.
The successive layers are `(F_p)^(d-2)`.

## Hostile Frobenius audit

These operations are canonical prime-power operations, but they are not an
arithmetic or geometric Frobenius:

- `P_p` is nilpotent on the `p`-primary component and induces zero on
  `H_(p)/pH_(p)`.
- It is scalar multiplication inherited from the `Z`-module structure, so it
  contains no information beyond `p^a_p | d`.
- It cannot distinguish groups or correspondences of the same degree.
- It supplies neither fixed-point counts nor unit eigenvalues from which a
  local Euler polynomial could be formed.

The independently supplied integral group ring can carry Adams operations
`psi^n`, but the prior Adams--Mackey gate shows that `psi^n` commutes with a
kernel correspondence only when `gcd(n,exp K)=1`.  Hence the candidate
`psi^p` fails precisely on a nontrivial `p`-primary kernel.  In the five-site
characteristic-two algebra, absolute Frobenius collapses the augmentation
ideal and every branch norm.

Thus the second program gate has a split verdict: canonical primary and
prime-power filtrations exist, with strict composition, but no nontrivial
Frobenius operator has been derived from them.

## Scope

This concerns the integral regular-fiber norm module and previously verified
algebraic Adams gates.  It does not exclude a separately derived geometric
object with Frobenius, and it supplies no physical relative-chain map.
