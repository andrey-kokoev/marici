# The phase-twisted Real structure preserves every radial wall fiber

## Question

Must Real conjugation exchange the wall phases \(u\) and \(\bar u\), or is there a canonical fiberwise Real structure compatible with the phase-decorated fold?

## Claim boundary

Coefficientwise conjugation exchanges the \(u\) and \(\bar u\) fibers and fixes one fiber only for \(u=\pm1\). However, every unit phase admits a canonical twisted conjugation

\[
J_u=\operatorname{diag}(1,u^2)K
\]

that is antiunitary, involutive, preserves the wall, commutes with reciprocal exchange, and is transported from ordinary whole-line conjugation by the canonical fold. This corrects the claim that fixed-fiber Real compatibility requires a Real phase.

## Problem

On the radial double, let coefficientwise conjugation be

\[
K_2(f_+,f_-)=(\bar f_+,\bar f_-).
\]

The wall is

\[
\Lambda_u=\{(c,uc):c\in\mathbb C\},
\qquad |u|=1.
\]

Then

\[
K_2\Lambda_u=\Lambda_{\bar u}.
\]

So \(K_2\) preserves \(\Lambda_u\) only when \(u=\bar u\), equivalently \(u=\pm1\).

## Bold conjecture

For non-Real wall phase, no Real structure can act within the fixed radial fiber while preserving reciprocal sewing.

## Named rivals

1. A phase-twisted conjugation preserves every fixed fiber.
2. Such a twist preserves the wall but fails involutivity.
3. It preserves the wall but fails to commute with \(W_u\).
4. It is fitted radial data rather than transport of the whole-line Real structure.

## Twisted Real structure

Let \(K_2\) denote coefficientwise conjugation and define

\[
J_u
=
\begin{pmatrix}
1&0\\
0&u^2
\end{pmatrix}K_2.
\]

Because \(|u|=1\), this map is antiunitary. Moreover,

\[
J_u^2
=
\begin{pmatrix}1&0\\0&u^2\end{pmatrix}
\begin{pmatrix}1&0\\0&\bar u^2\end{pmatrix}
=I.
\]

Thus rival 2 fails.

## Wall preservation

For \((c,uc)\in\Lambda_u\),

\[
J_u(c,uc)
=
(\bar c,u^2\bar u\bar c)
=
(\bar c,u\bar c)
\in\Lambda_u.
\]

Hence

\[
J_u\Lambda_u=\Lambda_u
\]

for every unit phase.

## Reciprocal compatibility

Let

\[
W_u=
\begin{pmatrix}
0&u^{-1}\\
u&0
\end{pmatrix}.
\]

For \((a,b)\), direct computation gives

\[
J_uW_u(a,b)
=(u\bar b,u\bar a)
=W_uJ_u(a,b).
\]

Therefore

\[
J_uW_u=W_uJ_u.
\]

Rival 3 fails.

## Fold transport theorem

Let whole-line conjugation be

\[
(Kq)(t)=\overline{q(t)}
\]

and let

\[
(C_uq)(r)=(q(r),u q(-r)).
\]

Then

\[
J_uC_uq
=(\bar q(r),u\bar q(-r))
=C_uKq.
\]

Thus

\[
J_uC_u=C_uK.
\]

The twisted radial Real structure is not fitted after choosing the wall. It is the unique Real structure obtained by unitary transport:

\[
J_u=C_uKC_u^{-1}.
\]

Rival 4 fails.

## Differential and Green compatibility

The radial differential is

\[
\mathbb D=
\begin{pmatrix}
\partial_r&0\\
0&-\partial_r
\end{pmatrix}.
\]

Its coefficients are real and the phase twist is constant, so

\[
J_u\mathbb D=\mathbb DJ_u
\]

on the transported domain.

For

\[
J_\partial=\operatorname{diag}(-1,1),
\]

the diagonal phase twist preserves the Green form. In antiunitary notation,

\[
\langle J_u x,J_\partial J_u y\rangle
=
\overline{\langle x,J_\partial y\rangle}.
\]

Hence the Real structure is compatible with both the maximal-isotropic wall and Green orientation.

## Reciprocal parity sectors

The eigenspaces

\[
X_+=\{(f,uf)\},
\qquad
X_-=\{(f,-uf)\}
\]

are preserved by \(J_u\):

\[
J_u(f,\pm uf)
=(\bar f,\pm u\bar f).
\]

Therefore the reciprocal parity decomposition is Real within each fixed \(u\)-fiber when the transported Real structure is used.

## Transpose--adjoint square

For a synthesis \(U:V\to H_u^{\rm rad}\) transported from a whole-line Real map, let \(J_V\) be source conjugation and \(J_u\) the target Real structure. Then

\[
J_uU=UJ_V
\]

and the analytic transpose satisfies

\[
U^\top=J_VU^*J_u.
\]

Under Real-compatible metrics,

\[
J_VU^*=U^*J_u,
\]

so

\[
U^\top=U^*.
\]

This equality is now typed fiberwise for every \(|u|=1\), not only \(u=\pm1\).

## Uniqueness under fold transport

If \(J\) is an antiunitary on the radial carrier satisfying

\[
JC_u=C_uK,
\]

then surjectivity of \(C_u\) forces

\[
J=C_uKC_u^{-1}=J_u.
\]

Thus the phase twist is uniquely determined by the declared fold and whole-line conjugation.

## Constructor-role correction

There are two legitimate Real constructors:

- `family_real_transport`: coefficientwise conjugation sends the fiber at \(u\) to the fiber at \(\bar u\);
- `fold_transport_real`: \(J_u=C_uKC_u^{-1}\) acts within the fixed \(u\)-fiber.

They are related by the diagonal gauge \(\operatorname{diag}(1,u^2)\) but are not identical. A contract must state which Real structure defines its transpose and adjoint.

## Strongest falsification attempt

The prior fixed-locus objection is correct for bare coefficientwise conjugation. It does not survive transport through the phase-decorated fold. The explicit formula for \(J_u\) passes involution, wall, reciprocal, differential, Green, and fold-naturality tests.

## Disposition

The bold conjecture is rejected. Every radial wall phase has a canonical fixed-fiber Real structure transported from the whole line. The principal worked example now supports a Real reciprocal decomposition for arbitrary \(u\), while preserving the distinction between family-level conjugation and fiberwise twisted conjugation.
