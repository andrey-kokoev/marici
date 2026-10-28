# What corresponds to an action inside the source system?

Search scope: retained-comparison, six-edge execution, native compiler and Yoneda sources. Source inspection only; no new compiler run. 'Action' here means a compositional action on a carrier/family, not a scalar action functional.

## Closest source-level construction: continuation by composition

`research/nima/agda/SeedFirstReturnActions.agda` defines History(v)=Path A v and advances a history by appending the actual directed occurrence. This is a canonical action of directed source paths on rooted histories. No group, physical state, matrix, or externally supplied transition table is required to define that regular continuation action.

Its Effects module separately accepts a family X(v) and an edge action. `run-append` proves chronological word action:

    run(p ++ q,x) = run(q,run(p,x)).

This distinction matters: the source supplies a regular action on its histories; an action on a different payload family requires an interpretation. Directed continuations need not be invertible.

`SeedGeometricResponseState` instead acts on paths in the declared free geometric realization by path concatenation. Those actions are reversible; the directed source alphabet does not thereby gain inverse occurrences. `OriginalRuleGeometricCompiler` constructs original-rule retained execution and compositional agreement for the declared geometric interpretation.

## Explicit retained-action interface already formalized

`research/nima/agda/RetainedActionYoneda.agda`, module Actions over RetainedComparisonStructure.Structure, defines:

    Carrier : P -> Type
    act : E(p,q) -> Carrier(p) -> Carrier(q)
    act-unit : act(id,v) = v
    act-comp : act(d,act(e,v)) = act(d composed with e,v)

Its SetAction requires set-valued fibers and retains both law witnesses. This is the typed/groupoid analogue of a group action; a one-object specialization recovers the usual shape. The E arrows are retained changes, not native equality proofs between raw object labels.

The source Structure retains P, change types E, comparison types K, composition/inverses/laws, and realization j:E->K. The regular action has Carrier(q)=E(p,q), with action by postcomposition. It is constructed from those operations. The realized action has Carrier(q)=K(p,q) and acts through j. The model proves that distinct retained changes can have equal realized actions.

The Structure is an explicit candidate input to this theorem, not a demonstrated identification of every original twelve-rule derivation with its arrows. Source grammar E (dependent extension) and Structure.E (retained changes) share a letter but are different interfaces.

## Stronger result: action reconstruction already exists

`retained-action-yoneda-iteration-05.md` and its source prove

    Nat_E(E(p,-),D) ~= D(p).

Evaluation at identity and extension by the action are inverse, including equivariance witnesses. Regular actions detect retained arrows by acting on identity. Invertibility of action maps is derived from source inverse laws and action laws, not independently supplied.

This is an exact internal answer to 'what represents an action?' and 'what does it retain?'. It is not a theorem selecting an arbitrary target action D. It also does not recover an unmarked raw object label from its regular action alone.

`research/nima/adapters/yoneda/README.md`, OrdinaryYoneda and NativeYoneda extend the reconstruction discussion to supplied categories with noninvertible arrows and set-valued contravariant presheaves, including native packaging. Categorical operations/laws remain supplied inputs there; the theorem is not their derivation from channel counts.

## Related concrete source action

`native-tick-interaction-action.md` binds chronological execution to actual Tick/History types with units, concatenation and retention. Its step policy is supplied. A stationary policy satisfies those same structural laws, and a kick/drift assignment fails an internal square comparison. Thus a list action is weaker than an interpretation preserving all internal source witnesses.

## Consequence for the programme

There is no missing generic action concept to introduce. The closest source-native notion is composable retained continuation; regular actions realize it on outgoing histories or retained changes. Actions on other carriers are interpretations, with explicit unit/composition/coherence laws. Native construction and observer comparison already have concrete instances.

Therefore structured-action coverage should be phrased as coverage by these existing source representations, preserving the specified relations and witnesses—not as importing a new group-action abstraction merely because the net used that word. Which target class is covered is a separate quantified question; this search does not choose one or assert global coverage.
