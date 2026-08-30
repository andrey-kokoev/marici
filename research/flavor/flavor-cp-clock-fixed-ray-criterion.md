# CP-clock isolated fixed-ray criterion

Work package: WP592  
Owner: marici.Figueiredo

## Candidate source architecture

WP591 leaves the common-clock ratio \(r=\chi/y^2\) free. A physically
motivated way to remove that freedom is a complete gauge-Yukawa-scalar RG
system whose dimensionless couplings lie on an isolated fixed ray.

Let

\[
x={y^2\over g^2},
\qquad
r={\chi\over y^2},
\]

and evaluate the reduced ray flow at a nonzero gauge fixed point. The minimal
positive-coefficient normal form is

\[
\beta_x=2xg^2(Ax-B),
\]

\[
\beta_r=rg^2\left[Crx-Dx-2(Ax-B)\right],
\]

with \(A,B,C,D>0\). These coefficients must ultimately be derived from
frozen representations, interactions, and one declared scheme.

## Exact isolated ray

The simultaneous nonzero root is

\[
x_*={B\over A},
\qquad
r_*={D\over C}.
\]

The overall fixed-point magnitude cancels from \(r_*\). The Jacobian in
\((x,r)\) has determinant

\[
{2B^2Dg^4\over A}>0.
\]

Thus the ray is locally isolated in both dimensionless directions. Combined
with WP591, it predicts

\[
{s^2\over f^2}={D\over6C}.
\]

Once \(C\) and \(D\) are derived from a frozen source theory, changing this
ratio requires changing the beta-function law. That is the desired
hard-to-vary structure.

## Hostile branches

Isolation is load-bearing. If \(C=D=0\), then at \(x=x_*\) the entire
\(r\)-line is fixed: RG supplies no normalization. More subtly, the equally
well-typed coefficient packets \((C,D)=(1,1)\) and \((1,2)\) predict
\(r_*=1\) and \(2\). Choosing those coefficients after inspecting flavor
data merely moves the fit into the beta functions.

WP592 is therefore an exact acceptance architecture, not evidence that the
current flavor action realizes it. The complete anomaly-free field content
must derive all four coefficients, thresholds must preserve the ray, and the
flow must reach it without a free relevant ratio amplitude.

## Experimental criticism

After a concrete source derives \(C/D\), the direct criticism is a joint
calibrated measurement of the CP magnitude and flavor clock:

\[
{s^2\over f^2}={D\over6C}.
\]

The relation must be transported through the physical CP invariant and a
flavor-scale pole or threshold in one source model. Existing packets provide
those ingredients separately, not an independently executable joint
experiment.

This fixes only one dimensionless relation. Explaining the observed flavor
packet requires enough additional isolated ray or boundary relations to
restrict the remaining physical16 moduli.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp592_cp_clock_fixed_ray_criterion.py

The generated result is
research/flavor/results/wp592_cp_clock_fixed_ray_criterion.json.
