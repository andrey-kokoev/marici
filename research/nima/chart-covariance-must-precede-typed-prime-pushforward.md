# Chart covariance must precede typed prime pushforward

## Local covariance law

Let \(E_P,E_Q\) be the primitive and square chart fibers and let the mixed form be represented by

\[
B_{\alpha,p}:E_P\to E_Q.
\]

Under unitary chart changes

\[
x_P\mapsto U_Px_P,
\qquad
x_Q\mapsto U_Qx_Q,
\]

the mixed operator must transform as

\[
B_{\alpha,p}\mapsto U_QB_{\alpha,p}U_P^*.
\]

The diagonal Green blocks transform simultaneously:

\[
G_P\mapsto U_PG_PU_P^*,
\qquad
G_Q\mapsto U_QG_QU_Q^*.
\]

Hence the complete block

\[
M_p=
\begin{pmatrix}
G_P&B_{\alpha,p}^*\\
B_{\alpha,p}&G_Q
\end{pmatrix}
\]

transforms by one block congruence,

\[
M_p\mapsto
\begin{pmatrix}U_P&0\\0&U_Q\end{pmatrix}
M_p
\begin{pmatrix}U_P&0\\0&U_Q\end{pmatrix}^*.
\]

This is the presentation-independent object. The individual matrix entries are not.

## Typed pushforward

A prime pushforward must act on \(M_p\) as a complete typed block. If \(V_{P,p}\) and \(V_{Q,p}\) are the authorized incidence maps into the arithmetic packet, the induced block is schematically

\[
\Pi_p(M_p)=
\begin{pmatrix}
V_{P,p}G_PV_{P,p}^*
&
V_{P,p}B_{\alpha,p}^*V_{Q,p}^*
\\
V_{Q,p}B_{\alpha,p}V_{P,p}^*
&
V_{Q,p}G_QV_{Q,p}^*
\end{pmatrix}.
\]

Variance conventions may reverse the displayed order, but the same incidence maps must transport diagonal and mixed blocks coherently.

The required comparison is

\[
\Pi_p\!\left(\operatorname{Pair}(\mathscr C_p)\right)
\Longrightarrow
\operatorname{Pair}\!\left(\Pi_p\mathscr C_p\right),
\]

where the arrow is equality or a source-authorized comparison cell. Scalar equality does not supply this cell.

## Minimal \(B\) versus \(B^*\) hostile

Take two-dimensional chart fibers and

\[
B=
\begin{pmatrix}
a&\eta\\
0&a
\end{pmatrix},
\qquad
B^*=
\begin{pmatrix}
\bar a&0\\
\bar\eta&\bar a
\end{pmatrix},
\]

with \(a\in\mathbb R\) and \(\eta\ne0\).

Let the scalar Euler observer retain only the first chart diagonal:

\[
\omega(T)=e_1^*Te_1.
\]

Then

\[
\omega(B)=\omega(B^*)=a.
\]

The trace observer also agrees:

\[
\operatorname{tr}B=\operatorname{tr}B^*=2a.
\]

Nevertheless \(B\ne B^*\), and they transport opposite ordered chart incidence. If reciprocal sewing distinguishes the two orientations, then replacing \(B\) by \(B^*\) preserves every declared scalar coefficient while reversing the seam character.

This is the requested hostile.

## Covariant hostile family

A chart change does not remove the defect. Under a common unitary presentation change,

\[
B\mapsto U_QBU_P^*,
\]

while its mate transforms as

\[
B^*\mapsto U_PB^*U_Q^*.
\]

These inhabit opposite variance types. Identifying them after choosing coordinates is not chart-covariant unless a source-authorized duality or reciprocal cell supplies the identification.

Thus the hostile is categorical, not a basis artifact.

## Pushforward failure mode

Suppose prime pushforward is replaced by scalarization:

\[
M_p\mapsto
\bigl(
\omega(G_P),\omega(B),\omega(G_Q)
\bigr).
\]

Then the two blocks built from \(B\) and \(B^*\) become identical. No later operation can reconstruct which chart arrow was used. Reciprocal orientation has been irreversibly erased.

The loss occurs even if:

- both blocks are positive;
- both mixed operators are contractive;
- every Euler coefficient is correct;
- the final determinant agrees.

Therefore pushforward-before-pairing is not merely lossy; it destroys the type needed to state the seam covariance law.

## Exact finite checker

For each prime \(p\), verify:

1. the chart frames \(E_P,E_Q\);
2. the transformations of \(G_P,G_Q,B\);
3. block congruence covariance of \(M_p\);
4. the reciprocal mate and its seam character;
5. the typed pushforward incidence maps;
6. commutation or a declared comparison cell for pairing versus pushforward;
7. preservation of orientation after pushforward;
8. scalar Euler agreement only at the end.

## Remaining source datum

The irreducible missing calculation is now the comparison cell between:

- local relative Green pairing followed by prime pushforward;
- prime pushforward of the two-chart cell followed by induced arithmetic pairing.

Its boundary must retain the primitive-to-square orientation. Once this cell is source-derived, chart presentation ceases to matter and the first Adams graph relation becomes a legitimate pushforward rather than a fitted scalar lift.
