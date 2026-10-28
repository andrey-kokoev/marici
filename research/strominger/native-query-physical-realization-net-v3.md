# Native query physical realization — revision 3: specification before proof

This revision corrects the readiness of the revision-2 targets. The two outputs and tetrahedral diagram are retained, but naming their boundaries is not treated as completing their definitions. No mathematical verdict changes and no new physical theorem is claimed.

## Task kinds

The net now has twenty nodes: seven previously resolved nodes and thirteen open nodes. The open nodes are explicitly partitioned into five specification gates, seven proof obligations, and one assembly objective.

### Five specification gates

1. **freeze-source-fragment.** Define objects, generators, word typing, units, composition, relations, initialization and readouts, with a native interpretation for each constructor. Explicitly distinguish group-label operations on A4 x Bool from endpoint-typed seed walks. Choose a free word language or a specified quotient before proving descent.
2. **freeze-realization-equivalence.** State the actual coordinate-change equations: preservation of generator labels, source labels, preparation, observations, carrier/pointer decomposition, eta and pairing. Declare permitted relabellings and scale normalization. Supply both an admitted and a rejected example.
3. **audit-named-physical-candidate.** Audit the existing directed-transition oscillator specialization, not an unspecified future apparatus. Each checklist item must have a sourced answer, an explicit absence, or an identified unknown.
4. **freeze-physical-model.** Freeze M only after its allowed operations/resources are completely specified. An unknown contract field blocks freezing. A KNOWN absence of the desired coupling does not: a fully specified model may be refuted by an implementation no-go. Do not make existence of the desired recorder a prerequisite for defining the model.
5. **freeze-comparison-witness-types.** Define protocol equivalence, exact or bounded approximate correctness, the four 2-cell types, composition and whiskering, and the 3-cell comparing complete pastings. Retain successor, preparation, pointer, auxiliary-return and continuation semantics.

Specification completion is not a mathematical construction theorem. It gives a stable question on which a proof or counterexample can bear.

## Bounded physical candidate audit

Named candidate: the directed-transition-probe 24-carrier/6-record oscillator specialization in:

- `../nima/seed-exchange-hypothesis-existing-instrument-realization.md`;
- `../nima/exchange-oscillator-preparation-and-measurement.md`;
- `../nima/exchange-detector-calibration-and-identifiability.md`.

It is selected for inspection because preparation, coupling and readout are already explicit, not because it is known to implement our recorder. Its 24-mode carrier is NOT silently replaced by the twelve-element A4 amplitude carrier. A group-mode adapter and Boolean-pointer interpretation must be audited, not assumed.

The fixed checklist covers domains; primitive Hamiltonians/controls; preparation/readout; auxiliaries/reset; timing/accuracy; assumption provenance; relation to A4 x Bool; and missing interfaces/obstructions. Permitted added primitives: NONE.

Valid audit outcomes are a complete candidate contract for review, a partial contract with identified unknowns, or scoped incompatibility. The audit may close even when it finds missing target capabilities. It does not authorize those capabilities, select a new interaction, or establish the physical implementation conjecture.

## Seven blocked proof obligations

- Output A: exact invariant-pairing/moduli classification after syntax and equivalence are frozen.
- Output B: compiler existence or scoped obstruction in the single frozen M, after correctness-witness types are fixed.
- Four face comparisons: S-N-R, N-P-R, S-P-R and S-N-P.
- Tetrahedral comparison of the two complete face pastings.

The component conditional classification proofs remain established at their previous scopes. Their packaging into Output A and comparison with a precise native fragment remains open. The diagram still has edges a:S->N, b:N->P, c:P->R, d:S->P, e:N->R, f:S->R, and requires

    (c whisker alpha);delta = (gamma whisker a);beta.

The witness-type gate must make that expression an actual typed proposition or higher cell before a proof is attempted. Four endpoint checks are not its substitute.

## Immediate recommendation

Only two nodes are actionable:

1. **Freeze the source fragment.**
2. **Audit the named physical candidate without enlarging it.**

Then define realization equivalence, review/freeze M, and define comparison witnesses. Only afterward attempt the corresponding proof obligations. The final same-source physical realization remains an open assembly objective.

## Versioning and validation

Contract: `contracts/native-query-physical-realization-net.v3.json`.
Revision-specific pointer: `contracts/native-query-physical-realization-net.v3.current.json`.
Audit: `results/native-query-physical-realization-net/verification.v3.json`.

Revisions 1 and 2, including their pointers and pins, are preserved. The completed WG parent is unchanged. This is owner-local registration only.

    python research/strominger/checkers/check_native_query_physical_realization_net_v3.py --freeze
    python research/strominger/checkers/check_native_query_physical_realization_net_v3.py

Validation checks explicit task kinds and prerequisites, named audit boundaries, no added primitives, unchanged historical verdicts, tetrahedral typing, actionable frontier, source proof metadata, receipts, immutable pins and corruption controls. It does not execute the proposed audit, rerun Agda, or prove the new obligations.
