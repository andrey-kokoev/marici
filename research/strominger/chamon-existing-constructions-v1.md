# Existing constructions to reuse for the Chamon branch

## Result

The search through **ask.sciencemadereadable.com** found explicit constructions, not merely related geometry. The strongest result is a tetrahedral-octahedral gauge model with a Clifford map to Chamon, followed by a topological defect-network construction on the same type of honeycomb. Public stabilizer/syndrome code is also available.

The engineering task is to import these constructions through an explicit coordinate, operator and retained-data dictionary. Our local compatibility checks remain the tests of that dictionary.

## 1. Gauge model, Clifford equivalence and coarse graining

Wilbur Shirley, Xu Liu and Arpit Dua, **Emergent fermionic gauge theory and foliated fracton order in the Chamon model**.

- Published: https://doi.org/10.1103/PhysRevB.107.035136
- Full text inspected: https://arxiv.org/abs/2206.12791v1
- Local: `references/2206.12791v1.pdf`.

### Explicit constructions read

Section III.A and Fig. 2 use a tetrahedral-octahedral honeycomb, expressed in lattice coordinates by slicing cubes with planes normal to `(1,1,1)`. The matter model in this version assigns fermionic orbitals to tetrahedra and qubits to octahedra. An edge coupling acts on the four adjacent cells: two tetrahedra and two octahedra. Gauging introduces one gauge qubit per edge and cell Gauss constraints.

Section III.D maps the resulting gauge model to Chamon. Six edge qubits per unit cell are augmented by two ancillary qubits to match eight Chamon qubits. The construction specifies images of Pauli generators preserving their algebra. It identifies ground spaces, not term-by-term equality of the Hamiltonians.

Appendix B gives Laurent-polynomial matrices, including a symplectic map V satisfying `V^dagger Omega V = Omega` and the stabilizer-map intertwining relation (B4). The paper points to a supplementary Mathematica file demonstrating finite-depth Clifford decomposition. The supplementary file has now been recovered from the pinned arXiv source archive. The [local import](chamon-gauge-map-v1.md) checks all 58 reduction steps and retains its wire translation; it does not silently call that translation an on-site gate.

Section IV and Appendix C give entanglement renormalization. For odd scale factors, the retained state includes a coarse Chamon model and separated two-dimensional topological layers. Explicit circuits for factors three and five are described as provided in the Mathematica supplement; the extracted layers are stacks of toric codes in four directions.

### Reuse

- Import the polynomial operator map rather than derive a new Pauli intertwiner from scratch.
- Carry the lattice-coordinate change and metric explicitly.
- Account for the two ancillas and extracted layers in the retained-data contract.
- Compare our refinement presentation with this exact operator-preserving construction. Eight qubits per unit cell and eight geometric sectors are distinct objects requiring an explicit dictionary.

## 2. Topological defect network on the honeycomb

Zijian Song, Arpit Dua, Wilbur E. Shirley and Dominic J. Williamson, **Topological Defect Network Representations of Fracton Stabilizer Codes**.

- https://doi.org/10.1103/PRXQuantum.4.010304
- Full text: https://harvest.aps.org/v2/journals/articles/10.1103/PRXQuantum.4.010304/fulltext
- Saved as `references/PRXQuantum.4.010304.pdf`.

Section VI.C, pp. 26-27 and Fig. 7 construct the Chamon defect network using tetrahedral-octahedral strata. The construction specifies:

- bosonic and fermionic three-dimensional toric-code regions;
- interface conditions with semion/antisemion attachments to terminating flux strings;
- four-charge condensation at edges;
- the relation of a honeycomb unit cell to a `2 x 2 x 2` Chamon unit cell.

The method is ungauging, fine graining and regauging. Its stated general guarantee applies to topological CSS codes; the Chamon non-CSS construction is treated explicitly in Section VI.C. Its cell matter assignment is its own convention and must not be silently identified with the earlier preprint's matter assignment.

**Reuse:** this provides explicit quantum gluing rules for tetrahedra, octahedra and their shared interfaces. The next operation is a cell/edge/face dictionary into our maintained geometry, not inventing gluing rules from the A4 action alone.

## 3. Public Chamon stabilizer and syndrome implementation

Zohar Schwartzman-Nowik and Benjamin J. Brown, **Generalizing the matching decoder for the Chamon code**, Quantum 9, 1775 (2025).

- https://doi.org/10.22331/q-2025-06-18-1775
- https://arxiv.org/abs/2411.03443v2
- Code: https://github.com/zoharno/chamon_decoder

The publisher page links the repository as reference 49. The README, repository listing and these source files were inspected:

- `chamdec_stabs_syndromes.py`: `create_chamon_stabs(px,py,pz)` constructs a binary X/Z support matrix; syndrome routines are also supplied. Inspected Git blob: `194d9ad3b5b2a0ecc1a64cc99b044392024bcb6d`.
- `chamdec_conversions.py`: index-to-coordinate and neighbor maps. Inspected Git blob: `840909bdf1c9b1e4f761c01a551fc6e3e6a81177`.
- README: simulator options for matching, greedy preprocessing, belief-propagation preprocessing and BP-OSD.

For `(px,py,pz)=(2,2,2)`, the construction has the 32-spin/32-check size of our completed benchmark. Selected pinned functions were executed through a minimal zero-array adapter: all 236 compared rows agree across three noncollapsed covers. The local signed test also retains phases and repeated factors, including the period-two collapse. No full decoder installation or decoder performance test is claimed.

## 4. Baseline theorem and boundary construction

Bravyi, Leemhuis and Terhal, **Topological order in an exactly solvable 3D spin model**:
https://doi.org/10.1016/j.aop.2010.11.002 . The search returned its abstract describing the ground-space formula, logical strings/membranes and rigid face-diagonal dipoles. This is the baseline already cited by the supplied boundary paper; the new search did not reread its full text.

Fontana and Pereira, **Boundary modes in the Chamon model**:
https://doi.org/10.21468/SciPostPhys.15.1.010 . The local `2210.09867v2.pdf` was read previously. Its boundary stabilizers, normal-derivative fields and endpoint-charge rules are the source construction for our boundary tests.

## Consequence for our work

1. **Benchmark — checked:** native signed stabilizers agree with the upstream support builder and the published Laurent column.
2. **Operator transport — checked:** Appendix B, the 58-step supplementary reduction, honeycomb edge incidence and signed lifts on three compatible covers. Ancilla-frame conventions and the sublattice translation remain explicit.
3. **Refinement comparison — checked:** all four existing charts preserve operator products, norms and shared-site identities. The quantum and scalar reader payloads remain distinct.
4. **Cell gluing — open:** import the defect-network interface/condensation rules, beyond the checked bulk gauge incidence.
5. **Boundary fields — open:** compare retained differences with the supplied boundary action and charge dictionary. The separate toric-code-layer renormalization construction also remains unimported.

The constructions found supply the bulk quantum model, an explicit honeycomb gauge description, Clifford equivalence, coarse graining, boundary theory and working decoder code. The project-specific bridge is their correspondence with our current reader fields and refinement charts.

## Reproducible discovery searches

- https://ask.sciencemadereadable.com/%22Chamon%22?k=30
- https://ask.sciencemadereadable.com/%22Chamon%22%20AND%20%28%22renormalization%22%20OR%20%22Clifford%22%20OR%20%22foliated%22%29?k=30
- https://ask.sciencemadereadable.com/%22Chamon%22%20AND%20%28%22tetrahedral%22%20OR%20%22octahedral%22%20OR%20%22defect%20network%22%29?k=15
- https://ask.sciencemadereadable.com/%22Topological%20order%20in%20an%20exactly%20solvable%203D%20spin%20model%22?k=30

The service searches OpenAlex titles and abstracts. The specific full-text sections and code inspection above supplied the construction details.
