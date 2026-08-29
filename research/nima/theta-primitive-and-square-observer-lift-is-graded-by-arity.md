# Primitive and square observer lifts are graded by source arity

## Decision

The proposed pair of parallel linear maps from one additive source carrier is ill-typed.

At finite cutoff, let a source packet \(\phi\) determine an operator \(A_\phi\), linearly in \(\phi\). The first two cyclic coordinates are

\[
j_1(\phi)=\operatorname{Tr}(A_\phi),
\qquad
q_2(\phi)=\frac12\operatorname{Tr}(A_\phi^2).
\]

The first is linear. The second obeys

\[
q_2(\phi+\psi)-q_2(\phi)-q_2(\psi)
=
\frac12\operatorname{Tr}(A_\phi A_\psi+A_\psi A_\phi).
\]

Its mixed term is source data, not an error. Therefore \(q_2\) cannot be represented by a linear map on the one-copy additive carrier unless the entire polarized two-copy form vanishes.

## Correct categorical type

The arithmetic observer begins as a graded cyclic construction:

\[
J_1:A\to B_1,
\qquad
\widetilde J_2:\operatorname{Sym}^2 A\to B_2.
\]

The diagonal readout is recovered only after the two-copy map exists:

\[
q_2(\phi)=\frac12\widetilde J_2(\phi\odot\phi).
\]

Primitive, square, and connected-tail coordinates are evaluations of one Euler feedback loop at different cyclic arities. They are not independent ports to append to the additive theta boundary state.

The completed target is also relative rather than scalar. Primitive and square cutoff increments are transition coordinates of a determinant-line system. Fourier naturality must therefore be checked by arity:

\[
J_1F=F_1J_1,
\qquad
\widetilde J_2\operatorname{Sym}^2(F)=F_2\widetilde J_2,
\]

or by a named line-valued comparison cell whose cutoff components satisfy the triangle law. Equality obtained only after choosing a scalar trivialization is insufficient.

## Finite hostile gate

Let \(A=\mathbb Q^2\) and use

\[
q(x_1,x_2)=x_1^2+2x_1x_2+3x_2^2.
\]

No linear functional \(\ell\) can equal \(q\), because \(q(-x)=q(x)\) while \(\ell(-x)=-\ell(x)\), and \(q\) is nonzero.

Polarization gives the unique symmetric bilinear form

\[
B(x,y)=x_1y_1+x_1y_2+x_2y_1+3x_2y_2
\]

with \(q(x)=B(x,x)\). For the quarter-turn

\[
F=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\]

the transported quadratic form is governed by \(F^{T}MF\), equivalently by the two-copy action \(F\otimes F\). Treating the square observer as a one-copy scalar transport loses this conjugation law.

## DPC

A proposed Fourier–Tate observer lift passes this gate only if:

1. its primitive coordinate is a one-copy linear evaluation;
2. its square coordinate is defined on a cyclic or symmetric two-copy source;
3. diagonalization occurs after the two-copy map is constructed;
4. the polarization term is retained;
5. Fourier transport acts at each arity before scalar determinant reconstruction;
6. primitive and square coordinates remain determinant-chart transition data rather than duplicated theta state channels;
7. cutoff transition coordinates satisfy their triangle law.

Immediate falsifiers are:

- additivity claimed for a nonzero quadratic square coordinate;
- absence of the mixed polarization term;
- use of \(F\) where \(\operatorname{Sym}^2(F)\) is required;
- finite Euler cutoff assumed invariant under global Poisson transport;
- scalar naturality manufactured by choosing a cutoff-dependent determinant-line origin.

## Outcome

The first two observer grades do not expose two missing additive theta maps. They expose a missing Fourier action on the cyclic source tower. The next construction target is the source-derived comparison from additive Poisson transport to the completed cyclic Euler object, together with its relative determinant-line coherence.
