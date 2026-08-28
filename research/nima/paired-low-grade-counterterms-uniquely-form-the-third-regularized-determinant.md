# Paired low-grade counterterms uniquely form the third regularized determinant

## Counterterms are fixed by the logarithmic grades

For a finite relative transfer \(T\),

\[
\log\det(I-T)
=
-\sum_{k\geq1}\frac1k\operatorname{Tr}(T^k).
\]

The all-prime threshold says that the terms at \(k=1\) and \(k=2\) cannot
belong to the ordinary completed determinant, while the tail beginning at
\(k=3\) can.

Consider a regularization with source-invariant trace counterterms

\[
\det(I-T)
\exp\left(
a_1\operatorname{Tr}T+a_2\operatorname{Tr}(T^2)
\right).
\]

Cancellation of the first two logarithmic grades forces

\[
a_1=1,
\qquad
a_2=\frac12.
\]

Thus the regularized determinant is uniquely

\[
\det_3(I-T)
=
\det(I-T)
\exp\left(
\operatorname{Tr}T+\frac12\operatorname{Tr}(T^2)
\right),
\]

with logarithm

\[
\log\det_3(I-T)
=
-\sum_{k\geq3}\frac1k\operatorname{Tr}(T^k).
\]

The primitive and square terms are not deleted. They are retained as the
boundary counterterm pair that relates the ordinary determinant chart to the
third-regularized chart.

## Reciprocal pairing

At every finite cutoff, reciprocal sewing gives

\[
T^-=T^{+*}.
\]

Therefore

\[
\operatorname{Tr}((T^-)^k)
=
\overline{\operatorname{Tr}((T^+)^k)}.
\]

The uniquely forced primitive and square counterterms are conjugate
automatically, and

\[
\det_3(I-T^-)
=
\overline{\det_3(I-T^+)}.
\]

This supplies the paired low-grade counterterms required by the Real
completion order. No independent sheet normalization remains to be chosen.

## Direct sums and the remaining anomaly

The construction is additive in logarithms under direct sum:

\[
\det_3(I-(T\oplus S))
=
\det_3(I-T)\det_3(I-S).
\]

This is enough for finite prime blocks and their restricted direct sum.

It does not make \(\det_3\) strictly multiplicative under arbitrary operator
products. Product composition may carry a regularized determinant anomaly.
That anomaly must be computed and retained as a higher comparison cell rather
than assumed absent.

## DPC verdict

Resolved:

- unique source-independent cancellation coefficients for the first two
  cyclic grades;
- reciprocal conjugacy of the paired counterterms;
- ordinary completion of the grade-three tail;
- direct-sum compatibility across prime blocks.

Withheld:

- the product-composition anomaly of the regularized determinant;
- proof that the completed prime blocks form the actual global theta–Euler
  comparison;
- the archimedean factor;
- the zero-state-to-flux bridge.

The smallest falsifier is any alternative coefficient pair. If
\(a_1\neq1\) or \(a_2\neq1/2\), a forbidden primitive or square grade
remains in the determinant tail.

## Verification

The checker `check_paired_det3_counterterms.py` verifies uniqueness of both
coefficients, conjugate pairing, direct-sum additivity, and hostile residuals
from incorrect counterterms.
