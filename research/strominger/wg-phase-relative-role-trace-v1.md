# One WG, four roles: exact Composer trace

## Result and scope

The existing `ComposableWitnessSpecialization.Composer.WG` supplies a concrete witness for the four-role conjecture. Generator, operator, object and witnessed transition roles are available simultaneously; this example has TWO explicit state phases, not four role phases. No universal role classification or assignment to the four arity vertices follows.

This is a source-level role interpretation of an existing checked construction, not a replacement WG or a new proof of its composition theorem. A fresh safe Cubical Agda check of `ComposableWitnessSpecialization` and its imported closure passed with ignored interfaces and stable input hashes. The known nonfatal `isPropIsContr` import warning remains.

## Fixed WG object and exact interfaces

The base record in `TypedGeneratorLayers.agda` is

    Layer1(l) : Type(l+1)
      State    : Type(l)
      Witness  : State -> State -> Type(l)
      generate : (s:State) -> Sigma(t:State) Witness(s,t)

and defines

    next(s) = fst(generate(s))
    edge(s) = snd(generate(s)).

For one fixed G:Layer1(l), the following roles are typed views of the same record:

| Role | Actual interface | Context needed |
|---|---|---|
| object | G:Layer1(l), retaining State, Witness, generate | a universe containing this record |
| generator | G.generate | source s:G.State to execute one step |
| operator | G.next:G.State->G.State | source s; this is only the endpoint projection |
| witnessed transport | (s,G.next(s),G.edge(s)) | the declared Witness relation and endpoints |

The unprojected `generate(s)` retains the target AND witness. The `next` projection by itself is not a faithful replacement for G. The transport in this table is an admitted witnessed transition; it is not automatically an equality path, an equivalence, or a transport function on arbitrary dependent payloads. Those stronger interpretations require the appropriate relation specialization or separately supplied action.

No change of G, state or phase is required to expose these views. Executing the operator DOES change its state; retaining or reifying that execution is another explicitly typed operation. A view of a packet is not automatically invertible back to the packet.

## Concrete instantiated object: Composer.WG

`Composer.Request` contains a base WG L, first refinement F, and second refinement H indexed over compile(F). Its answer is

    Answer(q) = Sigma(C:Refinement(base(q)))
                    Realization(compile(second(q)), compile(C)).

`solve(q)` constructs compose(F,H) together with Composite.correct(F,H), preserving full steps and sources. It does not receive a finished composite as input.

The fixed Composer WG has

    State = Request + Sigma(q:Request) Answer(q).

Its actual phases are therefore:

    request(q) -> answered(q, solve(q)) -> answered(q, solve(q)).

The first arrow carries `composed(q)`; the second carries `retained(q,solve(q))`. The answered state keeps the original request and the complete answer certificate. These are executable state constructors, not names assigned after observing endpoint equality.

The SAME G=Composer.WG is:

- an object supplied as a value of Layer1 at the stated higher universe;
- a generator via its generate field;
- an operator via its next projection;
- the provider of an endpoint-indexed transition witness for each action.

This occurs in BOTH request and answered phases. The construction provides no basis for a bijection between the four roles and four temporal phases. Its request/answer split is also not a theorem about the operator's two conceptual WG phases.

## Reuse and non-erasure in the existing fixture

`ProofDependentFixture` supplies actual Bool refinements F,H and a third refinement. The composite's generated step is checked definitionally:

    (false, true, false)
       -> (true, false, true)

with witness `(refl, true, refl)`.

`returned-composite` proves that Composer.solve returns exactly that composite refinement. `reused-is-left` and `generated-associator` check its reuse with a third refinement and the actual-operation associator. This is an existing route from a generated answer object into subsequent composition. It uses an explicit new request/context; the answered state's default self-loop does not invent a new task.

`rejects-erasure` is the decisive hostile. Keep the same endpoints and base equality witness but replace the first-layer Boolean proof payload true by false. The second-layer certification would require false=true; the source proves its type empty. Endpoint agreement is therefore insufficient for preserving the transport role required by the next refinement.

The counterexample is already in the module freshly checked here; it is not a new numerical proxy for proof retention.

## Action retained as object: two distinct existing mechanisms

1. Composer's answered state directly retains `(request, answer)` including its realization certificate. This is included in the fresh closure.
2. `WholePackageSigmaPi.reify` and the whole-history construction additionally package complete prior objects/derivations as new Complete values, with recovery and an explicit universe increase. `NativePromotionConstructorTrace` tracks another concrete promoted comparison through a second promotion.

These are related existing interfaces, not an asserted definitional equality between Composer states and native promoted comparisons. No fresh compilation of the reification/native-promotion branch is claimed in this turn. The narrow four-role trace needs no newly invented reification law.

## Consequence for the conjecture net

Constructed scoped instance: four roles coexist on one declared WG and its proof-relevant action; actual state phases and role views are distinct. The returned operation can be reused without erasing its certificate.

The broader `wg-phase-relative-roles` conjecture remains open because its interpretation for the intended primitive transport packet has not been supplied. Its next task is no longer to find an example. It is to compare this exact role interface to the operator's proposed packet/phase structure, stating which views preserve all required continuations and which require additional data.

Do not rename four projections as four phases, identify arbitrary Witness with equality transport, or assume a reflected package lives in its own universe.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module ComposableWitnessSpecialization -Fresh

Exit0, passed=true, ignore_interfaces=true, inputs_stable_during_check=true. Immutable copied receipt: `research/strominger/results/wg-role-composer-agda-v1.json`.

Inspected source anchors:

- `research/nima/agda/TypedGeneratorLayers.agda`: Layer1, Histories;
- `research/nima/agda/ComposableWitnessSpecialization.agda`: Composer, ProofDependentFixture;
- `research/nima/agda/WholePackageSigmaPi.agda`: Complete, reify;
- `research/nima/agda/NativePromotionConstructorTrace.agda`: actual promotion/recovery and inherited question.

No owner source code was modified. No rung/leaf grading, physical interpretation, universal Type theorem, or root assembly closure is claimed.
