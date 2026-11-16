# Tabular isotope reference

`isotope-reference.resource.json` is a **Frictionless Tabular Data Resource**:
its inline `schema` follows Table Schema and its `data` contains positional row
arrays. `schema.fields` defines the column order once. `dialect.header: false`
means the first array is a data row, not a header. The resource contains **96
isotopes, 80 elements, and 11 columns**.

This is an empirical-reference extraction from
`research/kitaev/isotope-electron-shells.html`, not an extension of the conjectural
geometry claims in `element-isotope-catalog.json`. The HTML viewer is unchanged;
it does not yet consume this resource. For now the HTML is the extraction source
and the JSON is reproducible output. Edit the source and regenerate rather than
maintaining divergent copies. A future viewer migration can explicitly transfer
source ownership to a maintained dataset.

The isotope-wiring editor (`examples/isotope-wiring/index.html`) now consumes a
generated, embedded copy for offline labels and Settings. Refresh that copy with
`node scripts/prepare-isotope-wiring-reference.mjs`; its `--check` mode verifies
freshness. `prepare-isotope-wiring-public.mjs` checks this before publication.
The separate original isotope-reference HTML remains unchanged.

## Contents and semantics

- Isotope name, proton count, neutron count.
- Neutral-atom electron populations for shells 1–6.
- Representative natural abundance, in percent of that element's atoms.
- Nuclear stability, preserving the source's exact display wording.

Rows are sorted by proton count, then neutron count, matching the rendered HTML.
The primary key is the source's full isotope name (`Lithium-6`), not `Li6`.
Source shell em dashes become JSON `null`, not imputed zeroes. Missing abundance
becomes `null` and its source stability display is `Not assessed`. JSON numeric
values preserve the supplied numerical values, not presentation trailing zeroes.

Lead-204 retains `No decay observed; t½ ≥ 1.4 × 10¹⁷ y`; it is not flattened to a
boolean or interpreted as an observed lifetime. Abundance uncertainties are absent
from the original and remain absent. Natural compositions can vary by sample,
and selected isotopes need not sum to 100 percent for an element.

The resource carries the HTML SHA-256, extraction script path, and the HTML's
NIST and IAEA/ENSDF source links. Extraction **does not fetch or independently
verify those upstream evaluations**. No retrieval date is invented. Spin/parity,
charge radii, magnetic and quadrupole moments, and binding energies are not in the
HTML and are not supplied by this extraction.

`unit` and `sourceRef` on fields and `provenance` and `notes` on the resource are
custom extension metadata; standard Frictionless validators do not assign them
scientific meaning. Standard field constraints, primary key, and data types are
machine-checkable.

## Regeneration and checks

From the repository root:

```sh
node scripts/extract-isotope-reference.mjs
node scripts/extract-isotope-reference.mjs --check
node --test tests/isotope-reference-fts.test.mjs
```

The extraction parser reads only the known table and string dictionaries; it does
not execute the HTML's JavaScript. Unsupported dictionary syntax, duplicate IDs,
orphan metadata, invalid numbers, and inconsistent mass/electron counts fail.
The Node tests check extraction and the subset of constraints used here; they are
not a general implementation of Frictionless Table Schema.

For official validation, use a Python environment with `frictionless` installed
(the initial extraction was checked with **5.21.0**):

```sh
python -c "from frictionless import Resource; report = Resource('research/matter/isotope-reference.resource.json').validate(); print(report.to_json()); raise SystemExit(0 if report.valid else 1)"
```

Specifications:
- https://specs.frictionlessdata.io/table-schema/
- https://specs.frictionlessdata.io/data-resource/
- https://specs.frictionlessdata.io/tabular-data-resource/
