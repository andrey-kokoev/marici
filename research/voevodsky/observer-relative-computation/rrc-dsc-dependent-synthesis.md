# Dependent witness synthesis with retained nontrivial index transport

`agda/ObserverRRCDependentSynthesis.agda` extends the finite solver to the existing circle-indexed Boolean cover in `IndexIdentityCoherenceRegression.agda`. This is a genuinely nontrivial dependent family: transport around its specified index loop flips the Boolean fibre value. Both query paths have the same index endpoints, so those endpoints alone cannot determine the action.

## Fixed query language and source

Two canonical path codes are admitted: reflexivity and the cover's designated loop. They reuse the names identity/swap as finite syntax, but their interpretation is now actual dependent transport, not simply an arbitrary Boolean equivalence callback. The solver constructs the normalization witnesses using substRefl and univalence computation uaβ.

The source generators are the two exhibited total-space packets `(base-index,true)` and `(base-index,false)`. Source membership retains a label and identity to its packet; no globally decidable package-equality or unique source-proof claim is made.

A Solution contains an actual fibre-transport equality and an RRC derivation of a comparison between these total-space packets. The comparison's carrier equivalence is identity on the TOTAL space. Its boundary path is constructed from the index path and dependent fibre witness by ΣPathP.

Consequently, the successful true-to-false comparison is not smuggling in a Boolean swap equivalence as its total-space comparison. Its nontrivial index path supplies the dependent content.

## Checked positive and negative results

- `synthesize` returns Dec(Solution mode x y), computing Boolean action and then constructing its actual transport witness and full compare-rule history.
- `complete` proves that any Solution of the specified query forces a positive result.
- The loop query true-to-false succeeds.
- The reflexive query true-to-false is impossible, even though the two queries have identical index endpoints.
- `recover-index` projects the index path from the actual output comparison package; `recovery-exact` recovers the selected canonical path.
- The successful loop's projected index witness cannot be replaced by refl, using the checked nontriviality of the cover loop.

Both source histories and the constructed total-space comparison path remain retained. Only source seeds and the declared compare-rule are used. This mathematical construction does not grant effect or ownership authority.

## Scope

This is complete for the specified two path codes and Boolean fibre endpoints at the chosen base index. It does not decide arbitrary circle paths, synthesize arbitrary source equivalences, enumerate all total-space paths, solve higher fillers or supply a general dependent evaluator. The example uses existing checked cover mathematics without modifying Nima-owned sources.

## Verification and continuation

Fresh standalone and aggregate checks pass safe Cubical Agda --ignore-interfaces -Werror. The canonical aggregate covers53 entries,196 stable source/checker files and two rejected false-theorem controls in168.745 seconds. See results/agda-rrc-dependent-synthesis.log and results/operational-checkpoint.json.

Next activate the existing source-completeness-instance obligation: the comparison bridge still assumes an actual Algebra/Law completeness premise. Neither this finite dependent decision procedure nor the preceding constant-carrier solver supplies that general premise.
