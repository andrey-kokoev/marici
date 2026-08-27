# Safe-separatrix transmutation-scale fiber: WP721

## Question

Does a gauge–Yukawa theory with an interacting fixed point and a
one-dimensional safe critical surface finally select the numerical
low-energy asymmetric portal?

## Primary-source candidate

Perturbative gauge–Yukawa theories can possess an interacting ultraviolet
fixed point, calculable scalar couplings, and a one-dimensional ultraviolet
critical surface. The fixed ratios define a safe separatrix connecting the
interacting fixed point to weak infrared coupling. This is a real candidate
for the WP719 basin gate, not merely a formal beta-function ansatz.

Primary sources:

- D. F. Litim, M. Mojaza, and F. Sannino, *Vacuum stability of
  asymptotically safe gauge-Yukawa theories*,
  https://arxiv.org/abs/1501.03061.
- G. Hiller, C. Hormigos-Feliu, D. F. Litim, and T. Steudtner, *Model
  Building from Asymptotic Safety with Higgs and Flavor Portals*,
  https://arxiv.org/abs/2008.08606.

The second source contains explicit flavor-portal model building and a full
two-loop fixed-point and critical-surface analysis. It does not instantiate
the Marici real-triplet portal or its detector.

## Exact residual fiber

Along the one-dimensional separatrix, use the effective flow

\[
\frac{d\alpha}{dt}=-B\alpha^2+C\alpha^3.
\]

The interacting fixed point is \(\alpha_*=B/C\). An exact primitive is

\[
F(\alpha)=\frac{1}{B\alpha}
+\frac{C}{B^2}
\left[\log(C\alpha-B)-\log\alpha\right],
\qquad
F'(\alpha)\beta(\alpha)=1.
\]

Hence every solution obeys

\[
F(\alpha)=t-t_0.
\]

The integration constant \(t_0\) is the logarithm of an RG-invariant
transmutation scale. The fixed point and separatrix select the shape of the
trajectory, but not its translation relative to a fixed experimental energy.
Implicit differentiation gives

\[
\frac{d\alpha}{dt_0}=-\beta(\alpha).
\]

For Clebsch-fixed portal contrast

\[
\Delta=\alpha(C_n-C_m),
\]

the remaining sensitivity is

\[
\frac{d\Delta}{dt_0}
=\alpha^2(B-C\alpha)(C_n-C_m).
\]

It is nonzero away from the fixed loci whenever the desired contrast is
nonzero.

## Interpretation

The asymptotically safe source fixes:

- the ultraviolet coupling values;
- projective gauge–Yukawa–quartic ratios;
- transverse irrelevant directions; and
- a one-dimensional safe trajectory.

It does not fix where the physical theory lies along that trajectory. A
dimensional-transmutation scale remains. Measuring that scale identifies the
trajectory point but does not explain why the source selected it.

If every heavy mass is dynamically proportional to the same crossover scale,
dimensionless threshold ratios may become fixed. Even then, the portal at a
declared external energy depends on that scale. The source must either derive
the relevant deformation amplitude from another physical normalization or
admit one measured dimensionful input explicitly.

## Claim boundary and disposition

WP721 upgrades WP719 from a formal possibility to an externally established
source class, while locating its exact residual fiber. A one-dimensional safe
critical surface is not a singleton low-energy prediction. The smallest
falsifier is a translation along the same separatrix.

The next test must determine whether the flavor carrier contains a
source-defined physical scale that can normalize this relevant direction. A
detector calibration cannot serve as that source without reversing the
explanatory arrow.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp721_safe_separatrix_transmutation_scale_fiber.py`

Generated result: `results/wp721_safe_separatrix_transmutation_scale_fiber.json`.
