# Higher first test: a retained path changes the next construction

Contract: `research/conjecture_net/contracts/witness-sensitive-route-realization.v1.json`.
Formal source: `research/voevodsky/agda/WitnessedRouteContinuation.agda`.
Run: `python research/voevodsky/checkers/check_witness_sensitive_route_realization.py`.
Receipt: `research/voevodsky/results/witness-sensitive-route-realization-v1.json`.

## The concrete claim

Every closed program in the existing independently defined stay/turn/follow route machine constructs a filled return triangle and a finite execution trace. Transport along the triangle's retained first edge agrees with source execution for every Boolean input. Route composition, inverse recovery and typed comparison transport are witnessed.

Yet NO function of the return diagonal alone can reproduce this continuation on every generated triangle.

This is a first higher instance of the constructive-identity proposal: path evidence is an input to a subsequent construction. It is not simply stored for inspection.

## Frozen source and target

Reuse `research/nima/agda/DependentTransportMachine.agda`. Its source syntax has stay, turn and follow; its directed execution has idle, flip-bit, split and under rules. The existing source normalizer constructs actual finite Step traces for all closed routes and Boolean inputs. No host-language callback is a source instruction.

Interpret stay as refl:Bool=Bool, turn as the existing univalent Boolean flip path, and follow as path composition. For every generated p construct the marked triangle

    (p, sym p, refl, cancellation witness).

All three vertices are Bool and the return diagonal is refl. The target is this generated route/triangle family, not arbitrary paths or prescribed faces in the universe.

The source reverse program reverses order and keeps the flip instruction self-inverse. Both all-input recovery laws are proved recursively. Semantic inverse recovery uses inverse path transport, independently of the source recursion.

## Two packages, identical visible return, different continuation

| Retained first edge | Reverse edge | Return diagonal | Transport false along first edge |
|---|---|---|---|
| refl | refl | refl | false |
| Boolean flip path | inverse flip path | refl | true |

Both have genuine cancellation fillers. Their full marked boundaries differ although their vertices and final diagonal agree.

The continuation is a precise typed operation:

    probe(t,b)=transport(first-edge(t),b).

The formal theorem `no-return-only-continuation` rejects every proposed observer of only the diagonal which claims to reproduce probe(triangle(p),false) for all p. This is an all-observer obstruction from two witnesses, not an enumeration of possible observers.

## What the formal construction retains and proves

`Completed(p)` retains the constructed triangle, its identification with the actual construction, the all-input result function, correctness of the witness-consuming continuation, and actual source execution traces.

- `route-sound` / `probe-sound`: source execution equals dependent transport, for every generated route and Boolean input.
- `compile`: constructs Completed(p) uniformly, not through a finite sample table.
- `source-return-left/right`: the independent reverse source program recovers inputs in both directions.
- `return-left/right`: semantic reverse path transport recovers inputs in both directions.
- `composition`: the witness-consuming continuation preserves route composition.
- `comparison-preserves-probe`: a typed path between full marked packages transports a continuation comparison.
- `higher-comparison-preserved`: a comparison of package comparisons induces the corresponding comparison of continuation comparisons.
- `same-return`, `continuation-distinguishes`, `no-return-only-continuation`: identical returned diagonal is insufficient for the specified legitimate continuation.

The deliberate negative module tries to equate the stay and turn probe results solely by reflexivity. Fresh closure must reject that identification while accepting the positive module.

## Where the extra content lives

This is nontrivial first-edge path evidence in an ambient type universe, packaged with actual 2-cell return fillers. It does not exhibit two different face fillers with EVERY edge held fixed. The latter is a further higher test and must not be inferred from this edge-sensitive example.

The univalent flip path and Cubical transport laws are declared target mathematics. Source execution is specified independently and then proved correct for it. This constructs an operational interpretation, not a derivation of univalence itself from primitive source operations.

The finite-bit theorem needed only extensional successor state. This instance enlarges the continuation interface to consume a retained identity path, making a distinction lost by the endpoint/diagonal projection operationally significant.

## Relation to the existence-square proposal

A returned identity does not contain the whole certificate by itself. For continued construction, the mark must retain the source/diagram/witness package or a proved sufficient representation. Here the probe consumes exactly the path component of that package; dropping it destroys continuation preservation even though the total return remains identity.

This supplies a concrete accepted-or-rejected proposition for the proposed identity-continuation branch. The contract records proposed ++ for construction and -+ for diagonal sufficiency, with separate independent outcome admission. Physical experiments remain parked.
