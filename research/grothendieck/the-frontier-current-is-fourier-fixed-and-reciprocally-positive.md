# The Frontier Current Is Fourier-Fixed and Reciprocally Positive

## Fourier convention

Use

\[
\widehat f(\xi)
=
\int_{\mathbb R}
f(\rho)e^{-2\pi i\rho\xi}\,d\rho.
\]

Let

\[
F(\rho)
=
\rho^2(2\pi\rho^2-3)e^{-\pi\rho^2}.
\]

## Exact Fourier fixed point

The Gaussian is Fourier-fixed. Applying the differentiation rules for
multiplication by \(\rho\) gives

\[
\widehat{\rho^3e^{-\pi\rho^2}}(\xi)
=
\frac{i\xi(2\pi\xi^2-3)}{2\pi}
e^{-\pi\xi^2}.
\]

Since

\[
F(\rho)
=
-\frac{d}{d\rho}
\left(
\rho^3e^{-\pi\rho^2}
\right),
\]

Fourier transformation yields

\[
\widehat F(\xi)
=
-2\pi i\xi
\widehat{\rho^3e^{-\pi\rho^2}}(\xi)
=
F(\xi).
\]

Thus the exact boundary-current profile is itself Fourier-fixed.

## Poisson sewing

For \(h>0\), Poisson summation gives

\[
h\sum_{n\in\mathbb Z}F(nh)
=
\sum_{k\in\mathbb Z}F(k/h).
\]

The profile is even and \(F(0)=0\), so

\[
h\sum_{n\geq1}F(nh)
=
\sum_{k\geq1}F(k/h).
\]

With \(h=e^{-u}\), the reflected theta source is

\[
\Phi(-u)
=
2\pi h^{1/2}
\sum_{n\geq1}F(nh).
\]

Therefore

\[
\Phi(-u)
=
2\pi h^{-1/2}
\sum_{k\geq1}F(k/h)
=
\Phi(u).
\]

This derives reciprocal evenness directly from the Fourier-fixed current.

## Reciprocal positivity

The profile has one positive zero:

\[
\rho_*=\sqrt{\frac3{2\pi}}<1.
\]

It is positive for \(\rho>\rho_*\). On the positive chamber \(u\geq0\), one
has \(0<h\leq1\), and hence

\[
\frac{k}{h}\geq1>\rho_*
\qquad
(k\geq1).
\]

Every term in the reciprocal Poisson chart is strictly positive. Consequently,

\[
\Phi(u)=\Phi(-u)>0
\qquad
(u\geq0).
\]

The primal fine-mesh chart contains both signs. The reciprocal coarse chart
lands wholly inside the positive lobe.

## Explanation

Completed theta positivity and reciprocal symmetry arise from one rigid
mechanism:

1. the moving frontier is an exact continuum boundary current;
2. its profile is Fourier-fixed;
3. lattice sampling leaves a discrete anomaly;
4. Poisson transport moves that anomaly to the reciprocal lattice;
5. the reciprocal lattice misses the negative lobe on the positive chamber.

This is stronger than source positivity alone. It explains why the particular
integer lattice and the particular Hermite-Gaussian current cooperate.

## Scope boundary

This closes positivity and evenness of the theta source. It does not prove that
the Mellin or Fourier transform of that positive source has only real zeros.
The RH frontier is now cleanly downstream: determine whether the same
Fourier-fixed current controls the oscillatory two-copy comparison.

## Falsifier

Any of the following rejects the mechanism:

- \(\widehat F\ne F\);
- failure of the Poisson identity;
- a reciprocal sample \(k/h\) entering the negative lobe for \(u\geq0\).

The displayed formulas exclude all three.
