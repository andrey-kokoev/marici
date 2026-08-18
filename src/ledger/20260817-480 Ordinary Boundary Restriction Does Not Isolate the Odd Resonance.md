# Entry 480 — Ordinary Boundary Restriction Does Not Isolate the Odd Resonance

Entry 478 gives the stable filtered decomposition

\[
\operatorname{im}\beta_-
=\langle b^jh:0\leq j\leq D-4\rangle\oplus\langle r\rangle,
\]

with

\[
h=3a^3(1+b),\qquad r=[a^{11}b].
\]

The first support test is restriction to the already existing boundary
\(b=\pm1\).  It does not isolate the resonance line.

## Endpoint values

For every \(j\),

\[
(b^jh)|_{b=1}=6a^3,
\qquad
(b^jh)|_{b=-1}=0.
\]

Thus the entire extensive \(h\)-orbit collapses under ordinary restriction,
but it collapses to one **nonzero** boundary direction rather than vanishing.
The resonance class has

\[
r|_{b=1}=a^{11},
\qquad
r|_{b=-1}=-a^{11}.
\]

Because the two surviving directions have different \(a\)-degree and
different endpoint profiles, they are independent.  At every stable cutoff
\(D=16,20,24,28\), the boundary restriction therefore has

\[
\operatorname{rank}=2,
\qquad
\dim\ker=(D-2)-2=D-4.
\]

## Consequence

Ordinary restriction removes the growing part of the tail but retains one
boundary value of it alongside the resonance line.  Hence neither ordinary
endpoint restriction nor its kernel alone produces the desired single reduced
odd matrix-factorization class.

This is a negative result only for the underived restriction of the displayed
filtered generators.  It does not evaluate the sought two-term relative
coefficient complex, whose differential may cancel the surviving \(h\)
boundary direction.  In particular, the source-derived odd lattice of Entry
465 must be retained; replacing it by bare polynomial evaluation would forget
its boundary divisor.

The next gate is to construct the boundary map on the two-term complex and
test whether its conormal/connecting component maps onto the residual
\(6a^3\) at \(b=1\).  Only that derived cancellation can leave \(r\) alone.
No additional carrier point is indicated.

The executable audit is
`research/voevodsky/check_soft_axis_odd_boundary_restriction.py`.
