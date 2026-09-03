# Bochner–Douglas–RKHS equivalence gate

## Question

Does a Gram factorization produce a functor, and can transport among positive-kernel descriptions advance the RH argument?

## Claim boundary

The packet types the factorization and verifies a finite atomic detection theorem. It does not prove positivity of the completed arithmetic kernel.

## Kernel factorization

A feature map \(\Phi:X\to H\) factors a kernel through the Hilbert pairing:

\[
X^{\mathrm{op}}\times X
\xrightarrow{\Phi^{\mathrm{op}}\times\Phi}
\overline H\times H
\xrightarrow{\langle-,-\rangle}
\mathbb C.
\]

Thus \(K\) and \(\Phi\) are not endpoints of a functor. Rather,

\[
K=\Phi^\dagger\Phi
\]

is a factorization in the dagger/profunctor sense.

If \(X\) is only a set, \(\Phi\) is only a map. If \(X\) is a category, a functor additionally requires coherent transports \(U_f\) for every arrow, preserving identities and composition. The Gram equation on objects does not supply these transports.

For a translation-invariant kernel, positivity yields a GNS representation \(U\) and cyclic vector \(v\):

\[
\Phi(x)=U_xv,
\qquad
K(x,y)=\langle v,U_{y-x}v\rangle.
\]

Here \(U\), not the bare feature assignment, is the functor from translations to unitaries.

## Equivalent positive faces

With the required continuity and test-class hypotheses, the following describe the same positivity gate:

1. the spectral measure or distribution \(\rho\) is positive;
2. every finite translate Gram packet is positive semidefinite;
3. \(K\) has a Hilbert feature factorization;
4. the comparison form has a Douglas contraction.

Moving around this square transports a proof but does not create one.

## Exact finite atomic detection

For atoms \((0,\pi)\) and translate labels \((0,1)\), the character matrix is

\[
V=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

With weights \((1,-1/2)\), congruence gives

\[
G=V\begin{pmatrix}1&0\\0&-1/2\end{pmatrix}V^*
=
\begin{pmatrix}1/2&3/2\\3/2&1/2\end{pmatrix},
\]

whose eigenvalues are \(2\) and \(-1\). The coefficient vector \((1/2,-1/2)\) isolates the negative atom and has quadratic value \(-1/2\).

Yet every scalar heat value

\[
1-\frac12e^{-\pi^2t}
\]

is positive for \(t>0\). Scalar heat positivity therefore does not imply translate-Gram positivity.

## Enumerable metaobserver

Continuity and closure of finite PSD cones reduce real translate labels to rational dense packets. Rational positive heat scales similarly generate continuous heat identities, while derivative order remains indexed by natural numbers. The metaobserver can therefore be enumerated by tuples

\[
(r,I,k,t,N)
\]

with rational packet and scale data.

Density proves semidefiniteness after continuity is established. It does not provide strict margins, because rational packets can approach collision strata.

## Disposition

A functor exists canonically only after positivity supplies the GNS/RKHS construction, or earlier if an explicit arithmetic representation \(U\) and cyclic vector are constructed. The latter would be proof-producing. Abstract RKHS, Bochner, Gram, and Douglas equivalences merely change coordinates on the same missing positive object.

## Verification

- `research/voevodsky/bochner-douglas-rkhs-equivalence-gate-v1.json`
- `research/voevodsky/checkers/check_bochner_douglas_rkhs_equivalence_gate.py`
- `research/voevodsky/results/bochner_douglas_rkhs_equivalence_gate.json`
