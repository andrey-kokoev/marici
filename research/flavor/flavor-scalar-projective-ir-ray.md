# Scalar projective infrared ray: WP704

## Source-derived reduction

Restrict the complete WP662 scalar flow to its invariant symmetric subspace

\[
\lambda_n=\lambda_m=a,
\qquad
\lambda_c=0,
\qquad
\lambda_x=b>0.
\]

The exact one-loop equations, up to the common positive normalization already
declared in WP662, are

\[
\dot a=176a^2+12b^2,
\qquad
\dot b=160ab+32b^2.
\]

For the projective ratio (r=a/b),

\[
\dot r=4b(2r-1)(2r-3).
\]

Thus the flow itself derives two invariant rays,

\[
r=\frac12,
\qquad
r=\frac32.
\]

## Stability removes one ray

The WP662 radial determinant is

\[
D=4a^2-b^2=b^2(4r^2-1).
\]

For positive couplings, strict radial stability requires (r>1/2). The lower
projective ray is exactly the stability boundary, while (r=3/2) lies in the
stable interior and in the WP700 open-decay corridor.

Introduce the monotone projective clock (s) by

\[
\frac{ds}{dt}=4b.
\]

Then

\[
\frac{dr}{ds}=(2r-1)(2r-3),
\qquad
\frac{2r-3}{2r-1}=C e^{4s}.
\]

On a perturbative trajectory extending toward the Gaussian infrared limit,
(s\to-\infty). Every strictly stable initial ratio therefore approaches
(r=3/2). This is a source-derived projective infrared attractor within the
closed scalar truncation.

## Hostile typing gates

The result is not yet a finite-scale flavor selector.

- At every finite (s), the integration constant (C) remains recoverable;
  the projective flow is invertible and does not collapse the stable domain.
- The limiting point has (a,b\to0). It selects a tangent ratio at the
  Gaussian infrared point, not a nonzero portal magnitude.
- Gauge, Yukawa, messenger, and threshold contributions were excluded from
  WP662 and can move or destroy the ray.
- A physical matching scale is finite. Threshold decoupling interrupts the
  ideal scalar flow before its asymptotic limit unless separately proved.
- RG evolution has no standalone experimental instrument; scale-resolved
  measurements only read boundary values.

## Disposition

WP704 identifies a genuine candidate selector mechanism rather than another
fitted scalar coincidence: stability plus the source-derived scalar beta field
chooses the unique stable infrared projective ray (r=3/2). Its present status
is an asymptotic selector on a scalar-truncation tangent cone and a finite-scale
transport rigidifier. Authority on `physical16` requires the full completed
beta field, a threshold-safe basin, a finite matching prediction with an error
bound, and an experimentally typed portal readout.

The smallest exact falsifier of finite-scale selection is any two distinct
constants (C_1\ne C_2): both lie in the stable basin and remain distinct at
every finite projective time.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp704_scalar_projective_ir_ray.py

Generated result: results/wp704_scalar_projective_ir_ray.json.
