# Chamon gauge map and operator-valued refinement interface

## Result

Appendix B is imported from the pinned arXiv source, including its supplementary Mathematica notebook. Exact Laurent identities, the notebook's 58-step reduction, signed finite-cover Pauli lifts, and the operator-valued extension of our **existing four refinement charts** pass.

The source has six gauge-edge qubits plus two product-state ancillas per coarse cell. The target has eight Chamon vertex spins per coarse cell. These are **not** the eight geometric sectors of an octahedron. Sector records are observables in one shared physical Pauli algebra; no center spin or copied boundary spin is added.

Implementation: `checkers/chamon_laurent.py` and `checkers/check_chamon_gauge_map.py`.
Evidence: `results/chamon-gauge-map/verification.json`; exact matrices: `results/chamon-gauge-map/matrices.json`.

## Dictionary and auxiliary-data contract

Let `B(u,v,w)=(v+w,u+w,u+v)`, with primitive Gram matrix diagonal 2 and off-diagonal 1. Appendix B's macro translations are **−2B**, not unit translations of the fine lattice. Its qubit and check slots, in printed order, have fine primitive offsets

```
111, 011, 101, 001, 110, 010, 100, 000.
```

For macro cell `c` and slot `b`, the vertex is `−2B(c)+B(b)` and the octahedron center is that vertex minus `(1,1,1)`. Blocking Appendix C's column with these offsets gives Appendix B's entire 16×8 stabilizer matrix exactly, after `X→Y, Y→Z, Z→X`. Composed with our earlier native-to-C1 dictionary, the physical Pauli labels are simply the native **X, Y, Z** labels.

Gauge edge types are `(0,x),(0,y),(0,z),(y,z),(z,x),(x,y)` in macro coordinates. Their physical midpoints have fine offsets

```
−100, −010, −001, −011, −101, −110.
```

Ancillas are placed at fine offsets `−111` and `000`. On each admitted cover, these six edge midpoints and two auxiliary sites are a bijection onto the same physical vertex set as the target. The Appendix A incidence columns reproduce two six-edge tetrahedra and the twelve-edge octahedron. Edges retain their type and cell address: equal wrapped endpoints do not justify merging parallel edges.

Records must retain: source/target cell and slot, physical address, unwrapped Laurent displacement, quotient periods, Pauli phase, ancillary preparation/frame, and the sector-to-shared-site incidence. The matrix artifact retains all unwrapped translations; periodic folding is performed only when constructing a declared finite cover.

The untwisted eight-slot quotient here requires each physical rectangular period to be divisible by four. Periods two and six, and `4×6×8`, are explicitly rejected for this map rather than folded as though their deck transformations preserved the enlarged unit cell. This does not invalidate their previously checked fine-lattice stabilizers.

## Exact algebra and the notebook

Over `F2[x±1,y±1,z±1]`, the checker verifies

- `V=CWT`, `V† Ω V=Ω`, and the explicit inverse;
- invertibility of the 8×8 stabilizer-generator change `V2`;
- `V SigmaGauge = SigmaChamon V2`;
- commutation of both stabilizer presentations;
- the supplementary reduction of `V` to identity in all 58 steps.

The printed ancillary blocks are `I2`; the notebook's are zero. Both conventions work when their preparations are retained: the printed version needs **Y** ancillary stabilizers where the notebook version uses **Z**. Mixing the printed map with the notebook's Z preparation fails the stabilizer identity. This is recorded, not repaired invisibly.

The reduction also contains `rowMul(7,y)`, a sublattice translation. We retain it as a wire permutation on the finite quotient. The result is a checked **gate-and-reindexing reduction**, not a claim that all 58 steps are strictly on-site/finite-depth gates on fixed wire positions.

For signed words `i^p X^x Z^z`, the inverse reduction is replayed using standard H, S, CNOT, CZ and SWAP conventions; S inverse is S-dagger. A recorded input X correction on ancilla 7 in every coarse cell aligns the preparation with +Z. Source bulk stabilizer signs are then determined by pulling back products of positive native stabilizers through `V2`.

This last step matters: on the `8³` cover, all 32 gauge-octahedron columns acquire a minus sign relative to their canonical Hermitian binary words. On the smaller tested covers those offsets alias and the corresponding signs are positive. The receipt retains every sign. A binary polynomial column alone does not specify these Hamiltonian phases.

## Finite closure checks

| Physical cover | Coarse cells | Gauge edges + ancillas | Spins | Stabilizer rank | Logical qubits |
|---|---:|---:|---:|---:|---:|
| `4³` | 4 | 24 + 8 | 32 | 24 | 8 |
| `4×4×8` | 8 | 48 + 16 | 64 | 56 | 8 |
| `8³` | 32 | 192 + 64 | 256 | 240 | 16 |

All 352 target columns match the signed six-site native-coordinate formula. All canonical X/Z images square correctly, have the correct mutual commutators, and invert exactly. Signed dependency elimination finds no minus identity in either presentation. The 141,312 error–stabilizer pairings verify the syndrome rule `sGauge=V2^T sChamon` for every single-site X and Z error.

## Operator-valued charts

At octahedron center `c`, assign its triangular face sector `s` the actual shared-site observable

`F_s = X_(c+sx ex) Y_(c+sy ey) Z_(c+sz ez)`.

Every antipodal pair satisfies `F_s F_−s = O_c`, the six-site stabilizer. A second family with axes `Z,X,Y` tests genuinely noncommuting products: 32 of its 64 pairings with F anticommute. A vertex appearing in four sectors is still one qubit.

The checker imports **the existing chart matrices**, including the source-root-labelled antipodal chart, rather than introducing another pairing convention. It retains all sums and differences. For exact rational arithmetic it stores chart numerators `a=H_i f`; actual mass-normalized coordinates remain `a/sqrt(2)`.

The product readout is explicitly

`m_st^(i)(a,b) = (H_i^T a/2)_s (H_i^T b/2)_t`.

For a coordinatewise fine-record product, its transported chart product is `H_i[(H_i^T a/2)_s (H_i^T b/2)_s]`. It is **not** multiplication of chart entries. This construction applies to arbitrary operator-valued records; preservation follows from invertibility and the checked Clifford algebra automorphism.

On each cover the executable tests verify four complete chart round trips, all 16 existing transitions, normalized Hilbert–Schmidt norms, 256 cross-family products, and recovery of all four antipodal stabilizer products. Clifford transport commutes with the linear chart maps. Controls reject average-only records, duplicated sector spins, naive chart-entry multiplication, a corrupted matrix, mixed ancilla frames, wrong W/T order, and incompatible quotients.

## Reader fields and scope

The same sector charts already carry full neutron coefficients, fields and source contexts. Operator-valued observables now use those same matrices and may accompany those reader records; the reader coefficients, bindings and provenance are not replaced by qubits. This is a common read-only comparison interface, **not** a newly derived coupling between neutron fields and a quantum state, nor a P/N reader lift. The native grammar, solver and viewer are unchanged.

The scoped `Chamon-refinement-observables` construction is supported. Spatial/internal symmetry, defect/boundary rules, quantum-to-reader couplings and the Appendix C toric-code-layer renormalization remain separate work.

## Reproduce

```
python research/strominger/checkers/check_chamon_gauge_map.py
python research/strominger/checkers/check_toroidal_space_evaluation_net.py
```

The checker verifies the imported chart receipt's direct source fingerprints before use. Upstream source provenance is in `references/chamon-gauge-map-source/README.md`.
