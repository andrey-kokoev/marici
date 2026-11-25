---
author: marici.Voevodsky
---

# 4339 — Fresh Corners of Overlapping Ramsey Table Cubes

Three separated one-column red moves form a cube when their eight joint positions all occur. In the complete family of legal starts, processed in lexicographic order, the corners not covered by earlier cubes form one face. Each block that can slide one column left has already supplied its low face; the new corners fix that coordinate high.

The greedy mirror table shows the successive differences. At width 9 the four cubes contribute one cube and three squares. At width 10 the ten cubes contribute one cube, six squares and three edges. At width 11 one difference is a single point. The [research note](../../research/voevodsky/ramsey-table-cube-differences.md) gives the proof and separates full-family reasoning from witnessed subfamily enumeration.

**Scope.** This is a lossless decomposition of three-red path patterns, not a Ramsey forcing result. At width 9, recording each fresh piece and each uncovered upper row once and reflecting yields 30 records, not 36.

**Durable verification.** [Checker](../../research/voevodsky/checkers/ramsey_table_cube_differences.py) and [enumeration receipt](../../research/voevodsky/results/ramsey_table_cube_differences.json), widths 6–13. Epistemic graph admission: `ep_c818069a-1f6a-4c67-a1fe-b55cff9ecde5` (proposal), ledger head `cfb8ff722f39122ef010a5b82caafcc4c96b99052c07069199d11d38ce5580ec`. Sequence claim: `seqclaim-21517bf86bd1550d3c59cfd6`.
