# A barycentric witness packet

A static guide to one finite, typed tetrahedral presentation. This is an incidence construction—not a physical particle, a metric-selection law, or a theorem identifying arbitrary types with spatial points.

![Left: four occurrence-labelled tetrahedral vertices. Right: fifteen vertices representing nonempty faces, with edges for nested face supports. Black marks vertices, blue edges, green triangular faces, and orange the full tetrahedron.](/experiments/barycentric-witness-packet.svg)

<a href="/experiments/barycentric-witness-packet.svg" target="_self">Open the full-size SVG</a>

## Reading the diagram

The left panel has four **state occurrences**, labelled 0–3. The right panel presents each nonempty face as a new marked vertex: four original vertices, six edges, four triangular faces, and the whole tetrahedron. Links connect strictly nested supports. Apparent crossings in this two-dimensional projection do not create extra incidences.

Each presentation vertex retains three fields: its **face occurrence mark**, its **witness type**, and its **actual witness term**. A triangular or tetrahedral witness can therefore be attached to a presentation vertex without erasing its original boundary role. The plotted affine coordinates illustrate the chosen realization; they do not replace the retained fields.

| Subdivision cells | Count |
|---|---:|
| Vertices | 15 |
| Edges | 50 |
| Triangles | 60 |
| Tetrahedra | 24 |

The original affine tetrahedron has volume $1/6$. Each of the 24 small tetrahedra has volume $1/144$, so total volume is preserved. These are geometric scores in the declared coordinate convention, not energies or masses.

## Two information-loss controls

- **Equal typed values, distinct occurrences:** in the concrete Boolean example, all four state occurrences have the same type and value. Those fields alone cannot recover their different occurrence marks. The positive construction retains the marks explicitly.
- **Equal scores, distinct flags:** all 24 maximal flags have volume $1/144$. The score cannot select which flag produced it. The full flags are retained alongside their scores.

## Evidence and boundary

The source reports Agda recovery proofs for face/type/term fields, an intended mark-erasure rejection, and exact rational checks for this finite subdivision, coordinates, orientations, and boundary cancellation. The SVG is a visualization of that evidence, not a fresh proof certificate or a machine-checked subdivision theorem for arbitrary complexes. Physical geometry, automatic contraction, and active-view clearing are not supplied.

[Research explanation and verification](https://github.com/andrey-kokoev/marici/blob/main/research/nima/barycentric-witness-packet.md) · [exact finite checker](https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/check_barycentric_witness_packet.py) · [retained-witness glossary](/research/theory/#witness-generator-glossary) · [construction gallery](/experiments/)
