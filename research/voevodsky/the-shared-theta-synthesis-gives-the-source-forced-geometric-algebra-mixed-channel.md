# The shared theta synthesis gives the source-forced geometric-algebra mixed channel

## Common source vector

The analytic tail and seam maps are constructed from one theta source:

\[
(Gc)(t)=\int_0^\infty\Phi(t+p)c(p)\,dp,
\]

\[
(Hc)(t)=\int_t^\infty\Phi(p-t)c(p)\,dp.
\]

Package them as the geometric-algebra-valued feature

\[
\boxed{
\Psi(c)=Gc\,e_{tail}+Hc\,e_{seam}.}
\]

Unlike the optional Clifford lift of two unrelated scalar differentials, both
components here have identical source provenance.

## Geometric square

The covariance of the shared feature is

\[
\Psi\Psi^*
=
\begin{pmatrix}
GG^*&GH^*\\
HG^*&HH^*
\end{pmatrix}.
\]

Its diagonal scalar/vector components are the tail and seam energies. Its mixed
geometric components are

\[
\boxed{
K_{sym}=\frac12(GH^*+HG^*),}
\]

\[
\boxed{
K_{or}=\frac1{2i}(GH^*-HG^*).}
\]

The first is the symmetric Green coupling and the second is its oriented
bivector/current channel. These maps are forced by the geometric square of one
source feature; they are not introduced by choosing noncommuting Clifford
labels afterward.

## Operator class

The theta Hankel map satisfies

\[
G\in\mathcal S_2,
\]

while the one-sided seam convolution satisfies

\[
H\in\mathcal B
\]

under \(\Phi\in L^1\). Hence

\[
GH^*,HG^*\in\mathcal S_2.
\]

Therefore both \(K_{sym}\) and \(K_{or}\) are bounded Hilbert--Schmidt mixed
channels. Their two-step return products are trace class.

## Clifford placement

Choose two Clifford directions for tail and seam. Then the off-diagonal matrix
units decompose into symmetric and oriented bivector coordinates. Up to a fixed
change of Clifford frame, the previously proposed \(B_{23}\) slot is occupied
by \(K_{or}\), while its symmetric mate occupies the complementary mixed
coordinate.

This is the correct promotion criterion: the Clifford slot receives a physical
operator only because the shared theta synthesis supplies its coefficient.

## Prime/grade attachment

The projective exponential Kothe incidence maps prime-power coefficients into
translated theta histories continuously and label-diagonally. The connected
\(k\ge3\) return is nuclear. Consequently the algebraic prime/grade source can
be inserted before \(G\) and \(H\), producing finite-packet mixed channels with
exact cutoff naturality.

The remaining global theorem is continuity of the full polarized arity-two
map after this arithmetic attachment, including the gamma and completed
endpoint terms. The local analytic mixed operator itself is constructed.

## Result

\[
\boxed{
	ext{The source-forced mixed geometric-algebra channel is }
GH^*\text{ and its adjoint }HG^*.}
\]

The Clifford commutator supplies a useful coordinate pattern, but shared theta
synthesis supplies the actual operator coefficient and breaks the arbitrariness
of the earlier lift.
