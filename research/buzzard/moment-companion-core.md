# Grothendieck arbitrary-degree moment/companion core

## Algebraic core

For an additive coefficient functional `moment : R[X] →+ R`, Lean defines

\[
B(p,q)=\operatorname{moment}(pq).
\]

`polynomialMultiplication_symmetric_for_momentForm` proves

\[
B(p,rq)=B(rp,q)
\]

for every multiplier `r`, purely from commutativity. The specialization
`multiplicationByX_symmetric_for_momentForm` is the arbitrary-degree source of
the matrix identity `H C = Cᵀ H`: after passing to the monic-polynomial
quotient, multiplication by `X` is the companion action and the moment Gram
matrix is Hankel/Hermite.

## Quotient gate

The polynomial statement does not automatically descend to representatives
modulo the companion polynomial. `AnnihilatesPrincipalIdeal` is the required
condition, and `moment_eq_of_congruentMod` proves representative independence
from it.

The `X²+1` hostile shows why this field is necessary: the polynomial is
congruent to zero modulo itself, but constant-coefficient readout gives `1`
and `0`. A coefficient functional that does not annihilate the defining ideal
cannot define the quotient Hermite form.

## Remaining bridge

The finite matrix theorem still needs a basis of the monic quotient and the
proof that Newton recurrence makes the chosen moment functional annihilate the
defining ideal. The classical rank/signature theorem and theta positivity are
separate and remain gated.

## Verification

No build was run under Nima's instruction; the module remains outside the root
import.
