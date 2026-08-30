# The affine trace splitting gives a canonical zero-trace projector for tail extension

## Result

The explicit boundary right inverse produces a canonical bounded projection from the history graph onto its zero-trace subspace:

\[
\Pi_{0,L}=I-R_L\Gamma_L.
\]

Applying this projector to every tail, principal-value, or auxiliary history before Schur elimination prevents endpoint leakage exactly.

Therefore extension of the cyclic Stieltjes cell by arbitrary projected auxiliary histories preserves the endpoint lower bound. The remaining source question is whether the declared tail constructor is this relative projection, or is linked to it by an authorized comparison cell.

## Trace splitting

Let

\[
\mathcal G_L=H^1([L,2L];\mathcal H)
\]

and

\[
\Gamma_Lh=(h(L),h(2L)).
\]

The affine right inverse satisfies

\[
\Gamma_LR_L=I.
\]

Define

\[
\Pi_{0,L}=I-R_L\Gamma_L.
\]

Then

\[
\Gamma_L\Pi_{0,L}
=
\Gamma_L-\Gamma_LR_L\Gamma_L
=
0.
\]

Hence

\[
\operatorname{ran}\Pi_{0,L}
\subseteq
\ker\Gamma_L.
\]

If \(h\in\ker\Gamma_L\), then

\[
\Pi_{0,L}h=h.
\]

Therefore

\[
\operatorname{ran}\Pi_{0,L}
=
\ker\Gamma_L.
\]

## Projection identity

Using \(\Gamma_LR_L=I\),

\[
\Pi_{0,L}^2
=
(I-R_L\Gamma_L)^2
=
I-2R_L\Gamma_L+R_L\Gamma_LR_L\Gamma_L
=
I-R_L\Gamma_L
=
\Pi_{0,L}.
\]

Thus \(\Pi_{0,L}\) is a genuine bounded projection onto the closed zero-trace history space.

It need not be orthogonal in the raw graph norm. Orthogonality is unnecessary for endpoint typing.

## Explicit formula

For a history \(h\),

\[
(\Pi_{0,L}h)(t)
=
h(t)
-
\frac{2L-t}{L}h(L)
-
\frac{t-L}{L}h(2L).
\]

The two endpoint values vanish literally:

\[
(\Pi_{0,L}h)(L)=0,
\qquad
(\Pi_{0,L}h)(2L)=0.
\]

No pseudoinverse or post-Schur correction is involved.

## Boundedness

The trace map \(\Gamma_L\) is bounded on \(H^1([L,2L];\mathcal H)\), and the affine right inverse obeys

\[
\|R_L\|^2
\le
\frac L2+\frac2L.
\]

Therefore

\[
\|\Pi_{0,L}\|
\le
1+\|R_L\|\|\Gamma_L\|.
\]

On \(L\ge\log2\), this has at most the ordinary history trace growth. In the standard rescaled interval norm it is uniform; in the unrescaled graph norm it is at worst polynomial in \(L^{1/2}\) and remains harmless under the \(p^{-3/2}\) endpoint loading.

The exact constant is secondary because zero-trace projection is applied before the prime-diagonal summable Green block.

## Reciprocal covariance

Let reciprocal path reversal act by

\[
(\mathcal Rh)(t)=Sh(3L-t),
\]

where \(S\) is the source sheet involution on \(\mathcal H\).

On endpoint coordinates,

\[
\mathcal R_\partial(x,y)=(Sy,Sx).
\]

Affine interpolation is natural under reversal:

\[
\mathcal RR_L
=
R_L\mathcal R_\partial.
\]

The trace is likewise equivariant:

\[
\Gamma_L\mathcal R
=
\mathcal R_\partial\Gamma_L.
\]

Hence

\[
\mathcal R\Pi_{0,L}
=
\Pi_{0,L}\mathcal R.
\]

The zero-trace regularization preserves reciprocal parity.

## Prime and cutoff covariance

The construction acts independently on each prime-labelled history interval. Therefore it commutes with prime idempotents and finite cutoff restrictions.

No cross-prime kernel is introduced.

## Auxiliary extension

Let

\[
J_{\mathrm{tail},p}:
\mathcal T_p\to\mathcal G_L
\]

be any source tail or principal-value history map. Define its relative version by

\[
J_{\mathrm{tail},p}^{0}
=
\Pi_{0,L}J_{\mathrm{tail},p}.
\]

Then

\[
\Gamma_LJ_{\mathrm{tail},p}^{0}=0.
\]

Thus every projected auxiliary coordinate lies in the authorized zero-trace subspace before representation and before Schur elimination.

## Endpoint lower bound

Let the complete Green energy satisfy

\[
\mathcal E_L(h)\ge m\|\Gamma_Lh\|^2
\]

on the history graph, with \(m>0\).

Choose any endpoint lift and eliminate any closed auxiliary subspace contained in

\[
\operatorname{ran}J_{\mathrm{tail},p}^{0}
\subseteq
\ker\Gamma_L.
\]

For fixed endpoint value \(x\), every auxiliary variation retains that value. Therefore the effective Schur form obeys

\[
Q_p(x)\ge m\|x\|^2.
\]

Combined with the Pauli twirl, the two-port lifted arithmetic frame remains uniformly positive.

This conclusion does not require the projected tail to exhaust the full zero-trace space.

## Wall separation

The coefficient wall is not a zero-trace history. It must not be passed through \(\Pi_{0,L}\).

The complete local object separates:

\[
\text{endpoint harmonic cell}
\oplus
\text{projected zero-trace tail}
\oplus
\text{coefficient wall}.
\]

The wall remains connected through its Wronskian boundary morphism and residue representation.

This prevents zero-trace regularization from erasing the wall carrier.

## Authority qualification

The projection \(\Pi_{0,L}\) is canonical once the history trace and affine cell coordinate are declared. But replacing an existing source tail by \(\Pi_{0,L}J_{\mathrm{tail}}\) changes the constructor unless the source defines the tail relatively or supplies a comparison theorem.

Therefore two outcomes are legitimate:

1. the source tail is already equal to its zero-trace projection;
2. the projected tail is a new relative object with an explicit forgetting/comparison map.

Silently projecting only to make the Schur estimate pass is not authorized.

## Next audit

The source-specific gate is now finite:

> Compute the endpoint traces of the declared tail/PV histories. If they vanish, the complete cyclic-to-tail extension preserves endpoint coercivity immediately. If not, record their harmonic endpoint component separately and compare it with the existing endpoint cell before projection.

This is the exact extension test needed before assembling the complete local Green block.
