# Composed origin and acquisition audits need only the origin bit

## Frozen extension

Before minimization, freeze two audits on the existing coupled system:

- origin audit: whether the known initial prefix was [0,1];
- acquisition-before-cut audit: whether an accepted acquisition occurred before source event 3.

The acquisition bit initializes false, becomes true on the relevant accepted acquisition, and thereafter persists. Origin stays invariant. Each audit accepts exactly its matching bit value and leaves the state unchanged; rejection is observable.

The existing source/evidence coupling verifier is freshly replayed. A reachable product exploration independently accumulates the acquisition bit from accepted transitions rather than inferring its historical truth from a displayed verdict.

## Result

| Continuation language | Minimal states |
| --- | ---: |
| Original | 62 |
| Origin audit | 70 |
| Acquisition audit | 62 |
| Both audits | 70 |

There are still 638 reachable augmented concrete states. Acquisition-before-cut is already determined by every old observer class. The two-bit lift is valid, but its acquisition coordinate is redundant. There are exactly 70 compatible (old class, origin bit, acquisition bit) triples.

This is a positive finite composition result and a correction to the expectation that this particular dynamic predicate would require additional provenance. The protocol retains operational consequences of acquisition: producer evidence can subsequently be delivered, while received/issued evidence already appears in the retained output. Acquisition is restricted to the pre-cut corner. Consequently its historical truth is already observable through present or future protocol behavior.

## Complete lift and composition certificate

The checker constructs all four minimal quotients and exports distinguishing words for every pair of different classes. The combined quotient projects to the base and both individual audit quotients. All 3,640 output/action projection checks pass.

Known initialization and all 12,760 extended-label update/lift checks establish the live lift for arbitrary finite executions. Audit and rejected transitions retain the provenance; the acquisition update is checked against the independently explored augmented source state.

The prior origin split still provides the necessity of one additional binary distinction. The acquisition audit adds none in this finite contract. Successful lift lookup continues to assume faithful origin initialization and retention.

## DPC disposition

Corroborated for the two declared audits. Combining individually sufficient provenance supports the combined language and its projection squares. This instance does not demonstrate a need for new dynamically updated storage, because the chosen evolving predicate is already present in the minimal operational state.

A future experiment could freeze delivery-before-cut: after the cut the same received value may conceal when delivery occurred. That is a distinct extension requiring its own test; no result for it is asserted here.

## Reproduction

    python research/voevodsky/checkers/check_composed_provenance_live_lift.py

Artifacts:

- `results/composed-provenance-live-lift-contract.json`
- `results/composed-provenance-live-lift.json`
