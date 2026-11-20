# Database constructor source-to-operation audit — 2026-11-19

Scope: first two seed papers of `db-literature-ramsey-constructor`, not a verdict on the literature. Compare the authors' preprint sections with our separately specified translation.

| Source and operator | Required input | What the paper supplies | Missing constructor step |
|---|---|---|---|
| [Free Join](https://arxiv.org/abs/2301.10841), §§3.1–3.3, definitions 3.1, 3.5, 3.7 | Base relation tuples; conjunctive query; valid plan partitioning its atoms | Generalized hash tries; progressively join compatible partial variable bindings; enumerate the query result | A join on `Red(x,y)` reads an existing graph. To *construct* graphs we supply tables of admissible assignments to edge variables and a role-set schedule. The paper supplies execution semantics rather than the choice of Ramsey cells. |
| [Space-Time Tradeoffs for Conjunctive Queries with Access Patterns](https://arxiv.org/abs/2304.06221), definition 2.1, §§3–4 | Populated database, query, designated access pattern, resource budget | Partially materialized tree decompositions and a preprocessing/online split; build intermediate views to answer subsequent bindings within space–time bounds | Choose which shared edge assignments form the boundary and what an answer must retain (existence versus actual witnesses). A policy to cache an intermediate relation does not establish that its cells are redundant for the Ramsey readout. |

## A constructive application, and its exact limitation

[SQLite probe](checkers/ramsey_db_constructor_join_probe.py) · [counts](results/ramsey_db_constructor_join_probe.txt). Let a column denote an unknown edge color, not a vertex in an input graph. For each red-pattern placement insert the relation of all local color vectors except all red; do the dual construction for the blue pattern. Rename columns by unordered role pairs and natural-join on the shared columns. Assignments in the join are in bijection with valid labeled colorings: every join row satisfies every local constraint, and any avoiding coloring restricts to a tuple in each relation. Isolated edge variables range over both colors. The external control loop generates role sets in increasing order and stops on the first empty join. Its role-set schedule, constraint compilation and stop rule are our inputs to the DB algorithm.

At (3,3) the counts for orders 2 through 6 are 2, 6, 18, 12, 0. SQLite evaluated ordinary natural joins; this does not benchmark the Free Join implementation or instantiate the second paper's complexity bounds. This is a finite-model enumeration baseline, not a four-dimensional lift, a threshold shortcut, or a literal cell-correction witness. Wide SQL plans also hit implementation limits.

## Next discrimination

Start with the nontrivial (3,3) benchmark. Cut the placement query into two groups of constraints. Compare partial assignments by their shared-boundary signature and by the sets of external assignments that complete them. Test whether a literature-derived projection or factorization yields the same completion classes while retaining provenance of multiple internal witnesses. Record actual class counts, sizes, and recovery cost against complete enumeration. Then test (3,4) under the unchanged projection. Reserving or materializing a cache entry and deriving an intrinsic reduction are distinct claims.

Forward citation leads (bibliographic leads, not audited theorem imports): [Conjunctive Queries with Free Access Patterns under Updates](https://doi.org/10.46298/lmcs-21(2:23)2025); [The Space-Time Complexity of Sum-Product Queries](https://doi.org/10.1145/3767719). No evidence here selects a definitive source for the full Ramsey constructor.
