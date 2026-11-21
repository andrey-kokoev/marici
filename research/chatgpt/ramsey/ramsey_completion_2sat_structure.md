# Fixed-block degree-preserving completion reduces to 2-SAT

This is a structural result, not a proof of the global low-order repair law.

Fix disjoint four-vertex blocks in a valid triangle-free graph with no independent seven. Delete a matching of two old edges in each block. Require each block to receive one of its TWO alternative perfect matchings, without restoring the original matching and without cross-block additions. One Boolean variable per block chooses the re-pairing. These are NOT the apply/omit variables used in the five-way cooperation cube.

## Red constraints are unary
An option containing an already-present edge is forbidden. A triangle-producing option is forbidden. Since added edges form a global matching, a new triangle cannot use two added edges. Each triangle test is therefore local to an option and imposes a unit clause. Guards can be read in the graph after all deletions; disjoint blocks do not remove one another's cross-support guard edges.

## Blue constraints have at most two literals
Consider any independent seven I in the graph after deletions. A completion must add some edge inside I.
- If I contains three or four vertices of one block, BOTH alternative perfect matchings have an internal edge in I. The repair clause is automatically true; discard it.
- Otherwise I meets each block in at most two vertices.
- Because the ORIGINAL graph had no independent seven, I contains an original red edge removed from some block. In that block I contains exactly its two endpoints. That pair cannot be restored by either allowed alternative, so this block contributes NO repair literal but consumes two of I's vertices.
- At most five vertices remain. Every other block contributing a repair literal consumes another two vertices. Thus at most TWO blocks can contribute.

Every nontrivial blue-repair clause is therefore empty, unary, or binary. Together with red unit clauses, the entire prescribed completion problem is exactly2-SAT. It can be decided by implication-graph contradictions rather than searching every finished graph. The obstruction sets still need to be generated or supplied as certificates; the reduction does not itself guarantee a constant-size proof.

More generally the same argument bounds clause width by floor((r-2)/2) for forbidden independent r-sets, under these exact completion rules.

## What the regular catalogue says about forced propagation

ramsey_completion_implication_probe.py tests three disjoint deletion blocks from all ten regular types, choosing blocks that admit an individually invalid but triangle-free switch. All663 distinct tested blocks have EXACTLY ONE triangle-free alternative. Thus red admissibility already fixes their rewiring choices.

Among46,720 block triples,46,702 are refuted by unit propagation and18 are satisfiable. No irreducible implication-cycle counterexample is found, but this is less mysterious than it first appears: the red constraints already fix every variable. Therefore this test does NOT establish a general theorem that all2-SAT completion obstructions admit short forced-edge chains. The selected regular instances simply have no remaining local re-pairing freedom.

Consequences for the larger investigation:
- For a prescribed collection of removal blocks, we now have an exact bounded-width constraint description.
- In the tested regular witnesses, the genuinely combinatorial choice lies in WHICH blocks to operate on, rather than how to reconnect a chosen block.
- This does not reduce five-way cooperation to one-way repair: block-selection/apply-omit variables are different from mandatory re-pairing variables. A unique local rewiring can still need four other selected blocks to make the global output valid.
- Global size/degree protection remains unproved. The reduction handles verification of candidate block systems, not their universal exclusion or generation.

Files: ramsey_completion_implication_probe.py/JSON/run log. The earlier ramsey_two_clause_completion_certificate.py is a particularly small unit-refutation example.
