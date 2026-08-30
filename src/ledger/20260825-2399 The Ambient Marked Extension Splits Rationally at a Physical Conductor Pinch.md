---
author: marici.Benincasa
date: 2026-08-25
---

# 2399 — The Ambient Marked Extension Splits Rationally at a Physical Conductor Pinch

## Question

Entry 2397 proves that each positive physical conductor collision carries a
separately observed rank-one wall Kummer class.  The remaining local gate is
whether the ambient rank-nine absolute block can attach a hidden supported
class through the rank-twelve localization extension

\[
0\longrightarrow\mathcal M_9
\longrightarrow\mathcal M_{12}
\longrightarrow\mathcal W_3
\longrightarrow0.
\]

This can be decided at generic conductor support without reconstructing a
particular \(9\times3\) primitive extension block.

Sequence claim: `seqclaim-ee4fbc3c2ef0fdfa68b67b76`.

## Exact physical witness

Use Entry 2397's point

\[
(x,y,z;E)
=\left(\frac5{14},\frac35,\frac3{70};1\right).
\]

At this point,

\[
\Delta_1=0,
\qquad
\Delta_2=\frac{561}{1225}\ne0.
\]

The signed-energy letters are

\[
(\ell_1,\ell_2,\ell_3,\ell_4)
=\left(-\frac27,-\frac15,\frac{32}{35},1\right),
\]

so the pure elliptic discriminant is nonzero.  The algebraic quartic is
also a unit:

\[
\mathcal Q=\frac{51}{245}\ne0.
\]

Thus this is a generic point of the first conductor divisor, not an
elliptic, soft, total-energy, or quartic intersection.  The absolute surface
family is smooth there.

## Local monodromy types

Around the punctured normal disk to \(\Delta_1=0\), the rank-nine absolute
Gauss--Manin system is locally unramified:

\[
T_{\mathcal M_9}=I_9.
\]

In the oriented wall basis \((q_0,q_1,q_2)\), only
\(q_1=g_{101}\) is ramified:

\[
T_{\mathcal W_3}=\operatorname{diag}(1,-1,1).
\]

Therefore the local extension problem for the supported line is governed by

\[
V=\operatorname{Hom}(\mathcal K_-,\mathcal M_9),
\qquad T_V=-I_9.
\]

For a local system on a punctured disk,

\[
H^1(\mathbf Z,V)=V/(T_V-I)V.
\]

Over \(\mathbf Q\),

\[
T_V-I=-2I_9
\]

is invertible.  Hence

\[
\boxed{
\operatorname{Ext}^1_{\mathrm{Loc}_{\mathbf Q}}
(\mathcal K_-,\mathcal M_9)=0.
}

Any logarithmic off-diagonal representative at this generic conductor
point is removable by a boundary-preserving rational triangular gauge.  No
choice of primitive solver section is required for this conclusion.

## Supported cone and observer

The rational supported nearby object therefore contains exactly the already
identified wall line:

\[
\psi_{\Delta_1}^{\rm supp}\mathcal M_{12}
\simeq\mathcal K_-.
\]

Entry 308's horizontal Leray matrix sends its generator to

\[
g_{101}\longmapsto(2,0,0)^T.
\]

Thus the ambient localization extension adds no rational class hidden from
the physical route observer.  By exchanging labels, the same theorem holds
at a generic positive point of \(\Delta_2=0\).

## Integral qualification

The argument is intentionally rational/de Rham.  Over \(\mathbf Z\), the
cokernel of \(-2I\) is \((\mathbf Z/2)^9\).  The calculation therefore does
not prove an integral splitting of the ambient extension.  This is a
specific remaining lattice question, not a rational rank or monodromy
class and not new support.

## Result

\[
\boxed{
\begin{gathered}
\text{the ambient rank-twelve marked extension splits rationally at a}\
\text{generic positive conductor pinch, and its only supported rational}\
\text{class is the already faithful wall Kummer line.}
\end{gathered}}
\]

## Classification

- Carrier support: existing conductor/Landau divisor;
- absolute coefficient block: smooth and unramified;
- wall coefficient block: one semisimple Kummer line;
- rational ambient extension class: zero;
- physical route kernel: zero;
- possible integral refinement: two-torsion, uncomputed;
- new Carrier datum: none.

## Scope

This theorem is local at a generic smooth point of either conductor divisor.
It does not cover intersections with soft, elliptic, Gram, or marked
endpoint support, nor the nonhomogeneous six-scale direct image or tensor
polarization system.

## Durable evidence

- `research/benincasa/check_conductor_ambient_extension_local_splitting.py`;
- `research/benincasa/conductor-ambient-extension-local-splitting.json`;
- Entries 307, 308, 851--855, 869, and 2397.

## Next falsifier

Test the same extension integrally.  Use the source Smith lattice and the
fixed occurrence/Leray map to determine whether any of the possible
\((\mathbf Z/2)^9\) ambient extension classes is actually realized.  A
realized torsion class must then be paired with the integral physical cycle;
it is coefficient/lattice data unless it forces additional support.
