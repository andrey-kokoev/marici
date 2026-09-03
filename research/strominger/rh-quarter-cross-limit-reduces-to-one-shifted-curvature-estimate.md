# Quarter cross limit reduces to one shifted-curvature estimate

## Problem

The exact shifted condensation recurrence did not yet identify the asymptotic datum whose control proves the cross limit.

## Bold conjecture

The only required datum is convergence of the normalized shift curvature

\[
\log\frac{R_{n-1,1}^2}{R_{n-1,0}R_{n-1,2}}-2\log n.
\]

## Named rivals

The rivals are a different power of \(n\), failure of shifted-curvature convergence, and a missing factor from the quartic polynomial \(q_0(n-1)\).

## Risky consequences

The recurrence variables must satisfy the exact reduction

\[
\frac{n^2\Theta_n}{q_0(0)}=
\frac{n^2R_{n-1,1}^2}
{q_0(n-1)R_{n-1,0}R_{n-1,2}}.
\]

Hence convergence of the displayed curvature to \(c\) must imply
\(n^2\Theta_n\to q_0(0)e^c\).

## Strongest falsification attempt

Exact rational recurrence values through degree twenty verify the reduction. The normalized curvature remains finite but its last-five spread exceeds \(0.002\), so the finite test explicitly does not supply convergence. A wrong degree shift in \(q_0\) is rejected. All five diagnostic gates passed.

## Disposition

Promote the exact reduction, not the limit. The first missing object is a uniform shifted-curvature asymptotic with an \(o(1)\) remainder; acceptance requires a source-derived bound proving convergence. Defer this proof branch. Reallocate to the executable rival `quarter-shifted-curvature-profile`, which tests whether the same balance and power hold uniformly for several integer shifts.

## Claim boundary

The reduction is exact. The convergence premise and the constant \(c\) remain unproved, so no exact cross-limit value follows.
