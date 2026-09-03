# The mixed Schur determinant is a quotient angle

## Question

What source condition is exactly equivalent to positivity of the effective two-coordinate determinant after auxiliary elimination?

## Shorted vectors

Let \(H\) be the completed Green Hilbert space after declared radicals, let \(N\subset H\) be the closed auxiliary history subspace, and let \(P_N\) be its orthogonal projector. For source endpoint lifts \(e_1,e_2\), define

\[
u=(I-P_N)e_1,
\qquad
v=(I-P_N)e_2.
\]

The Schur-shortened endpoint Gram is

\[
A^{\rm eff}
=
\begin{pmatrix}
\lVert u\rVert^2&\langle u,v\rangle\\
\langle v,u\rangle&\lVert v\rVert^2
\end{pmatrix}.
\]

Thus

\[
\det A^{\rm eff}
=
\lVert u\rVert^2\lVert v\rVert^2-|\langle u,v\rangle|^2
=
\lVert u\wedge v\rVert^2.
\]

## Exact qualitative criterion

The determinant is strictly positive exactly when the quotient classes

\[
[e_1],[e_2]\in H/N
\]

are linearly independent. Equivalently,

\[
\operatorname{span}\{e_1,e_2\}\cap N=\{0\}.
\]

This is the two-coordinate no-dark-endpoint condition. It is stronger than positivity of each diagonal, which only says \([e_1]\ne0\) and \([e_2]\ne0\) separately.

## Uniform criterion

Write

\[
\rho_p=
\frac{\langle u_p,v_p\rangle}
{\lVert u_p\rVert\lVert v_p\rVert}.
\]

Given lower diagonal margins \(\alpha_p\ge m_1>0\) and \(\beta_p\ge m_2>0\), a prime-uniform determinant bound follows from

\[
\sup_p|\rho_p|\le1-\varepsilon
\]

for some \(\varepsilon>0\). Then

\[
\det A_p^{\rm eff}
\ge m_1m_2\bigl(2\varepsilon-\varepsilon^2\bigr).
\]

The required datum is therefore a quotient angle, not another scalar mass estimate.

## Hostile cases

1. Each endpoint class is nonzero, but \([e_1]=[e_2]\); both diagonals survive and the determinant vanishes.
2. Every finite prime has independent quotient classes, but \(|\rho_p|\to1\); pointwise determinants are positive without a prime-uniform margin.
3. Parity labels differ algebraically, but the complete Green form does not carry the declared reflection unitarily; parity does not force \(\rho_p=0\).

## Claim boundary

The exterior-square identity and quotient criterion are exact. No current source artifact proves the required completed quotient injectivity or uniform angle. The previously requested full Gram table would evaluate the criterion, but a direct source proof of quotient injectivity plus angle separation is an alternative constructor.

## Disposition

Retype the mixed-coherence gate as a two-dimensional no-dark-endpoint theorem for the quotient map

\[
\operatorname{span}\{e_1,e_2\}\longrightarrow H/N.
\]

The next executable test is to type this quotient map on the retained completed carrier and seek either a source left inverse or an explicit dark linear combination.
