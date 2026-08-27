# Full KK-tower half-twist theorem: WP753

## Question

Is WP752's radiative half-twist selector an artifact of retaining only the
first Fourier harmonic?

## Complete massless tower

Consider

\[
V(\omega)
=\frac{\kappa}{R^4}
\sum_{n=1}^{\infty}\frac{\cos(2\pi n\omega)}{n^5},
\qquad
\kappa>0.
\]

The coefficient \(\kappa\) is the signed spectral multiplicity produced by the
bulk field content. WP753 treats its positivity as an explicit source gate.

For \(0<r<1\) and \(c=\cos x\), the Abel-regularized geometric kernel is

\[
K(r,c)
=\sum_{n=1}^{\infty}r^n\cos(nx)
=\frac{rc-r^2}{1-2rc+r^2}.
\]

Its derivative is

\[
\frac{\partial K}{\partial c}
=\frac{r(1-r^2)}{(1-2rc+r^2)^2}>0.
\]

The identity

\[
\frac{1}{n^5}
=\frac{1}{\Gamma(5)}
\int_0^\infty t^4e^{-nt}\,dt
\]

expresses the complete tower as a positive integral of these kernels with
\(r=e^{-t}\). Every slice is strictly increasing in \(c\). The tower is
therefore uniquely minimized by \(c=-1\), or

\[
\omega_*=\frac12
\]

modulo the twist period.

## Exact stability and basin

The curvature at the half twist is

\[
V''(1/2)
=\frac{3\pi^2\kappa\zeta(3)}{R^4}>0.
\]

The endpoint separation is

\[
V(0)-V(1/2)
=\frac{31\kappa\zeta(5)}{16R^4}>0.
\]

Because the tower is strictly increasing in \(\cos(2\pi\omega)\), its gradient
flow points toward \(1/2\) from both sides. The basin is the twist circle
except for the unstable zero-twist point.

## Portal consequence

The full tower preserves WP752's unit-mode result:

\[
\epsilon=\frac15,
\qquad
\Delta=\frac{g_*^2}{10}>0.
\]

Thus the selected sign, dimensionless magnitude, and attractive twist basin
are not first-harmonic artifacts.

## Remaining spectral gate

The sign of \(\kappa\) is decisive. If \(\kappa<0\), the endpoint ordering
reverses and the zero twist is selected. If \(\kappa=0\), the twist is flat.
Therefore the actual anomaly-free flavor bulk spectrum must derive
\(\kappa>0\); positivity cannot be inferred from the desired portal.

The theorem covers a massless tower with one common twist charge. Bulk masses,
multiple charges, radion stabilization, and boundary-localized operators can
change the spectral measure and remain separate completion gates.

## Disposition

WP753 upgrades WP752 to a full-tower conditional selector and basin theorem.
The next bounded task is no longer to guess a potential. It is to freeze the
actual anomaly-free bulk representation packet, calculate its signed spectral
index and charged multiplicities, and then audit its complete boundary
counterterm class.

The gauge normalization, absolute threshold support, physical16 descent, and
calibrated instrument remain open.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp753_full_kk_tower_half_twist_theorem.py

Generated result:
research/flavor/results/wp753_full_kk_tower_half_twist_theorem.json
