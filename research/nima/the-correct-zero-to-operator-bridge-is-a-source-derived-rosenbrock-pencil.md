# The correct zero-to-operator bridge is a source-derived Rosenbrock pencil

## Resolvent no-go

The exponential source orbit has a genuine semigroup resolvent, but a zero of
one scalar overlap only cancels a matrix coefficient. It need not create a
resolvent pole, generator kernel, or eigenvalue.

Therefore the scalar zero cannot be transported directly into internal
spectral noninvertibility.

## Transmission-zero bridge

For a source system with internal generator \(A\), input incidence \(B\),
output incidence \(C\), and direct boundary channel \(D\), form the
Rosenbrock pencil

\[
\mathcal P(s)=
\begin{pmatrix}
sI-A&-B\\
C&D
\end{pmatrix}.
\]

Its Schur complement is the transfer readout

\[
G(s)=D+C(sI-A)^{-1}B.
\]

A zero of \(G\) can be a rank loss of \(\mathcal P\) while the internal
resolvent remains regular. This is a transmission zero, not a pole.

That is the correct operator meaning of destructive cancellation between
nonzero source channels.

## Minimal model

Take

\[
A=0,
\qquad
B=1,
\qquad
C=-a,
\qquad
D=1.
\]

Then

\[
G(s)=1-\frac a s=\frac{s-a}{s}.
\]

The internal resolvent has its pole at \(s=0\), while the transfer zero is at
\(s=a\). The augmented pencil

\[
\mathcal P(s)=
\begin{pmatrix}
s&-1\\
-a&1
\end{pmatrix}
\]

has determinant \(s-a\) and loses rank exactly at the transfer zero.

The location \(a\) is unrestricted in this abstract realization. Hence
Rosenbrock realization alone does not confine zeros; hostile off-seam
transmission zeros remain possible.

## Source-derived gate

For theta/Tate, the programme must derive before scalar projection:

- the internal tail/seam state;
- source input incidence;
- boundary output incidence;
- direct endpoint and archimedean channel;
- the completed Rosenbrock pencil;
- an Evans or boundary determinant satisfying

\[
\Xi(s)=u(s)\det\mathcal P(s),
\]

where \(u\) is a source-derived nowhere-zero unit.

Defining a diagonal pencil with \(\Xi\) as an entry is circular and
inadmissible.

## Fixed-point reflection

Once the source pencil exists, RH becomes:

> The source-derived Rosenbrock pencil is full rank away from the fixed seam.

Equivalent constructive witnesses include:

- a canonical off-seam inverse;
- a contracting homotopy for its two-term complex;
- a source-positive real lemma;
- a Fitting minor that cannot vanish off seam.

The finite falsifier is one off-seam parameter where the complete source pencil
loses rank.

