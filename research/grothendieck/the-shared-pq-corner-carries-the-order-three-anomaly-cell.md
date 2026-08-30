# The Shared pq Corner Carries the Order-Three Anomaly Cell

## Joint depth-one colligation

For two distinct primes, the source valuation module is a tensor grid, not an
orthogonal direct sum. At depth one it has states

\[
e_{00},\quad e_{10},\quad e_{01},\quad e_{11}.
\]

The two prime shifts commute and meet at the shared state \(e_{11}\). If their
transfer parameters are \(a\) and \(b\), the joint transfer is

\[
(1+a)(1+b)=1+c,
\qquad
c=a+b+ab.
\]

The mixed term \(ab\) is the readout of the shared \(pq\) corner.

## Order-three anomaly

For a scalar increment \(x\), use the order-three regularized factor

\[
D_3(x)=(1+x)e^{-x+x^2/2}.
\]

Direct joint regularization and staged regularization differ by

\[
\log D_3(c)-\log D_3(a)-\log D_3(b)
=ab\left(a+b+\frac{ab}{2}\right).
\]

Thus the order-three determinant is not multiplicative even though the prime
actions commute.

## Source-derived boundary cancellation

The explicit primitive–square boundary factor is

\[
E(x)=e^{x-x^2/2}.
\]

Its direct-versus-staged discrepancy is

\[
\log E(c)-\log E(a)-\log E(b)
=-ab\left(a+b+\frac{ab}{2}\right).
\]

Therefore the product \(E(x)D_3(x)=1+x\) is exactly multiplicative on the
joint source incidence:

\[
E(c)D_3(c)
=E(a)D_3(a)E(b)D_3(b).
\]

The mixed boundary cell is not fitted. It is forced by applying the already
typed primitive and square currents to the source-derived combined increment
\(c=a+b+ab\).

## Falsifier and scope

Deleting the shared \(pq\) state replaces \(c\) by \(a+b\). Then even the
unregularized identity fails:

\[
1+a+b\ne(1+a)(1+b).
\]

This closes the finite two-prime algebraic coherence gate. It does not yet
identify the joint theta Green colligation with the endpoint Evans section,
nor prove completion stability of the global determinant unit.
