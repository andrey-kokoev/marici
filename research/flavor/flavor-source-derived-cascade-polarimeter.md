# Source-derived cascade polarimeter: WP674

## Existing route as analyzer

Use one protected frame channel followed by the already declared chiral exit
route:

\[
A\longrightarrow B+n,
\qquad
B\longrightarrow q_R+X.
\]

Under the relevant triplet flip, assign charges

\[
q(A)=0,\quad q(B)=1,\quad q(n)=1,\quad q(q_R)=0,\quad q(X)=1.
\]

Both vertices are even. This extends the protected charge table without adding
a new reference port.

The exact mass witness

\[
(M_A,M_B,m_n,m_X,m_q)=(5,3,1,1,0)
\]

has parent and daughter threshold margins one and two, so both cascade stages
are simultaneously open.

## Ideal angular port

In the massless-daughter, perfect-spin-transfer limit, let
\(u=|y|^2\), \(v=|z|^2\). The normalized distribution of the exit quark in
the reconstructed \(B\) frame is

\[
f(\cos\theta)=\frac12\left[1+\frac{u-v}{u+v}\cos\theta\right].
\]

Its signed first moment gives

\[
3W\langle\cos\theta\rangle=u-v,
\qquad W=u+v.
\]

The two-port determinant is exactly \(-2\). Hence the existing chiral exit
route can realize WP672's ideal analyzer at source level without a reverse
decay.

## Physical boundary

This packet proves a source-derived cascade and an ideal angular statistic. It
does not prove detector realization. Finite daughter masses, spin transport,
the decay and reconstruction of \(X\), jet assignment, acceptance,
backgrounds, resolution, and covariance must be supplied by one actual
analysis and calibrated independently of the target separation.

The cascade conditionally identifies protected vertex magnitudes and their
loop erosion. It does not select their values or a physical16 point.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp674_source_derived_cascade_polarimeter.py

Generated result: results/wp674_source_derived_cascade_polarimeter.json.
