# Isotope reference: shells, abundance and stability

**[Open the searchable reference table](/experiments/isotope-electron-shells.html)** · [Construction gallery](/experiments/) · [Element/isotope model catalogue](/experiments/matter-catalog.html)

This is a published copy of the repository's observational reference, **not a prediction of the geometric or wiring constructions**. It currently contains 96 selected isotope rows spanning 80 elements with observationally stable isotopes. It is not an exhaustive list of isotopes, abundance measurements or possible decay modes.

## Read the columns

- **Protons and neutrons** identify the selected nuclide. The electron-shell entries are the reference's neutral-atom populations, not a derived nuclear mechanism or a sequential shell-filling algorithm.
- **Natural abundance** is the percentage of an element's atoms represented by that isotope, not its percentage of all matter. The table retains representative NIST natural isotopic compositions with uncertainties omitted. Actual samples can differ; because only selected isotopes are listed, one element's rows need not sum to 100%.
- **Nuclear stability** follows the source's IAEA LiveChart / ENSDF convention: stable means no observed radioactive decay, not a proof that every theoretically possible decay is forbidden. Lead-204 is displayed with a half-life lower limit, not a measured decay lifetime.

The source's observational qualifications remain in the table itself. Publication does not refresh its upstream references, supply omitted uncertainties or independently validate every nuclear or abundance value.

## Controls and offline use

Use **Find an isotope** to filter by element or isotope name. The count reports selected rows; an unmatched search shows an explicit empty state. The table is 90vh high with its own vertical and horizontal scrolling, including on small screens. Print styling expands it for printing.

No WebGL, external script or data fetch is required. The complete standalone HTML contains the data and filtering code and can be retained for offline use, including opening the downloaded file directly. External NIST/IAEA provenance links still require network access. Use browser Back to return from the standalone table to this guide.

## Different from the construction interfaces

| Surface | Purpose | What coverage does not establish |
|---|---|---|
| This reference table | Display selected observed nuclides, representative abundance and shell/stability reference information. | A geometric construction, isotope-stability explanation or independently predicted abundance. |
| [Wiring editor](/experiments/isotope-wiring) | Edit supplied working definitions under a finite grammar. | Complete export/replay validity or physical nuclear geometry; read its [limitations](/experiments/isotope-wiring-limitations). |
| [Isotope / R-space viewer](/experiments/isotope-space) | Inspect candidate native constructions and a separate realization-space tessellation. | An established placement map between those frames or a validated binding/stability mechanism. |
| Element/isotope model catalogue | Separate observations and candidate mechanism records with their own provenance. | Exhaustive model coverage merely because this reference spans more elements. |

## Source and publication provenance

The authoritative file is [research/kitaev/isotope-electron-shells.html](https://github.com/andrey-kokoev/marici/blob/main/research/kitaev/isotope-electron-shells.html). The published HTML prepends a generation marker and its exact source SHA-256; the remaining bytes are copied unchanged. Edit the research source, not the generated public copy.

```sh
node scripts/prepare-isotope-reference.mjs
node scripts/prepare-isotope-reference.mjs --check
node --test tests/isotope-electron-shells.test.mjs
```

The normal website preparation also calls this publisher. Copy/hash, table-structure and browser checks establish publication fidelity and UI behavior, not scientific verification of the upstream dataset.

The source cites [NIST isotopic compositions](https://physics.nist.gov/PhysRefData/Compositions/index.html) and [IAEA LiveChart / ENSDF](https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html). This publication supplies no new data-retrieval date or claimed live synchronization.
