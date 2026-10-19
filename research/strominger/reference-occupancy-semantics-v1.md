# Occupancy semantics: reference geometry is already permitted for both species

## Main finding

The source does **not** contain a general species-specific rule saying “reference-only protons are permitted, reference-only neutrons are forbidden.” It already uses unoccupied reference geometry of both kinds.

The asymmetry relevant to the proposed isotope repair is operational:

- an advanced N reader may use an unoccupied P-shaped geometric reference without invoking that P reader as a construction source;
- an E reader's only supplied native incoming constructor is NE, whose source is an N reader that must be selected in the occupied construction.

Thus analogy with reference-only P geometry does not authorize a P->E transfer through an unselected N source reader. The proposed extension changes the selected-operation rule, not merely the availability of reference geometry.

## Source definitions, separated by type

The owning implementation is `demos/particle-overlap-tetrahedron/local-reference-rules.mjs`.

### Geometric reference

`completeN(cell,a)` finds the regular proton primitive across M0/C1/M1 and uses its opposite apex to supply C0. It validates the reference's geometry but does not select a packet on that proton body.

Conversely, `completeP(cell,a)` finds the split neutron primitive across the same marked face and uses its opposite apex to supply C2. It likewise does not select that neutron body.

Both are constructors of complete marked charts. Neither is a particle-number observation or a transfer using an absent source reader. Reference aliases also participate in global C/M-role validation; they are not unconstrained decorations.

### Available reader and coefficient response

A packet records a chart, realization origin and full coefficient permutation. Generating a packet or validating its possible transfer does not select it into an assembly. Its response to chosen root coefficients can be computed even when the packet is not selected.

This is consistent with the source contract: packets are retained construction maps from root coefficients, not asserted simultaneous copies of a physical quantum state. A computable nonzero reference response is therefore not an occupancy test.

### Occupied body

`describe(packetIds)` defines occupied bodies as the image of the selected packet charts under `(cell,species)`. Several selected readers on one body do not add particles. Selecting incompatible species on the same cell is rejected.

This is a structural counting convention attached to the selected assembly. It is not derived here from coefficient magnitude, a Hamiltonian, a number operator or a boundary measurement. Changing a root coefficient input between zero and nonzero does not change that selection or its counts.

### Admitted selected transfer

`validateTransfer` checks local native types, origins, full permutations, occurrence identifications and actual interfaces. It does not by itself assert that both endpoint readers belong to a selected assembly.

`inspect` includes a native link only when its source and target packets are selected. The enumerators additionally start at the root and add targets through operations from already selected sources. The isotope searches separately impose rooted reachability, pair guards, occupied-contact witnesses and selected-record exit reachability.

Consequently availability of a geometric chart, packet or locally valid factor does not imply availability of that factor inside a selected construction.

## Generated local distinction: all 24 hydrogen markings

For each recorded marking the checker creates fresh native rules and generates P, N and E packets.

With only the root P selected:

- the N reference primitive and its C2 mark already exist;
- its N reader can be generated and its response computed;
- the N response can be nonzero for a nonzero root input;
- the occupied counts remain 1P/0N/0E.

Thus reference-only neutron geometry, and an available nonzero response map on its reader, already occur in the unchanged implementation.

Next compare two selections with unchanged geometry, phases and factor maps:

| Selection | Geometry/role compatible | Rooted native construction | Native exit certificate |
|---|---|---|---|
| P,E | yes | no | no |
| P,N,E | yes | yes | yes |

For P,E, the occupied shapes share only the marked edge. The existing pair guard permits that geometry, but there is no selected native link connecting them. PN and NE remain locally valid available factors; their shared N reader is not selected.

The checker attempts to submit the direct endpoint pair as native `PE`, `NE` and `PN`. All three are rejected on every marking: PE is not a native operation, and relabelling it NE or PN violates the source/target carrier types. These are 72 rejection controls, not a physical exclusion theorem.

This is a distinguishing test for the missing rule: the source can already describe the needed reference geometry and coefficient composition, but the selected-operation predicate still refuses the transfer.

## Actual reference-only proton use in saved isotopes

For N-15 and Ne-22, the checker freshly regenerates each origin-bounded packet universe, compares saved packets/charts/operations exactly, and rechecks the selected witnesses with the original rules and an explicit rooted traversal.

The saved N-15 witness has **zero** selected neutron records with an unoccupied proton reference. Permission in the grammar does not imply that every witness uses it.

The saved Ne-22 witness has **two** such records:

| N packet | Occupied N body | Unoccupied P reference body | Actual selected incoming operation |
|---|---:|---:|---|
| 39 | 6 | 20 | same-body reader advance from packet 9 |
| 116 | 21 | 20 | same-body reader advance from packet 112 |

Both enter by supplied native same-body reader phase advances—not PN transfers from the absent proton. Every incoming source is selected and occupied. The more general audit admits either native neutron advance kind when recording such incoming edges; these particular witnesses use only same-body advances.

This is the concrete source of the “reference-only proton” allowance in those constructions: a geometric reference does not have to be occupied, and the actual constructor arrives by a separately supplied native operation. No occupied-P support obligation is silently removed from a PN history.

All occupied contacts remain witnessed and all selected records reach an electron exit. The audit does not infer new isotope witnesses from these reference classifications.

## Consequence for the proof attempt

The earlier [support nonderivability proof](neutron-support-nonderivability-v1.md) remains applicable. A native PN;NE history requires its N source/target body; geometric reference completion does not erase that operational dependency.

The additional premise can now be stated accurately:

> Permit a guarded composite of locally valid native factors to be used as a selected endpoint operation even when its internal source/target reader is not selected, while retaining that reader's full reference data.

For the proposed experiment this must be restricted to the specified same-origin terminal PN;NE pair, with vacancy, exact shared edge, full coefficient preservation and whole-assembly checks. It is an **operational reference-mediated constructor**, not a species-wide exemption from occupancy.

The source audit does not derive that constructor. There is no amplitude-based occupancy criterion in the inspected source that would authorize it automatically. A new source-level interface/observation principle or an explicitly declared grammar extension is still required. Defining the extension to fit N-14 or Ne-21 and then calling it derived would be circular.

## Productive continuation

An operational proposal should now be tested against the precise distinction above: what makes a composed reference response available at an occupied endpoint without selecting the internal reader? It must explain why that applies to the guarded zero-grade pair but does not automatically authorize arbitrary reader histories and higher-grade paths.

Until such a source principle is supplied, the honest alternatives remain native searches under the current rules, or separately labelled experiments under the new constructor. Production, viewer admission, physical isotope stability and global field sewing are unchanged.

## Reproduction

```
node research/strominger/checkers/check_reference_occupancy_semantics.mjs
```

Receipt: `research/strominger/results/reference-occupancy-semantics/verification.json`, containing per-marking distinctions, actual missing-P-reference records and their incoming operations, regenerated witness checks and source hashes. No source constructor or admission gate is modified.
