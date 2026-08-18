# 20260818-851 The Source Forms Fix the Marked Localization Boundary Matrices

## Question

Before choosing any primitive exact lift for the rank-twelve marked system, which maps in

\[
0\longrightarrow \mathcal M_q^{(9)}
\xrightarrow{j^*}
\mathcal M_{\rm mark}^{(12)}
\xrightarrow{\operatorname{Res}_W}
H^1(W)(-1)
\longrightarrow0
\]

are already fixed by the source forms and Poincaré-residue orientation?

## Frozen bases

Use the ordered marked basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9)
\]

and the source basis \((e_1,\ldots,e_9)\).  The open restriction is therefore

\[
j^*=\begin{pmatrix}0_{3\times9}\\ I_9\end{pmatrix}.
\]

No exact-lift convention enters this matrix.

## Oriented wall residues

With fiber orientation \(da\wedge db\), order each wall basis as its top-intersection class followed by its primitive wall class.  Direct residue gives

\[
\operatorname{Res}_{W_1}(\Omega_{111})=-t_1,
\qquad
\operatorname{Res}_{W_1}(\Omega_{101})=-g_1,
\]

\[
\operatorname{Res}_{W_2}(\Omega_{111})=+t_2,
\qquad
\operatorname{Res}_{W_2}(\Omega_{110})=+g_2,
\]

and all other basis images vanish.  In the stacked wall basis

\[
(t_1,g_1,t_2,g_2)
\]

the same-sheet top differential is

\[
\operatorname{Res}_{\rm top}=\begin{pmatrix}1&0&1&0\end{pmatrix}.
\]

Hence the two iterated residues of \(\Omega_{111}\) cancel:

\[
\operatorname{Res}_{\rm top}
\begin{pmatrix}
\operatorname{Res}_{W_1}\\
\operatorname{Res}_{W_2}
\end{pmatrix}=0.
\]

## Exact boundary complex

The stacked residue matrix has rank three, the top map has rank one, and

\[
\operatorname{im}
\begin{pmatrix}
\operatorname{Res}_{W_1}\\
\operatorname{Res}_{W_2}
\end{pmatrix}
=
\ker(\operatorname{Res}_{\rm top}).
\]

Choosing the three quotient basis vectors induced in order by

\[
(\Omega_{111},\Omega_{101},\Omega_{110})
\]

makes the combined source-normalized residue matrix

\[
\operatorname{Res}_W=\begin{pmatrix}I_3&0_{3\times9}\end{pmatrix}.
\]

Consequently

\[
\operatorname{rank}j^*=9,
\qquad
\operatorname{rank}\operatorname{Res}_W=3,
\qquad
\operatorname{Res}_Wj^*=0,
\]

so the vector-space localization sequence is exact in these source-normalized bases.

## Narrow result

The source forms uniquely fix \(j^*\), both oriented wall-residue matrices, and the same-sheet top differential before any choice among the large exact-reduction nullspaces.  These matrices are therefore mandatory boundary conditions on the rank-twelve Gauss--Manin connection.

This does **not** yet determine \(A_x^{(12)}\) or \(A_y^{(12)}\), prove horizontality, or establish compatibility with \(R_\infty\).  The next finite calculation is a wall-Laurent exact reduction with one common primitive normalization, constrained by the matrices above.  Any candidate connection that violates their horizontality is rejected; no nullspace may be selected by sparsity or by searching for \(\mathcal Q\).

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/marked_relative_source_maps.rs`
- `research/benincasa/marked-relative-source-maps.json`
- Epistemic event `ev-000000000466-72023481-bb63-4210-af05-155f538af8f5`
