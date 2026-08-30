# Rigid reciprocal sewing cannot make the two-by-two return determinant equal Xi

## Inputs now fixed

The reciprocal theta return in wall--jump coordinates is

\[
G(z)
=
\begin{pmatrix}
a(z)&b(z)\\
b(z)&a(z)
\end{pmatrix},
\]

with

\[
a=\frac{m_++m_-}{2},
\qquad
b=\frac{m_+-m_-}{2},
\qquad
a^2-b^2=m_+m_-.
\]

The completed scalar shadow is proportional to

\[
\Xi=2a.
\]

Independently, joint chain and Krein compatibility restricts the intrinsic sewing map to one of two phase families.

## Orientation-preserving sewing

The rigid preserving sewing is

\[
C=cI,
\qquad
|c|=1.
\]

Then

\[
\det(I-CG)
=
\det
\begin{pmatrix}
1-ca&-cb\\
-cb&1-ca
\end{pmatrix}
\]

and hence

\[
\det(I-cG)
=
(1-cm_+)(1-cm_-)
=
1-2ca+c^2m_+m_-.
\]

This determinant is quadratic in the reciprocal sheet returns. It is not proportional to \(2a\).

At a completed scalar zero \(a=0\),

\[
\det(I-cG)
=
1+c^2m_+m_-.
\]

There is no source identity forcing this expression to vanish.

## Orientation-reversing sewing

In the wall--jump frame, rigid reversing sewing is

\[
C=cR,
\qquad
R=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Then

\[
\det(I-cRG)
=
1-c^2m_+m_-.
\]

The linear even return \(a\) disappears entirely.

At \(a=0\), one has \(m_+m_-=-b^2\), so

\[
\det(I-cRG)
=
1+c^2b^2,
\]

which again is not forced to vanish.

## Exact no-go

Neither chain-compatible sewing class yields

\[
\det(I-CG)
=
u(z)\Xi(z)
\]

with a source-declared nowhere-zero unit \(u\) by formal covariance alone.

More sharply, scalar zeros of \(\Xi\) do not generically produce eigenvalue-one collisions of \(CG\) for either rigid sewing.

Therefore the previously proposed identification

\[
\Xi(z)=0
\quad\Longleftrightarrow\quad
\det(I-CG)=0
\]

is false for the intrinsic two-dimensional chain-compatible sewing map.

## Why this is not a normalization defect

The obstruction survives every unit phase \(c\). Changing the Wronskian sign, Hadamard convention, or common phase cannot remove the reciprocal product term.

Nor may one choose a nonunit modulus or add a shear: the chain-plus-Krein classification forbids those modifications.

Thus the discrepancy is structural. It distinguishes:

- boundary identification, which is rigid and metric;
- arithmetic constitutive loading, which would need additional source data;
- scalar completed readout, which is linear in \(a\);
- a Fredholm determinant, which is multiplicative and quadratic at rank two.

These objects cannot be identified merely because they use the same wall--jump carrier.

## Legitimate repairs

There are four possible architectures.

### 1. Matrix coefficient

Use the even matrix coefficient

\[
\langle w,Gw\rangle=a
\]

as the completed scalar section. This reproduces \(\Xi/2\) exactly but is not a spectral determinant and does not turn a scalar zero into an operator kernel.

A separate closed-state bridge remains necessary.

### 2. Bordered determinant

Introduce a source-authorized unit or constraint row and form a bordered determinant whose Schur complement is the even coefficient \(a\). The extra row must be derived before scalar comparison.

### 3. Different arithmetic relation

Construct a constitutive pencil

\[
\Theta(z)-G(z)
\]

whose determinant is linear in \(a\) because \(\Theta\) has a source-derived singular or graded structure. This \(\Theta\) is not the intrinsic chain sewing \(C\).

### 4. Larger typed boundary complex

Retain additional endpoint, archimedean, or determinant-line coordinates. A graded torsion or top exterior readout may then reduce to \(2a\) after authorized cancellation.

The larger complex must explain, rather than fit, why the reciprocal product term cancels.

## Bordered minimality condition

Any proposed repair must pass a minimality audit. Adding an auxiliary row that algebraically linearizes the determinant is not sufficient: the added coordinate must be controllable, observable, and source-typed.

Otherwise stabilization can manufacture the target determinant without changing the underlying return.

## Consequence for the five-margin programme

The one-sided propagation and local Adams edge remain valid. What fails is only the last proposed spectral identification.

Five-margin coercivity of a faithful Green packet cannot repair this algebraic mismatch. Coercivity says that the packet has no invisible state; it does not turn its even matrix coefficient into the determinant of the rigid sewing loop.

## New exact frontier

The next source audit must choose among the four architectures by reading the actual completed determinant constructor:

1. Is \(\Xi\) declared only as the even matrix coefficient?
2. Does the source supply a bordered unit/constraint cell?
3. Is there an arithmetic boundary relation distinct from reciprocal chain sewing?
4. Does the adelic or archimedean attachment enlarge the boundary complex?

Until one of these is constructed, the finite-rank sewing theorem remains a valid abstract identity but does not identify its determinant with \(\Xi\).

## Minimal hostile

Take any nonzero outer pair with

\[
m_-=-m_+.
\]

Then \(a=0\), so the completed scalar section vanishes. But the two rigid determinants are

\[
1-c^2m_+^2
\]

and

\[
1+c^2m_+^2
\]

up to the orientation convention. For generic \(m_+\), both are nonzero.

This is the smallest exact witness that reciprocal scalar cancellation is not yet a boundary eigenvalue collision.
