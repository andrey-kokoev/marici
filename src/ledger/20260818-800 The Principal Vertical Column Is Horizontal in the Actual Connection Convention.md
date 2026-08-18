---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 800 — The Principal Vertical Column Is Horizontal in the Actual Connection Convention

## Hard-to-vary claim

For the canonical two-prime reconstructed weighted packet, the complete
principal vertical residue column is compatible with the tangential
Gauss--Manin transport.  No mixed homotopy is required at this residue level.

The apparent obstruction obtained from

\[
\partial_tR_e+A_tR_e-R_eA_t
\]

uses the opposite connection convention from the one obeyed by the
reconstructed matrices.

## Frozen packet and convention audit

Use Entry 793's reconstructed matrices and weighted chart

\[
u=e,
\qquad
v=2-e+2e^2t,
\qquad
(w_1,w_2,w_3,w_4)=(0,0,4,2).
\]

Direct evaluation of the original two-variable matrices at three exact
generic rational points distinguishes the two signs:

\[
\partial_uA_v-\partial_vA_u-[A_u,A_v]=0,
\]

whereas the same expression with (+[A_u,A_v]) is nonzero.  Thus the
packet obeys

\[
\boxed{dF=A F,\qquad dA-A\wedge A=0.}
\]

This corrects the sign statement serialized in Entry 793's derived packet.

## Complete exceptional residue data

The tangential exceptional connection is

\[
A_t=
\operatorname{diag}\left(0,\frac{2t}{t^2-1},0,0\right).
\]

Retaining the full normal residue after the weighted shear gives

\[
R_e=
\begin{pmatrix}
-\frac32&0&0&0\\
0&4&0&0\\
0&-\frac1{2(t^2-1)}&\frac72&0\\
0&\frac3{2(t^2-1)}&0&\frac52
\end{pmatrix}.
\]

Its lower-left block is precisely the principal vertical map before taking
the endpoint residues:

\[
C_E(t)=
\begin{pmatrix}
0&-\dfrac1{2(t^2-1)}\\[1mm]
0&\dfrac3{2(t^2-1)}
\end{pmatrix}.
\]

The diagonal entries of (R_e) retain the source and target normal-residue
connections.  They may not be discarded when testing whether (C_E) is
horizontal.

## Mixed-flatness calculation

For the actual convention, the coefficient of the mixed curvature is

\[
\Theta
=
\partial_tR_e-A_tR_e+R_eA_t.
\]

Exact symbolic reduction gives

\[
\boxed{\Theta=0.}
\]

In particular, on the principal lower-left block,

\[
\boxed{
\nabla_{mathrm{target}}C_E
=
C_E\nabla_{mathrm{source}}.
}
\]

No equation of the form

\[
\Theta=d_{\rm vert}H+Hd_{\rm vert}
\]

is needed at this level: one may take (H=0).

Using the opposite sign instead produces the spurious defect

\[
\begin{pmatrix}
0&\dfrac{2t}{(t^2-1)^2}\\[1mm]
0&-\dfrac{6t}{(t^2-1)^2}
\end{pmatrix}.
\]

This is exactly the earlier apparent obstruction.

## Interpretation

There is no need to manufacture a rank-five connection.  The smallest typed
object is the two-term relative de Rham complex

\[
\left(
P^\bullet,\nabla_P
\right)
\xrightarrow{\ C_E\ }
\left(
E^\bullet,\nabla_E
\right),
\]

or its cone with the existing Čech orientation.  The vertical map is already
a morphism of the reconstructed connections.

This does **not** make the constant vector

\[
(0,1,0,-3)
\]

horizontal.  That vector is only a coordinate presentation obtained after
forgetting the source and target normal-residue actions.  The invariant object
is the map (C_E(t)), not its constant projective numerator.

## Classification

- carrier: unchanged resolved infinity/soft closure;
- coefficient object: a typed relative de Rham--Čech cone;
- mixed obstruction: zero in the two-prime reconstructed packet;
- new carrier datum: none;
- remaining qualification: exact identification of the two-prime lift with
  the source characteristic-zero connection, as already stated in Entry 793.

## Verification

- exact Symbolica checker:
  `research/benincasa/marici-gm/src/bin/weighted_mixed_flatness_convention.rs`;
- machine-readable packet:
  `research/benincasa/weighted-mixed-flatness-convention.json`;
- allocator claim `seqclaim-d55e388485c91adb7b8d48c8`.

## Next falsifier

Insert this horizontal principal map into the oriented three-divisor supported
Čech complex.  Verify all signed vertex-to-edge squares as morphisms of
connections, then compute the horizontal cohomology of the supported cone.
Only if that cohomology has a canonical rank-one factor may it replace the
nonhorizontal constant projective line in the physical pairing.
