# DPC: transport composition

## Problem

Do pivot-canonical A14 DAG closures define a compositional transport of source words?

## Bold conjecture

Canonical DAG closure is a path-independent source-word transport from A12 through A14 to A16.

## Named rivals

- an endpoint-normalized exact section depending only on the target descriptor;
- identity coefficient transport;
- shifted-basis re-solving without total span.

## Risky consequences

Every output must bind its input basis and word, serialize a linear generator map, link A12-to-A14 and A14-to-A16 predecessors, and compare direct with iterated A16 words by exact residuals.

## Strongest falsification and exact residual

All 780 closure records omit the input basis digest, input word digest, linear generator-map digest, and predecessor transport ID. There are zero A16 records and zero composition witnesses. The closure algorithm selects an exact word from the endpoint target; it does not apply a map to the input word.

## Disposition

The conjecture is rejected at the first missing typed object: a linear map on labelled source-generator modules. Surviving scope is exact pivot-canonical endpoint sections for 780 A14 targets. No source-word transport, composition, path independence, or arbitrary-even functor follows.

Acceptance requires a serialized generator map on every `T`, `S_K`, and `Q` descriptor, linearity and exact row-commutation tests, and direct-versus-iterated A16 comparisons for x4, both x2y2 orders, and y4.

## Verification

- `research/voevodsky/check_cosmology_transport_composition_dpc.py` — exit 0
- `research/voevodsky/results/cosmology_transport_composition_dpc.json`
