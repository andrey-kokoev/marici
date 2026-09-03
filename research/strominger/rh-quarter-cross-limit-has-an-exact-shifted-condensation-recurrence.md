# Quarter cross limit has an exact shifted condensation recurrence

## Problem

Finite extrapolation could not prove the quarter cross limit because no source recurrence had been isolated.

## Bold conjecture

Dodgson condensation closes on the integer shift half-lattice and reproduces every determinant from unit boundary data.

## Named rivals

The rivals are a recurrence requiring unavailable off-lattice data, a shift convention mismatch, and agreement only at the cross-ratio level rather than at determinant level.

## Risky consequences

Writing \(R_{n,a}\) for the determinant with every staircase parameter shifted by \(a\), the recurrence must be

\[
R_{n,a}=
\frac{q_a(n-1)R_{n-1,a}R_{n-1,a+2}
-q_a(0)R_{n-1,a+1}^2}{R_{n-2,a+2}},
\qquad R_{0,a}=R_{1,a}=1.
\]

It must reproduce independently evaluated determinants across several degrees and shifts.

## Strongest falsification attempt

Exact rational checks through \(n=8\) and shifts zero through six give 63 determinant agreements, reproduce every tested cross ratio, preserve positivity, and reject a deliberate shift mismatch. All five gates passed.

## Disposition

Promote the recurrence as an exact source-derived representation. It replaces determinant growth by a closed nonlinear recurrence on \((n,a)\), but does not yet prove the limit. The next leaf is `quarter-shifted-recurrence-asymptotic-balance`, deriving which uniform shifted asymptotic data are necessary and whether the recurrence determines the leading cross-limit constant.

## Claim boundary

Closure and finite exact verification do not supply uniform asymptotic estimates. Division is valid on the tested positive domain; a general positivity proof remains separate.
