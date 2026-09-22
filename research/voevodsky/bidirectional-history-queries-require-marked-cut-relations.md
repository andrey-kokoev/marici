# Bidirectional history queries require marked-cut relations

## Frozen question

Test whether the current local view and transported endpoint witness set suffice for both future behavior and backward questions conditioned on the whole observed history. The backward question is fixed before search: which behavioral witness occupied the immediately preceding marked cut of a two-step admitted history?

The actual relational runtime packet is independently verified. Both compared histories start from the same known singleton behavioral witness and have equal length. The candidate state retains only the endpoint view and witness set.

## Exact counterexample

Starting from packet row 2 (origin zero, a pending record, nothing received), consider:

    audit-origin(0); deliver: 2 -> 2 -> 1
    deliver; deliver:         2 -> 1 -> 1.

All steps are admitted. Both histories end at row 1 with the same local view and singleton witness set. Their initial/final relation is also identical, {(2,1)}.

At the marked intermediate cut, the first history has no received record and the second has received zero. Their history-conditioned predecessor sets are {2} and {1}. Thus neither the endpoint witness set nor the unmarked initial/final relation answers this query faithfully.

Direct transpose of delivery returns both predecessors {1,2}. That is the correct unconditioned compatibility answer. It loses the conditioning supplied by the earlier part of the observed history.

## Minimal structural repair for the queried cut

Retain the history-constrained relation from the marked cut to the current cut. Here the relations are {(2,1)} and {(1,1)}. Their backward fibers at the current endpoint recover the respective answers.

The checker additionally verifies the marked-cut construction for all 1,524 accepted two-step paths in the packet. General correctness is the elementary relational join/projection identity: preserve the shared intermediate witness before projecting to the requested pair of cuts. These checks do not establish a finite storage bound for arbitrarily many requested historical cuts.

## DPC disposition

The endpoint-set sufficiency conjecture is refuted for history-conditioned backward queries. Forward continuation sufficiency remains valid, as does unconditioned predecessor querying from the current set. The distinction is which history constraints are part of the question.

Structurally, a state is a boundary summary. A marked development retains correlations between boundaries. Exchanging history and possibility relative to an interior cut requires those correlations; an endpoint-only summary need not preserve them.

The result does not require a unique concrete source history. Set-valued relations across marked cuts retain multiple possibilities while preventing witness switching. It also does not turn a backward compatibility query into authorized reverse execution.

## Reproduction

    python research/voevodsky/checkers/check_endpoint_witness_bidirectional_sufficiency.py

Artifacts:

- `results/endpoint-witness-bidirectional-contract.json`
- `results/endpoint-witness-bidirectional-sufficiency.json`
