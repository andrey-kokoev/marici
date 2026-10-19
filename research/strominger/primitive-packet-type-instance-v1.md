# Extension turn1: finite native packet/type candidate

## Fresh-state selection

The current56-node net has four open non-root tasks and a constructed conditional root. This turn addresses `primitive-packet-type-binding` using the actual NativeTableRules constructors, not a new four-corner drawing. Subsequent turns address grading/orientation, uncertainty, and the whole retained half-step.

## Concrete inhabitants and native adapters

`PrimitivePacketTypeInstance.agda` selects I=Bool and the constant family of complete native atom packages with carrier Bool and selected value false. This is an explicitly chosen finite candidate, NOT an inferred intended physical packet or source-generated137 family.

| Proposed component slot | Actual native construction | Actual carrier / selected witness |
|---|---|---|
| id | identity-comparison(atom) | Compare Bool Bool idEquiv; (false,false,refl) |
| Q2 candidate | E-package Bool family i | Bool × Bool; (i,false) |
| Q3 candidate | Pi-package Bool family | Bool → Bool; constant false |
| Q4 candidate | Congruence.Pi-comparison | Compare (Bool→Bool) (Bool→Bool) idEquiv; pointwise reflexive comparison |

The Q labels in this table are proposed slots, NOT proved quadratic/cubic/quartic operations. The formal module deliberately uses `selected`, `assembled`, and `reconciled` rather than laundering the proposed degree labels into definitions.

Ten checked declarations give four carrier paths, selected-mark and payload recovery, assembled evaluation, stable-witness recovery, pointwise reconciliation, and a mark-erasure contradiction. A further declaration proves that the unary reset map Bool→Bool has no left inverse. This distinguishes general state change from the equivalence transport required by the native comparison constructor.

At the native rule boundary, E and Pi both accept the Bool family and return one complete package. Internally E retains a selected dependent-sum mark while Pi retains all component values. Those are different presentations: no field adapter can silently replace the selected mark with only false. The module proves that the selected true and selected false values cannot be equal although their payload projections agree.

## What presents a type here

Each complete native package contains a carrier type, an indexed construction node of that carrier, and an inhabitant. At this explicitly selected level it therefore presents an inhabited type with retained construction. Its carrier is not the packet itself, and neither is identified with the universe Type. The reconciled package also retains pointwise comparison data through the existing native Congruence construction. Family access/terminal reuse remains the previously verified supplied-family adapter, not a newly source-generated chronological phase law.

The proposed id/Q2/Q3/Q4 degree claim is NOT supported by these carrier adapters. Identity comparison already changes the presented carrier from Bool to a comparison type; the common two-port domain does not determine whether a constructor forms a sum, product or comparison. Polynomial grading needs independently supplied variables and a formation/degree law. This candidate is an explicit typed alternative to positional degree inference, not a proof that no other candidate can realize that interpretation.

## Disposition and remaining boundary

The task's acceptance explicitly permits a scoped candidate with a field adapter or a mismatch. It is constructed at this finite native candidate scope, with the failed mark-erasure and noninvertible-transport identifications retained. A universal primitive-packet=Type claim, operator-selected phase cycle, generated F/G, and id/Q2/Q3/Q4 degree realization remain unproved; they are not part of this narrowed result. The constructed root's source assumptions are unchanged.

## Verification

    python research/strominger/checkers/check_primitive_packet_type_instance.py

Fresh --safe --cubical --guardedness --ignore-interfaces Agda check passes, exit0, stable source/compiler/checker inventory. No holes or postulates. Receipt: `research/strominger/results/primitive-packet-type-instance-agda-v1.json`. The initial compile exposed an omitted product-type import; it was corrected before the final fresh check.
