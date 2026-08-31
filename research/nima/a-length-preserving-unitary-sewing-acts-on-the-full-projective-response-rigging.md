# A length-preserving unitary sewing acts on the full projective response rigging

## Question

Can the Fourier--Poisson sewing operator and its contragredient response action
be defined simultaneously on the primitive, square, connected, wall, and
Hilbert strata of the declared arithmetic rigging?

## Claim boundary

Yes whenever the source sewing is a length-preserving unitary fiber transport
on the valuation-labelled object. This proves stratified continuity and ideal
preservation. It does not prove that the complete Evans response trace obeys
the sewing intertwining square.

## Projective source

Let the valuation-labelled test object have seminorms

\[
 q_\delta(x)=\sum_\nu e^{\delta\ell(\nu)}\|x_\nu\|_{T_\nu},
 \qquad \delta>0.
\]

Assume the sewing sends each label \(\nu\) to \(\sigma\nu\), with

\[
 \ell(\sigma\nu)=\ell(\nu),
\]

and acts by a unitary fiber map

\[
 W_\nu:T_\nu\longrightarrow T_{\sigma\nu}.
\]

Then

\[
 q_\delta(Wx)
 =\sum_\nu e^{\delta\ell(\sigma\nu)}\|W_\nu x_\nu\|
 =q_\delta(x).
\]

Thus \(W\) is an isometry for every projective seminorm and extends to a
topological automorphism of \(\mathcal A_{\exp}\).

## Hilbert middle rung

On

\[
 \mathcal H_0=\ell^2(\mathcal M;T),
\]

label permutation and fiber unitarity give

\[
 \|Wx\|_{\mathcal H_0}=\|x\|_{\mathcal H_0}.
\]

Hence \(W\) is unitary on the Hilbert observation rung.

## Strong dual and contragredient

For \(r\in\mathcal A_{\exp}'\), define

\[
 (W^{-*}r)(x)=r(W^{-1}x).
\]

Because \(W^{-1}\) is continuous on every test seminorm,
\(W^{-*}\) is continuous on the strong dual. On the Hilbert middle rung,
unitarity gives

\[
 W^{-*}=W
\]

under the declared Riesz pairing, while the test/dual formulation remains
valid without using Riesz for primitive currents.

A finite-order row remains finite order because \(W\) preserves
\(\ell(\nu)\). Thus primitive distributional currents stay in the strong dual.

## Three determinant strata

### Primitive

Primitive currents are dual rows, not Hilbert states. The transpose action
above is their authorized transport.

### Square

Square packets on the Hilbert rung are transported unitarily. Hilbert--Schmidt
class is invariant under left or right unitary composition.

### Connected

If \(K\) is nuclear or trace class, then

\[
 WKW^{-1}
\]

has the same ideal norm. Therefore the connected return remains nuclear and
its determinant-class status is preserved.

No equality among these three modalities is inferred.

## Wall and finite boundary fibers

The wall/jump module is finite-dimensional. Its source reciprocal matrix and
orientation act continuously. If the normalized sewing is unitary for the
polarized wall metric, its graph is maximal isotropic in the doubled boundary
space.

The reciprocal odd sign changes the oriented coordinate but not its norm.

## Archimedean qualification

A scalar archimedean Tate multiplier of unit modulus on the sewing axis acts
unitarily on its boundary fiber. Off that axis, or on a stronger graph domain,
its continuity must be proved in the corresponding topology. The present
argument does not transport on-axis unitarity away from the declared locus.

## Restricted product

Finite local sewing operators commute because they act on distinct labelled
fibers. Their restricted product is isometric on every finite packet. The
projective seminorm identity permits completion to the full restricted product
without a norm loss, provided the vacuum is fixed outside finitely many labels.

## Remaining response theorem

Topological transport does not imply that the source response traces commute
with sewing. Candidate two still requires

\[
 \mathcal O_{\partial,+}\operatorname{Tr}_+
 =W_{\rm FP}\mathcal O_{\partial,-}\operatorname{Tr}_-
\]

and the dual equation with \(W_{\rm FP}^{-*}\), on the complete Evans kernel
packet.

This is an equality of source maps across every stratum. The scalar Xi
functional equation verifies at most one contracted coefficient.

## Disposition

Length-preserving unitary Fourier--Poisson sewing is compatible with the full
projective test--Hilbert--dual rigging and preserves the square and connected
operator ideals. The remaining SCC candidate is the actual complete response
intertwining square, not existence of the stratified transport. No RH
conclusion is authorized.
