# Barycentric presentation of one generated tetrahedron

## Question and result

Can a completed typed face become a vertex in a geometric presentation while retaining its boundary mark, type and witness?

For one generated tetrahedron, the construction succeeds. Agda attaches actual Layer 2 types and witnesses to its fifteen nonempty faces. An exact finite checker builds their barycentric subdivision, verifies oriented boundary cancellation, and checks geometric coordinates against the same source face supports.

Active SCC obligations: forward realization, route/coherencer compatibility, and readout descent. This is a bounded presentation experiment, not an additional foundational layer.

## Typed source

`agda/BarycentricWitnessPacket.agda` defines the four vertices, six edges, four triangular faces and full tetrahedron. `Packet` takes a state type, a path-producing generator and a starting state.

`CellType` gives the type attached to each face. `cell` supplies the actual term from Layer 2. In particular, the fourth face and top witness come from the checked tetrahedral completion.

Each generated presentation vertex retains:

1. its face occurrence mark;
2. its witness type;
3. its witness term.

All three have reflexive recovery proofs. A higher-dimensional witness becomes a value attached to a vertex in this new presentation. Its original type and boundary role remain recorded. The state type, generator and initial state remain fixed packet parameters; the vertex recovery theorems concern the face/type/term fields.

## Face incidence and geometry

The fifteen literal supports in the Agda source identify nonempty subsets of four occurrence labels. The checker reads this finite literal grammar and verifies the complete support inventory.

A barycentric vertex has equal positive weights on the labels in its support and zero weights elsewhere. A chain of strictly nested supports is a simplex of the subdivision.

| Dimension | Subdivision cells |
|---|---:|
| Vertices | 15 |
| Edges | 50 |
| Triangles | 60 |
| Tetrahedra | 24 |

The original tetrahedron uses the standard affine coordinates in three dimensions and has volume 1/6. Every consistently oriented small tetrahedron has volume 1/144. The total volume remains 1/6.

All 36 internal triangular interfaces occur twice with opposite orientations. The remaining 24 triangles agree with the barycentric subdivision of the original oriented boundary. The boundary cell counts are 14 vertices, 36 edges and 24 triangles.

For each ordering of the original coordinates, the checker verifies the exact inverse affine-coordinate matrix for its maximal flag. Its coefficients are successive coordinate differences multiplied by their prefix sizes. They are nonnegative precisely when those coordinates follow that order. Sorting a point's barycentric coordinates therefore selects a containing small simplex; ties give shared boundaries.

These are exact rational checks over this finite tetrahedral complex. They are not a machine-checked general subdivision theorem for arbitrary complexes.

## What the controls show

### Type labels need occurrence marks

The concrete Agda example uses Bool with an identity generator starting at false. Its four state occurrences have the same type and value, while their face marks remain different.

`no-type-decoder` proves that no decoder from types recovers every face mark. `no-typed-value-decoder` proves the same even when the type is paired with its value. The positive presentation retains the mark explicitly.

The geometric vertices thus represent marked typed cells. Their affine positions represent abstract occurrences, rather than separating the underlying Boolean values into four distinct values.

### A score need not recover its source

All twenty-four maximal flags have the same volume score, 1/144. Each flag determines that score, but the score cannot select its originating flag. The result artifact retains the full flags alongside their scores.

## View

`results/barycentric-witness-packet.svg` shows the original occurrence-labelled tetrahedron and the face-incidence graph of its subdivision. It is a two-dimensional projection of the chosen three-dimensional realization. Apparent crossings in the drawing add no incidences.

`results/barycentric-witness-packet.json` contains exact coordinates, typed source references, all maximal flags, orientations, and scores.

## Verification and scope

Fresh safe compilation of `BarycentricWitnessPacket` and the intended mark-erasure rejection passed. Execution reference: `structured_command_execution:e_25120_1791069129059194300_250`.

The source-bound checker and exact geometry controls passed. Execution reference: `structured_command_execution:e_25120_1791069302705998800_251`.

- Formal receipt: `results/barycentric-witness-packet-formal-audit.json`.
- Checker: `checkers/check_barycentric_witness_packet.py`.
- SCC model: `nima-barycentric-witness-packet`.

The geometric realization is chosen from the abstract face incidence. It does not identify arbitrary types with barycenters, reconstruct witness information from coordinates, or supply a physical geometry. It also does not yet implement automatic contraction or active-view clearing. Those require their own specified operations and recovery or readout conditions.
