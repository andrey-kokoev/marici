# Unitary cross-sewing of two strictly passive sectors forbids off-seam closed modes

Author: `marici.Nima`

Date: 2026-08-26

Status: exact abstract zero-confinement theorem and one source-sewing gate

## Two oriented passive nodes

Let the right and left sector nodes have incoming ports (u_+,u_-), outgoing
ports (v_+,v_-), and internal defect states (g_+,g_-). After orienting each
half-plane toward its own disk interior, suppose their energy identities are

\[
\lVert u_+\rVert^2-\lVert v_+\rVert^2
=
\delta_+\lVert g_+\rVert^2,
\]

and

\[
\lVert u_-\rVert^2-\lVert v_-\rVert^2
=
\delta_-\lVert g_-\rVert^2,
\]

with (delta_+,delta_->0) at paired off-seam points.

For the reflected pair (zeta) and (-\zeta), the two local Cayley charts
give the same positive defect scale. In the simplest normalization,

\[
\delta_+=\delta_-=2|\operatorname{Re}\zeta|.
\]

## Lossless cross-sewing

Let (J) be a unitary source sewing map between the two port spaces. Close the
two nodes by

\[
u_-=Jv_+,
\qquad
u_+=J^{-1}v_-.
\]

Unitarity gives

\[
\lVert u_+\rVert^2+\lVert u_-\rVert^2
=
\lVert v_+\rVert^2+\lVert v_-\rVert^2.
\]

Adding the two passive identities therefore yields

\[
\delta_+\lVert g_+\rVert^2
+\delta_-\lVert g_-\rVert^2
=0.
\]

Both coefficients are positive, so

\[
g_+=g_-=0.
\]

If the complete source system is observable, vanishing defect states force
the entire closed mode to vanish. Hence no nonzero closed mode exists away
from the seam.

## Meaning for RH

Suppose the completed theta zero is identified source-forward with a nonzero
closed mode of the doubled tail system. Then the theorem gives a symbolic
zero-confinement mechanism:

```text
off-seam closed mode
  -> two strictly positive sector defects
  -> lossless reciprocal cross-sewing
  -> zero total boundary supply
  -> both defect states vanish
  -> observability forces the mode to vanish
  -> contradiction
```

This is the geometric puncture intuition compiled into passive-system
algebra. It uses two sectors essentially; one sector alone has an open
boundary supply and cannot close the contradiction.

## The exact missing source theorem

Local Tate factors are unitary on the critical seam but generally not unitary
off it. Therefore the theorem cannot be applied by assigning each prime a
lossless cross-map.

The required statement is stronger and global:

> After retaining primitive, square, seam, connected-tail, and archimedean
> channels, completed reciprocal sewing becomes a unitary cross-connection
> between the two locally oriented passive port spaces.

This must hold on the full operator-valued boundary carrier. Scalar functional
equation symmetry and modulus-one determinant data are insufficient.

## Why the seam remains special

On the critical line, the defect coefficients vanish. The energy argument
then permits nontrivial lossless closed modes and unitary spectral flow. Thus
the proof mechanism excludes modes only in the two open sectors and leaves
the common seam available as the characteristic locus.

The location of the critical line comes from reciprocal modular orientation;
the exclusion comes from strict passivity plus lossless cross-sewing.

## Hostile nonunitary sewing

If (J) has gain different from one, the cross-connection can inject or
remove boundary energy. Then its supply residual can cancel the positive
sector defects and support a nonzero closed mode.

This exactly matches the local-prime obstruction: off-seam Tate comparison
has nonunit gain. Only the completed coupled sewing could repair it.

## Finite falsifier

At each arithmetic cutoff, form the full sewing operator (J_X) on all typed
ports and compute

\[
\mathcal U_X=J_X^*J_X-I.
\]

One nonzero typed residual disproves exact losslessness at that cutoff. If
(mathcal U_X=0), compute the observability Gramian of the closed
interconnection. A nonzero null vector disproves strict zero confinement.

For completion, both the sewing residual and the smallest observability value
must remain controlled in the constructor-derived topology.

