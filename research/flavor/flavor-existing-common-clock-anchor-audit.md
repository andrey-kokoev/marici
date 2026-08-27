# Existing common-clock anchor audit: WP723

## Question

Does the admitted WP489 common-singlet source provide the dimensionful anchor
required by WP722 and thereby complete the asymmetric-portal explanation?

## What the common source really achieves

WP489 replaces independent flavor, electroweak, connector, and messenger
scales by one singlet clock. Its stationary relations include

\[
f_{\mathrm{phys}}^2=6y^2w^2,
\qquad
v^2=2aw^2,
\qquad
M_A^2=z_A^2w^2,
\qquad
M_B^2=z_B^2w^2.
\]

This is a genuine parallelization theorem. Once \(w\) and the dimensionless
coefficients are given, all listed masses and ratios follow coherently and a
strict threshold cone is nonempty.

## First fiber: absolute clock

The source potential contains the parameter \(w\). Under

\[
w\longmapsto sw,
\]

every physical mass square scales by \(s^2\), while all dimensionless source
ratios remain unchanged. The lift makes the vacuum follow \(w\); it supplies
no equation selecting the numerical value of \(w\).

Therefore WP489 propagates an anchor but does not derive one. It cannot remove
WP722's autonomous RG-translation fiber without treating \(w\) as a boundary
input.

## Second fiber: fixed electroweak clock

External electroweak calibration does not finish the job. WP537 exhibits the
exact family

\[
a=t^2,
\qquad
w=\frac1t,
\qquad
v^2=2,
\]

for which

\[
\frac{g_Ff_{\mathrm{phys}}}{v}=\frac{\sqrt3}{t}.
\]

The points \(t=1\) and \(t=2\) are both stationary, stable under the declared
radial test, and inside the same strict tree-level threshold cone. Their clock
ratios differ by exactly two.

WP543 proves that even after granting the fixed electroweak norm, the dual
gauge ray, and an independent \(g_F\) normalization, the authorized equality
Jacobian has the kernel tangent

\[
v_t=(2,-1,0,0).
\]

That tangent preserves every admitted equality and changes the logarithmic
flavor clock ratio by minus one.

## Selector and instrument verdict

The common singlet is a source-derived parallelizer and a conditional
relational selector. It is not:

- an absolute scale selector, because \(w\) remains a dimensionful input;
- a numerical clock-ratio selector, because the fixed-\(v\) direction \(t\)
  survives;
- a portal-magnitude selector, because neither direction is fixed by the
  admitted coefficient dynamics; or
- a physical instrument.

WP674 supplies a source-derived ideal cascade polarimeter and WP658 supplies
an exact five-record calibration architecture. Neither is an actual calibrated
common-frame experiment, and neither may be reversed into a source equation.

## Claim boundary and disposition

WP723 closes the existing flavor-anchor audit negatively. No admitted
mass-generation operation supplies the source-defined anchor required by
WP722. Reopening requires an independent dynamical equation that fixes both
the absolute singlet scale and the fixed-electroweak coefficient direction
before threshold locations or detector records are inspected.

This does not prove that no ultraviolet theory can provide such an equation.
It proves that the current common-clock constructor does not.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp723_existing_common_clock_anchor_audit.py`

Generated result: `results/wp723_existing_common_clock_anchor_audit.json`.
