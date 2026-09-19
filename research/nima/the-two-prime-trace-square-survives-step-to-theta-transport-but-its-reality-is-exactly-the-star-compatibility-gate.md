# The two-prime trace-square survives step-to-theta transport, but its reality is exactly the star-compatibility gate

## Exact carrier transport

For `L_p=log p`, the step-history map

\[
J_p:\ell^2(\mathbb N_0)\to L^2(\mathbb R_+)
\]

satisfies

\[
T_{L_p}J_p=J_pB,
\qquad
A_{0,p}J_p=E_0.
\]

Therefore it preserves the complete local resolvent

\[
A_{0,p}(I-qT_{L_p})^{-1}J_p
=E_0(I-qB)^{-1}.
\]

The reciprocal doubled transport has the same eigenvalue ratio `q=p^{-z}` on
both sides. Hence its projective trace-square invariant

\[
\kappa_p=q+2+q^{-1}
\]

survives the discrete-to-step-history embedding exactly.

## Theta smoothing

Theta history is the fixed semigroup functional

\[
H^*=\int_0^\infty\Phi(u)R_u\,du.
\]

Translation commutes with this functional on the common invariant core. The
full translated-theta synthesis is injective on the labelled projective source.
Thus theta smoothing does not algebraically change `q` or `kappa_p` before
prime labels are codiagonalized.

This closes preservation of the two-prime invariant through:

\[
\text{valuation shells}
\to
\text{prime-mesh steps}
\to
\text{labelled translated-theta histories}.
\]

## Exact remaining issue

Preservation does not imply reality. On the reciprocal two-plane, Hilbert
adjunction sends

\[
q=p^{-z}
\longmapsto
\overline q=p^{-\bar z},
\]

while reciprocal transport sends

\[
q\longmapsto q^{-1}=p^z.
\]

Their compatibility would make

\[
q+q^{-1}
\]

real, and therefore `kappa_p` real. But this compatibility is precisely the
star condition that is known to hold on the critical seam and has not been
derived from scalar zero-state boundary data.

## Reduced finite gate

Full continuous-interval star compatibility is stronger than needed. The
confinement argument requires only

\[
\kappa_2(z)=\overline{\kappa_2(z)},
\qquad
\kappa_3(z)=\overline{\kappa_3(z)}.
\]

Equivalently, the completed zero-state quadratic comparison must make the
trace-square of the doubled `p=2` and `p=3` transports self-adjoint. These are
two scalar, frame-invariant consequences of the four polarized matrix-unit
identities.

## Disposition

The transport and smoothing arrows preserve the required invariant. The sole
remaining assertion is its zero-state reality. Assuming that reality directly
would assume the seam detector, so it must come from the corrected polarized
Green comparison or an independently sourced adjoint boundary law.