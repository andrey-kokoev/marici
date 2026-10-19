# Conditional richer-control synthesis for the finite witness

Implementation/contract: `pilot_controls.py`, `contracts/pilot-control-screen.v1.json`.
Audit: `check_pilot_control_screen.py`, `results/pilot-control-screen.json`.

## What is being screened

The original pair of pi-scaled local generators is retained unchanged. Candidate extensions below are **declared additional source/control premises**, not independently verified actuators. Mathematical observer availability does not imply control availability; a symmetry is not automatically an executed interaction.

Assume independent signed continuously adjustable coefficients, common phase-framed generators, the same finite C4 carrier and ideal closed dynamics. The common nonzero pi factor does not affect the real Lie span. These assumptions supply neither physical clocks nor energy calibration.

## Exact Lie-closure comparison

| Family | Added premise | Real Lie dimension |
| --- | --- | ---: |
| Existing Q_L,Q_R | None | 2 |
| Existing pair plus Q_swap=(I-S)/2 | Factor-exchange symmetry is made an actuator | 5 |
| All six label-transposition projectors | Every transposition independently actuated | 9 |
| Existing pair plus both local Z-projector controls | Coordinate markings become actuators | 7 |
| Local-phase family plus Q_swap | Both phase controls and exchange interaction supplied | 16 |

Dimensions are computed by exact rational row reduction and commutators in the real skew-Hermitian matrix space. Closure is verified on the final bases. This is not an associative-algebra/commutant proxy for controllability.

Under the stated driftless signed continuous-control assumptions, the dimension-sixteen family has the full u(4) control algebra. This is a conditional finite mathematical control result, not a physical implementation or proof that five controls are minimal. Removing the added channels recovers the original two-dimensional subsystem.

## Why permutation enrichment alone stops short

Every involutive label permutation P fixes the uniform vector w=(1,1,1,1). The canonical projector generator Q=(I-P)/2 annihilates w. Linear combinations and commutators of their skew generators still annihilate w. Therefore these controls act only on its three-dimensional orthogonal complement: at most u(3), real dimension nine. The six transpositions attain that bound exactly.

This applies to the specified canonical permutation-projector construction, not every possible Hamiltonian logarithm compatible with finite endpoints. Adding a specially chosen logarithm or marked phase is a new premise.

## What the successful extension changes

The native flip X and coordinate marking Z yield noncommuting local generator directions **if** Z-projector controls are admitted as actuators. Both factors then supply local unitary control (including a shared global phase in this normalization), with Lie dimension seven. Local control cannot create an arbitrary coupled transformation.

Q_swap supplies an interaction: using the tensor Pauli convention, `S=(I+X tensor X+Y tensor Y+Z tensor Z)/2`, hence `Q_swap=(I-X tensor X-Y tensor Y-Z tensor Z)/4`. With the local-phase family its brackets span u(4). The checker verifies the identity and full span.

The original factor-local laws remain valid for the original local legs. The **enlarged control set** is not wholly factor-local. It would be false to import the old locality claim as a theorem about every new control.

## Repository source gates

- `commutant-separation-does-not-imply-sector-controllability.md`: projectors and sector distinguishability do not supply independent executable actions; associative products cannot be substituted for Lie controls.
- `coherent-control-does-not-descend-from-unframed-quantum-channels.md`: controlled execution requires phase-framed source lifts. Completed channel tomography cannot retrospectively supply relative control phase.
- `exchange-contact-gate-comparison.md`: the actual six exchange updates are noncommuting, and a global adapter into commuting fixed gates loses their active mismatch response. This is a potential separate source-enrichment direction, **not** an existing identification of that 22-coordinate source with this C4 pilot.

These gates prevent the conditional dimension-sixteen calculation from being called source-derived physical control. No new exchange-source adapter, apparatus calibration or common phase standard is supplied.

## Next synthesis obligation

Choose and justify an actual source enrichment. A positive bridge must specify the additional operations, independent control coefficients, phase framing, composition/record transport, locality changes and measurement pairing **before** physical claims or data fitting. An adapter from an existing noncommuting retained source is a possible route, but needs its own typed witness and preservation laws.

Alternatively retain the original restricted-control fragment and pursue a second independently constrained sector. Full u(4) capability is a declared screening target, not a requirement imposed on every physical system.

No new programme proof outcome, physical control authorization or kernel theorem is generated by this screen.
