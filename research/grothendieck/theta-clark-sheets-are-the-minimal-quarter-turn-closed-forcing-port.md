# Theta Clark sheets are the minimal quarter-turn-closed forcing port

## Quarter-turn obstruction for one forcing channel

Let

\[
 e=\begin{pmatrix}1\\1\end{pmatrix},
 \qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The undifferentiated doubled tail forcing lies on the line spanned by \(e\).
But

\[
 Je=\begin{pmatrix}-1\\1\end{pmatrix}
\]

is linearly independent of \(e\). Therefore no one-dimensional real source
port can intertwine the quarter-turn. The smallest \(J\)-invariant target
containing the forcing line is the full two-dimensional plane spanned by
\(e\) and \(Je\).

## Clark sheets supply the missing quadrature

Let

\[
 H_a=G+ia\,\partial_zG,
 \qquad
 H_{-a}=G-ia\,\partial_zG.
\]

After adjoining the common source term \(f\), the two Clark sheets form

\[
 \begin{pmatrix}
 H_a+f\\
 H_{-a}+f
 \end{pmatrix}
 =
 (G+f)e-ia\,\partial_zG\,Je.
\]

Thus the symmetric Clark component occupies the original forcing direction
\(e\), while the sheet-odd derivative component occupies exactly its
quarter-turn \(Je\). No phase or extra source cell has been fitted.

Define the full incidence

\[
 B_J(u,v)=ue+vJe.
\]

Then

\[
 JB_J(u,v)=B_J(-v,u).
\]

The source port carries the same complex structure

\[
 j(u,v)=(-v,u),
\]

and the incidence intertwines it exactly:

\[
 JB_J=B_Jj.
\]

## Positive bulk as the incidence norm

The two columns are orthogonal and have squared norm two:

\[
 \langle e,Je\rangle=0,
 \qquad
 \|e\|^2=\|Je\|^2=2.
\]

Therefore

\[
 \|B_J(u,v)\|^2=2|u|^2+2|v|^2.
\]

For the Clark amplitudes

\[
 u=G+f,
 \qquad
 v=-ia\,\partial_zG,
\]

this becomes

\[
 \left|H_a+f\right|^2+\left|H_{-a}+f\right|^2
 =
 2|G+f|^2+2a^2|\partial_zG|^2.
\]

The native positive Gram bulk is therefore the ordinary norm of the minimal
quarter-turn-closed forcing incidence.

## Meaning

This identifies the algebraic role of Clark doubling:

- one sheet retains the common theta forcing;
- the sheet involution generates its missing spin-two quadrature;
- together they form the smallest source module compatible with Nima's
  cofactor quarter-turn; and
- positivity follows from orthogonality of the two incidence columns.

The construction closes the incidence representation, not the complete
Green conservation law. Packet 199 still requires the infinite shift state
to control propagation of the boundary residual through \(q\).

## Falsifier

The interpretation fails if the fully normalized Clark sheets have unequal
coefficients, an additional forcing component outside
\(\operatorname{span}\{e,Je\}\), or a source frame in which the sheet
involution does not act by \(v\mapsto-v\).

## Scope

This proves quarter-turn covariance and positive norm factorization of the
Clark forcing port. It does not establish endpoint flux cancellation,
completion stability, or RH.
