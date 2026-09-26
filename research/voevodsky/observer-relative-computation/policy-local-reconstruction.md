# When mere admissibility faithfully recovers a history

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverPolicyReconstruction.agda`; output: `results/agda-policy-reconstruction.log`. The older whole-programme audit predates this addition.

## Exact general criterion

For ANY type A, a recovery function from ∥A∥ to A that returns EACH originally supplied witness a on input ∣a∣ forces isProp(A). The proof compares two truncated inputs using propositionality and transports through the alleged recovery.

Conversely, if isProp(A), truncation elimination gives recovery with that faithful law, and an equivalence ∥A∥≃A with both inverse laws. This is a necessary-and-sufficient condition for faithful recovery of hidden witnesses, not merely for choosing SOME inhabitant.

Bool separates the two claims: a constant function can choose true from any input ∥Bool∥, but no function recovers both true and false faithfully after their distinction has been truncated.

## Actual deterministic fixture

For the concrete two-step run from the supplied dependent program to the finished numeral, the module proves uniqueness by inspecting the ACTUAL Run/Step constructors. The terminal numeral has no outgoing step; the middle configuration admits only the selection step; the initial configuration admits only the required flip step. Every history with these fixed endpoints equals the existing execution.

Thus this specific History type is a proposition and mere admissibility is equivalent to that full history. No whole-machine determinism/termination theorem is being assumed or claimed. The same criterion can be applied elsewhere only after its uniqueness hypothesis is established.

## Foundational qualification

Recoverability here does not supply a decision procedure for admissibility or a search algorithm that discovers an execution. A proof of mere admissibility is still an input. The fixture already has a checked actual execution. There is no assertion that arbitrary programmes become executable merely because an observer exists.

The result does refine the earlier lossless-record construction: retaining the whole history is unnecessary for faithful recovery when the history type is already proof-irrelevant. If distinct histories remain, some witness-sensitive access is necessary to distinguish which was supplied. Orientation alone does not prove uniqueness.

Next build a concrete witness-bearing nondeterministic policy with two distinct histories at identical endpoints and equal semantic values. Check that the obstruction survives a fixed orientation, and identify the extra comparison/rule evidence that makes the histories observable. This tests execution-as-access-to-existing-history against execution-as-merely-knowing-a-history-exists, without requiring a primitive clock.
