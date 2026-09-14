# The Douglas contraction on rung four is equivalent to the original Gram inequality

## Setup

The Krein--Langer decomposition gives, on an observer subspace `M`,

\[
Q_\Theta(f)=\|A_Sf\|^2-\|A_Bf\|^2.
\]

A proposed source repair is a contraction `C` satisfying

\[
A_B|_M=C A_S|_M,
\qquad \|C\|\le1.
\]

We now determine whether constructing `C` abstractly on a four-dimensional observer space gives any leverage beyond the original positivity problem.

## Coordinate form

Choose a basis `e_1,...,e_4` of `M` and define the two positive Gram matrices

\[
G_S=(\langle A_Se_j,A_Se_i\rangle)_{i,j},
\qquad
G_B=(\langle A_Be_j,A_Be_i\rangle)_{i,j}.
\]

Then

\[
G_\Theta=G_S-G_B.
\]

Douglas factorization gives the exact equivalence

\[
\boxed{
G_S-G_B\succeq0
\iff
\exists C\text{ with }A_B=C A_S,\ \|C\|\le1.
}
\]

There is also a necessary radical condition:

\[
\ker G_S\subseteq\ker G_B.
\]

It is already implied by `G_B <= G_S` and is required for the formula below to be well-defined.

## Canonical finite-dimensional candidate

On `ran A_S`, the only possible comparison map is

\[
C_0(A_Sf)=A_Bf.
\]

It is well-defined exactly when

\[
\ker A_S\subseteq\ker A_B.
\]

Its squared norm is the largest generalized eigenvalue of the pencil `(G_B,G_S)`:

\[
\boxed{
\|C_0\|^2
=
\sup_{c\notin\ker G_S}
\frac{c^*G_Bc}{c^*G_Sc}.
}
\]

Equivalently, on the support of `G_S`,

\[
\|C_0\|^2
=
\lambda_{\max}
\left(G_S^{\dagger/2}G_BG_S^{\dagger/2}ight),
\]

where `dagger` denotes the Moore--Penrose inverse. A contractive extension to the ambient positive feature space exists exactly when this number is at most one.

Thus the canonical formula

\[
C_0=A_BA_S^\dagger
\]

constructs a contraction only after the desired Gram inequality has been established. It cannot establish that inequality by itself.

## Equivalence with rung-four Schwarz positivity

For a four-vector family, Schwarz positivity is positivity of the corresponding Gram matrix or of its Schur complements. But

\[
G_\Theta=G_S-G_B.
\]

Therefore the conditions

\[
G_\Theta\succeq0,
\qquad
G_B\preceq G_S,
\qquad
\|C_0\|\le1
\]

are three coordinate presentations of the same statement.

In particular, defining `C_0` by interpolation on the four source vectors and then declaring it contractive is circular. The contraction norm is the hostile generalized Rayleigh quotient of the original rung-four form.

## What would make a contraction proof non-tautological

A valid construction must produce `C` on a larger source space from independently contractive operations. Examples would include:

1. a composition of source-defined orthogonal projections and isometries;
2. a conditional expectation between positive arithmetic `L^2` spaces;
3. a transfer operator with a proved sub-Markov norm bound;
4. a coisometric boundary map whose defect operator is explicitly the endpoint--gamma completion.

The map must be defined before restricting to the four observer vectors. Its norm bound must follow from the constructor, not from diagonalizing `G_S-G_B`.

No such map is supplied by the Krein--Langer factorization. There `A_B` is defined from the forbidden divisor, while the interpolation map `C_0` is merely the minimal operator encoding the desired inequality.

## A useful strengthened target

Although Douglas factorization alone is tautological, it specifies a stronger source theorem worth seeking. Let `A_src` be a positive feature map formed directly from endpoint--gamma--prime data. Seek contractions `J_S,J_B` such that

\[
A_S=J_SA_{src},
\qquad
A_B=J_BA_{src},
\]

and an independently contractive factorization

\[
J_B=CJ_S.
\]

The common source map is essential: separate positive realizations do not preserve the deterministic cross-sector polarization. If all three arrows are source-defined and `||C||<=1` follows functorially, then

\[
Q_\Theta(f)
=\|J_SA_{src}f\|^2-\|CJ_SA_{src}f\|^2
=\|(I-C^*C)^{1/2}J_SA_{src}f\|^2.
\]

This would be a genuine positive factorization. It is stronger than constructing `C_0` after observing a four-dimensional Gram matrix.

## Disposition

The finite-rung Douglas contraction does not itself advance positivity:

\[
\boxed{
\exists C,\|C\|\le1
\iff
G_B\preceq G_S
\iff
G_\Theta\succeq0.
}
\]

It is an exact normal form for the missing theorem, not its proof. The next acceptable constructor must be a globally defined source contraction assembled from operations whose norm bounds are independently known.
