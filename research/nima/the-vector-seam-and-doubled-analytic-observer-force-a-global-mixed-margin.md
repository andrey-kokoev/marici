# The vector seam and doubled analytic observer force a global mixed margin

## Assembled reduced coordinates

Let \(x\) be the arithmetic/front coordinate and \(y\) the analytic cut/history
coordinate.  The full labelled seam comparison is a bounded isomorphism

\[
Jx\in\mathcal H_I^G,
\qquad
\|Jx\|\ge m_J\|x\|,
\qquad
m_J>0.
\]

Let the doubled analytic observer satisfy

\[
\|\mathcal Ay\|^2\ge c_A\|y\|^2,
\qquad
c_A>0.
\]

The reduced assembled G3 energy contains at least

\[
E_0(x,y)
=
\|\mathcal Ay\|^2+\|Jx-y\|^2.
\]

Arithmetic Pauli energy, endpoint walls, and other positive retained outputs
may be added afterward and cannot weaken the estimate below.

## Direct coercivity

Set

\[
d=Jx-y.
\]

Then

\[
\|x\|
\le m_J^{-1}\|Jx\|
\le m_J^{-1}(\|d\|+\|y\|).
\]

Hence

\[
\|x\|^2
\le\frac2{m_J^2}(\|d\|^2+\|y\|^2),
\]

and therefore

\[
\|x\|^2+\|y\|^2
\le
C_J
\left(\|d\|^2+c_A\|y\|^2\right),
\]

where

\[
C_J
=
\max\left\{
\frac2{m_J^2},
\frac{1+2/m_J^2}{c_A}
\right\}.
\]

It follows that

\[
E_0(x,y)
\ge g_0(\|x\|^2+\|y\|^2),
\qquad
g_0=C_J^{-1}>0.
\]

This estimate includes every connected grade because \(J\) is bi-bounded on
the full labelled front-cut sum.  It does not use arithmetic coercivity on the
nuclear tail.

## Coherent/disagreement block

Decompose the reduced joint space orthogonally as

\[
H_{\rm joint}=H_{\rm coh}\oplus H_{\rm dis},
\]

where \(H_{\rm coh}=\ker D\) for \(D(x,y)=Jx-y\).  Let the complete Green Gram
be

\[
B=
\begin{pmatrix}
B_{cc}&B_{cd}\\
B_{dc}&B_{dd}
\end{pmatrix}.
\]

The direct estimate gives

\[
B\ge g_0I.
\]

Let

\[
M_B=\max\{\|B_{cc}\|,\|B_{dd}\|\}<\infty
\]

in the declared graph normalization.  The diagonal blocks are already bounded
and coercive by the coherent and disagreement margins.

Normalize the mixed block:

\[
K=B_{cc}^{-1/2}B_{cd}B_{dd}^{-1/2}.
\]

Congruence gives

\[
\begin{pmatrix}I&K\\K^*&I\end{pmatrix}
=
\operatorname{diag}(B_{cc}^{-1/2},B_{dd}^{-1/2})
B
\operatorname{diag}(B_{cc}^{-1/2},B_{dd}^{-1/2}).
\]

Since \(B\ge g_0I\) and both diagonal block norms are at most \(M_B\),

\[
\begin{pmatrix}I&K\\K^*&I\end{pmatrix}
\ge\frac{g_0}{M_B}I.
\]

The least spectral value of this normalized two-block operator is
\(1-\|K\|\).  Therefore

\[
\|K\|
\le1-\frac{g_0}{M_B}<1.
\]

## Mixed margin

The normalized global mixed margin may be chosen as

\[
\delta_{\rm mix}
=\frac{g_0}{M_B}>0.
\]

The estimate is cutoff uniform because \(m_J\), \(c_A\), and the graph-block
upper bounds are uniform on the labelled completion.  Prime diagonality
prevents coherent accumulation across prime fibres.

## Why scalarization breaks the proof

If \(J\) is replaced by its scalar Wronskian projection, \(m_J=0\).  Then
\(C_J\) diverges, \(g_0=0\), and no strict mixed margin follows.  The full
vector seam is therefore essential for both glue and mixed control.

## G3 consequence

The vector seam plus doubled analytic observer directly coerce the complete
reduced pair \((x,y)\).  This closes the normalized mixed-coupling gate on the
full labelled boundary-front architecture.  Adding the retained arithmetic
Pauli observer strengthens the low-grade block but is not needed for the
connected-grade estimate.

Together with the previously established arithmetic, analytic, glue, and
coherent-diagonal bounds, all five G3 margins are closure candidates before
terminal scalarization.  Any additional analytic summand outside the declared
closed history/cut graph requires a separate audit.  No RH conclusion is
authorized.
