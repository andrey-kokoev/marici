# Neutrino 1→3: what is actually constructed

Owner: `marici.Strominger`. Disposition: conditional source constructions and exact obstructions; **no physical neutrino identification**.

## Correction and source priority

A geometric neutrino candidate already existed. Earlier blanket statements that no neutrino source was supplied overlooked it. The active [arrow-first hypothesis](neutrino-arrow-seed-science.md) is the standalone three-cycle realized by the unchanged geometric assembler as a triangular disk. Its earlier spin/charge decoration is explicitly parked. The [inherited selection/attachment test](neutrino-triangle-selection-attachment.md) already established local equivalence with an ordinary proton face and an attachment-dimension obstruction.

The missing object is an **independently physically selected neutrino preparation/interaction interface**, not all geometric modeling material. The following two constructions have different types and must not be identified by their common 1→3 counts.

## A. Arrow-first geometric placement: constructed

Use candidate #1's unmarked source from `results/neutrino_seed_candidates.json`, replay the pure assembler, and retain its three center-cone triangles. For their oriented sum D:

    D = t1+t2+t3,
    boundary(D) = s(AB+BC+CA),  s = +1 or -1 from source orientation.

The actual six-edge, three-triangle boundary matrix has rank 3. Its restriction to the three internal radial edges has rank 2. Requiring radial cancellation therefore leaves exactly **one global disk-chain coefficient**, mapped to **three outer edge coefficients**. The signed mean recovers that coefficient given the retained source filling archive. This is not recovery of an arbitrary filling from an unlabelled loop, a one-coordinate spinor, or an admitted quantum measurement.

The disk is dimension 2; its edges have codimension 1 in that carrier. This gives a literal source-relative **one main disk port → three boundary-edge records**. The unmarked source nevertheless has **zero inherited external attachment ports**. Available boundary records are not automatically licensed couplings.

### Where it sits relative to the neutron

Run the inherited centroid selector on actual `research/voevodsky/inputs/mode-neutron.json`. The two zero-score supporting triangles are its reserved caps. For each cap, its actual source-generator orbit p0,p1,p2 defines

    J(u,v) = p0 + u(p1-p0) + v(p2-p0).

Both affine action squares commute exactly. However, the native cap has squared edges 3, while the original standalone fixture has squared edges 8:

    J^T G_neutron J = (3/8) G_candidate.

Thus the old fixed-scale isometry claim **fails**. A separately declared cap-induced metric variant is exactly isometric; the old fixture is unchanged. This is geometric scale comparison, not physical mass calibration. Cap centroids have selector score 0, while their three edge centroids have score 3/4. Standalone old-scale edge scores are 2.

| Object | In standalone candidate | In neutron's 3D carrier |
|---|---:|---:|
| Whole disk / cap | main, codimension 0 | codimension 1 |
| Its three edges | codimension 1 | codimension 2 |

This is a precise relative meaning of “neutron, but in codimension.” It is not an embedding in physical spacetime. Both caps pass; the retained source cycle preserves each cap and selects neither as a neutrino sector. Their cap-centroid subdivisions are not the neutron's bulk-center cone cells.

### Discriminants and blocked stronger claims

* The closed outer boundary is the **trivial C3 character**. Both nontrivial cyclic modes `(1,omega,omega^2)` and its conjugate have nonzero vertex boundary. Neither can be the boundary output of this lone global disk under the same closed-boundary requirement. This is a chain obstruction, not a statement about electric charge.
* An ordinary proton face has the same local three-edge boundary template and, at the original fixture scale, the same metric and cyclic action. The count/mode does not distinguish a neutrino.
* The inherited pole operation selects **one edge**, not the whole disk. Whole-carrier inclusion into a neutron cap is not an already licensed disk-boundary attachment, reaction or weak vertex.

[Contract](contracts/neutrino-triangle-cap-boundary.v1.json), [checker](checkers/check_neutrino_triangle_cap_boundary.py), [receipt](results/neutrino-triangle-cap-boundary-v1.json): **13 exact check groups pass**, including all boundary/transport and affine metric squares. The contract preceded implementation. A prototype failed on converting a string-valued center to exact fractions; that adapter was corrected. The passing SCC run is a fresh replay, **not a claimed prospective challenge**.

## B. Separate coherent spinor realization: constructed, conditional

On the retained electron tetrahedral spinor fixture, omit a marked face o and set

    R_o = P_o + (I-P_o)/sqrt(2),
    A_(f|o) = P_f R_o,  f != o,
    V_o = stack(A_(f|o)).

Exactly `V_o* V_o=I_2`: **one input port carries a full C^2 spinor**, recovered coherently from three tagged rank-one face-lines in C^6. The face-lines have complex codimension one in the logical carrier; source normals also construct dual-tetrahedron codimension-one facets. Neither supplies physical spacetime meaning.

The positive normalization, nonunitary port maps and omitted-face mark are supplied derived capabilities. The changed protocol has L/G/N ranks 3/2/2 and supports 12/36/36, total **84**, not the original electron protocol or an energy/mass valuation. All 96 source covariance squares and 2,304 family composition equations pass. Exactly six native spin operations preserve a fixed omission; all 24 transport the four-variant family. No invariant single omission is selected.

**Information-loss hostile:** orthogonal input projectors P_o and I-P_o yield identical flagged dephased records P_f/3 at each retained face. The coherent outputs recover their different input readers; the dephased records cannot.

**Counter-construction:** complementary face projectors have opposite normal eigenvalues but the same counts, recovery and covariance. Native rotations cannot be intertwined with three rotation-inert flavor labels by any of the six label bijections. The quaternion-generator commutant is scalar, excluding a fixed invariant rank-one spin line at that full-group scope. These are not physical helicity, antiparticle or flavor derivations.

[Construction receipt](results/neutrino-three-port-boundary-v1.json): **14** exact check groups. [Discriminant receipt](results/neutrino-three-port-discriminants-v1.json): **6**. Both prior prospective SCC challenges pass. Neutral and charged scalar attachments fit the same maps, so they do not select neutrino identity. This branch does not replace the arrow-first candidate or bridge geometric chain coefficients to quantum spinor amplitudes.

## Existing mixing/scale work

The discovered `research/nima/checkers/check_pmns_from_gram.py` constructs a matrix using supplied measured mixing angles, phase and mass differences; `check_neutrino_scale.py` estimates a seesaw scale conditional on a chosen Yukawa ratio and neutrino masses. `check_pmns_cp_phase.py` compares a declared Gram-number phase expression to observation; `check_lepton_yukawa.py` compares hierarchy guesses. These records exist and must not be described as absent. Their inspected scripts supply no attachment from either construction above to independently selected weak/flavor sectors. They were **not executed or modified**, and their wider scientific validity is not adjudicated here.

## What would make this a neutrino construction?

First supply a retained, source-admitted **global particle-selection and interaction/attachment witness** distinguishing the standalone cycle from ordinary face/cap modes. It must identify preparation and physical readers, not just rename boundary records. Physical spin/chiral propagation, charge/weak coupling, momentum/helicity, mass/mixing and particle/conjugate status then need their own bound maps and tests. No such physical completion is claimed.

Fresh replay commands:

```text
python research/aspect/scc/scc.py check neutrino-three-port-boundary-v1
python research/aspect/scc/scc.py check neutrino-three-port-discriminants-v1
python research/aspect/scc/scc.py check neutrino-triangle-cap-boundary-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
```

The follow-up has **33** check groups, separate from the original table comparison's 22. Native producer CLIs, gallery and proof-assistant sources were not run. Other-owner sources and shared fixtures were not edited; pure inherited constructors were called as specified. No commit, push or deployment was performed.
