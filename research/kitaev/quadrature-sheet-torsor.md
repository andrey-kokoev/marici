# Complementary quadrature sheets form a represented torsor

## Bounded question

When can a two-sheet \(C_2\)-packet turn two rank-one nonnegative Green forms
into a positive-definite norm, while keeping sheet choice distinct from
linear-amplitude reconstruction?

Put \(x=(A,B)^T\), \(\psi=A+iB\), and

\[
T(x)=x^Tx=|\psi|^2.
\]

For \(c=\cos 2\theta\), \(s=\sin 2\theta\), define

\[
Q_\theta=
\begin{pmatrix}c&s\\s&-c\end{pmatrix},
\qquad
x^TQ_\theta x=\Re(e^{-2i\theta}\psi^2).
\]

Exactly, \(Q_\theta^2=I\) and \(\operatorname{tr}Q_\theta=0\). Thus \(T\)
is the trace component and \(Q_\theta\) is the normalized spin-two component.

## Minimal representation theorem

Let \(R\) represent the nontrivial sheet displacement on the real
quadrature plane. Suppose \(R\) is an orthogonal involution. Then

\[
T(Rx)=T(x)
\]

automatically, while the spin-two component flips exactly when

\[
\boxed{R^TQ_\theta R=-Q_\theta.}
\]

Because \(R^{-1}=R\), this is equivalent to the anticommutation law

\[
RQ_\theta=-Q_\theta R.
\]

One exact representative is

\[
R_\theta=
\begin{pmatrix}-s&c\\c&s\end{pmatrix}.
\]

It is the reflection whose axis bisects the two eigenquadrature axes of
\(Q_\theta\). The central actions \(I\) and \(-I\) preserve rather than flip
the spin-two form, so a bare sign change of \(\psi\) is insufficient.

## Complementarity theorem

At \(|\lambda|=1\), after absorbing its sign into the sheet label, define

\[
E_\pm(x)=x^T(I\pm Q_\theta)x.
\]

Since \(Q_\theta^2=I\),

\[
(I+Q_\theta)(I-Q_\theta)=0,
\qquad
I+Q_\theta+I-Q_\theta=2I.
\]

Each form has eigenvalues \(0,2\), hence rank one and one null quadrature.
Their null lines are complementary, and

\[
\boxed{E_+(x)+E_-(x)=2|\psi|^2.}
\]

Moreover \(R_\theta^T(I+Q_\theta)R_\theta=I-Q_\theta\). The nontrivial
sheet displacement therefore exchanges the two rank-one forms.

This proves positive definiteness of the *retained two-sheet sum*. It does
not prove that a physical or completed construction retains both sheets with
that relative normalization.

## Torsor bit versus amplitude coordinates

The sheet set is a \(C_2\)-torsor. One origin bit decides which complementary
quadrature is called \(+\). The amplitude \(x=(A,B)\), however, has two real
coordinates. A map to one bit or one scalar has rank at most one and cannot
reconstruct it. Thus

\[
\text{sheet framing}\ne\text{linear state tomography}.
\]

This is the same type distinction as in the \(D(S_3)\) Wilson correction,
but no \(D(S_3)\) datum supplies the Fourier--Tate representation.

## Displacement cocycle

Write the displacement of a transport \(C\) as
\(\epsilon(C)\in\mathbf F_2\). Coherent composition requires

\[
\epsilon(D\circ C)=\epsilon(D)+\epsilon(C)\pmod2,
\]

and hence

\[
\rho(D\circ C)=\rho(D)\rho(C),
\qquad
\chi(D\circ C)=\chi(D)\chi(C),
\]

where \(\chi=(-1)^\epsilon\) is the spin-two sign character. A proposed
normalization that repairs individual formulas but violates these equations
is not a transport cell.

## Finite falsifier

At \(\theta=0\),

\[
I+Q_0=\operatorname{diag}(2,0),
\qquad
I-Q_0=\operatorname{diag}(0,2).
\]

The correct pair sums to \(2I\), of rank two. Repeating the same sheet gives

\[
(I+Q_0)+(I+Q_0)=\operatorname{diag}(4,0),
\]

which still has rank one and the same null direction. Therefore
nonnegativity on two named sheets is insufficient: the spin-two characters
must be opposite.

## Source-authority boundary

This theorem is an algebraic template. Grothendieck must independently derive
from the doubled-tail operator, endpoint orientation, Clark shear, and Mellin
normalization:

- the actual sheet displacement \(g_C\) and its action on \((A,B)\);
- the coefficient \(\lambda\) and angle \(\theta\);
- retention of both sheets with the same trace normalization;
- the cocycle law through Fourier--Tate composition;
- stability of the rank-two sum under global completion.

Canonical vacuum transport also does not imply nonzero vacuum overlap. Even
if the finite two-sheet energy is \(2|\psi|^2\), RH strength still requires
that the completed zero state has nonzero controlled Hilbert-level amplitude
and that no distributional or endpoint channel escapes this norm.

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_quadrature_sheet_torsor.py
```

The checker works exactly over
\(\mathbf Q[c,s]/(c^2+s^2-1)\), verifies the anticommutation and rank
identities, and retains the same-null-line pair as a deliberate failure.
