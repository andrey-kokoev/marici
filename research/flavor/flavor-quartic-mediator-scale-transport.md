# Stable quartic mediation repairs curvature but transports the target scale

Work package: WP622  
Owner: marici.Figueiredo

## Process and optionality snapshot

Pre-objective activation:

- excitement: 7/10;
- confidence that the branch genuinely selects the numerical target: 3/10;
- expected information gain: 8/10;
- immediate reason: this is the smallest stable non-Gaussian reopening of
  WP621;
- confound: a derived-looking center may only rename a target-valued source
  scale.

Frozen optionality space:

- one real quartic mediator;
- positive locking, quartic, and vacuum-scale parameters;
- the WP618 inner relational support component;
- one hostile vacuum-scale deformation;
- full weak-basis descent versus reference-stabilizer descent;
- ten exact checks declared.

## Bounded question

Does the smallest stable non-Gaussian mediator produce WP620's positive
curvature and calculate its target center independently?

## Frozen source grammar

Let (z=QR) be the WP619 relational coordinate and let (phi) be one real
mediator. Freeze

\[
V(z,\phi)
=
\frac K2(z-\phi)^2
+\frac\lambda4(\phi^2-v^2)^2,
\qquad K,\lambda,v>0.
\]

The first term locks the mediator to the relational coordinate. The quartic
term is the minimal stable non-Gaussian self-interaction with a nonzero
vacuum.

## Exact stationary fiber

The stationary equations imply

\[
z=\phi,
\qquad
\phi(\phi^2-v^2)=0.
\]

Hence the complete stationary fiber is

\[
(z,\phi)=(0,0),(v,v),(-v,-v).
\]

At either nonzero point the Hessian determinant is

\[
2K\lambda v^2>0,
\]

and its trace is positive. Both are strict minima. At the origin the
determinant is (-K\lambda v^2), so the origin is a saddle. The quartic
mediator therefore repairs WP621's wrong-curvature obstruction and genuinely
selects a proper relational subfamily.

## The numerical center is transported

On the WP618 inner component (s=1),

\[
z=36(1-r^2).
\]

The observed lens coordinate (r=3/5) requires

\[
v=z_0=\frac{576}{25}.
\]

Nothing in the frozen quartic grammar fixes that value. The equally stable
hostile choice (v=24) moves the selected inner lens to

\[
r=\frac{\sqrt3}{3}.
\]

More generally (v\mapsto v+\delta) moves the positive center by exactly
(delta) without changing the field content, symmetry, interaction degree,
or stability class. The branch derives nonzero selection but transports its
numerical scale.

## Quotient and reference typing

The coordinate (z=QR) uses the independently prepared stabilizer (H).
It is therefore defined only in the relational experiment whose groupoid is
the stabilizer of that reference. The operation does not descend as a scalar
on the original full weak-basis experiment. This is a new relational port,
not recovery of an absolute flavor phase or coordinate.

Within that changed groupoid and the declared inner support, the operation is
both a conditional selector and a presentation rigidifier. On the original
`physical16` quotient it has no admitted selector authority.

## Physical criticism

A same-lineage experiment would have to reconstruct:

1. both scalar normal-mode pole masses and widths;
2. their mixing angle;
3. the cubic and quartic mediator self-couplings;
4. the mediator vacuum displacement (v) in calibrated units;
5. the WP618 root-vector masses and referenced interference record.

These data distinguish the target (v=576/25) from the exact hostile value
(v=24) before fitting the flavor spectrum. No admitted detector-calibrated
apparatus currently joins those scalar and flavor records in one source
frame.

## Disposition

Stable quartic mediation is progressive relative to WP621 only in the narrow
sense that it supplies positive bounded curvature and selects a proper
relational subfamily. It does not explain the observed number: its vacuum
scale is a continuously movable source parameter. It also requires the
(H)-reference port and thus changes the physical groupoid.

The branch should remain conditional unless a separate source construction
calculates (v) without flavor input. Otherwise it is scale transport, not a
hard-to-vary flavor selector.

## Post-objective process report

- excitement: 8/10;
- confidence in the exact conditional-selection result: 10/10;
- confidence that this grammar explains the numerical target: 1/10;
- realized information gain: 9/10;
- immediate reason: the branch cleanly separates curvature repair from
  numerical explanation;
- remaining confounds: loop quantization, constrained topology, and a
  source-derived normalization may discretize (v).

Raw optionality delta:

- the minimal stable non-Gaussian branch is constructed;
- positive bounded curvature is restored;
- the stationary family reduces to two strict nonzero minima plus one saddle;
- the numerical target remains one free continuous scale;
- one exact hostile value moves the selected lens while preserving the source
  grammar;
- full weak-basis descent fails and stabilizer-groupoid descent is explicit;
- all ten declared exact checks pass;
- loop, constrained-auxiliary, and independently normalized source branches
  remain open.

These process ratings are non-evidential.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp622_quartic_mediator_scale_transport.py

The generated result is
`research/flavor/results/wp622_quartic_mediator_scale_transport.json`.
