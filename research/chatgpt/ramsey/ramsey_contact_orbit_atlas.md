# Six-label contact incidence orbit atlas

These systems are conditional on the 6-regular branch and the preliminary contact-size and singleton-count reductions. The 478-system input is reconstructed by `ramsey_composition_propagation.py`. The matching, fiber, and repeated-triple restrictions reduce it to 84 representatives, or 34 complete incidence-isomorphism types under permutations preserving singleton labels.

For every recorded type, Hall-deficient subset clauses (sizes 2 to 5) and A-triangle clauses are subjected to Boolean unit propagation without degree constraints. The two surviving types are excluded by separately verified signed-capacity inequalities.

| Type | Singleton labels | Input representatives | Missing pairs | Triple contacts | Double contacts | Closure |
|---:|---:|---:|---|---|---|---|
| 1 | 4 | 2 | 03, 12 | 014, 235 | 01, 02, 05, 13, 15, 23, 24, 34, 45, 45 | Hall–triangle closure |
| 2 | 4 | 4 | 05, 14, 23 | 034, 125 | 01, 02, 04, 13, 15, 24, 25, 34, 35, 45 | Hall–triangle closure |
| 3 | 4 | 1 | — | 034, 125 | 01, 02, 05, 13, 14, 23, 24, 35, 45, 45 | Hall–triangle closure |
| 4 | 4 | 2 | 03, 12, 45 | 024, 135 | 01, 04, 05, 14, 15, 23, 24, 25, 34, 35 | Hall–triangle closure |
| 5 | 5 | 2 | 05, 14 | 012, 023, 345 | 01, 04, 13, 15, 24, 25, 35, 45 | Hall–triangle closure |
| 6 | 5 | 2 | 04, 15 | 012, 023, 345 | 01, 05, 13, 14, 24, 25, 35, 45 | Hall–triangle closure |
| 7 | 5 | 4 | 04, 13 | 012, 025, 345 | 01, 03, 14, 15, 23, 24, 35, 45 | Hall–triangle closure |
| 8 | 5 | 1 | 05, 13 | 012, 034, 245 | 01, 03, 14, 15, 23, 25, 35, 45 | Hall–triangle closure |
| 9 | 5 | 2 | 04, 13 | 012, 035, 245 | 01, 03, 14, 15, 23, 25, 34, 45 | Hall–triangle closure |
| 10 | 5 | 2 | 05, 14 | 012, 135, 234 | 01, 03, 04, 15, 24, 25, 35, 45 | Hall–triangle closure |
| 11 | 5 | 2 | 13 | 012, 045, 235 | 01, 03, 14, 15, 24, 25, 34, 35 | Hall–triangle closure |
| 12 | 5 | 2 | 04, 13 | 012, 245, 345 | 01, 03, 05, 14, 15, 23, 25, 34 | Hall–triangle closure |
| 13 | 5 | 1 | 23 | 045, 125, 135 | 01, 02, 03, 14, 24, 25, 34, 35 | Hall–triangle closure |
| 14 | 6 | 2 | 05, 14 | 012, 013, 234, 245 | 01, 04, 15, 23, 35, 45 | Hall–triangle closure |
| 15 | 6 | 8 | 05, 14 | 012, 013, 245, 345 | 01, 04, 15, 23, 24, 35 | Hall–triangle closure |
| 16 | 6 | 4 | 05, 14 | 012, 013, 234, 235 | 01, 04, 15, 24, 35, 45 | Hall–triangle closure |
| 17 | 6 | 2 | 05, 14 | 012, 013, 234, 345 | 01, 04, 15, 24, 25, 35 | Signed capacity required |
| 18 | 6 | 1 | 05, 13 | 012, 023, 034, 345 | 01, 14, 15, 24, 25, 35 | Hall–triangle closure |
| 19 | 6 | 1 | 05, 13 | 012, 023, 034, 245 | 01, 14, 15, 25, 34, 35 | Hall–triangle closure |
| 20 | 6 | 2 | 05, 13 | 012, 023, 034, 145 | 01, 15, 24, 25, 34, 35 | Hall–triangle closure |
| 21 | 6 | 2 | 05, 34 | 012, 023, 145, 235 | 01, 04, 13, 24, 35, 45 | Hall–triangle closure |
| 22 | 6 | 8 | 05 | 012, 023, 145, 345 | 01, 04, 13, 24, 25, 35 | Hall–triangle closure |
| 23 | 6 | 1 | 05, 14 | 012, 023, 234, 345 | 01, 04, 13, 15, 25, 45 | Hall–triangle closure |
| 24 | 6 | 1 | 05, 14 | 012, 023, 235, 345 | 01, 04, 13, 15, 24, 45 | Hall–triangle closure |
| 25 | 6 | 1 | 05, 14 | 012, 023, 235, 245 | 01, 04, 13, 15, 34, 45 | Hall–triangle closure |
| 26 | 6 | 2 | 05, 14 | 012, 023, 245, 345 | 01, 04, 13, 15, 25, 34 | Hall–triangle closure |
| 27 | 6 | 2 | 05 | 012, 023, 134, 345 | 01, 04, 15, 24, 25, 35 | Hall–triangle closure |
| 28 | 6 | 2 | 05 | 012, 023, 134, 245 | 01, 04, 15, 25, 34, 35 | Hall–triangle closure |
| 29 | 6 | 2 | 05, 14 | 012, 023, 135, 245 | 01, 04, 15, 23, 34, 45 | Hall–triangle closure |
| 30 | 6 | 1 | 05, 14 | 012, 023, 135, 234 | 01, 04, 15, 25, 34, 45 | Hall–triangle closure |
| 31 | 6 | 4 | 05, 13, 24 | 012, 023, 145, 345 | 01, 04, 15, 23, 25, 34 | Hall–triangle closure |
| 32 | 6 | 2 | — | 012, 023, 045, 134 | 01, 15, 24, 25, 34, 35 | Hall–triangle closure |
| 33 | 6 | 8 | — | 012, 045, 134, 235 | 01, 03, 15, 23, 24, 45 | Hall–triangle closure |
| 34 | 6 | 1 | — | 045, 124, 134, 234 | 01, 02, 03, 15, 25, 35 | Signed capacity required |

**Total:** 34 complete incidence types; 32 Hall–triangle contradictions and 2 signed-capacity types.

This is an exact finite orbit reduction, **not** a non-enumerative proof of a universal obstruction theorem.
