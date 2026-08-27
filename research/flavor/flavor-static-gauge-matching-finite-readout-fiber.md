# Gauge symmetry protects static matching but not the finite readout: WP769

## Question

Does an unbroken boundary gauge symmetry derive the endpoint completion that
remained free in WP768?

## Gauge-authorized boundary class

A boundary Proca mass is forbidden while the gauge symmetry is unbroken. A
boundary gauge-kinetic term is invariant and remains part of the complete
source grammar. At Euclidean momentum (p), it supplies Robin data

\[
a=r_0p^2,
\qquad
b=r_Lp^2.
\]

Writing

\[
\mu=\sqrt{m^2+p^2},
\]

the exact boundary-to-boundary response is

\[
G_p(0,\ell)=
\frac{1}{
\left(\mu+r_0r_Lp^4/\mu\right)\sinh(\mu\ell)
+(r_0+r_L)p^2\cosh(\mu\ell)}.
\]

## Static matching theorem

At zero momentum every boundary kinetic contribution vanishes:

\[
G_0(0,\ell)=\frac{1}{m\sinh(m\ell)}.
\]

Thus locality plus unbroken gauge symmetry removes the quadratic endpoint
fiber from the static matching coefficient. Within this admitted class, the
portal sign and static threshold exchange survive without setting a boundary
coefficient to zero.

## Finite-readout hostile pair

A physical detector does not generally operate at (p=0). At
(m=\ell=p=1), the legal boundary packets ((r_0,r_L)=(0,0)) and ((1,0))
give respectively

\[
G_{00}=\frac{1}{\sqrt2\sinh\sqrt2},
\]

and

\[
G_{10}=\frac{1}{\sqrt2\sinh\sqrt2+\cosh\sqrt2}.
\]

They have identical static matching and the same response sign, but distinct
finite-energy transfer functions.

## Classification

The combined principle of locality and unbroken gauge symmetry conditionally
protects the static threshold portal. It does not yet provide the requested
physical readout. Substituting a zero-momentum Wilson coefficient for a
finite-energy detector response would change the explanandum.

A complete source explanation must derive or independently calibrate the
boundary spectral function in the same frame as the flavor measurement. It
must also fix (m\ell), the common gauge normalization, the source RG basin,
and the descent to `physical16`.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp769_static_gauge_matching_finite_readout_fiber.py

Generated result:
research/flavor/results/wp769_static_gauge_matching_finite_readout_fiber.json
