# Quarter Hankel condensation does not close positivity

## Question

Can Desnanot–Jacobi condensation turn lower-order Hankel positivity into an all-order induction?

## Claim boundary

The exact test covers sizes two through six, moment starts zero through eight, and shifts zero through four. The algebraic closure diagnosis is general for this recurrence, but it does not exclude another inductive invariant.

## Disposition

All 225 identities

\[
H_{r,k}H_{r+2,k-2}
=H_{r,k-1}H_{r+2,k-1}-H_{r+1,k-1}^2
\]

hold exactly, and every tested right-hand Turán gap is positive. However, assuming the lower factor is positive, positivity of that gap is equivalent to positivity of the target \(H_{r,k}\). Condensation therefore repackages rather than proves the missing sign. The next leaf is `quarter-hankel-shift-log-convex-invariant`, testing whether normalized Hankel determinant ratios expose a stronger shift invariant with a noncircular induction.
