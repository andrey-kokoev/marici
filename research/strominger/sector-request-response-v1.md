# Sequential signal and response on the sector square

## Candidate and frozen policies

Following the operator's suggestion, launch one signal first and construct the return only from its delivered receipt. This tests a sequential alternative to the two simultaneously launched traces in [two-ended-sector-trace-v1.md](two-ended-sector-trace-v1.md).

Keep the same candidate sector table, endpoint charts A and D, and alternating L/R outbound moves. At delivery retain all twelve labelled rows, their source fibers and the ordered operation history. The response consumes this actual receipt by replaying its self-inverse operations in reverse order. This inverse-replay response is an explicit candidate policy, not a claim that coherence uniquely selects it. No history is cancelled from the retained record.

P/E remain hypothetical names for the two endpoint presentations; the oriented three-plus-context window binding has not been supplied.

## Results

| Request stopping rule | Response completion rule | Outbound | Response | Total |
|---|---|---:|---:|---:|
| First arrival at E | Consume delivered receipt | 2 | 2 | 4 |
| Impose arrival at step 14 | First arrival back at P | 14 | 2 | 16 |
| Impose arrival at step 14 | Consume the entire receipt | 14 | 14 | 28 |

The natural first-arrival trace is:

    A --L--> B --R--> D --R--> B --L--> A.

The reply genuinely uses the received table and ordered word. Reversing the initial traversal sense changes the word but not its four-step completion count.

In the delayed control, E is already reached at outbound steps 2,6,10 before step14. The response likewise visits P after 2,6,10 reverse operations before completing its14-operation receipt. The delivered tables at outbound steps2 and14 are identical, but their retained histories differ. Thus the receipt can determine the amount of replay work, while the endpoint table cannot determine why the longer request was needed.

All possible arrival lengths of this alternating square candidate have form 2+4m. Full inverse replay therefore has total length 4+8m. Twenty-eight corresponds to m=3, not a preferred value of this law. This formula follows from the four-periodic label action; the checker also enumerates outbound arrival lengths through30 as controls.

## Disposition

Sequential propagation is implemented and retains fibration recovery at every step. It does not by itself select28. The28-step trial is deliberately marked a forced-length control, not a successful derivation.

Its endpoint type is P -> E -> P, not the original28-stage P -> E passage. Neither interpretation replaces the other silently. The original global conjecture remains open.

The next missing ingredient is a source-defined **completion predicate**: what retained interfaces, sectors or ancestry must have been processed before a request is complete and a response may begin? First arrival at the visible endpoint is demonstrably weaker than receipt completion. Merely adding a stage counter or asking for the fourth arrival would fit the desired length rather than explain it. A candidate based on contextual-window/ancestry coverage would need an actual binding and a proof that its required coverage follows from the source.

## Verification

`python research/strominger/checkers/check_sector_request_response.py`

14 exact checks passed. [Receipt](results/sector-request-response.json) contains all three traces, their histories and fibers, an arrival-length census and source hashes. Only labelled incidence, marked-table recovery and the specified response policy are tested. No coefficient dynamics, continuous rotation, physical P/E readout, esd7 assembly or Pb-208 realization is claimed.
