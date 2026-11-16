# Isotope data: Turtle and SHACL core draft

## Question

Can the constituent inventory and directed-incidence records be represented and checked without deriving their meaning from a drawing?

## Claim boundary

- `vocabulary.ttl`: RDF/RDFS names, without OWL axioms or imports.
- `shapes.ttl`, `profiles.ttl`, `structure-shapes.ttl`, `organization-shapes.ttl`, `provenance-shapes.ttl`, `identity-shapes.ttl`, and `reader-shapes.ttl`: additive SHACL Core and SHACL-SPARQL constraints. The validator loads all seven. Concrete records are closed; referenced records must have explicit types and provenance.
- `fixtures/valid.ttl`, `fixtures/inventory.ttl`, and `fixtures/all-bindings.ttl`: synthetic partial, inventory-only, and fully bound partial records, NOT ground-derived isotope diagrams.
- `profile_tests.py`: profile, constituent-coverage, identity-separation and readout CLI integration tests.
- `STRUCTURE.md`: explicit semantics of ordered occurrences, closed boundaries, cells, and witness declarations.
- `fixtures/two-cells.ttl` and `structure_tests.py`: independently authored shared-edge/multipath fixture and composition, closure, payload, membership, loop and identity controls.
- `fixtures/complete-organization.ttl` and `organization_tests.py`: explicit complete-fixture construction, shell/frame constraints, completeness controls and loop-end tests.
- `check.py`: two-stage validator and inventory readouts, with inference disabled.
- `shape_bundle.py`: full graph-isomorphism comparison against the local authoritative shape files, including constraint contents rather than just shape names.
- `adversarial_tests.py` and `AUDIT-6.md`: reproduced false acceptances, targeted repairs, and source/import CLI integration controls.
- `scope_tests.py` and `SOURCE-SCOPE.md`: per-root replay evidence, shared-record disclosure, cross-root controls, and inspection of the saved native Ne-22 finite-reader candidate. Inspection is not constructor replay or a native Turtle import.
- `provenance.py`, `provenance_tests.py`, and `PROVENANCE.md`: local artifact resolution, pins, allowlisted operations, and source/output tampering controls.
- `native_replay.mjs`, `native_projection.py`, `native_replay_tests.py`, and `NATIVE-REPLAY.md`: fresh saved Ne-22 constructor replay and an actual typed reader-incidence import. Reader states are not spatial vertices; transitions are not colored arrows.
- `results/native-ne22-readers.ttl` and `results/native-ne22-source-replay.json`: source-backed, totally bound partial reader structure and its replay evidence.
- `results/neon-20-inventory.ttl` and `results/neon-20-source-replay.json`: actual repository-reference import and replay evidence; inventory only, not a diagram.
- `validation_tests.py`: exact rejection expectations and adversarial/readout controls. Each SHACL rejection must match the focus node, constraint component, source shape, and result path; SPARQL rejections must also match the named source constraint. A deliberately removed disjointness rule demonstrates that a different rejection at the same node cannot satisfy its test.

The schema covers constituent inventories, separate electronic states, vertices, undirected supports, directed arrows, indexed path and boundary occurrences, cells, typed non-transport witness declarations, and constituent-to-role interpretations. Ordered sequences have unique consecutive indices and explicit reciprocal ownership. Paths compose; boundaries close at their declared bases. Empty paths are identities and empty boundaries are constant loops. Repeated support/arrow occurrences retain separate identities. Arrow endpoints must match their support; supports, vertices, and interpretation targets must belong to the referencing structure. Multiple arrows may share a support without being identified. Loops are not excluded by construction.

Every root now declares exactly one `iso:profile` and `iso:bindingScope`. `InventoryProfile` permits no structural members and requires `NoBindings`. `PartialStructureProfile` declares `PartialBindings` or `TotalBindings`. `TotalBindings` requires an in-structure role binding for every declared constituent; it permits shared roles and multiple roles per constituent, without asserting a bijection. Constituents cannot themselves be vertices, edges, arrows, witnesses, paths, boundaries, cells, shells, junctions, or their occurrences. New roles participate in total binding coverage and inventory exclusions.

`CompleteStructureProfile` now requires a nonempty arrow/cell record, total constituent bindings, exactly one shell assignment for each cell and declared electron, exactly one junction frame for each vertex, and a port for each edge end. Existing payload, membership, composition and closure checks remain mandatory. It can conform on an explicitly authored complete fixture; missing components fail their specific constraints. This is combinatorial completeness, not source-derived physical correctness.

Shell levels are unique positive integers; no orbital occupancy law is inferred. Junction port indices define a declared positive cyclic order. Ports distinguish edge-end slots, including both ends of loops. Opposite ports form a local reciprocal fixed-point-free partial pairing, not a proof of Euclidean collinearity. See `STRUCTURE.md` for the precise contract.

`derive_readouts` validates the graph before computing Z, N, A, electron count, and `charge_e` (net charge in elementary-charge units). The CLI exposes this via `check.py <data.ttl> --readouts`. Electronic state omission returns null for electron count and charge; a present electronic state declares its complete inventory, including an explicitly empty inventory. These are counts of declared records, not independently verified physical measurements. RDF sets count distinct constituent IRIs: repeated triples do not encode multiplicity. Repeated occurrences require distinct IRIs. Attribution-only source references must resolve locally and are reported as such. A derived-input source additionally needs an artifact pin, supported operation, selector and output correspondence; application-stage replay must succeed. Neither status certifies source authenticity or physical truth.

SHACL class targets do not themselves reject an empty graph. The supplied validator additionally requires at least one explicitly typed `IsotopeStructure`. Every concrete record needs one explicit registered type and exactly one effective record classification; subclass aliases cannot evade application enumeration or conceal a second record role. Unrelated annotation types remain allowed. The validator rejects OWL IRIs/datatypes and altered or incomplete shape bundles, and does not load imports or run inference. Ordinary text quoting an OWL URI is not an OWL axiom. Raw evaluation of weakened shapes is available only as a private diagnostic helper, not overall conformance.

Witnesses now require a kind, Declared status and typed subjects: boundary, cell with boundary, or two paths. Cells and filling declarations must reference each other and the same boundary; comparisons require matching path endpoints. Description-only records and self-declared verified status are rejected. Well-formed declarations are not proofs of path equivalence, filling existence, or physical interpretation.

**Still unimplemented:** a complete native spatial isotope-diagram operation, region outer-boundary derivation, geometric realization, layout and physical validation. Native finite-reader incidence and its saved construction/exit replay are now supported, but do not supply the spatial diagram or a general routing engine. The reference import deliberately produces no electrons or structural topology. These remain explicit limits; no existing drawing files were modified.

## Disposition

Repair iteration 5 added source verification and actual reference imports for Hydrogen-1, Neon-20 and Calcium-46. Iteration 6 reproduced and repaired source-type enumeration bypasses, a cross-role identity collision, an inadequate shape-bundle guard, and an overbroad OWL text guard. Source verification is an application stage after SHACL, not an inference rule. Unresolvable or changed inputs, unsupported operations, missing selectors, and output mismatches reject overall validation. Fixture/operator attributions are not mislabeled as replayed derivations. Source/import CLI argument handling, successful output, attribution/replay separation, and tampered-output refusal are now integration-tested. Iteration 8 adds fresh native constructor replay and a faithful finite-reader incidence projection, with independent source-row comparisons and profile-promotion controls. Partial reader roles cannot discharge CompleteStructureProfile's spatial binding coverage. See `REPAIR.md` and `NATIVE-REPLAY.md` for exact scope and remaining external review.

RDF parsing, SHACL meta-validation, application-source checks and **212/212 tests passed** with pySHACL 0.30.1 and RDFLib 7.1.4. The operator explicitly authorized the two commands below through bash after structured-command refused the dependency invocation. Dependencies were installed in an ephemeral uv environment, not globally.

The initial run exposed a checker isolation defect: pySHACL annotated the shared shapes graph with OWL metadata, causing subsequent calls to trip the no-OWL input guard. The checker now passes a separate shapes copy to the library. The original nonempty conformance cases verify that both caller-owned graphs remain unchanged; a repeated valid fixture after all rejection cases is a regression control. Readout variants check data immutability. No data constraints were weakened. OWL inference and imports remain disabled.

Reproduction:

```sh
uv run --python 3.12 --with pyshacl==0.30.1 --with rdflib==7.1.4 python -c "import pyshacl, rdflib; print(pyshacl.__version__, rdflib.__version__)"
uv run --python 3.12 --with pyshacl==0.30.1 --with rdflib==7.1.4 python research/strominger/isotope-schema/check.py --self-test
```

The second command writes `test-results.json` with package versions, source hashes, expected and actual conformance, and per-test status. It now also runs the fixed Node.js native replay checker (tested v24.19.0) and regenerates owner-local native import/replay evidence. It also regenerates the Neon-20 reference inventory and replay receipt in `results/`. To validate another Turtle file, replace `--self-test` with its path. `--source-report` emits resolution/replay evidence; `--import-reference Neon-20` emits a checked inventory as Turtle. `--import-native-reader` emits the checked Ne-22 reader projection as Turtle. All references resolve relative to this repository root; remote fetches and arbitrary operation execution are unsupported.
