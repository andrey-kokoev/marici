# The intrinsic norm-module determinant is trivial

Epistemic-graph event: 1376.

## Determinant audit

Let `H_d=(Z/d)^(d-2)`.  There are two canonical ways one might try to form a
local determinant from the present data.

First, rationalize.  Since `H_d` is torsion,

`H_d tensor Q=0`.

Every endomorphism then has determinant

`det(1-uF | H_d tensor Q)=1`.

Second, take the `p`-primary filtration and its finite-dimensional associated
graded over `F_p`.  The intrinsic prime operator `P_p=p` raises the filtration
and induces a nilpotent total operator.  Consequently

`det(1-uP_p | gr_p H_d)=1`.

Equivalently, every eigenvalue is zero.  Neither construction produces the
nontrivial local denominator expected of an Euler factor.

## Why alternative determinants are not yet admissible

For indices `n` coprime to `p`, scalar or Adams operations can act invertibly
on the `p`-primary layers, and their determinants need not be one.  But no
intrinsic rule selects such an `n` as Frobenius at `p`; choosing it imports
the missing arithmetic datum.  The obvious choice `n=p` is precisely the
nilpotent or Mackey-incompatible operation identified in Ledger 1351.

A regularized determinant, a cohomological sign convention, or an alternating
product could create nontrivial rational functions only after adding a new
graded complex and a source-derived operator.  None is present in the norm
module alone.

## Verdict

The current regular-fiber norm homology cannot generate a nontrivial Euler
factor by its canonical rational or primary-graded determinants.  This is a
failure of the third program gate for the present object, not a proof that no
enlarged geometric correspondence can succeed.

## Scope

No physical relative-chain operator, geometric Frobenius, point-counting
theory, or global trace formula is asserted.
