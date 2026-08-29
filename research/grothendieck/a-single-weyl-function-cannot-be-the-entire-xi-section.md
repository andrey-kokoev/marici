# A Single Weyl Function Cannot Be the Entire Xi Section

## Obstruction

The minimal self-adjoint block from the preceding packet has reduced Weyl
function

$$
D(\zeta)=d-\zeta-V^*(A_0-\zeta)^{-1}V.
$$

The Evans boundary glues the two reciprocal half-line transport channels into
a full-line Dirac carrier. Its self-adjoint principal operator $A_0$ therefore
has real continuous spectrum. Write

$$
m(\zeta)=V^*(A_0-\zeta)^{-1}V.
$$

By the spectral theorem,

$$
m(\zeta)=\int_{\mathbb R}\frac{d\mu_V(t)}{t-\zeta},
$$

where $\mu_V$ is the spectral measure of the source coupling. Whenever its
absolutely continuous density $\rho_V$ is nonzero, the boundary values obey

$$
m(x+i0)-m(x-i0)=2\pi i\rho_V(x).
$$

Thus $D$ has a genuine additive jump across the real spectral seam for every
nontrivial source coupling with continuous spectral mass.

The centered completed Xi section is entire. Consequently no single
holomorphic nowhere-zero unit $u$ defined through the seam can satisfy

$$
\Xi(1/2+i\zeta)=u(\zeta)D(\zeta)
$$

on both sides of an interval carrying spectral mass. Multiplication by a
nonvanishing holomorphic unit cannot remove the resolvent jump.

This falsifies the minimal identity proposed in the preceding packet. It does
not falsify the self-adjoint carrier or the Evans boundary. It changes the
typing of the determinant bridge.

## Corrected bridge

The two half-plane Weyl functions $D_+$ and $D_-$ are legitimate local
objects. The entire section must arise only after reciprocal sewing cancels
their cut data. A plausible form is a relative perturbation determinant or a
boundary-triple characteristic section whose logarithmic derivatives recover
the two Weyl branches:

$$
\partial_\zeta\log\Delta_\pm(\zeta)
=\text{source-fixed expression in }D_\pm(\zeta).
$$

The global object is then a descent datum

$$
(\Delta_+,\Delta_-,g_{+-}),
$$

not one meromorphic function multiplied by a unit. The reciprocal transition
$g_{+-}$ must absorb the spectral jump and retain the primitive, square,
seam, and archimedean boundary currents. Xi can be entire only after this
two-chart descent.

This matches the earlier geometric intuition: the two open half-planes are
shadows of two genuine sectors pretending to be one scalar analytic plane.
The critical line is their common continuous-spectrum boundary. Asking one
Weyl chart to equal Xi globally erases exactly the comparison cell that the
programme has repeatedly found necessary.

## Stronger analytic consequence

For $\operatorname{Im}\zeta>0$, the resolvent convention above gives
$\operatorname{Im}m(\zeta)>0$. Hence

$$
\operatorname{Im}D(\zeta)
=-\operatorname{Im}\zeta-\operatorname{Im}m(\zeta)<0.
$$

The local Weyl condition is automatically zero-free in the upper half-plane,
with the conjugate statement below. This is the desired self-adjoint
orientation, but it lives separately on the two resolvent charts. The only
remaining question is whether the source-derived sewn determinant has
exactly the Xi divisor and no additional transition zeros.

## Next falsifier

Construct finite-volume approximants, where $A_{0,L}$ has discrete real
spectrum and $D_L$ is meromorphic. Compute the canonical reciprocal product
or ratio of the two perturbation determinants before taking $L\to\infty$.
The route fails if:

- spectral poles do not cancel under source-authorized reciprocal sewing;
- the transition factor introduces divisor-bearing zeros;
- the sewn finite determinant differs from the completed theta approximant by
  more than a fixed nowhere-zero normalization;
- cancellation occurs only after discarding primitive, square, or seam data;
- the finite-volume sewing has no completion-stable limit.

The live theorem is therefore a two-chart determinant descent theorem, not a
single Weyl-function identity.
