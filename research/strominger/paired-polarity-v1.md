# Retain both polarity sheets in 12x12 fibration

**Viewer update:** the [coarsened fold](folded-fibration-v1.md) supersedes the half-face display described below. Both sheets remain retained, but each face is now whole and a selector chooses its displayed reading. The half-face rendering helper has been removed.

The existing viewer now retains the original comparison-role sheet and its opposite, rather than overwriting one in place. The declared candidate action is **P ↔ E, N fixed**, with the interface-flow direction reversed.

## Geometry and surface readings

Both sheets use exactly the same 686 primitive cells / 660 composite comparison bodies and shared-face identities. No physical cell is cloned. The original single-entry traversal remains −P → +P → −P, with 37 outward and 37 return rounds; the second sheet is not an independent growth seed.

Each charged face displays two equal-area coloured portions: the original and opposite reading. This is a display partition of one existing triangle, not a new lattice subdivision or two half-particles. N/N faces remain neutral. The deterministic partition is identical for every ordering of a shared triangle's vertices.

On the complete tiling:

| Sheet | E-labelled body readings exposed on the surface | Interior E-labelled readings |
|---|---:|---:|
| Original | 1 | 70 |
| Opposite | 107 | 30 |

These are sheet-labelled readings, not additional electron particles. The extra visible E assignments follow from the **declared** P/E role exchange; they do not independently prove that exchange is a physical law. Boundary labels continue to refer to the original sheet.

## Full five-coefficient local interface law

Let A be the native PN coefficient permutation and B the native NE permutation. Define

```
J_P = B A : P -> opposite-sheet E
J_E = (B A)^(-1) : E -> opposite-sheet P
J_N = identity on the five coefficients, with opposite interface direction.
```

Then J squared returns the complete state, including provenance and flow direction. Both outputs are retained separately.

The native comparison squares hold exactly on every coefficient basis vector:

```
B^(-1) J_P = A
J_E B = A^(-1).
```

Thus the opposite sheet reads the same N interface from the other endpoint. This is a contravariant interface comparison, not an added native E-to-N growth operation or electric charge conjugation.

The viewer's expanded 2×2×2 bank uses distinct test coefficients from this checked local P/E/N interface. Those coefficients are not advertised as a solved field on all 660 tiling bodies. Applying the role exchange to the full tiling remains the explicit candidate extension.

## Checks

```
node --test tests/paired-polarity.test.mjs
node scripts/prepare-normal-ray.mjs
node scripts/test-fibration12-process.mjs
```

Seven new test groups cover full-state involution, native interface intertwining, all eight bank readings, unchanged physical cell counts, neutral-mediated adjacency on both sheets, exact face-display coverage, and retained single-entry traversal. The combined model suite passes 21 tests; the browser test verifies both sheets in the existing process.

Files:

- `paired-polarity-model.mjs`: local coefficient action and display partition.
- `../realization-tower/fibration-coherent-process.mjs`: paired roles on the retained tiling.
- `../../examples/normal-ray/scene.js`: simultaneous face readings.
- `results/coherent-fibration-v1.json`: geometric and sheet-count receipt.

The old prescribed surface words remain unmatched. The 37+37 traversal is still not derived from the 28×2×2×2 indexing proposal.
