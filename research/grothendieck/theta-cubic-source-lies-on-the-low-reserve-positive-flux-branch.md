# Theta cubic source lies on the low-reserve positive-flux branch

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: stable bounded reconnaissance and certification target; not yet an interval proof

## Question

The monotone reserve-flux barrier has a unique threshold

\[
 C_*=1.08411717002567\ldots.
\]

Below this threshold, cubic coherence requires positive translated
Mellin-variance flux.  Above it, a controlled amount of negative flux is
allowed.  The first task is to determine which branch contains the completed
theta source.

## Direct moment evaluation

Using the fixed completed theta source and

\[
 Z_t=\int_0^\infty u^{2t}\Phi(u)\,du,
\]

the source coordinates are

\[
 x_3=\frac{Z_4Z_2}{Z_3^2},
 \qquad
 x_4=\frac{Z_5Z_3}{Z_4^2},
\]

\[
 C_3=7-5x_3,
 \qquad
 C_4=9-7x_4,
\]

and

\[
 \Omega_3^{\mathrm{glob}}=\log\frac{x_3}{x_4}.
\]

The existing dependency-free theta integrator gives

\[
 x_3\approx1.32789109040690,
 \qquad
 x_4\approx1.22676751891918,
\]

and therefore

\[
 C_3\approx0.36054454796549,
 \qquad
 C_4\approx0.41262736756572.
\]

The source lies far below the reserve threshold:

\[
 C_3-C_*\approx-0.72357262206018.
\]

Its global flux is positive:

\[
 \Omega_3^{\mathrm{glob}}
 \approx0.07920936081211.
\]

This reverses the sign of the local seam-pinned exponential model.  Global
theta completion does not merely weaken the local negative flux; it changes
its orientation.

## Cubic margin in the monotone coordinate

At the observed reserve,

\[
 b\left(\sqrt{C_3/7}\right)
 \approx-0.06709087289674.
\]

The lower-gate margin is therefore

\[
 b\left(\sqrt{C_3/7}\right)
 +\Omega_3^{\mathrm{glob}}
 \approx0.01211848791537.
\]

The equivalent secular remainder is

\[
 C_3C_4-
 \left(3\sqrt{C_3}-\sqrt{7C_4}\right)^2
 \approx0.1384003865837.
\]

Both are comfortably positive at diagnostic precision.

## Stability audit

Composite Simpson evaluations with 3,000, 6,000, 12,000, and 24,000 panels
agree to at least thirteen decimal places on (C_3\), the global flux, the
barrier margin, and the secular remainder.  This is strong reconnaissance,
not directed interval certification.

The nearby value in an earlier third-saddle Stokes scan is not treated as
evidence.  It occurs at an arbitrary scanned height and supplies no
source-derived comparison map.

## Revised proof target

The actual theta branch removes the earlier case split.  A proof may target
the two inequalities

\[
 C_3<C_*,
\]

and

\[
 \Omega_3^{\mathrm{glob}}
 \ge
 -b\left(\sqrt{C_3/7}\right).
\]

The first has a very large numerical margin.  The second has reserve about
(1.21\times10^{-2}\).  Both depend only on four fixed positive theta
moments.

The most economical certification should enclose (Z_2,Z_3,Z_4,Z_5\)
directly using source positivity, a finite quadrature interval, and a
super-exponential analytic tail bound.  No zero data, complex contour, or
operator realization is required.

## Explanatory meaning

The completed source occupies the branch where quadratic reserve alone is
too small to tolerate negative curvature flux.  Cubic coherence survives
because global modular completion reverses the local seam tendency and
produces enough positive translated variance flux.

That is the first concrete source-level phenomenon in this lane:

> The cubic gate is passed not by accumulating a large static reserve, but by
> globally reversing the direction of adjacent variance transport.

This interpretation remains provisional until the four moment enclosures are
certified.

## Falsifier

Directed enclosures falsify the claimed branch or gate if they permit either

\[
 C_3\ge C_*
\]

or

\[
 b\left(\sqrt{C_3/7}\right)
 +\Omega_3^{\mathrm{glob}}\le0.
\]

The observed margins indicate that neither boundary should be numerically
delicate.
