# Whole-programme strict transport gate is now green

The current `check_transport_gate.py` run passes all three checks: local transport regression under -Werror, whole aggregate ordinary acceptance, and whole aggregate under -Werror. Inventoried source bytes remain unchanged during the run. Receipt: results/transport-gate.json. The previous failing receipt and its three referenced logs are archived under results/before-machine-repair/ rather than presented as current results.

## Repair, without replacing the actual history type

The original machine Config, Step and bridge Run datatypes are unchanged. The three problematic specialized matches in ObserverPolicyReconstruction.Fixture now call general elimination lemmas in `agda/ObserverMachineElimination.agda`.

Those lemmas establish:

- closed index/configuration syntax is a set, using explicit retractions into Nat/Bool and sum/product codes; no K/UIP axiom is assumed;
- every actual IndexStep/Step agrees with the machine's computed progress result;
- the outgoing destination-plus-Step witness type is a proposition;
- any Run decomposes into an explicit endpoint equality for stop, or an actual outgoing step and tail, without matching specialized indexed constructors;
- terminal-run uniqueness and one-step peeling follow while retaining endpoint paths explicitly.

The original finished-unique, middle-unique and history-unique statements are recovered from these lemmas. The previously accepted fixture theorem has not been weakened to a different Bool witness or a synthetic replacement history.

## Computation checks

`agda/ObserverMachineTransportRegression.agda` passes a fresh -Werror check. The length of the actual two-step execution after transport in the constant History family computes to2 by refl. Recovering it from its truncated witness also yields length2 by refl. The original endpoint-uniqueness theorem applies to that transported history.

These are concrete definitional computation tests. They are not a test of every conceivable nonconstant transport, a compiler-correctness theorem, or a proof that all programmes terminate. General step agreement and outgoing determinism are proved for this small machine; endpoint history uniqueness remains scoped to the stated fixture lemmas.

The canonical foundation and aggregate checkpoint scripts now also pass -Werror by default. The aggregate imports include the new eliminators and regression. Older receipts remain historical; the current transport gate is the evidence for this repaired source closure.

## Next

Return to the internal observer programme now that its dependency computation gate is clear. Classify the existing compositional access-code language completely: result-only versus rule-sensitive, taking admissible replies rather than arbitrary impossible reply combinations. Test whether repeated access adds recoverable content or merely presentation redundancy. Keep this finite fixture's information distinctions separate from geometric observer area and physical access authority.
