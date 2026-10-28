# Constructor-induced occurrence and source-witness agreement

## Result

A generic recursion extracts an occurrence map and its explicit leaf-relation witness from a P/E constructor correspondence. It traverses every prerequisite family, including unselected E branches.

For all24 actual four-facet correspondences, fresh safe Cubical checking proves:

- agreement with the earlier full occurrence involution for arbitrary occurrences;
- equality of the resulting occurrence functions;
- dependent path agreement of the source-relation witnesses along the occurrence agreement;
- inverse laws and equivalences for the constructor-induced occurrence maps.

Thus the constructor-level and occurrence-level certificates no longer merely agree on canonical examples: their full maps and leaf-transport witnesses are connected by kernel-checked laws.

The witness comparison is a dependent path, preserving the target source index while comparing its transport evidence. No generic proof-irrelevance assumption is used for this relation.

A hostile claim collapsing an unselected E prerequisite onto the selected branch is rejected.

## Boundary

The round-trip statements concern induced occurrence maps. They do not assert equality of constructor-correspondence proofs or whole native derivations. The native comparison remains owner-local and the complementary contexts remain independently admitted. Parent descent remains open.

## Next action

Consolidate the five pending results since revision26: common-edge triple naturality, actual different-edge transport, the generic constructor comparison, its actual four-facet instantiation, and the constructor/occurrence agreement. Preserve the distinction between the proved comparison and the still-missing source-generating transition.

A further nonredundant audit can compare the admission-policy transport induced by these constructor maps with the previously checked policy-transfer functions, rather than assuming that function agreement automatically identifies every realization proof.

## Verification

- `agda/RamseyPEComparisonOccurrences.agda`
- `fixtures/ramsey-constructor-occurrence-agreement/RamseyConstructorOccurrenceAgreement.agda`
- `checkers/check_ramsey_constructor_occurrence_agreement.py`
- `results/ramsey-constructor-occurrence-agreement-v1.json`
- passing freeze `scc-freezes/ramsey-constructor-occurrence-agreement-v1.9679aaaedb496551.json`

An initial module-name collision with Prelude's `Lift` was corrected before the passing fresh check. Owning signatures, net revision26, external admission revision19 and scientific verdicts remain unchanged. No graph event or Git checkpoint occurred.
