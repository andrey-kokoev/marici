# The even chart boundary is a two-row cocircuit

Companion to `checkers/magnetic_chart_cocircuit_checks.py` (5/5, exit 0) and
`results/magnetic_chart_cocircuit.json`.

At the even primary-chart locus

\[
q=2g+8,\qquad k=\frac g2+4,\qquad a=g+8,
\]

the preferred Hall matrix does not lose rank through a large determinant
cancellation.  Its target rows (R_1) and (R_0) obey the columnwise identity

\[
\boxed{(2g+7)R_1-(3g+7)R_0=0.}
\]

Thus the preferred square matrix has a left cocircuit supported on exactly two
target rows.  Its primitive coordinates are

\[
\frac1{\gcd(2g+7,3g+7)}(2g+7,-3g-7).
\]

For (g=2,4,6,8,10,12,14), these are

\[
(11,-13),(15,-19),(19,-25),(23,-31),(27,-37),(31,-43),(5,-7).
\]

The checker constructs every source column from the exponent-lattice action
and verifies the identity before taking a determinant.  Shifting (2g+7) to
(2g+8) leaves a nonzero residual in every case, so the formula is rigid in
the tested family.

The alternate chart replaces target row (1) by row (3).  Its maximal minor
is nonzero at every onset.  Therefore the cocircuit belongs to the chosen row
frame, not to the transported column space:

\[
\text{two-row target dependence}
\Longrightarrow
\text{preferred Plucker coordinate zero}
\not\Longrightarrow
\bigwedge^rM=0.
\]

This supplies the local explanation for the arithmetic divisor (q=2g+8).
The chart boundary occurs when the Hall selection simultaneously includes the
two proportional target evaluations (R_1,R_0).  Moving to (R_3) removes
the duplicate evaluation without altering the invariant object.

## Scope

The cocircuit formula is exactly verified for the seven even grades
(2\le g\le14).  A symbolic all-even-grade proof should now be short: split
the admitted source columns by their two reflected branches, substitute
(q=2g+8, a=g+8) into the path coefficients, and prove the displayed row
identity branchwise.  Nonvanishing of the row-(3) replacement for arbitrary
even (g) remains a separate determinant-line transport statement.
