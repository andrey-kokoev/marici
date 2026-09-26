# Consuming queries preserve the four-cell channel semantics

Implemented an attributed principal-port net with two rules: EB--FB becomes two independent VALUE agents, each retaining exactly one original boundary record; VALUE--READ consumes both agents and returns an ANSWER at its OUT. This replaces the shared-remainder representation with separate channel carriers, not copies of either source record.

Both family cancellations and all four one-shot queries may interleave. Exhausting all 80 complete schedules (224 schedule-tree edges, including 140 partial-answer occurrences) preserves the live denotation of every pending/completed channel and ends in four identical named answers. Consumed pairs cannot be replayed. Erasing a still-pending value after another query finishes is detected by the observer.

This experiment supports a linear interface that preserves source identity, normalized pole record and two exact fermionic components through query execution. It does not promise unlimited reuse: there is no duplicator, and re-querying consumed source support is not an admitted operation. Values are mathematical attributed payloads; arithmetic has not been compiled into a finite alphabet. No contour weights or amplitude normalization are inferred.

Implementation: `research/nima/checkers/four_cell_query_net.py`.
Checker: `research/nima/checkers/check_four_cell_query_net.py`.
Result: `research/nima/results/four-cell-query-net.json`.
