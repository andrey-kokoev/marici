# Innerness of a xi-built boundary phase would be circular

The lossless-boundary route has a precise no-circularity test.

Given an entire function \(E\), the quotient
\[
\Theta_E(z)
=
\frac{E^{\#}(z)}{E(z)},
\qquad
E^{\#}(z)=\overline{E(\bar z)},
\]
has unit modulus on the real axis wherever defined. If \(E\) has no zeros in the upper half-plane and satisfies the appropriate bounded-type conditions, then \(\Theta_E\) is inner there.

This is tempting for the completed zeta function: construct the seam phase from a ratio involving \(\xi\), declare it inner, and use unitary feedback. But upper-half-plane analyticity and contractivity of that ratio already encode the location of the zeros of its denominator. In a Hermite--Biehler or de Branges formulation, the required inequality is generally the hard zero-location statement.

Therefore the following chain is circular:
\[
\xi
\to
\text{ratio built from }\xi
\to
\text{assume the ratio is Schur or inner}
\to
\text{deduce RH}.
\]

Boundary unimodularity alone is not enough. A meromorphic quotient can have modulus one on the real line while possessing poles in the upper half-plane. Those poles are exactly what a Schur theorem forbids.

The constructor must instead be ordered as follows:

1. Build a conservative colligation from source-local wall, archimedean, prime, and sewing data without using the unknown zero divisor.
2. Prove its transfer \(G(z)\) is Schur from an energy identity.
3. Prove its boundary unitary part from conservative transport.
4. Only then identify
   \[
   \det(I-CG(z))
   \]
   with \(\xi(\tfrac12-iz)\) up to a known zero-free factor.

This makes the energy identity logically independent of the determinant identity.

A useful audit is dependency-sensitive. For every coefficient entering \(G\), record whether it is derived from:

- theta/Mellin source kernels;
- gamma and endpoint factors;
- prime incidence;
- reciprocal reflection;
- or \(\xi\) itself.

Any use of \(\xi^{-1}\), a logarithmic derivative across the critical strip, a zero-dependent canonical product, or a branch of \(\log\xi\) upstream of Schur contractivity invalidates the explanation.

There is one legitimate role for completed scalar data before the final identification: values known from source integrals that are independently convergent and do not require choosing a zero-free chart. Equality first proved in \(\operatorname{Re}s>1\) may then be analytically continued only after both constructor sides are independently defined.

The strongest acceptable theorem is:

> The source colligation is conservative by a Green/Stokes identity, its transfer determinant agrees with the Euler--Mellin scalar in the classical half-plane, and both sides continue independently to the completed domain.

The identity theorem can then extend their equality without importing RH, provided the constructor continuation was established without dividing by \(\xi\).

The smallest hostile defines
\[
G(z)=C^{-1}\left(I-\xi(\tfrac12-iz)P\right)
\]
for a rank-one projector \(P\). Its determinant has exactly the desired scalar shadow, but contractivity of \(G\) is simply another formulation of a bound on \(\xi\).

A subtler hostile uses the phase of \(\xi\) on the seam and extends it by a Schwarz integral. The extension is inner only after selecting boundary data and singular factors that already know the zero divisor.

Thus the next packet should include an authority DAG:
\[
\text{source kernels}
\to
\text{colligation blocks}
\to
\text{energy identity}
\to
\text{Schur theorem}
\]
independent of
\[
\text{Euler/Mellin scalar}
\to
\text{determinant identification}.
\]
The two branches may meet only at the final comparison theorem.

This is the decisive guardrail for the emerging scattering proof architecture.
