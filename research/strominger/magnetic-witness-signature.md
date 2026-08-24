# Magnetic failure witnesses are typed by their ambient map

Companion to `checkers/magnetic_witness_signature_checks.py` (6/6, exit 0)
and `results/magnetic_witness_signature.json`.

Let (M:S\to T) be the full exponent-lattice map and let
(P_I:T\to T_I) select a square observation chart.  Two superficially
similar right-null vectors have different types:

\[
v\in\ker(P_IM)
\qquad\text{versus}\qquad
v\in\ker M.
\]

Only the second is an invariant transport circuit.  The first may be an
artifact of observations discarded by (P_I).

At every tested even chart boundary, (g=2,4,\ldots,14), the preferred
square map (P_IM) has left and right nullity one.  Nevertheless,

\[
\ker M=0,
\]

and the apparent chart-kernel vector (v_I) satisfies

\[
Mv_I\ne0.
\]

After replacing target row (1) by row (3), the neighboring chart
(P_JM) is invertible.  Thus both artificial null directions disappear.
The intrinsic presentation witness is the left cocircuit of the failed
observation set,

\[
\lambda_I=\operatorname{prim}\bigl((2g+7)e_1-(3g+7)e_0\bigr)
\in\ker(P_IM)^T.
\]

At the genuine grade-two exceptions the situation is different.  The
primitive vectors

\[
\kappa_1=(1,-1),
\qquad
\kappa_7=(1,0,0,0,0,-3,0,2)
\]

obey (M\kappa=0) for the full target matrix.  No change of target
observations can restore injectivity, because every restriction factors
through the already singular map (M).

The witness signature must therefore retain its ambient typing:

\[
\boxed{
\Sigma(M,P_I)=
\left(
[\lambda_I\in\ker(P_IM)^T],
[\gamma\in H_{\mathrm{support}}],
[\kappa\in\ker M]
\right).
}
\]

An untyped list of integer vectors would conflate an artificial kernel of a
projection with a genuine kernel of the represented object.

## Functorial behavior

Changing observation charts acts only on the first coordinate.  It may remove
or transport a cocircuit witness but cannot change (ker M).  Conversely, a
source degeneration that creates (ker M) persists under every target
projection.  The support-homology coordinate is separate and is not computed
in this magnetic checker.

This supplies the first exact typing law for the proposed higher algebra:

\[
\text{presentation witnesses are relative to }P,
\qquad
\text{residue witnesses are intrinsic to }M.
\]

## Scope

The distinction is a general linear-algebra theorem.  Its magnetic instances
are verified exactly on seven even chart boundaries and the two grade-two
transport failures.  The checker does not construct the cross-sector support
homology coordinate.
