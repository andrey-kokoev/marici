# An eight-leg cross-polarized positive dilation realizes the exact left-cutoff relative product placement

## Placement mismatch

Let

\[
\Delta Q_L
=Q_L^T-Q_L^0
\]

be the difference between the Tate and pure-reference Hardy projections.

The four-leg positive dilation `Psi_L` satisfies

\[
\Psi_L^*J_4\Psi_L
=\Delta Q_L.
\]

If it is applied to the compressed observer leg `P A_g`, its signed Gram is

\[
\langle
P A_h,
\Delta Q_L
P A_g
\rangle.
\]

This realizes the relative **triple compression**

\[
P\Delta Q_LP.
\]

Connes's ordered product instead places the physical cutoff only on the left:

\[
\boxed{
P\Delta Q_L.
}
\]

These are not equal when the observer does not commute with `P`.

## Exact sewing discrepancy

The difference is

\[
\boxed{
P\Delta Q_L
-
P\Delta Q_LP
=
P\Delta Q_L(I-P).
}
\]

This is the relative sewing block. It should not be discarded or assumed small before regulator analysis.

## Four-leg relative feature

Recall

\[
\boxed{
\Psi_Lx
=
\frac1{\sqrt2}
\left(
Q_L^Tx,
(I-Q_L^T)x,
Q_L^0x,
(I-Q_L^0)x
\right),
}
\]

with

\[
\Psi_L^*\Psi_L=I
\]

and

\[
\Psi_L^*J_4\Psi_L
=
\Delta Q_L,
\qquad
J_4
=
\operatorname{diag}(I,-I,-I,I).
\]

## Cross-polarized observer feature

Define the doubled feature

\[
\boxed{
\Theta_L(g)
=
\frac1{\sqrt2}
\left(
\Psi_L(PA_g),
\Psi_L(A_g)
\right)
}
\]

in the eight-leg carrier

\[
\mathcal H^{\oplus8}.
\]

Its ordinary norm is positive:

\[
\begin{aligned}
\|\Theta_L(g)\|^2
&=
\frac12
\left(
\|P A_g\|^2
+
\|A_g\|^2
\right).
\end{aligned}
\]

At finite outer regulator, both terms are finite. In the noncompact limit the regulator must remain until the relative readout is taken.

## Off-diagonal fundamental symmetry

Define

\[
\boxed{
K_8
=
\begin{pmatrix}
0&J_4\\
J_4&0
\end{pmatrix}.
}
\]

Since `J_4=J_4^*=J_4^(-1)`,

\[
\boxed{
K_8=K_8^*,
\qquad
K_8^2=I.
}
\]

Thus `K_8` is a bounded fundamental symmetry on the positive eight-leg Hilbert carrier.

## Exact signed readout

For observer pair `g,h`,

\[
\begin{aligned}
\langle
\Theta_L(h),
K_8\Theta_L(g)
\rangle
&=
\frac12
\left[
\langle
\Psi_L(PA_h),
J_4\Psi_L(A_g)
\rangle
\right.\\
&\qquad\left.
+
\langle
\Psi_L(A_h),
J_4\Psi_L(PA_g)
\rangle
\right]\\
&=
\frac12
\left[
\langle
P A_h,
\Delta Q_L A_g
\rangle
+
\langle
A_h,
\Delta Q_L P A_g
\rangle
\right].
\end{aligned}
\]

Since `P` and `Delta Q_L` are self-adjoint, this is

\[
\boxed{
\langle
\Theta_L(h),
K_8\Theta_L(g)
\rangle
=
\left\langle
A_h,
\frac{
P\Delta Q_L
+
\Delta Q_LP
}{2}
A_g
\right\rangle.
}
\]

Thus the eight-leg feature realizes the Hermitian part of the exact left-cutoff relative product.

## Diagonal observer

For `h=g`,

\[
\boxed{
\langle
\Theta_L(g),
K_8\Theta_L(g)
\rangle
=
\operatorname{Re}
\langle
A_g,
P\Delta Q_LA_g
\rangle.
}
\]

The imaginary part is

\[
\boxed{
\operatorname{Im}
\langle
A_g,
P\Delta Q_LA_g
\rangle
=
\frac1{2i}
\langle
A_g,
[P,\Delta Q_L]
A_g
\rangle.
}
\]

A Hermitian Weil/Gram form can receive only the real part. Any claim that the ordered product itself equals a positive or Hermitian boundary must separately control this commutator imaginary part.

## Triple compression plus sewing

Expand the Hermitian product:

\[
\begin{aligned}
\frac12
(P\Delta Q+
\Delta QP)
&=
P\Delta QP\\
&\quad+
\frac12
P\Delta Q(I-P)\\
&\quad+
\frac12
(I-P)\Delta QP.
\end{aligned}
\]

The first term is the four-leg triple-compression readout. The last two are adjoint sewing blocks.

Therefore the eight-leg dilation includes the sewing exactly rather than estimating it after the fact.

## Finite regulator identity

Let `Z_(R,N)` be the common outer/angular regulator and set

\[
X_g
=Z_{R,N}A_g.
\]

Define

\[
\Theta_{L,R,N}(g)
=
\frac1{\sqrt2}
\left(
\Psi_L(PX_g),
\Psi_L(X_g)
\right).
\]

Then every leg is an ordinary regulated Hilbert-space vector/operator, and

\[
\boxed{
\begin{aligned}
&\langle
\Theta_{L,R,N}(h),
K_8\Theta_{L,R,N}(g)
\rangle\\
&
=
\left\langle
A_h,
Z_{R,N}
\frac{
P\Delta Q_L+
\Delta Q_LP
}{2}
Z_{R,N}
A_g
\right\rangle.
\end{aligned}
}
\]

This is an exact finite `(L,R,N)` identity.

## Relation to the ordered trace

For `h=g*g^*` represented by an observer factor `A_g`, the ordered relative product is

\[
\operatorname{Tr}
(P\Delta Q_L
A_gA_g^*).
\]

By cyclicity at finite regulator,

\[
\operatorname{Tr}
(P\Delta Q_L
A_gA_g^*)
=
\operatorname{Tr}
(A_g^*P\Delta Q_LA_g).
\]

The eight-leg readout equals its real part. If the regulated relative product is real, they agree exactly. More generally, polarization of the Hermitian part is the correct Gram-valued object.

## Anti-Hermitian residual

Define

\[
\boxed{
\mathcal A_L
=
\frac1{2i}
(P\Delta Q_L-
\Delta Q_LP)
=
\frac1{2i}
[P,\Delta Q_L].
}
\]

This is self-adjoint and records the imaginary part of the ordered product. It is a separate signed channel, not part of the positive Weil Gram.

To identify the full ordered regulator with the Hermitian `C_34` boundary, one must prove

\[
\boxed{
\operatorname{Tr}
(A_h^*
\mathcal A_L
A_g)
\longrightarrow0
}
\]

or identify a source boundary term receiving it.

## A second eight-leg readout for the imaginary channel

The same positive carrier can encode the commutator channel by replacing `K_8` with

\[
\boxed{
K_8^{skew}
=
\begin{pmatrix}
0&-iJ_4\\
iJ_4&0
\end{pmatrix}.
}
\]

This is also a self-adjoint involution. Its signed readout is

\[
\boxed{
\Theta_L^*
K_8^{skew}
\Theta_L
=
\frac1{2i}
(P\Delta Q_L-
\Delta Q_LP).
}
\]

Hence real and imaginary placements are two readouts of one positive eight-leg feature.

## No placement loss

The eight-leg construction retains:

- the uncompressed observer leg `A_g`;
- the physically compressed leg `P A_g`;
- Tate and reference projection rows;
- projection and complement polarities;
- Hermitian and anti-Hermitian ordered-product channels.

Therefore no observer factor is silently moved through `P` or `Q`.

## Relation to positive refinement

The four-leg feature is sufficient for the symmetric relative projection pair. The eight-leg feature is the minimal direct doubling that records the asymmetric left-cutoff placement while keeping an ordinary positive Hilbert carrier.

At the simplicial level, the extra binary coordinate records whether the observer leg is:

\[
A_g
\]

or

\[
P A_g.
\]

The off-diagonal readout sews these two presentations.

## Remaining regulator comparison

The exact operator-placement problem is reduced to two scalar/form limits:

1. the Hermitian eight-leg readout converges to the Tate--Weil form;
2. the anti-Hermitian readout vanishes or converges to a separately identified boundary current.

The first follows from the centered scalar theorem once the characterwise Hardy conjugation is matched. The second is an explicit commutator estimate involving

\[
[P,Q_L^T-Q_L^0].
\]

It is now isolated rather than hidden inside “sewing.”

## Disposition

The exact left-cutoff relative placement has the positive realization

\[
\boxed{
\Theta_L(g)
=
\frac1{\sqrt2}
(\Psi_L(PA_g),
\Psi_L(A_g)),
}
\]

with Hermitian signed readout

\[
\boxed{
\Theta_L^*K_8\Theta_L
=
\frac12
(P\Delta Q_L+
\Delta Q_LP).
}
\]

A companion involution records the anti-Hermitian commutator channel. Thus the finite operator placement is fully represented on a positive eight-leg carrier. The sole remaining placement gate is the fate of the anti-Hermitian channel in the regulator limit.
