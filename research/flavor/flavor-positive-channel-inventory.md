# Positive pairings read; positive expectations are unauthorized (WP66, move 7/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

Four canonical positive structures were audited on the full quotient:

| Structure | Descends | Proper image | Source-authorized operation | Instrument/readout | Ensemble |
|---|---:|---:|---:|---:|---:|
| invariant word Gram pairing | yes | no | yes | yes | survives |
| commutator score | yes | no | yes | yes | survives |
| (H_u)-spectral pinching | yes | yes | no | no | fails |
| center expectation | yes | yes | no | no | fails |

The exact word Gram matrix is positive and invariant under simultaneous
weak-basis conjugation. It and the commutator score are experimentally
reconstructible readouts, but have no proper image.

Pinching and center projection are genuine mathematical channels with proper
images. No declared flavor dynamics applies them. Their fixed loci are also
falsified respectively by one nonzero mixing entry and one nondegenerate mass
splitting.

Therefore positivity supplies neither the missing physical operation nor its
authority. Verification:
`uv run --with sympy python research/flavor/checkers/wp66_positive_channel_inventory.py`.
