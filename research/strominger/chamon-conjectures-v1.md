# Chamon model: construction branch

Source: Fontana and Pereira, **Boundary Modes in the Chamon Model**, arXiv:2210.09867v2, [local PDF](../../references/2210.09867v2.pdf).

Registration: [toroidal space evaluation net](contracts/toroidal-space-evaluation-net.v1.json), introduced in revision 4, updated for reuse in revision 5 and checked in revisions 6–7. The FCC benchmark and operator-refinement interface are supported; the remaining three original claims are open local compatibility tasks. The new `Chamon-polynomial-dictionary` node records the exact operator-column import. See the [benchmark report](chamon-fcc-benchmark-v1.md).

**Existing constructions found:** [reuse report](chamon-existing-constructions-v1.md). Start from the published honeycomb gauge model, polynomial Clifford map, defect-network gluing rules and public Chamon stabilizer code. The bulk models and transformations already exist; our task is their explicit correspondence with our geometry and field/reader interfaces.

## Geometric and operator dictionary

The paper places spins on the even-sum FCC lattice and stabilizers at odd-sum octahedron centers. The odd classes `100,010,001,111` become the even classes `000,110,101,011` after a shift by `111`, with the resulting label permutation retained.

For every odd center r, use

```
O_r = X_(r+ex) X_(r-ex) Y_(r+ey) Y_(r-ey) Z_(r+ez) Z_(r-ez)
H = -sum_r O_r.
```

This supplies a quantum interaction on the unsplit octahedron. Spins belong to its existing FCC vertices, not to the center or to newly introduced refinement sectors. Native constructors and the meanings of existing coefficients are unchanged.

## Conjectures and tests

| Node | Construction target | Prerequisite |
|---|---|---|
| `Chamon-FCC-benchmark` | Exact incidence-to-Pauli realization on a periodic cover; commutation, phases, rank and class products. | Checked FCC quotient |
| `Chamon-spatial-internal-symmetry` | Spatial generator actions paired with internal Clifford actions; lifted translations retain deck offsets. | Benchmark and existing pose/deck results |
| `Chamon-defect-boundary-rules` | Four class parities, dipole ribbons, tetrahedral cages and the two boundary terminations. | Benchmark |
| `Chamon-refinement-observables` | Lossless operator-valued refinement charts preserving multiplication, stabilizers and syndromes with shared qubits. | Benchmark and eight-sector interface |
| `Chamon-boundary-difference-fields` | Discrete normal derivatives, two-component boundary brackets and line-operator endpoint charges. | Boundary rules and refinement observables |

### Completed discriminator: period four

Use a `4 x 4 x 4` periodic cubic coordinate box. Its even sublattice has 32 spins and its odd sublattice 32 octahedral stabilizers. The target is binary stabilizer rank 24, no generated minus identity, and ground-space dimension `2^(32-24) = 256`. This is the paper's `2^(4 gcd(px,py,pz))` prediction for `px=py=pz=2`.

Keep the four parity classes as labels on this cover. In the period-two control, opposite vertices coincide and the paired Pauli factors cancel, making every stabilizer identity. Checking that collapse prevents a four-label description from being mistaken for the nontrivial periodic model.

Use signed binary symplectic Pauli arithmetic so generator phases, not only binary ranks, are checked.

### Symmetry and refinement

The coordinate cycle must be paired with the internal cycle `X -> Y -> Z -> X`. Proper root rotations and affine cover translations are distinct actions. A translation that has order two on parity labels can have nonzero deck displacement on the cover; the checker must retain it.

For refinement transport, scalar sum/difference invertibility is the starting tool. Operator products must also be retained. Specify shared-vertex identifications and the transported multiplication law; do not create independent copies of a spin when it belongs to several sectors. Six-site stabilizers and their phases are decisive tests of cross-sector information retention.

### Boundary construction

Section 2 supplies the five-site boundary stabilizers, broken/surviving class parities, dipole conversion and half-cage words. Those are the discrete target observations.

Equations 37-43 retain the scalar field and its normal derivative in the boundary action. Our sector centroids are `c + (sx,sy,sz)/4`, so axis-paired sector values have known separation and an exact finite-difference normalization. Equations 64-67 connect the normal-derivative boundary condition to endpoint charge.

The proposed boundary construction must explicitly specify its compact fields and symplectic bracket. The paper's antisymmetric K matrix is not our positive field metric. Any choice of existing field components used to represent these boundary fields is part of the interface contract.

## Priority decision

The benchmark and first polynomial import pass: 236 upstream support rows agree and 240 native octahedral operators match the published column. The full results and signed dependency relations are stored in `results/chamon-fcc-benchmark/verification.json`.

The [Appendix B map and operator-valued refinement interface](chamon-gauge-map-v1.md) now pass, including the supplementary reduction, signed phases and all four existing charts on three compatible covers. Spatial/internal symmetry is next; defect/boundary rules are also ready. Boundary fields await the latter. Existing reader-lift tasks retain their verdicts and dependencies.
