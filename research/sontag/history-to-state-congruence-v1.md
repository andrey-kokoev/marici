# History-to-state congruence: scoped continuation witnesses v1

## Result and boundary

For the declared energy gain/read vocabulary, equality of numeric `(a,b)` is a predictive continuation congruence. For the finite contextual command vocabulary, equality of full context is a congruence and immediate capability is not. For retained WG histories, source-dependent proof payloads and relation-module attachments cannot be discarded merely because endpoints or terminal recordings agree. Existing typed WG comparisons supply scoped transport certificates; this packet does not prove transport across arbitrary WG equivalences.

This closes bounded mathematical subcases, not the net's full WG history-congruence gate. No physical dynamics, noise tolerance, controller authority over context updates, or completed-system claim is added.

## Definition

Fix task, operation vocabulary, initial context policy, reader family and resource-effect convention. A relation R on retained histories is a continuation congruence when related histories have matching admissible next events (with transported payloads/witnesses), their next histories remain related, and observations and declared resource effects match. Induction then transports every finite admitted continuation. Policy transport additionally requires that each decision use only the matching available information.

Equality of a task summary is not equality of retained history. Histories with different provenance may be predictively related without erasing their actual records. An observation model must be fixed before claiming sufficiency.

## Energy: analytic finite-continuation theorem

Source functions: `gain_step`, `EnergyTaskState.energy`, `infer_components`; see the interface packet.

Take summary π(h)=(a,b), nonnegative, with nonempty provenance retained separately. Events are declared gains q∈[0,1] and exact total readings. The next-step domain depends on component nonnegativity, provenance validity and gain domain, not provenance text. For equal valid summaries, the same gain is admissible and both outputs are `(q²a,q⁴b)`; total readings and model energy changes agree. Therefore equality of `(a,b)` is a congruence for this vocabulary. Induction gives, for Q equal to the product of a finite gain word,

`(a,b) -> (Q²a,Q⁴b)`, with readout `Q²a+Q⁴b`.

With all exact gains admitted, it is also the coarsest predictive equivalence on numeric component states: equality of H at q=1 and at any fixed 0<q<1 solves the invertible two-reading system whose determinant is q⁴−q². Thus identical observations for all such continuations imply equality of a,b. This minimality is vocabulary-relative; it fails if the reader or intervention family is restricted.

H-only fails: `(8,0)` and `(0,8)` both read 8 initially but read 2 and 1/2 after q=1/2. Provenance strings and full source records are not minimized by this theorem. No theorem about unmodelled resource reservoirs follows from matching visible energy change.

Exact observation-based policies transport because equal information histories give equal decisions. Two-reading identification narrows the compatible-state family to a singleton; the probe's gain has already updated that state. This is a sufficiency argument, not a new physical measurement implementation or robustness result.

## Context: exhaustive finite congruence

The full state `(actor,budget)` is preserved under the actual `advance` maps. With identical context and command, the next context and `enabled_actions` coincide; induction proves matching future capability traces. The source has no budget consumption transition for set0/set1, so the theorem covers only grant/replenish and capability observations.

The immediate-capability quotient merges observer/0, observer/1 and controller/0. Grant separates observer/0 from observer/1; replenish separates observer/0 from controller/0. Hence this quotient is not a congruence. One-step continuation signatures distinguish all four contexts, so the full-context partition is the coarsest behavioral equivalence for this exact vocabulary. These are observationally supplied context events; no grant authority is inferred.

## WG: two separate obstructions, not one universal quotient failure

### Actual proof payload

`research/nima/composable-witness-specialization.md` supplies `Composite.correct`, `Composite.rebase`, behavioral units and associativity on full steps. Its `ProofDependentFixture` requires the second-layer witness to depend on the actual first proof payload. `rejects-erasure` excludes substituting false for a required true payload despite equal endpoints and the same base relation witness. Therefore an endpoint-only representation cannot promise transport of those proof-dependent continuations.

Complete retained identity is sufficient for replay with identical generator and dependent premises. The existing source comparisons provide transport on their explicitly indexed composition/rebase interfaces. Arbitrary comparisons of histories, arbitrary-domain compatibility inference, and execution transport are not established by those certificates; the source packet expressly separates them.

### Relation attachment

Sources: `research/strominger/wg-I-squared-rehydration-correction.md` and `research/nima/derived-terminal-quotient-retains-the-product-attachment-as-a-shift.md`.

For the admitted marked path algebra S and multiplicative typed recorder rho, I=ker(rho) is an ideal. Therefore equality modulo I IS a congruence for ordinary algebra multiplication and terminal observations. It would be incorrect to refute that congruence using a hidden relation product.

The stronger source-module task requires the attachment `0 -> I² -> I -> I/I² -> 0` and source action. Choose endpoint-compatible a,b∈I with ab≠0. In C=I/I², `[a]b=0`, while in I the actual continuation is ab≠0. A source-linear splitting preserving the required lift would force `sigma([a]b)=sigma([a])b=ab`, contradicting sigma(0)=0. Thus C alone cannot recover the original module action/attachment; a bare vector-space direct sum is insufficient. The specified one-sided derived quotient instead retains I² in degree −1 and the nonzero connecting projection. This is a source-module/derived observation distinction, not a physical scalar detector.

The precise rejected candidate is “terminal or first-order summaries preserve all source-module attachment observations,” not “terminal equality fails multiplication.” Retain typing, source action, product and connecting witnesses for the stronger task.

## Disposition and next acceptance test

Constructed: energy gain/read predictive congruence and context-command congruence. Rejected: H-only, immediate capability, and proof-erased/attachment-erased claims of full retained-source sufficiency. WG transport remains scoped to the already supplied indexed certificates.

To resolve the full `history-to-state-congruence` node, declare one specific WG history equivalence and continuation category, supply event/witness transport including source action and attachment observations, and prove the replay/composition squares for that relation. No arbitrary WG equivalence theorem is claimed. The owner-local result should be reviewed by Nima before changing the work-net verdict or frontier.

Verification: `research/sontag/checkers/history_to_state_congruence_v1.py`; result `research/sontag/results/history-to-state-congruence-v1.json`. Exact Python checks corroborate energy/context finite fixtures and inspect cited source evidence without rerunning WG Agda or the 1040-dimensional relation calculation.
