# Compare first, complete second: 144-channel incidence pilot

## Proposed search and explicit trial interpretation

Operator correction: compare the selected domain cells through their codomain
representations, making all 12 x 12 comparisons; for each match, attempt a
coherence complex containing its codomain cell and both domain cells.

This pilot uses the prior six-carrier geometry without particle labels in the
search algorithm. Each tetrahedron has twelve directed edges. Its codomain
map is its explicit inclusion in the common FCC incidence space. A match is
exact equality of both ordered endpoints. The matched codomain cell is therefore
an **edge (1-cell)** in this trial, not a tetrahedral carrier.

The tested completion rule is a face-connected chain through that edge, with
at most one additional carrier from the existing six-carrier pool. Every shared
face, matched edge and source channel is retained. This is an incidence-level
candidate completion, not the full WG coefficient/filler law.

## Fresh result

| Domain pair | Comparisons | Matches | Candidate completion |
|---|---:|---:|---|
| P1, E1 | 144 | 2 | P1 -> N1 -> E1 |
| P2, E2 | 144 | 2 | P2 -> N1 -> E2 |

The two matches in each case are opposite orientations of the shared edge.
They produce one geometric cell chain, with both comparison witnesses retained.
The middle carrier shares a full face with each endpoint, and both faces
contain the matched edge. Its label N1 is read only after the geometry search.
No neutron-species predicate was used to select it.

This recovers the existing shared-neutron construction. It does not generate
its carriers from scratch or identify the second neutron by this pair alone.

## Full bounded audit

All 30 ordered pairs of distinct carriers were tested: **4,320 comparisons**.
The receipt contains pair summaries and all 144 individual comparisons for
each of the two displayed cases. A common signed coordinate permutation plus
lattice translation preserves every match decision and candidate cell chain.

Four negative controls reject:

- a fabricated codomain match;
- the endpoint union with only a common edge, lacking the required face chain;
- the wrong middle carrier;
- reusing the entry as the bridge.

The completion pool is explicitly finite. The result is not a proof of unique
completion across the entire lattice. The two-step face-chain requirement is
the trial's operational closure criterion, not a theorem that arbitrary WG
coherence is equivalent to it. The other existing field comparator (operator
outer products of decorated complex fields) remains a separate interface.

## Reproduce

```sh
node scripts/prepare-helium-carriers.mjs --check
python research/realization-tower/check_codomain_match_search.py
```

Both freshly passed. [Receipt](results/codomain-match-search-v1.json).
No viewer search implementation, glossary change or proof-status promotion is
included in this result.
