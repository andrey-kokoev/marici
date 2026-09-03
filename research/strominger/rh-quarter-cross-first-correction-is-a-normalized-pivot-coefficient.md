# The quarter cross first correction is a normalized pivot coefficient

## Question

What exact next-order asymptotic would prove \(u=6/5\)?

For the source parameter vector \(s\), the divided condensation recurrence gives

\[
1-\Theta_n(s)
=
\frac{d_n(s)}
{q_{n-1}(s)d_{n-1}(s+2)}.
\]

Consequently

\[
\Theta_n
=\frac{13}{60n^2}
\left(1+\frac{6}{5n}+O(n^{-2})\right)
\]

is equivalent to the normalized pivot expansion

\[
\frac{d_n(s_0)}
{q_{n-1}(s_0)d_{n-1}(s_0+2)}
=1-\frac{13}{60n^2}-\frac{13}{50n^3}+O(n^{-4}).
\]

The cubic coefficient follows exactly because

\[
\frac{13}{60}\frac65=\frac{13}{50}.
\]

This target couples pivots at \(s_0\) and \(s_0+2\). A pointwise asymptotic at the source vector cannot determine it; the proof requires a common-shift-uniform pivot expansion through relative order \(n^{-3}\).

## Disposition

Resolve the first-correction candidate to the normalized-pivot coefficient \(-13/50\). The next leaf is `quarter-normalized-pivot-cubic-coefficient`: derive this expansion from a simultaneous shifted LU system.

## Claim boundary

The equivalence is exact at the level of asymptotic coefficients but does not prove the expansion. The finite fit remains the only evidence for \(u=6/5\).
