# Iteration2: actual exchange admitted by a retained-history WG

## Fresh recommendation and result

Freshly read the33-node net and the current certified-image source. The recommended role task required a retained-history extension admitting the actual target exchange without pretending it preserves the old certified image.

That extension is now checked. It reuses `TypedGeneratorLayers.Histories`, preserving the original certified source package, every intermediate comparison and edge witness, and the current target view. It supplies an actual Layer1 WG on those extended states.

## Explicit interface

Let L be the existing target exchange packaged as a WG on After.Compared, with witness t=exchange(s). Let H=Histories(L). Define

    Extended = Sigma(seed:Generated) Sigma(y:After.Compared)
                   H.History(view(seed),y).

`start(seed)` has empty history. `advance` appends the actual exchange edge using H.join. Theorems `seed-preserved` and `origin-preserved` recover the same initial certified packet and source after every step. `view-exchange` identifies the current target action exactly. `continue-associative` reuses the existing history associator to prove composition of supplied exchange histories on extended records.

No newly invented history datatype or unrecorded inverse is used. The original seed's complete image certificate remains attached even while the current target leaves that image. It certifies the initial boundary, not a false claim that every later view is another original promotion output.

## A witnessed return that is not identity of the complete object

For the actual admitted input:

- initial: current view=run(input), history length0;
- once: current view=exchange(run(input)), history length1, outside the old image;
- twice: current view returns to run(input), history length2.

Origin and the chosen even/odd exchange phase return after two steps. `no-history-erasure` proves twice is NOT equal to initial as a complete Extended record. Equal source, current view and phase do not erase a performed history.

The phase bit is bookkeeping for this selected involutive action. It is not identified with the operator's two conceptual phases, four arity stages, powers Q2/Q3/Q4, or rung numbers.

`no-view-preserving-normalizer` also proves there is no map from all Extended records back into the old Generated carrier that preserves every current view: at once it would supply a forbidden preimage for the known outside target. Forgetting to the retained original seed is allowed, but is a different observation.

## Four roles on the complete extended construction

The module's actual `WG : Layer1 level` has State=Extended, next action advance and witness y=advance(x).

| Role | Concrete retained interface |
|---|---|
| object | Extended records and the WG record containing their action specification |
| generator | WG.generate returns the advanced record and actual witness |
| operator | advance on a supplied Extended input |
| transport | original source anchor, current boundary and retained typed exchange history, plus generated-step witness |

These roles coexist. Execution changes current target, history length and the selected phase; selecting a role view does not itself execute a transition. The returned complete record is already an input to the same WG. Thus the requested concrete role/phase/context example now includes genuine continuation outside the initial image, reuse, composition, and a history-erasure hostile.

## Net disposition

Resolve `wg-phase-relative-roles` ONLY at its concrete scoped interpretation: existing Composer and the native retained-history fixture exhibit the claimed four roles with explicit phase/context distinctions and preserved witnesses. Do not promote this to a universal characterization of every WG or to the proposed primitive packet being Type.

The broader packet/Type, arity/rung binding, generative137 schedule and source-relation attachment tasks remain open. A further generic exchange-history example would be redundant. The next recommended root-relevant frontier is `relation-layer-wg-binding`, using the existing source product/attachment instead of prolonging this now-closed role example.

## Verification

Source: `research/strominger/agda/NativePromotionHistoryExtension.agda`.

Executed `python research/strominger/checkers/check_native_promotion_history_extension.py`. Fresh safe Cubical Agda closure with ignored interfaces and stable input inventories passed. The first compile required importing Histories as a module rather than a term; this was corrected before the successful fresh run. The existing nonfatal owner import warning remains.

Receipt: `research/strominger/results/native-promotion-history-extension-agda-v1.json`.

No source-owner code, physical model, universe axiom, free-seed face,137 counting rule or root assembly claim was changed.
