# Proton, hydrogen and helium: residuals and three counting-rule tests

## Question

Can the 1836 tetrahedral count and a common composition rule explain the mass pattern of a bare proton, hydrogen-1 and helium-4?

## Frozen test

Use the rounded reference inputs already stated in the conversation. These inputs were not independently precision-audited here. Separate constituent mass excess, nuclear binding and electronic binding. Calibrate three simple electronic rules on hydrogen only; use helium as the discriminator. No WG-derived environment operator is supplied in this calculation.

The baseline 1836(Z+N)+n_e gives 1836, 1837 and 7346. Proton and neutron excesses over 1836 are respectively 0.152673 and 2.683662 electron units. Thus the helium constituent excess is 5.672670 before binding. Its supplied nuclear binding removes approximately 55.3733 electron units; electronic binding removes approximately 0.000154609. Hydrogen electronic binding removes approximately 0.0000266114 electron units.

The calculated helium mass is 7296.29921 electron units using these rounded binding inputs. This is constituent bookkeeping, not a prediction or a replacement of the previously quoted isotope mass. The roughly 0.00018 difference from that mass is consistent with the deliberately coarse 28.2957 MeV nuclear-binding input; do not use that discrepancy as a new structural correction.

## Held-out electronic test

With hydrogen binding fixed to 13.5984 eV:

| Rule | Predicted helium electronic binding, eV | Prediction minus reference, eV |
|---|---:|---:|
| Per electron | 27.1968 | -51.8084 |
| Per proton-electron pair | 54.3936 | -24.6116 |
| Z squared per electron | 108.7872 | +29.7820 |

The reference is 79.0052 eV. All three counting rules fail to reproduce it. The independent hydrogenic rule has the sign of residual expected when electron-electron repulsion/screening is omitted: the required interaction raises the energy, reducing binding by 29.7820 eV in this calibrated model. That difference is inferred from the reference, not derived from WG. An effective-charge fit is likewise descriptive, not a held-out prediction.

## Disposition

A uniform unit increment or a single per-pair binding coefficient does not survive this test. The proton's 0.152673 excess is already present before adding an electron. The next substantive object would be a coupled electronic operator derived from the generating structure, with charge dependence and inter-electron interaction retained. Nuclear binding requires its own source calculation. No universal quartic kernel is identified by these three systems.

## Verification

`python research/nima/checkers/check_proton_hydrogen_helium_structure.py` passed through structured-command execution `structured_command_execution:e_32876_1791215819702799900_7`.

Exact rational arithmetic conditional on the rounded inputs verifies mass decomposition and rejects a reversed binding sign. Results: `research/nima/results/proton-hydrogen-helium-structure.json`. No publication or commit is claimed.
