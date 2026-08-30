# Full spectral rotation forbids a fixed pointed flag cone

## Status

Exact symmetry no-go theorem. On every distinct ordered label pair, reciprocal
spectral motion rotates the two real quadratures through a full circle. No
nonzero pointed convex cone can be invariant under that full rotation. Hence a
fixed source flag cannot obtain global sign protection from Fourier covariance
alone.

A moving cone can avoid individual chart walls, but then its motion is an
additional constructor. Unless that constructor is derived before inspecting
the scalar divisor, it merely follows the answer.

## Flagged quadrature

Fix two logarithmic positions

\[
q_1<q_2
\]

and write

\[
d=q_2-q_1>0.
\]

After removing the center phase, the relative Fourier character is

\[
e^{itd}.
\]

Its real quadrature vector is

\[
v(t)=
\begin{pmatrix}
\cos(td)\\
\sin(td)
\end{pmatrix}.
\]

Spectral translation by \(h\) acts through

\[
v(t+h)=R(hd)v(t),
\]

where

\[
R(\theta)=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
\]

Because \(t\) ranges over the real line, this orbit contains the full circle.

## Invariant-cone theorem

Let \(C\) be a convex cone in \(\mathbb R^2\) satisfying

\[
R(\theta)C=C
\]

for every \(\theta\in\mathbb R\). If \(C\) contains a nonzero vector \(x\),
then invariance under the half-turn gives

\[
-x=R(\pi)x\in C.
\]

Therefore

\[
C\cap(-C)
\]

contains a nonzero line. The cone is not pointed.

Consequently the only pointed cone invariant under all spectral rotations is

\[
C=\{0\}.
\]

No invariant strict sign sector exists for a nontrivial flagged Fourier
quadrature.

## Direct arithmetic half-turn

For labels \(n<m\), put

\[
d=\log(m/n).
\]

The spectral increment

\[
h=\frac{\pi}{d}
\]

sends

\[
v(t+h)=-v(t).
\]

This is a source-local finite witness. Every fixed label pair admits an exact
spectral displacement reversing its entire oriented quadrature.

The obstruction does not depend on prime weights or completion.

## Why a half-plane does not repair it

Restricting the complex spectral parameter to one open half-plane constrains
its real displacement from the critical seam. It does not bound the spectral
height. The tangential parameter still ranges over all real values, so the
quadrature completes arbitrarily many turns within either open half-plane.

The two-sector architecture supplies the normal displacement and reciprocal
reflection. It does not create a preferred tangential quadrant.

## Moving flags

One can define a time-dependent frame

\[
P(t)=R(-td)
\]

for which

\[
P(t)v(t)=v(0).
\]

This freezes the quadrature and creates a constant positive ray. But \(P(t)\)
contains the full phase being removed. It is a parallelization, not a
consequence of positivity.

For one label pair this parallelization is tautological. For many pairs, a
single frame would have to cancel all rates

\[
\log(m/n),
\]

which are different. A pair-dependent family of frames changes the ordered
readout from one coordinate to a collection of adapted coordinates.

Thus a moving flag is legitimate only if the source independently constructs:

1. one common connection for all admitted labels;
2. its incidence with the endpoint/source flag;
3. its reciprocal transformation law;
4. its primitive, square, seam, and archimedean curvature;
5. its completion stability.

## Categorical form

The Fourier transport functor acts on the full Pluecker object. A fixed cone
would be a subobject preserved by every spectral-translation morphism. The
half-turn morphism forces that subobject to contain both orientations, so it
cannot be an ordered positive subobject.

A moving cone instead belongs to a bundle with connection. Its comparison maps
are new authority-bearing arrows. They cannot be inferred from equality of
unflagged Gram energies.

## Finite falsifier

Choose any \(n<m\), any spectral height \(t\), and

\[
h=\frac{\pi}{\log(m/n)}.
\]

Then \(v(t+h)=-v(t)\). Any claimed nonzero pointed cone containing the full
spectral orbit must contain both vectors. This contradicts pointedness.

## Decisive conclusion

There is no fixed globally preserved acute or positive cone for the ordered
Fourier flag. Tangential spectral motion rotates every local flag through its
negative while remaining inside the same half-plane.

The only surviving orientation mechanism is connection-relative: a
source-derived moving parallelization must compare rotating flags before
projection. But its curvature and holonomy, rather than cone invariance, then
carry all possible RH-strength information. If the connection is merely the
Fourier phase written backward, it adds no information.
