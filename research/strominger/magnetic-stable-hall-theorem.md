# Hall support stabilizes after a finite reflection window

Companion to checkers/magnetic_stable_hall_checks.py (6/6, exit 0) and
results/magnetic_stable_hall.json.

Let \(w=\lfloor q/2\rfloor\). Once \(k>w+1\), match the newly admitted minus
column to

\[
r_k^-=-2k-g
\]

and the newly admitted plus column to

\[
r_k^+=-2k-g+2w+1.
\]

The two row families have opposite parity, while each family advances by two
at every cutoff. Hence these rows never collide with one another or with an
earlier stable assignment.

The minus edge is the left path endpoint \(B_0\), which is nonzero in the
stable range. For odd \(q\), the plus edge is also \(B_0\), with strictly
negative derivative weight. For even \(q\), it is \(B_1\). Here \(a>4\), the
two adjacent path coefficients have the same sign, and both derivative
weights are negative, so their sum cannot cancel.

Therefore:

\[
\boxed{\text{Any complete Hall matching extends forever after }k>w+1.}
\]

Equivalently, no new Hall deficiency can begin beyond the finite initial
reflection window. A deficiency already present in the prefix persists; the
stable matching does not repair it.

The finite-prefix census over \(2\le g\le15\), \(1\le q\le30\) finds onset
only at

\[
(g,q)=(2,1),\qquad(2,7).
\]

The symbolic stable theorem is unbounded in \(g,q,k\). The assertion that
these are the only prefix defects globally remains a finite census. Hall
support also does not prove actual-weight determinant noncancellation for
\(q>1\); it proves only that support cannot develop a late new deficiency.

