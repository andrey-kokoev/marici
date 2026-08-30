# An Isolated Fixture Fixes Intrinsic Data, Not the External Portal

WP800 tests a three-punctured \(Z_3\)-twisted \(D_4\) fixture as the isolated
source suggested by WP799. Its complex-structure moduli dimension is zero, so
normalized spectra, central charges, flavor levels, and OPE coefficients can
be intrinsic SCFT data without a gauge-coupling modulus.

The flavor portal is nevertheless an interface. Coupling a normalized
dimension-two fixture operator \(\mathcal O\) to a dimension-two Standard
Model bilinear \(B_{\rm SM}\) requires

\[
\mathcal L_{\rm int}=\kappa B_{\rm SM}\mathcal O,
\qquad
\Delta_{\rm portal}=\kappa C.
\]

The fixture does not fix \(\kappa\). Intrinsic probes have Jacobian
\((1,0)\) on \((C,\kappa)\), with the entire interface direction as kernel.
Adding the portal response restores rank only after the external coupling
experiment has been admitted. The same fixture with \(\kappa=1,2\) gives
different magnitudes, and \(\kappa=\pm1\) reverses the sign.

A relevant dimension-two deformation introduces a threshold proportional to
\(\sqrt m\), with \(m\) free, and the rank-one Coulomb vacuum remains a
coordinate. Thus fixture isolation is an intrinsic-data selector, not a
portal, massive-vacuum, threshold, or physical16 selector. The required
source must contain the Standard Model operator and portal internally and
select its deformation, vacuum, matching, and instrument in the same action.

Evidence:

- research/flavor/flavor-isolated-fixture-interface-deformation-fiber.md
- research/flavor/checkers/wp800_isolated_fixture_interface_deformation_fiber.py
- research/flavor/results/wp800_isolated_fixture_interface_deformation_fiber.json
- exact checker: 11 of 11 checks pass
