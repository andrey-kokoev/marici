# The magnetic chart divisor is a primitive row cocircuit

At every tested member of the chart-boundary family

\[
(g,q,k)=(2r,4r+8,r+4),
\]

the two preferred observation rows obey the exact vector relation

\[
(2g+7)R_1=(3g+7)R_0.
\]

The preferred maximal minor therefore vanishes because its observation packet
contains a rank-one cocircuit: two rows have become redundant. Its primitive
integer representative is

\[
\frac{1}{\gcd(g,7)}\bigl(2g+7,-(3g+7)\bigr).
\]

The content is \(7\) precisely when \(14\mid g\); otherwise the displayed
relation was already primitive. This is not a
column circuit and hence does not exhibit a kernel state. Replacing \(R_1\)
by \(R_3\) crosses to a transverse chart; at the preregistered \(r=8\) target
its determinant is nonzero and proves rank 26.

Categorically, the divisor \(q-2g-8=0\) marks failure of one jointly faithful
presentation of the invariant subspace. The invariant object does not change.
This explains why the closure-capability category placed the event in the
presentation coordinate rather than the observation coordinate.

The relation follows symbolically for every even \(g\). At the divisor, only
two columns meet rows 0 and 1. The \(a=0\) minus column contributes
\(-(4)^{\overline g}(2g+7,3g+7)\), while the \(a=g+8\) plus column contributes
\(-(g+8)^{\overline{g-1}}(2g+7,3g+7)\). All other columns vanish on those
rows by support. This proves the unbounded primary-chart zero. What remains
The row-exchanged minor is now proved nonzero at every admissible even grade.

The prior triangular-core theorem reduces that open half to fixed size. After
removing the two endpoint columns and the two boundary rows, the remaining
\((g+8)\)-dimensional matrix is upper triangular with explicit nonzero
diagonal. Hence the full alternate determinant is
\(\det(A_g)\det(S_g)\), where \(S_g\) is the \(2\times2\) boundary Schur
complement. Endpoint support fixes its first column, while the row-\(3\)
response touches only the plus column \(a=g+6\). The transverse pivot is

\[
-\frac{8(2g+3)(g^2-g-26)(2g+1)!}
{3(g+5)(g+6)(g+7)(g-1)!},
\]

which is nonzero at integral \(g\) because \(g^2-g-26\) has nonsquare
discriminant \(105\). Thus the alternate chart is full rank for every
admissible even grade. Since its shared \(n-1\) rows are independent, while
the preferred extra row is proportional to row \(0\), the preferred chart has
rank exactly \(n-1\): its failure is one-dimensional and purely presentational.
