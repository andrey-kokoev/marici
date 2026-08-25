# The commuting parity-to-cohomology diagram

Fix `g>=2`, a finite admitted even-depth constructor, a finite source Laurent
window, and the full target.  All vector-space statements below are over `Q`;
the final row records the integral lattice refinement.

## Transport and parity layer

Let

\[
J_g:S\longrightarrow\mathcal P,
\qquad D\longmapsto(A_D,B_D)
\]

be mixed-derivative sheet transport.  The one-sheet theorem gives

\[
\ker J_g=0.
\]

The character transform

\[
\mathcal F_{\mathbb Z_2}:
(A,B)\longmapsto(E=A+B,M=A-B)
\]

is invertible.  Hence the joint observer

\[
O_g=(E_g,M_g)=\mathcal F_{\mathbb Z_2}J_g
\]

is injective and

\[
\ker E_g\cap\ker M_g=0.
\]

This gives the two short exact sequences

\[
0\to\ker M_g\to S\xrightarrow{M_g}\operatorname{im}M_g\to0,
\]

\[
0\to\ker E_g\to S\xrightarrow{E_g}\operatorname{im}E_g\to0.
\]

Moreover the complementary restrictions are injective:

\[
E_g|_{\ker M_g}:\ker M_g\hookrightarrow\operatorname{im}E_g,
\]

\[
M_g|_{\ker E_g}:\ker E_g\hookrightarrow\operatorname{im}M_g.
\]

Thus a single parity port aliases states; the complete character observer does
not erase them.

## Closedness and rational cohomology layer

Fold transport gives

\[
F_g:S\to\Omega_K^1,
\qquad
dF_g(D)=-M_g(D)\,dz\wedge d\bar z.
\]

Therefore the square

\[
\begin{array}{ccc}
S&\xrightarrow{F_g}&\Omega_K^1\\
\downarrow M_g&&\downarrow d\\
\operatorname{im}M_g&\xrightarrow{-\,\cdot dz\wedge d\bar z}&
\Omega_K^2
\end{array}
\]

commutes, and `ker M_g` is precisely the inverse image of closed forms.

Restricting to that kernel gives

\[
0\longrightarrow K_g^{rat}
\longrightarrow\ker M_g
\xrightarrow{[F_g]}H_g^{rat}
\longrightarrow0.
\]

The classified basis identifies this quotient map with the global residue
augmentation.  If no positive-depth tower is visible, `H_g^rat=0`.  Otherwise

\[
H_g^{rat}=\mathbb Q[\eta],
\qquad
\eta=d\log\frac{u}{1+u},
\]

and

\[
[F_g(D_{g,a})]=r_{g,a}[\eta].
\]

The depth-zero tower and both grade-two exceptional circuits lie in
`K_g^rat`.  Relative positive-depth combinations lie there exactly when their
weighted residue sum vanishes.

## Integral refinement

Let `K_{g,Z}^M=ker(M_{g,Z})`.  Intersect rational exactness with this source
lattice:

\[
K_{g,\mathbb Z}^{rat}
=K_{g,\mathbb Z}^M\cap K_g^{rat}.
\]

For nonempty visible positive-depth set `T`, the integral row is

\[
0\longrightarrow K_{g,\mathbb Z}^{rat}
\longrightarrow K_{g,\mathbb Z}^M
\xrightarrow{\rho_g}d_{g,T}\mathbb Z\eta
\longrightarrow0,
\]

where

\[
d_{g,T}=\gcd_{a\in T}|r_{g,a}|.
\]

The quotient lattice is free of rank one.  Torsion appears only in the ambient
accessibility comparison

\[
\operatorname{coker}
(d_{g,T}\mathbb Z\eta\hookrightarrow\mathbb Z\eta)
=\mathbb Z/d_{g,T}\mathbb Z.
\]

## Failure taxonomy by first nonfaithful arrow

\[
\begin{array}{c|c|c}
\text{event}&\text{first arrow}&\text{status}\\
\hline
\text{transport loss}&J_g&\text{excluded}\\
\text{single-port alias}&E_g\text{ or }M_g&\text{towers/circuits}\\
\text{chart failure}&\text{chosen maximal minor}&\text{presentation only}\\
\text{rational contraction}&\ker M_g\to H_g^{rat}&\text{intentional quotient}\\
\text{integral inaccessibility}&d\mathbb Z\eta\hookrightarrow\mathbb Z\eta&
\text{ambient cokernel}\\
\text{physical loss}&\text{physical source/readout map}&\text{not typed}
\end{array}
\]

A local magnetic circuit is not automatically a homology class: that would
require an independently derived preceding repair map.  The present de Rham
class is instead defined by the folded rational one-form and its divisor
residue.
