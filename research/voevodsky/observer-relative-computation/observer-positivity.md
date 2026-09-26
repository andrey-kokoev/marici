# Initial leaf: observer positivity has several inequivalent meanings

For a probe p:O→X into a family F:X→Type, the checked module distinguishes:

- Supported = O: an available access position.
- Participation = Σ(o:O) F(p(o)): a position AND actual content witness.
- Observation = Π(o:O) F(p(o)): a coherent choice over the entire probe.
- SupportedObservation = O × Observation: excludes the empty-support/vacuous-section case.
- PointwisePossible = Π(o:O) ∥F(p(o))∥: every fibre is merely inhabited, without coherent witness selection.
- Distinguishable: two observations with evidence that they are unequal.

SupportedObservation implies Participation, which implies Supported. Observation implies PointwisePossible. Converse principles fail:

1. Unit support with empty content has no Participation.
2. Unit support with Unit content has actual coherent Participation but no distinguishable observations.
3. The circle double cover has actual Participation and PointwisePossible over its whole base, but NO Observation. The new proof constructs the pointwise possibility around the loop by propositional truncation; it cannot be untruncated into a coherent selection.

The third result is stronger than merely saying a solver has not found a solution. No coherent section can exist, although every fibre is locally possible. Thus a scalar test of nonemptiness cannot replace compatibility.

## Provisional foundational vocabulary

If the intended positive observer area means actual witnessed access, Participation is the minimal candidate. If it means a filled coherent observer interface, use SupportedObservation. Both permit static content and impose no clock. Neither is proven equivalent to all conventional execution. The choice between these meanings remains an explicit interpretive decision; the leaf resolves their formal separation, not the user's ontology by fiat.

No geometric measure has been introduced: nonempty support is NOT asserted to have positive geometric area. No dimension, probability, resource budget, irreversible record or physical causality is inferred.

## Evidence

`agda/ObserverPositivity.agda` checked with safe Cubical Agda --ignore-interfaces. Reproduce: `python research/voevodsky/observer-relative-computation/check_positivity.py`.

`results/positivity.json` records the command, Agda version, resolved source/import hashes, unchanged-source check, unresolved toolchain imports and log hash. `results/agda-observer-positivity.log` retains the fresh headless output. The checker passed; it does not certify the toolchain or physical interpretation.

## Successor

Test invariance of Participation and Observation under equivalent presentations of a probe. Distinguish re-presentation from genuinely adding observational distinctions; duplicated support should not silently become an information or geometric area metric. This will constrain the nongeometric positivity proposal without prejudging a physical measure. Higher overlap coherence and direction/records remain independent open branches.
