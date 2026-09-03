# Rees provenance memory bound

Problem: decide whether all-pivot provenance retention is feasible for the full
Rees presentation.

Bold conjecture: provenance remains sparse enough for direct retention, or its
density is already controlled by current receipts.

Rivals: direct sparse vectors; dense vectors; checkpointed elimination replay;
and target-only certificate extraction.

Risky consequence: existing receipts must report density or operation counts to
support direct feasibility. Independently, dense storage gives an exact raw
ceiling.

Strongest falsification attempt: the three relation systems have 9,780, 19,560,
and 29,340 rows and ranks 4,275, 8,558, and 12,847. Storing a 32-bit row id and
32-bit coefficient for every dense provenance entry requires 4,689,079,680
bytes, about 4.37 GiB, before map and allocator overhead. Existing receipts
report neither provenance density nor elimination-operation count.

Disposition: revised. Direct feasibility is unestablished; the bounded
prototype does not predict full density. No full run was launched. The next
leaf adds count-only bounded-prefix instrumentation to discriminate direct
vectors from checkpointed or target-only replay.
