# Full parity-even degree-four quantum Gram relaxation remains unbounded

Use the quadratic operator basis

\[
(1,A,B,C)=(1,Q^2,S,P^2),
\qquad
S=\frac{QP+PQ}{2},
\qquad [Q,P]=2i.
\]

Freeze the covariance and one fourth moment:

\[
\langle Q^2\rangle=1,
\qquad
\langle S\rangle=0,
\qquad
\langle P^2\rangle=2,
\qquad
\langle Q^4\rangle=2.
\]

For arbitrary real \(Z=\operatorname{Re}\langle Q^2S\rangle\), set

\[
\langle S^2\rangle=Z^2+5,
\qquad
\langle P^4\rangle=4Z^2+9,
\]

and choose the remaining real cross entries

\[
\operatorname{Re}\langle Q^2P^2\rangle=0,
\qquad
\operatorname{Re}\langle SP^2\rangle=0.
\]

The canonical commutators force

\[
\operatorname{Im}\langle Q^2S\rangle=2,
\quad
\operatorname{Im}\langle Q^2P^2\rangle=0,
\quad
\operatorname{Im}\langle SP^2\rangle=4.
\]

The leading \((1,Q^2,S)\) determinant is exactly one.  Its Schur cost for the
\(P^2\) column is \(4Z^2+8\), so the full Schur complement is also exactly one.
Therefore the complete parity-even degree-four Gram matrix is positive
definite for every \(Z\).

The decoupled odd block \((Q,P)\) is positive as well, since its fixed
covariance obeys \(1\cdot2-0^2\geq1\).  Hence the same construction extends to
the full basis \((1,Q,P,Q^2,S,P^2)\) under the parity-even specialization.

This is a truncated noncommutative-moment relaxation, not yet a proof that
every member extends to a density operator.  It proves that degree-four Gram
positivity and the canonical commutators alone cannot bound the mixed
fourth-cumulant direction; extension/localizing constraints from higher degree
are indispensable.
