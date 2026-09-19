# Hermitian Gram matching alone cannot make the two-prime trace-square real

## Test

Let the reciprocal translated-history Gram be

\[
G_p=
\begin{pmatrix}
D_p&C_p\\
\overline{C_p}&D_p
\end{pmatrix},
\qquad D_p>0,
\]

and let spectral valuation transport be

\[
T_{p,z}=\operatorname{diag}(1,q_p),
\qquad q_p=p^{-z}.
\]

Then

\[
G_{p,z}=T_{p,z}^*G_pT_{p,z}
=
\begin{pmatrix}
D_p&q_pC_p\\
\overline{q_pC_p}&|q_p|^2D_p
\end{pmatrix}.
\]

This matrix is Hermitian for every complex `z`, on and off the critical seam.
Thus equality of all four polarized matrix entries with another Hermitian Gram
can hold without implying

\[
q_p^{-1}=\overline{q_p}.
\]

## Missing operator relation

The two-prime invariant is

\[
\kappa_p=q_p+2+q_p^{-1}.
\]

Its reality is controlled by compatibility of two operations on the transport
operator:

\[
T_{p,z}^{-1}
\quad\text{and}\quad
T_{p,z}^{\sharp},
\]

where `sharp` is the adjoint induced by the completed Green form. The required
identity is

\[
T_{p,z}^{-1}=T_{p,z}^{\sharp}
\]

on the reciprocal prime plane, or the weaker trace consequence

\[
\operatorname{tr}(T_{p,z}+T_{p,z}^{-1})
=
\overline{
\operatorname{tr}(T_{p,z}+T_{p,z}^{-1})
}.
\]

A Gram table specifies a metric. It does not by itself state that valuation
transport is unitary for that metric.

## Revised finite gate

The four endpoint matrix-unit identities remain necessary for transporting the
metric from the Stieltjes carrier to the theta carrier. They must be augmented
by an operator intertwining square

\[
Q_p^{\rm lin}T_p
=T_p^\theta Q_p^{\rm lin}
\]

and a source-derived adjoint law for `T_p^theta`. At `p=2,3`, only the
trace-square consequence is needed, but it cannot be extracted from Hermitian
symmetry alone.

## Falsifier

Choose any off-seam `z` and any positive `G_p`. The congruence

\[
G_{p,z}=T_{p,z}^*G_pT_{p,z}
\]

is a valid positive Hermitian Gram while

\[
\operatorname{Im}(q_p+q_p^{-1})
\]

is generically nonzero. This explicitly separates metric positivity from star
compatibility of transport.

## Disposition

The remaining RH-bearing cell is operator-level: reciprocal inversion must
coincide with Green adjunction on the zero-state prime transport. Completing
the target Gram alone, even all four entries, does not prove the two-prime
reality condition.