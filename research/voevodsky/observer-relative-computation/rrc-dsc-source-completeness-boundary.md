# A concrete obstruction to automatic source completeness

`agda/ObserverRRCCompletenessBoundary.agda` instantiates the actual WholeHistoryComparisons.Structural.Generated relation and proves its Completeness premise false for a specified source/algebra/law instance.

## Explicit instance

- Source: the previously exhibited Boolean packets and their actual source witnesses.
- Algebra: constant lifted Unit, with every seed and rule interpreted as its unique exhibited value. This is a valid information-forgetting algebra, not a proposed physical or operational semantics.
- Law(q,d,e): actual equality of the Boolean outer-rule discriminator, lifted to the required universe. This is a nonempty law family admitting all same-tag pairs, not just an empty theory.
- Law interpretation: equality of the unit-valued interpretations, constructed using the evaluator's collapse paths.

## Checked obstruction

Every Generated constructor preserves the outer-rule tag: reflexivity, inversion, concatenation and law preserve its equality; congruence changes children but keeps the same outer rule.

The existing compare-rule and identity-rule histories have the SAME Complete endpoint and equal unit interpretations, but different outer tags. Therefore no Generated comparison connects them. In particular `not-complete : G.Completeness → ⊥`.

The obstruction survives the RRC–DSC comparison bridge. The encoded histories still have equal interpretations. A translated generated route would reflect, and transport along history roundtrips, to the impossible original route; `no-translated-route` rejects it.

Thus finite witness synthesis, representation roundtrips, soundness and two-way comparison simulation do not automatically supply source completeness. A chosen law basis must account for the distinctions forgotten by its chosen semantics if completeness is required. Alternatively the semantics or the claimed coverage must be refined. Merely importing every semantic equality as a law would change the problem.

## Relation to existing Nima results

Freshly read `research/nima/source-relative-comparison-completeness.md` explicitly distinguishes its supported decomposition language from WholeHistoryComparisons.Structural.Generated. Its local theorem assumes Requirements(Q), including the relevant source and higher-witness theories. Its all-code reduction is an equivalence of completeness obligations, not a finite source basis or an identification of raw histories.

This countermodel does NOT refute those conditional results or any intended theory with additional cross-tag laws. No Nima-owned source was changed. It demonstrates why the comparison adapter's source premise cannot be silently discharged by the existing decomposition theorem.

## Remaining work

For intended resolution semantics, choose and state the actual Algebra/Law interpretation, then establish the necessary source adequacy or exact coverage boundary. The deliberately forgetting algebra here is a diagnostic countermodel, not that intended instance. This remaining task is separate from the completed counterexample.

Continue the existing observer-internalization branch locally: determine how the already checked finite access/transport interfaces sit in the retained RRC/DSC representation without opaque evaluator callbacks.

## Fresh verification

Safe Cubical Agda --ignore-interfaces -Werror canonical aggregate passes54 entries,197 source/checker files unchanged, with two rejected false-theorem controls in136.627 seconds. See results/operational-checkpoint.json and results/agda-operational-checkpoint.log.
