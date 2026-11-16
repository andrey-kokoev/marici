# Iteration 6: hostile regression audit

This is a self-authored implementation audit, not independent physical/source verification or an independent reviewer signoff.

## Observed before repair

The first expanded suite passed 174/179 cases. Its five failed expectations are preserved in `results/audit-iteration6-before.json`, with source digests:

1. A Source replaced by an RDFS subclass instance passed SHACL but disappeared from the application's explicit Source enumeration. A nonexistent reference was accepted.
2. Calling the source verifier directly on that graph likewise silently skipped the referenced source.
3. A vertex simultaneously typed as an empty ElectronicState was accepted. The previous disjointness checks did not cover all concrete record types.
4. Keeping shape names while deleting junction/port completeness constraints let a missing-junction complete record pass. Checking for NodeShape declarations was not a complete-bundle check.
5. A plain description beginning with an OWL URI was rejected as though the quoted text were an asserted ontology term.

## Repairs and controls

- `identity-shapes.ttl` requires exactly one explicit registered record type and exactly one effective record classification. Inherited class membership alone is insufficient. An inherited second record role also fails; unrelated annotation types remain allowed. A registry-consistency test covers every other concrete class target.
- `verify_sources` independently rejects referenced sources lacking an explicit Source type. This helper is not a substitute for full SHACL validation.
- `shape_bundle.py` compares the full supplied RDF graph with the local authoritative files by graph isomorphism. Fresh blank-node labels are accepted. Changed constraints and mutation of an already accepted graph are rejected. Caches use immutable triple snapshots and fresh authoritative file bytes, not mutable graph identity.
- Private `_evaluate_shapes` exists only for diagnostic testing, including the existing wrong-reason falsifier. It does not claim production conformance, artifact resolution, or schema authority.
- The OWL guard distinguishes URI terms/datatype IRIs from ordinary text. Actual OWL vocabulary and OWL datatypes remain rejected.
- The actual CLI parser/output branches exercise reference import, missing selectors, source reports, attribution versus replay, conflicting options, and tampered output.
- A subclass-only extra root cannot silently disappear from inventory readouts.

Fresh full-suite result: **186/186 passing**, including all 167 previous controls and 19 hostile/integration controls. `test-results.json` records the current run; the pre-repair audit file is historical, not current conformance evidence.

## Remaining boundary

The replay operation still imports only the reference nuclear inventory. No native isotope-topology operation, physical authenticity, or proof of witness declarations has been established. Existing drawings and native source files were not changed. Remaining work is to inspect actual structural source candidates, determine whether a faithful native adapter is possible, and audit cross-record ownership/output scope. Do not substitute the green inventory suite for that missing evidence.
