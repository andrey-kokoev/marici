# Isolated Fixture Interface and Deformation Fiber

## Question

Can an isolated \(Z_3\)-twisted \(D_4\) fixture remove WP799's free
transmutation scale and thereby fix the complete asymmetric flavor portal?

## What isolation fixes

A class-S fixture is a sphere with three punctures. Its complex-structure
moduli dimension is

\[
3g-3+n=0
\qquad (g=0,\ n=3).
\]

Unlike a four-punctured sphere, which has one gluing modulus, the fixture has
no intrinsic gauge-coupling coordinate of this type. Once operators are
normalized, its spectrum, central charges, flavor levels, and OPE data are
intrinsic properties of the SCFT. This is a genuine way to avoid WP799's
weak-coupling \(\Lambda\) fiber.

## The external-interface obstruction

The required flavor portal is not among those intrinsic data. Let
\(\mathcal O\) be a normalized dimension-two fixture operator and \(B_{\rm SM}\)
a dimension-two Standard Model flavor bilinear. Coupling the sectors requires

\[
\mathcal L_{\rm int}=\kappa\,B_{\rm SM}\mathcal O.
\]

The fixture may fix an intrinsic normalized coefficient \(C\), but the
physical portal is

\[
\Delta_{\rm portal}=\kappa C.
\]

Fixture isolation does not fix \(\kappa\). The same isolated theory with
\(\kappa=1\) and \(\kappa=2\) has identical intrinsic spectra and correlators
but different portal magnitudes. The pair \(\kappa=\pm1\) reverses the
relative portal sign without changing the fixture.

This is not a hidden conformal modulus of the fixture. It is a new interface
operation between two source objects. Treating an intrinsic OPE coefficient
as the complete portal would omit that arrow.

## Contextual faithfulness

On the coordinate packet \((C,\kappa)\), the intrinsic fixture probe has
Jacobian

\[
J_{\rm fixture}=\begin{pmatrix}1&0\end{pmatrix}.
\]

Its kernel is exactly the external-interface direction. Adding the portal
response \(\kappa C\) makes the two-row Jacobian rank two at nonzero \(C\), but
that complementary probe exists only after the external coupling experiment
has been added. It cannot retroactively give the fixture authority to select
\(\kappa\).

## Vacuum, threshold, and instrument gates

The conformal point has no massive threshold hierarchy. A dimension-two
relevant deformation \(m\mathcal O\) introduces a scale proportional to
\(\sqrt m\). The exact values \(m=1\) and \(m=4\) give different thresholds
while leaving the isolated UV fixture unchanged. A rank-one fixture also has
a Coulomb vacuum coordinate; isolation of the theory does not select a point
on its vacuum moduli space.

Intrinsic SCFT correlators are genuine physical instruments for intrinsic
SCFT data. They are not calibrated probes of the faithful physical16 flavor
quotient. The cited \(N=2\) source supplies neither a chiral Standard Model
embedding nor the detector map required for the ordered real-triplet portal.

## Classification

- Fixture isolation: intrinsic dimensionless-data selector.
- Triality twist: orbit-three rigidifier.
- External portal coupling: unselected interface coordinate.
- Relevant deformation and Coulomb expectation value: unselected threshold
  and vacuum coordinates.
- Fixture correlators: intrinsic instruments, not physical16 instruments.

The isolated fixture improves magnitude typing but still does not explain the
flavor portal.

## Smallest exact falsifier

Keep the entire isolated fixture fixed and compare \(\kappa=1\) with
\(\kappa=2\). Every intrinsic fixture probe agrees, while the portal differs
by a factor of two. The sign pair \(\kappa=\pm1\) is the corresponding
orientation falsifier.

## Successor

The Standard Model flavor operator and asymmetric portal must be internal
parts of one isolated source rather than externally glued sectors. That
single source must have no marginal portal direction, select its relevant
deformation and vacuum, produce a massive threshold completion, and expose a
calibrated physical16 response. Merely finding another isolated SCFT with
attractive OPE coefficients is insufficient.

Verification:

- checker:
  research/flavor/checkers/wp800_isolated_fixture_interface_deformation_fiber.py
- generated result:
  research/flavor/results/wp800_isolated_fixture_interface_deformation_fiber.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp800_isolated_fixture_interface_deformation_fiber.py
- \(Z_3\)-twisted \(D_4\) fixtures:
  [Chacaltana, Distler, and Trimm](https://arxiv.org/abs/1601.02077)
- class-S source construction:
  [Gaiotto](https://arxiv.org/abs/0904.2715)
- categorical fixtures and cylinders:
  [Cecotti](https://arxiv.org/abs/1203.6734)
