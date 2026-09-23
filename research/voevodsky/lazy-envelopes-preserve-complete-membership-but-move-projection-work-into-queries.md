# Lazy envelopes preserve complete membership but move projection work into queries

## Executable state

The prototype retains original rational fine rows and a sequence of projection nodes. A node names one coordinate to retire. It streams zero rows and normalized positive/negative pairs from its parent on demand; it never stores the entire projected row table. Each emitted row carries a sparse nonnegative derivation over the original row context.

For membership at a proposed point, it streams its parent's rows, rejects any violated zero row, and computes the greatest lower and least upper bound for the retired coordinate. Incompatible bounds produce one separating pair with an exact original-row derivation. Compatible bounds select a value in the interval and recursively request a parent lift. The eventual lift satisfies every original row.

Thus the state represents all possibilities, not the rows used in one answer. Completeness follows inductively from the scalar lower/upper pairing theorem. This is a complete finite rational membership/separation/lifting construction for the represented linear systems, not a time bound or a fully validated external API.

## Owning quadratic-family controls

Use the source-certified local box of the m=4 joint image from Grothendieck's quadratic projection construction, in coordinates (x,y,H,z). The n lower/upper envelope pieces and eight box rows are retained exactly.

First retire H, leaving (x,y,z). Then retire x, leaving (y,z). The second operation retires a public moment coordinate in this chart, not a second raw atom audit. This tests successive coordinate projection; a two-raw-audit retirement workload is not claimed.

A new public frame z<=1 is appended to the original row context, with zero coefficients on retired coordinates. Both original and refined states are queried; earlier evidence is never replaced. The wrapper recreates the projection nodes over the enlarged tuple rather than implementing a public immutable-state API.

For n=2,4,8, 30 queries pass independent verification: 18 exact separating proofs and 12 admitted fine lifts. The verifier reconstructs the fine evidence, checks every cut's original-row combination, and independently inverts the owning (U,V,t0,t1) map to obtain actual source-box lifts. It also checks the analytic expected answers for the chosen controls. The all-point completeness argument is the envelope induction, not the finite tests.

## What successive retirement costs

The retained base state has 2n+8 rows (one extra after refinement). The first projected body already has n^2 genuine pair facets. For the unrefined five-query workload:

| n | Retained base rows | Genuine first-stage pair facets | Original-row visits | First-stage rows generated |
| --- | ---: | ---: | ---: | ---: |
| 2 | 12 | 4 | 228 | 45 |
| 4 | 16 | 16 | 400 | 93 |
| 8 | 24 | 64 | 888 | 261 |

The second stage consumes the first stage's streamed rows, so quadratic work has not vanished. At further stages, repeated scans and nested pair generation can grow much faster. This implementation trades projected-table storage for recomputation; it proves no controlled arbitrary-depth growth law. Sparse provenance is flattened into dictionaries of original row weights; shared proof-DAG storage is not yet implemented or measured.

These counts are workload operations, not bit complexity. Original frames, schema, provenance context and exact rational values remain retained. The prototype does not reclaim evidence storage; it offers complete projected queries without persistent flat compilation.

## Remaining gate

Optimization is not implemented here. The oracle can in principle provide a finite projected cut dictionary for an exact bounded LP loop, but the large implicit dictionary and nested generation costs still need explicit treatment. A useful next backend would choose between direct fine-space solving, flat projected compilation, and this lazy envelope access based on their actual costs rather than assume laziness always wins.

This result establishes the missing complete-oracle layer alongside sparse individual-proof transport. It does not establish compactness of every successive projection, general solver totality, audit re-exposure after discarded provenance, or equality of fine carriers after projection.

## Reproduction

    python research/voevodsky/checkers/check_lazy_envelope_state.py
    python research/voevodsky/checkers/verify_lazy_envelope_state.py

Artifacts:

- `results/lazy-envelope-state.json`
- `results/lazy-envelope-state-verification.json`

No optimizer is invoked. The local source lift is checked directly; upstream all-m analytical admission was not freshly replayed.
