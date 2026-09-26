# Joint binary/ternary refinement retains six readings, not the full path

`agda/ObserverJointRefinement.agda` combines the binary comparison-action bit with the ternary cover's reading. The ternary interpreter is proved to agree with actual transport for every word and every starting value.

Checked results:

- Every Bool×Three pair is realized by a word of zero through five turns. The admissible joint image is equivalent to this six-element product, with both roundtrips.
- Equality of joint readings is exactly the conjunction of the two component equalities.
- Neither individual observer determines the other: zero/two turns refute a binary-to-ternary factor, and zero/three turns refute a ternary-to-binary factor.
- Six turns and zero turns have equal joint readings.
- A four-state cyclic cover distinguishes their actual interpreted paths. No decoder from the six joint readings can faithfully recover every path in the language.

Thus joint refinement genuinely adds information, unlike repeated access to one Boolean observer, but remains observer-relative and lossy with respect to semantic comparison witnesses. Realizing the entire product here does not assert statistical or physical independence.

The four-state cover is a concrete finite permutation, interpreted through univalence on the existing loop. Its action agrees with transport for every word and starting value. The residual distinction is consequently between actual paths, not merely code labels.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror: results/agda-joint-refinement.log. Aggregate imports include the new module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Replace the growing list of hand-chosen cyclic examples with a uniform finite-family boundary. For explicitly coded finite cyclic probes, test whether a common positive multiple of their periods yields a nontrivial path invisible to the whole family. Retain semantic path separation, not just modular arithmetic or syntax inequality. Scope any result to those probes rather than claiming incompleteness of every conceivable observer.
