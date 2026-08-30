# Fixed-electroweak selector fiber

## Question

Does WP489's positive common-source and tree-level width-closure domain select
a numerical value of the physical clock ratio once the electroweak norm is
held fixed?

## Exact source family

Retain WP489's field content, symmetries, and sum-of-squares action. Freeze

\[
y=g_F^2=1,\qquad b=32,\qquad g_P^2={1\over68},
\qquad z_A=z_B=1,
\]

and set every positive quartic used by its conservative stability test to
100. Introduce the positive source-label family

\[
a=t^2,\qquad w={1\over t}.
\]

The stationary source relations then give

\[
v^2=2aw^2=2,
\qquad
{g_Ff_{\mathrm{phys}}\over v}={\sqrt3\over t}.
\]

Thus the electroweak calibration does not remove the coefficient direction
(t).

## Exact hostile pair

The checker evaluates (t=1) and (t=2). At both points the full four-radial
gradient vanishes exactly. Sylvester's criterion applied after subtracting
one quarter of the largest vector mass squared proves that every radial mode
is above every vector half-threshold. The vector-pair and declared nonquark
pair margins are also strictly positive.

The two points nevertheless give

The first ratio is

\[
{g_Ff_{\mathrm{phys}}\over v}=\sqrt3,
\]

whereas the second is

\[
{g_Ff_{\mathrm{phys}}\over v}={\sqrt3\over2}.
\]

They share the same source grammar and fixed electroweak norm; they differ
only along an admitted continuous coefficient direction. This is the smallest
exact falsifier of numerical selection by the current source action.

## Disposition

WP489 remains a genuine relational selector for fixed source coefficients and
also rigidifies the isotropic connector presentation. It is not a numerical
selector across its admitted coefficient domain. Width closure does not repair
that failure: the hostile pair lies inside the same declared closure cone.

This is not a universal no-go. A concrete RG fixed ray, threshold matching
condition, quantization rule, or additional symmetry could fix (t). Such a
condition must be derived independently of the desired ratio. Its selected
vacuum must then be used to recompute poles, residues, all open widths, and the
WP535 instrument response rather than transporting the existing benchmark.

## Reproduction

Run:

```text
uv run --offline --with sympy python research/flavor/checkers/wp537_fixed_v_selector_fiber.py
```

The generated result is
research/flavor/results/wp537_fixed_v_selector_fiber.json.

The claim and report to marici.Nima were reviewed and admitted at graph
event ev-000000004835-e7583ca1-47c8-4876-998b-6b85ecf76819. Graph admission
records reviewed provenance; it does not certify truth.
