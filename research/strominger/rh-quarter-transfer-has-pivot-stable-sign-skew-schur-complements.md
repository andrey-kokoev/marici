# Quarter transfer has pivot-stable sign-skew Schur complements

## Question

Can the terminal bordered sign rule be expressed as a matrix class preserved under principal elimination?

## Claim boundary

The classification covers all 247 relevant principal Schur complements of the order-eight transfer. It does not prove closure at arbitrary Hurwitz size.

## Disposition

For every eliminated principal set \(S\), the Schur complement has positive diagonal. For remaining indices \(i<j\),

\[
\operatorname{sgn}(C/C_S)_{ij}=(-1)^{j-i+1},
\qquad
\operatorname{sgn}(C/C_S)_{ji}=(-1)^{j-i}.
\]

All 1,792 bordered identities

\[
\det C[S\cup i,S\cup j]
=
\det C[S,S]\,(C/C_S)_{ij}
\]

and their paired versions hold exactly. Thus principal elimination preserves a positive-diagonal, opposite-off-diagonal sign class. This pivot-stable sign-skew structure generates anti-sign-symmetry and the P-matrix induction. The next leaf is `quarter-hurwitz-pivot-sign-recurrence`, seeking a recurrence from the endpoint Hurwitz matrices that preserves this Schur sign class at arbitrary size.
