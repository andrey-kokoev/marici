# Source-derived instrument gate

## Question

Does any presently admitted Marici sector already supply enough physical data
to derive—not choose—a state-transforming instrument?

For outcomes (x), the target is a family of completely positive maps

[
mathcal I_x(ho)
 = operatorname{Tr}_A!left[
  (1otimes P_x),
  U(hootimessigma_A)U^dagger,
  (1otimes P_x)
 ight].
]

This formula makes the provenance burden explicit. A source must provide a
system state space, an apparatus state and pointer algebra, the interaction
(U) (or a typed equivalent), and the conditioning/readout rule. Effects or
probabilities determine only

[
p(x|ho)=operatorname{Tr}mathcal I_x(ho);
]

they do not determine (mathcal I_x(ho)).

## Bounded census

| Sector | Strongest admitted object | First missing datum |
|---|---|---|
| scattering/Bell | fixed-kinematics Born table after chosen polarization effects | detector/apparatus coupling |
| radiative gravity | covariant memory–detector pairing | outcome-bearing apparatus dynamics |
| cosmology | positive scalar period | outcome algebra and apparatus |
| flavor | weak-basis invariants and transition/fit observables | apparatus coupling and conditioning |

The exact capability checker is
`research/nima/checkers/check_source_derived_instrument_gate.py`; its result
packet is
`research/nima/results/source_derived_instrument_gate.json`.

## Result

[
oxed{
	ext{No current sector derives a physical instrument from its admitted source.}
}
]

This is not evidence against the Interaction-Surface Conjecture. It identifies
its first untested interface. The earlier projective/Lüders constructions are
valid formal completions of the effect algebras, but the physical source does
not select them.

The radiative sector is the closest linguistically because it has detectors,
but those detectors are dual test functions paired with memory. They are not
apparatus Hilbert spaces with pointer outcomes. Flavor has physical
transitions, but the admitted packet describes amplitudes and invariants, not
a detector dilation or conditional successor state. These type distinctions
prevent us from silently promoting either object to an instrument.

## Next severe test

The next packet must contain, from one physical source:

1. system and apparatus state spaces;
2. apparatus preparation;
3. a system–apparatus interaction;
4. exclusive pointer outcomes;
5. the conditioning rule.

Only then should we derive the outcome maps and test:

- complete positivity and trace preservation after summing outcomes;
- reproduction of the established readout probabilities;
- descent through the sector's internal equivalences;
- coherent sequential composition;
- agreement of coarse-graining at both record and successor-state levels.

The information-bearing prediction is now sharper: if the resulting
source-derived instrument fails descent while its probability table descends,
then public records and state updates are genuinely different layers. If both
descend and compose, the capability-indexed interaction surface gains its
first physical realization.
