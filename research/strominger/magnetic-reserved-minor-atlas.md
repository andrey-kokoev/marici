# The reserved Hall chart has a separate presentation boundary

The closed Hall assignment proves that a nonzero determinant term exists, but
does not prevent cancellation among all determinant terms.  Exact evaluation
of its selected weighted minor reveals a simple candidate degeneracy locus:

\[
g\equiv0\pmod2,
\qquad
q=2g+8.
\]

This is not a rank defect.  At every audited point on that locus, replace the
selected observation row

\[
R_1\longmapsto R_3.
\]

The resulting maximal minor is nonzero.  Hence

\[
\text{preferred coordinate vanishes}
\quad\not\Rightarrow\quad
\bigwedge^r M=0.
\]

The defect is transported from the earlier onset chart.  At
`a_max=g+8`, `magnetic-chart-cocircuit-symbolic.md` proves the literal
two-row identity

\[
(2g+7)R_1-(3g+7)R_0=0
\]

for every even grade.  Continuing the component to the reserved old block
`a_max=q=2g+8` leaves the corresponding right circuit on its onset columns
and transports the dual observation witness through the triangular tail.

Every audited preferred-chart zero has corank one.  In the later chart the
primitive row dependence has expanded support

\[
\{1,0,-2,-4,\ldots,-g-2\},
\]

and the corresponding column circuit has support

\[
\{(0,-)\}\cup\{(a,+):a=4,6,\ldots,q-g\}.
\]

Thus the growing matrix is not the irreducible obstruction.  The right
circuit terminates exactly at the onset depth `a=q-g=g+8`; all later column
coordinates vanish.  Dually, the row cocircuit spreads to a reflection-side
window of width `g+3`.  The remote tail transports the presentation witness
but creates no new dependence.

The support matching and the weighted atlas therefore solve different
problems.  The former establishes Hall admissibility; the latter must cover
coordinate boundaries created by cancellation.  The family above supplies a
particularly clean cocircuit-type presentation witness: the old row set loses
faithfulness while a single alternate observation restores it.

The exact checker covers

\[
2\le g\le12,
\qquad
2\le q\le30,
\qquad q\text{ even}.
\]

The preferred-chart divisor is already explained symbolically at its onset.
What remains conditional is unbounded nonvanishing of the alternate chart:
the observed hypergeometric recurrence for the row-`3` transverse response
`tau_g` still requires a symbolic Schur-elimination derivation.
