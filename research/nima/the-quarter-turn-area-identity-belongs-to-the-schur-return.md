# The quarter-turn area identity belongs to the Schur return, not automatically to the completed endpoint Gram

## Notation separation

Let

\[
Q_p=C_pD_p^{-1}C_p^{*}
=
E_{Q,p}+iH_{Q,p}
\]

be the auxiliary Schur return, and let

\[
G_p^{\mathrm{eff}}=A_p-Q_p
\]

be the completed endpoint form. In the minimal two-endpoint cell, write the single oriented coordinate of \(H_{Q,p}\) as \(h_{Q,p}\).

The exact quarter-turn identity previously derived is

\[
h_{Q,p}^{2}
=
\kappa_p^{2}\det E_{Q,p},
\qquad
\kappa_p=\frac{|\tau_p|}{s_p}.
\]

Therefore

\[
\det Q_p
=
(1-\kappa_p^{2})\det E_{Q,p}.
\]

This is the local auxiliary-return determinant identity.

## Completed endpoint determinant

The real part of the completed endpoint form is

\[
E_{G,p}=A_p-E_{Q,p},
\]

and its odd coordinate is

\[
h_{G,p}=-h_{Q,p}
\]

up to the frozen sign convention. Hence

\[
\det G_p^{\mathrm{eff}}
=
\det E_{G,p}-h_{G,p}^{2}
=
\det(A_p-E_{Q,p})-h_{Q,p}^{2}.
\]

In general this is not equal to

\[
(1-\kappa_p^2)\det E_{Q,p}
\]

and not equal to

\[
(1-\kappa_p^2)\det E_{G,p}.
\]

Either equality requires an additional source theorem relating the bare endpoint block \(A_p\) to the even Schur return \(E_{Q,p}\).

## Two independent finite gates

The local constructor-admissibility gate is

\[
\delta_{KV,p}=1-\kappa_p^2>0.
\]

It ensures that the reciprocal auxiliary block and its return remain inside the quarter-turn positivity cone.

The assembled endpoint gate is

\[
\Delta_{G,p}
=
\det(A_p-E_{Q,p})-h_{Q,p}^{2}>0,
\]

together with positivity of the diagonal entries. This tests whether the bare endpoint energy dominates the complete Schur return.

Thus the local quarter-turn margin feeds the later diagonal/mixed Green margin but cannot replace it.

## Completion requirements

Uniform construction requires separate control of:

1. the normalized auxiliary margin \(1-\kappa_p^2\);
2. the absolute even-return scale \(E_{Q,p}\);
3. the bare endpoint scale \(A_p\);
4. the assembled endpoint Schur margin \(\Delta_{G,p}\).

A lower bound on \(\det E_{Q,p}\) is meaningful only in a normalized source frame. It does not by itself lower-bound \(\det(A_p-E_{Q,p})\).

## Hostile

Choose a uniformly nonsaturated auxiliary cell with fixed \(\kappa<1\) and fixed positive \(E_Q\), but let \(A_p\downarrow E_{Q,p}\). The local quarter-turn constructor remains perfectly admissible while the completed endpoint Gram becomes singular or indefinite.

Conversely, a large \(A_p\) may keep the completed endpoint form positive even when the auxiliary resolver approaches saturation; that does not repair the loss of constructor-level completion control.

## Correct hierarchy

The exact hierarchy is:

\[
\text{auxiliary reciprocal positivity}
\longrightarrow
\text{quarter-turn return identity}
\longrightarrow
\text{Schur subtraction from }A_p
\longrightarrow
\text{completed endpoint positivity}.
\]

The next source calculation must therefore freeze whether its symbol \(E_p\) denotes the even return \(E_{Q,p}\) or the real completed endpoint block \(E_{G,p}\). The area identity is currently proved only for the former.
