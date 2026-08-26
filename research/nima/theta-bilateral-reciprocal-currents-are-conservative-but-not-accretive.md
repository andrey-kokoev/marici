# Bilateral reciprocal currents are conservative but not accretive

## Native operator current

On the bilateral valuation chain \(\ell^2(\mathbb Z)\), let \(U\) be the
unitary shift and let \(R\) be reflection, so that

\[
RUR=U^{-1}.
\]

For a prime \(p\), grade \(k\), and centered coordinate
\(z=s-\tfrac12\), define

\[
J_{p,k}(z)
=
\frac{p^{-k/2}}{k}
\left(
e^{kz\log p}U^k
-
e^{-kz\log p}U^{-k}
\right).
\]

This is reciprocal-odd:

\[
RJ_{p,k}(z)R
=
-J_{p,k}(-z).
\]

On the critical seam \(z=it\),

\[
J_{p,k}(it)^*
=
-J_{p,k}(it).
\]

Thus the source-native glued current is exactly skew-adjoint on the seam. The
distributional augmentation applied to \(J_{p,k}e_0\) recovers the polarized
Euler cumulant before scalarization.

## Fourier symbol

Under the Fourier transform

\[
\ell^2(\mathbb Z)\longrightarrow L^2(S^1),
\]

the shift \(U\) becomes multiplication by \(e^{i\theta}\). Write

\[
z=x+it,
\qquad
L=\log p,
\qquad
\phi=k(tL+\theta).
\]

The symbol of \(J_{p,k}\) is

\[
j_{p,k}(z,\theta)
=
\frac{2p^{-k/2}}{k}
\left(
\sinh(kxL)\cos\phi
+
i\cosh(kxL)\sin\phi
\right).
\]

Its Hermitian part is therefore

\[
\Re j_{p,k}(z,\theta)
=
\frac{2p^{-k/2}}{k}
\sinh(kxL)\cos\phi.
\]

For every \(x\ne0\), this takes both signs as \(\theta\) runs around the
circle.

## Zero-mean obstruction

More generally, any finite reciprocal-odd Laurent current built only from
nonzero powers of \(U\) has zero angular mean:

\[
\int_0^{2\pi}\Re j(z,\theta)\,d\theta=0.
\]

If its Hermitian part were positive semidefinite almost everywhere, the
zero-mean identity would force it to vanish almost everywhere. The same holds
for negative semidefiniteness.

Consequently a nontrivial bilateral reciprocal current cannot be accretive or
dissipative in either open half-strip under the native common Hilbert metric.

This is not a defect in the construction. It is the operator expression of a
lossless two-direction current: positive and negative Fourier quadratures
coexist.

## What the adjoint law does prove

The native bilateral construction supplies:

- source-derived direct and reciprocal transport;
- a common metric;
- exact seam skew-adjointness;
- the primitive, square, and connected currents before scalarization;
- a canonical conservative flow and Cayley-unitary seam evolution.

It does not supply:

- a positive real part off the seam;
- coercivity of the global boundary operator;
- nonvanishing of a selected scalar overlap;
- confinement of the intrinsic divisor.

The distinction matches the earlier control-theoretic result: losslessness of
a realization does not exclude a dark transmission zero.

## Why a one-sided restriction is not free

Restricting to a Hardy or unilateral cone can create a preferred sign because
it removes one direction of the bilateral spectrum. But reciprocal sewing
exchanges the two directions.

Therefore any such compression requires a source-derived polarization
projector \(P\) satisfying declared compatibility with reflection, boundary
augmentation, and completion. Choosing \(P\) from the desired sign would
reintroduce the missing orientation by hand.

The exact new gate is not another metric. It is a source operation selecting
a polarization while preserving enough reciprocal information to reconstruct
the completed section.

## Finite falsifier

For any proposed accretivity law on the bilateral current:

1. Fourier-diagonalize the finite Laurent approximation;
2. compute the Hermitian symbol on a uniform angular grid;
3. verify its angular mean;
4. exhibit two angles separated by a sign change;
5. test whether a proposed positive compression uses a source-authorized
   projector.

A nonzero zero-mean Hermitian symbol falsifies semidefinite orientation. A
projector lacking source authority only hides the negative quadrature.

## Disposition

The bilateral valuation shift is the correct pre-scalar operator object and a
substantial provenance advance. It closes the question of how reciprocal
Euler currents acquire a common adjoint structure.

It simultaneously closes native Hilbert-space accretivity on the full
bilateral carrier. Any RH-bearing advance must now provide an independently
source-derived polarization or a different non-inequality law on the rigged
boundary system.
