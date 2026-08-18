# 20260818-855 The Oriented Wall Quotient Connection Is Explicit and Flat

## Construction

Entry 854 derives the \(W_1\) connection.  Apply the same source-normalized Laurent reduction to

\[
W_2:\qquad L_2=a+\frac{v-u}{2}-1=0
\]

with fiber coordinate \(b\) and oriented residue basis

\[
t_2=\frac{db}{L_1\sqrt{K|_{W_2}}},
\qquad
g_2=\frac{db}{\sqrt{K|_{W_2}}}.
\]

The two independently computed top coefficients agree exactly:

\[
\alpha^{(1)}_u=\alpha^{(2)}_u
=-\frac{2(u-1)}{u(u-2)},
\qquad
\alpha^{(1)}_v=\alpha^{(2)}_v
=-\frac1{v-2}.
\]

Therefore the same-sheet top relation

\[
t_1+t_2=0
\]

is horizontal.

## Rank-three quotient

Use the source-normalized quotient basis

\[
(q_0,q_1,q_2)
\]

induced by

\[
(\Omega_{111},\Omega_{101},\Omega_{110}).
\]

The Poincaré-residue signs are

\[
q_0\mapsto(-t_1,+t_2),
\qquad
q_1\mapsto-g_1,
\qquad
q_2\mapsto+g_2.
\]

Both base connections are therefore

\[
\boxed{
A_{3,\mu}=
\begin{pmatrix}
\alpha_\mu&0&0\\
\beta_{1,\mu}&\gamma_{1,\mu}&0\\
\beta_{2,\mu}&0&\gamma_{2,\mu}
\end{pmatrix}.
}
\]

All ten characteristic-zero coefficient functions are exported in the durable packet.  They are obtained from the two wall reductions, not from the finite-field reconstruction table of Entry 853.

## Flatness

The checker verifies the three diagonal curvature identities

\[
\partial_u a_v-\partial_v a_u=0
\]

and both extension identities

\[
\partial_u\beta_{i,v}-\partial_v\beta_{i,u}
+\beta_{i,u}\alpha_v+\gamma_{i,u}\beta_{i,v}
-\beta_{i,v}\alpha_u-\gamma_{i,v}\beta_{i,u}=0.
\]

Hence

\[
\boxed{
\partial_uA_{3,v}-\partial_vA_{3,u}
+[A_{3,u},A_{3,v}]=0.
}
\]

## Consequence

The wall quotient connection required by Entry 852 is now source-derived, explicit, and flat.  The rank-twelve problem is reduced to deriving

\[
B_u,B_v\in\operatorname{Mat}_{9\times3}
\]

with the frozen \(A_9\) and the \(A_3\) above.  No diagonal block, upper-right block, or wall-basis adjustment remains admissible.

This does not yet establish the extension blocks, their triangular-gauge class, infinity-Gysin compatibility, or intrinsic \(\mathcal Q\)-support.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/marked_wall_laurent_reduction.rs`
- `research/benincasa/marked-wall-quotient-connection.json`
- Epistemic event `ev-000000000470-b3be6f01-9bca-463f-8ad2-5f2e7a8e75f3`
