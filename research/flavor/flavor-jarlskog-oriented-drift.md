# Jarlskog-oriented drift (WP280)

## Intrinsic orientation candidate

`physical16` contains signed Jarlskog \(J\), which is invariant under weak-basis
changes and odd under orientation or CP reversal. Use it to orient WP278's
drift:

\[
A(J)=J\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Under reflection, both \(J\) and the orientation generator change sign, so
their product is covariant. This repairs WP279's descent defect without an
external orientation port at the algebraic level.

## Generic closure and singular locus

With the same one-port sensor and actuator, the time towers are

\[
\begin{pmatrix}C\\CA(J)\end{pmatrix}
=\begin{pmatrix}1&0\\0&J\end{pmatrix},
\qquad
\begin{pmatrix}B&A(J)B\end{pmatrix}
=\begin{pmatrix}1&0\\0&-J\end{pmatrix}.
\]

Their determinants are \(J\) and \(-J\), and both Gram determinants are
\(J^2\). Dynamic observability and reachability therefore hold generically for
\(J\neq0\), while the CP-conserving locus \(J=0\) reopens both rank-one kernels.
The physical conditioning margin scales with \(|J|\).

## Source-authority boundary

Signed \(J\) is available as a quotient readout. That does not mean it
physically drives Yukawa evolution. Declaring \(A(J)\) is a self-reading law
unless a CP-odd dynamical field or source coupling produces both the orientation
and clock normalization. Different nonzero values of \(J\) give different
drift speeds while satisfying the same covariance rule.

Thus WP280 repairs descent and establishes generic formal closure, but not a
source-generated selector or instrument. The next constructor must derive the
CP-odd dynamical substrate and its coupling before flavor readout.

Run `uv run --with sympy python
research/flavor/checkers/wp280_jarlskog_oriented_drift.py` for the exact
reflection covariance, towers, Gram determinants, CP-conserving kernel, and
hostile speed pair.
