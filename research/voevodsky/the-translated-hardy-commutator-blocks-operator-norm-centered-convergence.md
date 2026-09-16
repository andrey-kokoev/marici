# The translated Hardy commutator blocks operator-norm centered convergence

## Proposed strong criterion

A convenient sufficient condition for convergence of the finite physical polarity residuals would be

\[
\|D_{L,F}-A_F\|\to0
\]

at each conductor level \(F\).

The corrected left-Hardy placement calculation shows that this criterion is generally too strong.

## Placement decomposition

For observer multipliers \(M_{m_g},M_{m_h}\), the finite placement term decomposes as

\[
\operatorname{Tr}
(M_{m_h}^*\Pi_L\Delta Q_0M_{m_g})
=
\operatorname{Tr}(\Pi_LT_{g,h})
+
\mathcal C_L(g,h),
\]

where

\[
T_{g,h}=M_{m_h}^*\Delta Q_0M_{m_g}
\]

and

\[
\mathcal C_L(g,h)
=
\operatorname{Tr}
([M_{m_h}^*,\Pi_L]\Delta Q_0M_{m_g}).
\]

The exterior trace-class term converges by strong convergence of \(\Pi_L\). The commutator term converges only through oscillation.

## Constant norm under translation

Since

\[
\Pi_L=U_L^*\Pi U_L
\]

and observer multipliers commute with \(U_L\),

\[
[M_{m_h},\Pi_L]
=U_L^*[M_{m_h},\Pi]U_L.
\]

Hence

\[
\boxed{
\|[M_{m_h},\Pi_L]\|_2
=
\|[M_{m_h},\Pi]\|_2.
}
\]

The translated commutator does not converge to zero in Hilbert--Schmidt norm or operator norm unless it vanishes identically.

Its pairing with a fixed localized block tends to zero because its kernel acquires the oscillatory factor

\[
e^{-2iL(s-t)}.
\]

This is weak convergence, not norm convergence.

## Consequence for the centered physical error

The finite centered error contains the placement channel represented by this translated commutator. Therefore the established scalar theorem gives

\[
\langle h,(D_{L,F}-A_F)g\rangle
\to0
\]

on fixed observer pairs, but does not give

\[
\|D_{L,F}-A_F\|\to0.
\]

Indeed, translated compact operators provide the standard hostile model:

\[
K_L=U_L^*KU_L.
\]

Then

\[
K_L\rightharpoonup0
\]

under the same oscillatory hypotheses while

\[
\boxed{
\|K_L\|=\|K\|.
}
\]

Thus operator-norm centered convergence is not the correct expected theorem for the transported placement regulator.

## What remains sufficient for common-bulk positivity

Norm decay is unnecessary for an extensive common edge. A uniform fixed-conductor bound

\[
\boxed{
\|D_{L,F}-A_F\|
\le K_F
}
\]

is enough.

Together with

\[
G_{L,F}^0\succeq(L-\delta_{L,F})I
\]

and

\[
A_{F,-}\preceq(F+C_S)I,
\]

it gives

\[
G_{L,F}^T
\succeq
\left(
L-
\delta_{L,F}-
F-C_S-K_F
\right)I.
\]

Hence a positive common scalar bulk exists whenever

\[
\boxed{
L
\ge
\delta_{L,F}+F+C_S+K_F.
}
\]

The translated placement error consumes only bounded edge capacity; it need not disappear in norm.

## Residual boundary

Because the error need not vanish in norm, the finite residual positive legs need not converge in the ordinary Hilbert-feature category. Their scalar cross observations still converge by the Riemann--Lebesgue argument.

This is precisely the distinction encoded by the relative positive-feature category:

- common row retained as a bounded module;
- difference row observer-localized and Hilbert--Schmidt;
- cross readout convergent in trace pairing;
- no claim of norm convergence for the translated common/placement row.

## Correct physical objective

There are therefore two separate targets.

### Finite filtered positivity

Prove a uniform fixed-conductor form bound

\[
-K_FI
\preceq
D_{L,F}-A_F
\preceq
K_FI.
\]

This yields a genuine positive common bulk for sufficiently large \(L\).

### Boundary observation

Use weak oscillatory convergence on fixed observer pairs to identify the limiting signed Tate current. This lives naturally in the relative feature category and does not require residual-Gram norm convergence.

## Disposition

The operator-norm convergence target is withdrawn as an expected conclusion. Translation preserves the norm of the Hardy commutator remainder.

The correct quantitative gate for positive filling is only

\[
\boxed{
\sup_L\|D_{L,F}-A_F\|<\infty
}
\]

at fixed conductor, together with extensive reference coercivity. The limiting tetrahedral observation is then weak/relative rather than an ordinary norm limit of positive residual legs.
