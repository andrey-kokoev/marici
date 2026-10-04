# Specialization and finite witnessed execution

`agda/WitnessedHistories.agda` defines a length-indexed `History`: every successor stores the next state, the full relation witness, and the remaining history. Nothing is truncated. `run` iterates a witnessed generator for any natural-number length.

For two compatible domain specializations, `history-iso` gives inverse flatten/unflatten maps on all histories, not just generated ones. `run-commutes` proves by induction that flattening the nested generator's entire run equals iterating the independently defined `direct-generator` from `NestedWitnessSpecialization`. This is full dependent-history equality, including all admission certificates and relation witnesses. A certified-selection fixture checks the statement for every finite length.

`HistoryPentagon` lifts each of the five explicit edges of `FourDomainPentagon` recursively to histories. `history-pentagon` equates the three-edge and two-edge routes on every witnessed history; `generated-history-pentagon` specializes this to runs. A four-domain certified-selection fixture instantiates the latter with the full fourth compiled relation and generator. The extra admission layers are unit-valued structural tests, not new independent domain operations.

Scope: finite histories and dependent-pair presentation coherence for a fixed compatible chain. This does not define a binary algebra on arbitrary domain-composition objects, compare independently compiled four-domain specifications, establish infinite/coinductive trace equivalence, or prove termination of application-level computation. Each supplied WG is already a total step function.

Verification: fresh Agda `--ignore-interfaces --safe --cubical --guardedness --transliterate`, using research/nima/agda, the native-application and application-extension adapters, and Cubical 0.9, passed after the fixture was added. The pre-existing TypedGeneratorLayers import warning remains. Log: `.ai/tmp/histories-check.log`.
