# The endpoint two-by-two Paley--Wiener block has exact even/odd Schur data

## Finite-window analytic carrier

Fix `L>0` and use the Fourier--Laplace transform

\[
F(z)=
\int_{-L}^{L}f(x)e^{-izx}dx,
\qquad
f\in L^2([-L,L]).
\]

This realizes the Paley--Wiener space `PW_L`. Evaluation at `z` is represented by

\[
e_z(x)=e^{i\bar z x},
\]

because

\[
F(z)=\langle f,e_z\rangle_{L^2([-L,L])}
\]

for the convention linear in the first variable.

## Completed endpoint pair

The zeta endpoints `s=0,1` correspond to displacement by `plus-or-minus i/2` from the critical line. Their reproducing vectors are

\[
e_+(x)=e^{x/2},
\qquad
e_-(x)=e^{-x/2}.
\]

Their exact Gram matrix is

\[
G_{end}(L)=
\begin{pmatrix}
\langle e_+,e_+\rangle&\langle e_-,e_+\rangle\\
\langle e_+,e_-\rangle&\langle e_-,e_-\rangle
\end{pmatrix}
=
\begin{pmatrix}
2\sinh L&2L\\
2L&2\sinh L
\end{pmatrix}.
\]

Thus the endpoint channel is intrinsically two-dimensional before functional-equation symmetry is imposed.

## Even/odd diagonalization

Let

\[
e_{even}=
\frac{e_++e_-}{\sqrt2}
=
\sqrt2\cosh(x/2),
\]

\[
e_{odd}=
\frac{e_+-e_-}{\sqrt2}
=
\sqrt2\sinh(x/2).
\]

They are orthogonal by parity, with norms

\[
\boxed{
\|e_{even}\|^2
=2(\sinh L+L),
}
\]

\[
\boxed{
\|e_{odd}\|^2
=2(\sinh L-L).
}
\]

Both are positive for `L>0`. The even channel carries the leading endpoint growth; the odd channel is smaller near zero but has the same exponential scale for large `L`.

Therefore a scalar endpoint model is justified only after a parity condition kills one of these channels. Without that condition, the minimal boundary rank is two.

## Exact growth

As `L -> infinity`,

\[
\|e_{even}\|^2
=
e^L+2L+O(e^{-L}),
\]

\[
\|e_{odd}\|^2
=
e^L-2L+O(e^{-L}).
\]

Hence both evaluation norms grow like `e^(L/2)`. Their difference is only

\[
\|e_{even}\|^2-
\|e_{odd}\|^2
=4L.
\]

This linear residual after exponential cancellation is a useful completion invariant: pairing the two endpoint orientations before taking `L -> infinity` removes the common exponential scale but leaves a nontrivial boundary term.

## General bulk--endpoint block

Let `H_bulk,L` be the finite-window gamma--prime carrier. Suppose its positive bulk form is represented by a positive operator

\[
A_L\succeq0.
\]

Let

\[
B_L:\mathbb C^2\to H_{bulk,L}
\]

encode the endpoint--bulk cross pairing, and let `C_L` be the endpoint block fixed by the explicit formula. The completed Hermitian form is

\[
\mathcal G_L=
\begin{pmatrix}
A_L&B_L\\
B_L^*&C_L
\end{pmatrix}.
\]

The operator Schur-complement theorem gives

\[
\boxed{
\mathcal G_L\succeq0
}
\]

if and only if

\[
\operatorname{ran}B_L
\subseteq
\operatorname{ran}A_L^{1/2}
\]

and

\[
\boxed{
C_L
-
B_L^*A_L^\dagger B_L
\succeq0.
}
\]

Equivalently, there exists a contraction

\[
K_L:C_L^{1/2}\mathbb C^2
\longrightarrow
\overline{\operatorname{ran}A_L^{1/2}}
\]

such that

\[
B_L=A_L^{1/2}K_LC_L^{1/2}.
\]

## Source-fixed endpoint normalization

The free endpoint Gram is `G_end(L)`, but the actual completed formula may assign signs or rational coefficients to the two endpoint evaluations. Let `J_end` denote that source-fixed `2x2` coefficient matrix. Then

\[
C_L=G_{end}(L)^{1/2}
J_{end}
G_{end}(L)^{1/2}.
\]

A positive endpoint sector requires `J_end >= 0`; if `J_end` is indefinite, positivity can arise only after the cross term is included and cannot be proved by an ordinary positive Schur complement with `C_L >= 0`.

Thus the first exact source calculation needed is the matrix `J_end` in the same Fourier convention as the bulk supertrace.

## Parity-reduced scalar criterion

If the observer family is even, the odd endpoint coordinate vanishes and the block reduces to one scalar channel. Write

\[
c_L=2(\sinh L+L)j_{even}
\]

and let `b_L in H_bulk,L` represent the cross term. Positivity is equivalent to

\[
b_L\in\operatorname{ran}A_L^{1/2}
\]

and

\[
\boxed{
c_L\ge
\|A_L^{\dagger/2}b_L\|^2.}
\]

This is the exact finite-window contraction inequality analogous to the Connes--Consani rank-one repair.

## Uniform completion condition

Because `c_L` grows exponentially, a useful direct-limit statement must be formulated after the source-prescribed endpoint--bulk cancellation. Separate bounds on `C_L` and `B_L` will diverge.

A valid completion theorem needs a renormalized Schur complement

\[
S_L=C_L-B_L^*A_L^\dagger B_L
\]

with

\[
S_L\succeq0
\]

and a finite or controlled limit as `L -> infinity`. The large `e^L` terms must cancel inside `S_L`, not after independently taking limits.

This exactly parallels the correlated Arb lesson: sectorwise interval or norm bounds lose the decisive cancellation.

## What has been constructed

The endpoint part of the `2x2` tower is now explicit:

\[
\boxed{
G_{end}(L)=
\begin{pmatrix}
2\sinh L&2L\\
2L&2\sinh L
\end{pmatrix},
}
\]

with canonical parity eigenchannels and known growth. No fitted boundary vector is required.

## Remaining source computation

To complete the trial construction, derive from the same explicit-formula convention:

1. the signed coefficient matrix `J_end`;
2. the cross operator `B_L` between endpoint evaluations and the gamma--prime superconnection;
3. the correlated Schur complement `S_L`;
4. a source proof that `S_L >= 0` uniformly in the prime stage and support exhaustion.

The first two are identities; only the fourth is the positivity theorem.
