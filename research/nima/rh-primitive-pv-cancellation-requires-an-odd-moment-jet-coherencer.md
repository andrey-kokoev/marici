# RH primitive principal-value cancellation requires an odd moment-jet coherencer

## Question

Which existing source channel could cancel the algebraic moment tail in the
primitive principal-value lane before prime aggregation, while retaining the
odd orientation signal?

## Typed classification

The boundary carrier has an even overlap/delta coordinate and an odd
front/principal-value coordinate. This immediately excludes three tempting
identifications.

The reciprocal Maslov cancellation occurs before arithmetic currents and is
therefore the wrong source channel. The reciprocal unit-current anomaly is
forced boundary data, but it lies in the overlap/current coordinate and has
the wrong parity. Primitive and square Euler jets share one abelian nilpotent
generator, so their flat transport supplies no independent odd direction.

Pairing the entire odd front with its reciprocal negative is also invalid: it
cancels both the divergent moment and the orientation residue. Convergence
would then have been bought by erasing the channel that was meant to carry
the comparison.

The only surviving type is a relative odd moment-jet subtraction. It removes
the nondecaying Hilbert moment before aggregation while leaving an odd
remainder. Grothendieck's local first-cumulant theorem fixes the arithmetic
coefficient that such a subtraction must reproduce; it does not yet construct
the required boundary incidence.

## Finite model

Use coordinates `(even overlap, odd moment, odd residue)`. The primitive tail
is represented by `(0,1,1)`.

- An even counterterm changes the first coordinate and leaves the divergent
  odd moment untouched.
- Full reciprocal negation sends the vector to zero and erases orientation.
- The typed moment jet `(0,-1,0)` leaves `(0,0,1)`.

On dyadic scales, the last pattern replaces the divergent primitive term
`2^n/n^2` by the summable term `1/(n 2^n)` when the source supplies an
exponentially controlled remainder.

## Source candidate and missing theorem

The two comoving front charts are presently the sole source-derived carrier
with the correct ingredients: an exchanged odd front, a retained even
overlap, and a mandated relative pushforward before integration over prime
scale. The next theorem must construct an odd moment-jet incidence on this
Čech object and prove all of the following:

1. Its coefficient equals the independently derived local primitive first
   cumulant at every prime.
2. It cancels the Hilbert moment before prime aggregation.
3. It preserves a nonzero odd residual rather than cancelling the whole front.
4. The residual has exact or exponential scale control, not merely finitely
   many vanishing moments.
5. The construction uses no scalar zeta continuation or divisor information.

Aspect's off-grid moment alias gives the immediate hostile: finite full rank
on an assumed support does not authorize that support. Consequently, any
finite moment calculation must be paired with a source-derived support law or
an exact nonperturbative remainder identity.

## Verdict

No already completed scalar or jet channel supplies the cancellation. The
two-front relative pushforward is the unique viable source location, and the
local first cumulant fixes its target coefficient. The missing constructor is
an odd moment-jet coherencer joining those two results. Until that incidence
is derived, primitive principal-value completion remains blocked rather than
renormalized by declaration.

## Verification

Run:

```powershell
python research/nima/checkers/check_rh_odd_moment_jet_coherencer.py
```
