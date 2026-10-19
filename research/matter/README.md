# Matter research catalogue

Shared, machine-readable index of element/isotope observations and our construction research. The authoritative data is `element-isotope-catalog.json`, not a viewer, generated website asset, or an individual researcher's summary.

## Assembly implementation guide

For arrow assembly, proton/electron constructors, reversible cycles and assembly
measures, use [the canonical assembly guide](../../docs/arrow-assembly.md).

## Initial coverage

- Hydrogen-1 (protium) and hydrogen-2 (deuterium).
- Referenced proton, neutron, electron and positron candidate constructions.
- Separate records for observed stability, proposed geometric assembly, mass readout, binding, and a model-derived stability explanation.
- Sixteen shared mechanisms and selection audits: retained phase/energy bridging and reversible memory, common geometric assembly with retained interfaces, deuterium two-rim response and mass accounting, source-weighted matter/link feedback, collective carrier excitation modes, persistent seam occupations, native-operation energy/belt formation, source-coherent cost selection, constraint dynamics/retained energy accounting, the geometry/energy-channel bridge, core dressing, quotient charge, locking dynamics/preparation, neutral pairing, hydrogen mass accounting, and the failed direct Gram-energy alternative.
- Constituent and isotope `mechanism_ids` describe relevance and proposed applications, not completed physical identifications.

This is **not** a complete catalogue of stable isotopes. Missing entries mean unrecorded, not unstable or impossible. Stability belongs to an isotope, not an element as a whole. Unstable isotopes should be added as comparison cases when their observations and research status can be sourced.

## Files and validation

- `element-isotope-catalog.json`: shared data.
- `element-isotope-catalog.schema.json`: JSON Schema Draft 2020-12 structure.
- `check_catalog.py`: dependency-free validation of the schema subset used here, local references, unique IDs and isotope bookkeeping.

Run from the repository root:

```sh
python research/matter/check_catalog.py --self-test
```

The local validator is deliberately not a general JSON Schema implementation. It rejects unsupported schema keywords. Any new schema vocabulary must either be implemented and tested here or validated with a full Draft 2020-12 implementation. The schema file can also be used by standard JSON Schema tools.

Validation is not scientific verification. It does not rerun cited construction checkers, confirm an experimental assertion, fetch external references, or certify particle identifications. Its negative tests exercise malformed records, invalid statuses, unresolved references, escaped paths, duplicate IDs, and inconsistent isotope counts.

## Observation/model boundary

`observations` contains conventional nuclide bookkeeping and empirical stability classification. The counts are not claimed as deductions of our simplex model. `neutral_atom_electrons` specifically describes a neutral atom, not an ion or bare nucleus.

`observationally_stable` means no radioactive decay is observed in the referenced classification. It is not a mathematical proof of an infinite lifetime. `radioactive` and `unknown` are separate values. No measured masses, abundances, lifetimes, or energy scales have been copied into this initial catalogue. Add such quantities only with units, provenance and an appropriate schema extension.

The initial NNDC/NIST links are reference pointers; they were not fetched or independently audited when these entries were created. Their source descriptions preserve that limitation. Before quantitative use, obtain the specific data records and record their versions or retrieval dates. Do not invent retrieval dates.

`model` describes our proposals. A checked geometric coincidence does not upgrade binding or stability to checked. The initial isotope entries remain conjectural overall, with binding and stability explanations explicitly unconstructed.

## Research status vocabulary

| Status | Meaning |
|---|---|
| `checked` | The specific mathematical or implementation claim has cited verification. This is not physical validation. |
| `conditional` | The conclusion depends on explicit supplied assumptions or adapters. |
| `conjectural` | Proposed identification or law not established by the cited work. |
| `illustrative` | Display or explanatory convention, not a derived law. |
| `unconstructed` | Required map, operator, mechanism or readout is not supplied. |
| `refuted` | A specific stated proposal fails a cited test or argument; scope must be explicit. |

Statuses attach to statements, not merely to evocative names. A constituent may simultaneously have checked local algebra and conjectural physical identification. Exact-matching failure and a positive lowest-mode result can coexist if their different assembly rules are stated.

## References and identifiers

- Element identity: atomic number and conventional symbol.
- Isotope ID: `Symbol-MassNumber`, e.g. `H-2`.
- Constituent IDs describe candidate constructions, not established particle objects.
- Source IDs resolve through the top-level `sources` array.
- Repository sources use root-relative forward-slash paths and must exist.
- External sources use HTTPS URLs. URL presence does not assert retrieval.
- `constituent_ids` lists referenced construction types, not multiplicities; do not infer counts from that array.

Existing research notes and result artifacts remain in their owning directories. This catalogue references them rather than moving or duplicating their contents. The positron candidate is available for comparison; it is not a constituent of either initial neutral-atom entry.

## Updating the catalogue

1. Add the external observation source separately from internal model evidence.
2. State the exact scope of each claim and choose its status accordingly.
3. Preserve failed tests and additional interface/normalization costs in the cited research.
4. Keep binding and stability obligations open unless their specific mechanisms have actually been supplied and checked.
5. Add new source and constituent IDs before referencing them.
6. Run the validator and relevant scientific checkers for changed mathematical claims.
7. Review whether claims of scientific progress are warranted; schema validation cannot make that decision.

Changing an isotope's observed stability must never automatically change the model's explanatory status. Do not infer mass from support counts, charge from polarization arrows, or stability from an animation.

Schema version `1.1.0` adds shared mechanisms, constituent statuses and links, and isotope mass readouts. The prior elementary rotor/reference excitation is not automatically the later 144-transfer spinor construction. Hydrogen mass accounting is now recorded as constructed conditionally; neither its supplied binding nor its input masses are independently predicted. The neutron/proton splitting remains a specific common-energy comparison to perform.

## Common geometric assembly update

The `common-geometric-assembly` mechanism records ledger 4319, the six-hypothesis
audit, the common source-driven constructor, reversible centroid-mode motion and
the subdivision counterexample. It is linked to the proton, neutron and electron
candidates and both isotope records. Positron construction is not inferred.

Exact geometric reconstruction is checked under supplied metrics, symmetries
and seed data. Admission is evaluated on maximal supporting facets: applying the
centroid rule to arbitrary refined neutron cells admits 24 triangles instead of
18 and restores the caps. This failed generalization remains explicitly refuted.
Geometric channels do not replace the existing coefficient counts, binding or
stability obligations, nor establish physical particle identities.

## Retained phase, energy and memory update

The `retained-phase-energy-memory` mechanism records the exact proton/belt
geometric-to-native energy bridge, the occupation-necessity control, recovered
prior mechanisms and the actual belt's reversible amplitude memory construction.
It links to proton, neutron and electron candidates and both isotope records;
links indicate relevance, not completion of isotope dynamics.

The belt lift has 18 phase and 21 seam memories on a 75-dimensional complex
space. Recovery, metric-budget transfer and back-action are checked. The record
norm budget, each gate's positive spectral energy and the bare carrier constraint
Hamiltonian are distinct. No stationary storage, calibrated mass, binding or
stability status is upgraded. The electron five-cell transport remains open.
A uniform constructive witness is not rejected merely because occupation is not
uniquely forced by weaker geometric data. Earlier mass failures remain recorded.

## Interactive public pages

The **Matter** navigation menu exposes:

- `/experiments/matter-catalog.html` — the element and isotope catalogue;
- `/matter/standard-model-graph` — an interactive reference graph of Standard Model field species and interaction families.

The graph's authoritative data is `standard-model-graph.json`; `website/public/standard-model-graph.json` is its generated public copy. Validate it with `python research/matter/check_standard_model_graph.py`.

The page supports search, record-type and status filters, expandable claims and assumptions, isotope comparison, source links, related-record navigation and hash deep links. Filters use the overall record status; individual result statuses remain visible inside each record. It is self-contained so opening the generated HTML locally requires no network or JSON fetch. Website navigation and external source links require their respective sites.

Edit `catalog.template.html`, not the generated public HTML. After registry or template changes:

```sh
python research/matter/check_catalog.py --self-test
python research/matter/check_standard_model_graph.py
python research/matter/prepare_catalog_asset.py
python research/matter/prepare_catalog_asset.py --check
node research/matter/check_catalog_page.mjs
```

Generation validates the registry, embeds escaped JSON in the HTML, and copies the authoritative JSON to `website/public/experiments/matter-catalog.json`. `--check` rejects missing or stale assets. The normal website preparation/build also checks atlas freshness through `scripts/check-matter-assets.mjs` and fails with a regeneration command if the registry or template has changed. The homepage link is maintained in `docs/landing-page.md`, the source of `website/index.md`. No separate browser-maintained scientific data is introduced. The browser test checks interactions, embedded-data equality, source URL construction, deep links and mobile layout; it does not verify the scientific claims.
