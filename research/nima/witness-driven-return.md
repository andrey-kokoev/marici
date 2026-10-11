# A retained witness now controls the return action

## Move from transport to an active question

Ordinary transport around the filled boundary returns an existing reference unchanged. It does not prevent a prepared comparison from observing a retained edge witness and using the answer in a separate active operation.

`agda/TetrahedralWitnessControl.agda` forms the explicit question

    control(P,p,r) = disagrees(transport(first-edge(P),p), r),

where p is a prepared source probe and r a prepared target reference. The question stores the complete tetrahedral package and both pointings; its answer does not replace the question. Recovery is proved.

For the existing ordinary/twisted packages and p=r=false, the compiler proves that the answers are respectively false and true. These results use the already checked edge transport computations, not an externally entered flip stream.

## Declared coupling

Keep the previous selected seed routing and root-return trigger. At a root return:

- if the retained question's answer is false, leave reference orientation unchanged;
- if true, apply the existing flip conjugation to the first reference;
- then execute the existing controlled conservative exchange.

This is an explicit policy binding a witnessed Boolean comparison to a prior operation. It is not claimed that WG uniquely selects the question, its prepared values or that policy. The question remains unchanged through this experiment, so the controller can recompute its answer for inversion.

The construction is an executable conditional controller without an independently supplied event-bit stream. It still is not a proof of a physical or uniquely source-selected autonomous law.

## Computed return histories

For the previous numerical initial carrier and banks, the first three root-return carrier values are:

| Retained package | Witness answer | Return 1 | Return 2 | Return 3 |
|---|---|---:|---:|---:|
| ordinary | no mismatch | +1/2 | +1/2 | +1 |
| twisted | mismatch | +1/2 | -1/2 | -1 |

These are scalar-basis coefficients. The first outputs now agree: the newly controlled reference action cancels the old immediate sign difference. The histories separate at the second response. This change is computed, not hidden by reusing the older fixture expectations.

The checker retains twelve primitive occurrences and three numerical response advances for each case, then reverses every step exactly. It checks the body budget and inverse at all controller phases, reference sign choices and numerical basis states.

## Frame scope

The selector is covariant when the prepared probe and target reference are transported with their local frames. For Boolean flips, write e for the edge permutation bit; then the answer is e xor p xor r. Local changes g0,g1 transform these to g1 xor e xor g0, p xor g0, r xor g1 and leave the answer unchanged. All 32 cases are checked.

This is covariance of the QUESTION and its answer. It is not a new proof of arbitrary-frame covariance of the entire numerical coupled model, nor permission to hold prepared pointings fixed while calling a record change passive.

## Disposition

The return action now responds to an actual retained witness through a specified comparison, rather than being attributed to null boundary transport or supplied as a free event stream. The full source question is retained and the numerical controller remains reversible.

Selection still matters: the prepared pointings, chosen edge, cycle-cover criterion and mismatch-to-action policy are inputs. The experiment does not prepare those inputs from nothing, realize the six seed arrows as physical transport, assign time/energy units, or derive G. It supplies a concrete candidate witness-consuming coupling for further source-policy tests.

## Follow-up: the prepared reference is not the certified endpoint

`marked-witness-control-audit.md` proves that choosing the witness's own inhabited source and target vertices makes this comparison agree identically. The nonzero question here requires the explicitly prepared independent target reference; it cannot be obtained by relabelling the certified target inhabitant.

## Verification

Fresh safe Cubical/guardedness check passed for `TetrahedralWitnessControl` with ignored interfaces and stable inputs. Receipt: `results/agda-TetrahedralWitnessControl.json`.

`python research/nima/checkers/check_witness_driven_return.py` passed with exact arithmetic. Result: `results/witness-driven-return.json`. The Python test validates the proof receipt/source digest and uses its explicit finite Boolean contract; it is not extracted Agda execution. No prior dynamics implementation was modified. No ledger entry, commit or publication is claimed.
