# Proton witness: body slot versus face closure

## Question

The operator proposes that a proton is witnessed by a neutron or outer closure. The controlled task is to decide whether that obligation can belong to a whole proton or to its faces, using existing source constructions without modifying them. Active obligation: forward realization of this new geometric/support test, not physical stability or field sewing.

The initial protocol is `inputs/proton-witness-protocol-v1.json`. This audit does not implement the preceding alternative electron-as-octahedron particle model. Electron bodies remain the supplied reference carriers and are included as obstacles when determining the exterior vacant component. Exterior means the complement of closed occupied tetrahedral cells; permeable, hollow or open shells would require a different boundary model. No claim about physical empty space is made. Enclosure and witnessing are not identified.

## Two explicit hypotheses

**Body model:** every neutron filler must have an occupied proton witness, with one witness slot per proton body. Different protons may witness the same neutron, but every neutron must be covered. A maximum bipartite matching from neutron bodies to adjacent proton bodies decides whether all neutrons can receive distinct primary proton witnesses. Remaining protons can use an adjacent neutron or an exterior boundary face. Failure retains an actual Hall-deficient neutron/proton subset, not only the aggregate inequality N>Z.

**Face model:** actual PN contacts label proton faces with their neighboring neutron. Different faces of one proton may have different neutron witnesses, and one neutron may supply faces on several protons. Every neutron must have at least one actual occupied-proton face contact. Every other proton face must reach the unbounded vacant complement, not merely a vacant cell. No unoccupied reference proton is silently counted as an occupied witness.

Each source proton is a four-face MMCC tetrahedron. Exactly two faces have the two-M/one-C marking eligible for native PN contact. The other faces are still checked for actual exterior closure; they are not erased.

### Boundary is not just vacancy

For a vacant neighboring cell, flood the vacant primitive-cell adjacency graph. A cell with a vertex beyond the coordinate bounds of all occupied tetrahedra certifies access to infinity: an interior point of that cell lies beyond the occupied bounding half-space and has an outward ray avoiding the occupied union. Exhausting a vacant component certifies an enclosed cavity. A resource stop remains unknown.

The coordinates are source integer barycentric addresses; no floating-point geometric threshold is used. Every detected cavity is separately verified by coordinate face incidence: every face of its finite vacant cell set has exactly one neighboring cell in that set or the occupied enclosing geometry. Removing an enclosing body from the certificate must break that check.

## Finite evidence

Fifteen selected configurations were tested. Saved native fixtures are reloaded through fresh source universes, with packet/operation equality and native exit certification checked. The additional PE selections are the previously checked fixed-footprint experimental fixtures. This audit checks their geometry; it does not rerun all original PE guard/prefix suites.

| Construction | Z/N | Body rule | Face rule | Neutron faces / exterior faces on protons |
|---|---:|---|---|---:|
| H-1 experimental geometry | 1/0 | Pass | Pass | 0 / 4 |
| H-2 native | 1/1 | Pass | Pass | 1 / 3 |
| N-15 native | 7/8 | Fail | Pass | 14 / 14 |
| O-16 native | 8/8 | Pass | Pass | 16 / 16 |
| O-17 native | 8/9 | Fail | Pass | 15 / 17 |
| O-18 native | 8/10 | Fail | Pass | 16 / 16 |
| F-19 native | 9/10 | Fail | Pass | 18 / 18 |
| Ne-20 native | 10/10 | Pass | Pass | 20 / 20 |
| Ne-22 native | 10/12 | Fail | Pass | 20 / 20 |
| Na-23 native | 11/12 | Fail | Pass | 22 / 22 |
| N-14, delete N-15 body16 | 7/7 | Pass | Pass | 13 / 15 |
| N-14, delete N-15 body17 | 7/7 | Fail | Fail: cavity | 12 / 14, plus2 cavity-facing faces |
| Ne-21, delete Ne-22 body16 | 10/11 | Fail | Fail: cavity | 18 / 20, plus2 cavity-facing faces |
| Ne-21, delete Ne-22 body29 | 10/11 | Fail | Pass | 19 / 21 |
| Ne-20, delete Ne-22 bodies16/29 | 10/10 | Fail | Fail: cavity | 17 / 21, plus2 cavity-facing faces |

The body model passes5/15; the face model passes12/15. No boundary exploration returned unknown. Every neutron in these fixtures has an occupied-proton face witness, so all three face-rule failures are specifically about outer closure.

### Exact residuals

- N-15 deletion17 leaves the one-cell cavity17. Its body-rule Hall obstruction is neutron bodies16/8 sharing only proton body9: two fillers, one body slot.
- Ne-22 deletion16 leaves the one-cell cavity16.
- Ne-22 double deletion16/29 retains that same cavity16; removing the exterior body29 does not open it.

All three cavity certificates pass the independent coordinate-incidence check; deleting an enclosing body is rejected. All numerical body IDs are local to their source witness, not isotope labels or universal lattice names.

## Structural interpretation

A whole-body exclusivity rule is too restrictive for the already certified neutron-rich structures. Under the face interpretation the source marks give the necessary coarse capacity bound N<=2Z, rather than N<=Z. This is only a capacity bound, not a stability law, shell rule or sufficient constructor.

The literal outer-closure condition separates configurations with identical isotope counts. N-14 and Ne-21 each retain at least one passing experimental witness; the independent native Ne-20 passes while the new fixed-footprint Ne-20 double deletion fails. Thus this sample does not eliminate an isotope—it selects between its candidate arrangements.

The face rule is therefore compatible with all tested native fixtures but not with every experimental PE configuration. This is counterevidence to universal compatibility with the prior experimental family. It is not repaired by calling an enclosed vacancy “outer boundary.” An explicit alternative would allow a separate internal reference-closure witness; that would be a changed hypothesis and is not adopted here.

No electron shell capacity, octahedral enclosure map, energetic stability, physical occupancy law, A4-specific symmetry or global field sewing follows. The source markings and actual face labels remain part of the data; a tetrahedral drawing alone does not select the decorated configuration's symmetry.

## Reproduction and disposition

```sh
node research/strominger/checkers/check_proton_witness_faces.mjs
```

`results/proton-witness-faces/verification.json` retains the protocol, source hashes, all15 fixtures, body/face matchings, Hall deficits, actual proton faces, exterior/cavity labels, occupied geometry, three closed-cavity certificates and hostile checks. A passing checker means the comparison and certificates passed; its `allFaceRulePass:false` explicitly retains the rejected face hypothesis instances.

The tested refinement of the proposal is **one witness per actual interface, with an independently verified distinction between exterior boundary and enclosed vacancy**. Whether those cavities should instead carry a separate internal reference-closure object is the remaining model choice, not a missing implementation of the existing PE constructor. Other-owner sources, production admission and viewer behavior are unchanged.
