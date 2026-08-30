# Autonomous RG translation no-go: WP722

## Question

Is the transmutation-scale fiber in WP721 specific to one asymptotically safe
model, or is it unavoidable for every autonomous dimensionless flavor RG
flow?

## General theorem

Let the dimensionless source couplings obey

\[
\frac{dx}{dt}=\beta(x).
\]

If \(x(t)\) is a solution, then \(x(t+c)\) is also a solution for every
constant \(c\). Fixed points, invariant manifolds, projective rays, critical
exponents, and transverse basins can determine the orbit. They do not
determine its translation relative to a declared physical energy.

For a readout \(O(x)\), translation sensitivity is the Lie derivative

\[
\frac{dO}{dc}=\nabla O\mathbin\cdot\beta.
\]

Only an RG invariant with \(\nabla O\mathbin\cdot\beta=0\), or a fixed-point
readout, is insensitive. A running low-energy portal is not protected merely
because its projective ratios are fixed.

## Smallest exact witness

The two-coupling system

\[
\frac{dx}{dt}=x^2,
\qquad
\frac{dy}{dt}=2xy
\]

has the family

\[
x(t)=\frac{1}{c-t},
\qquad
y(t)=\frac{K}{(c-t)^2}.
\]

Every member lies on the same projective ray,

\[
\frac{y}{x^2}=K,
\]

but at the fixed external scale \(t=0\),

\[
y(0)=\frac{K}{c^2}.
\]

This is the finite-fiber lesson in RG form: even a uniquely rigidified orbit
is not a uniquely placed physical trajectory.

## Minimal repair

One source-authorized boundary condition such as

\[
x(t_{\mathrm{anchor}})=x_{\mathrm{anchor}}
\]

fixes

\[
c=t_{\mathrm{anchor}}+\frac{1}{x_{\mathrm{anchor}}}.
\]

The anchor must be dimensionful in physical units or provide an equivalent
relation to a dimensionful carrier. Candidate scales have different typing:

- the electroweak scale is experimentally calibrated but not derived by the
  admitted flavor source;
- messenger masses are flavor-source parameters but currently remain free;
- the dimensional-transmutation scale is the integration constant itself;
- the Planck scale belongs to another sector and requires a named interface
  constructor before it can normalize flavor.

Using any measured scale as a boundary datum can make the theory predictive
conditional on that datum. It does not make the numerical portal
source-selected.

## Consequence for the sought principle

The necessary source object is now typed more sharply:

1. a representation-fixed asymmetric gauge–Yukawa algebra;
2. an isolated interacting fixed point and attractive critical surface;
3. a source-derived dimensionful anchor fixing the RG translation;
4. a threshold theorem relating all mediator mass ratios to that anchor; and
5. a calibrated, representation-labelled detector map.

No currently admitted flavor object supplies item 3. This is a source-support
gap, not a missing beta-function manipulation.

## Claim boundary and disposition

WP722 proves the translation no-go for autonomous RG flows and gives the
minimal mathematical repair. It does not prove that a suitable physical
anchor exists. The next bounded search must examine declared messenger and
electroweak mass-generation operations for a source-derived anchor relation,
without treating a measured scale as flavor authority.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp722_autonomous_rg_translation_no_go.py`

Generated result: `results/wp722_autonomous_rg_translation_no_go.json`.
