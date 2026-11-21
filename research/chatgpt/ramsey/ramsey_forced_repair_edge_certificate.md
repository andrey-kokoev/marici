# A short completion obstruction, before choosing finished switches

The general size/degree theorem remains open, but the regular182 example now has an explicit small certificate ruling out ALL completions of the prescribed deletions into two separate nontrivial switches.

Delete red edges(2,11),(8,21),(4,19),(10,17), leaving a partial graph H. The two independent support blocks are {2,8,11,21} and {4,10,17,19}. Require one new perfect matching in each block, without restoring the deleted edges. There are two choices per block.

In H, the seven-set I={0,10,11,15,16,17,21} is independent. Among ALL permissible new edges in either block, the ONLY edge inside I is(11,21). Every valid completion must therefore add(11,21).

Degree restoration in the first block then FORCES the companion(2,8). But H already contains(2,16),(8,16). The forced companion creates triangle(2,8,16). Contradiction.

This certificate needs just:
1. one explicit independent-seven clause;
2. the four-endpoint degree constraint;
3. one explicit common-neighbor triangle guard.
It excludes both alternative rewirings in the second block as well as the unsafe choice in the first. It does not merely reject the originally proposed completed pair. The seven-set can be checked directly on H; no graph catalogue or enumeration of completed outputs is required to verify the argument.

A second seven-set J={1,2,3,4,6,8,11} is also independent in H and has candidate repair edges(2,8) or(8,11). This explains why simply omitting the unsafe companion does not make a valid repair. Under the full degree constraint, J is redundant: I plus degree balance already forces the triangle. The checker is named ramsey_two_clause_completion_certificate.py because it records both clauses; the logical core is one clause.

A separate omission check, keeping only safe repair edges(11,21) and(10,19), yields triangle-free graphs with8 individual-A sevens,4 individual-B sevens,21 joint sevens; the other operation leaves5 and3 individual defects unrepaired. Thus removing degree-balancing edges is not a solution even if one temporarily tolerates degree deficits.

Scope is essential: removed edges and the two four-vertex blocks are prescribed; added edges may not connect the blocks or undo deletions. Allowing a different removal pattern, cross-block re-pairing, or non-degree-preserving changes defines a different completion problem. We have not proved every would-be low-order repair counterexample at22 vertices and minimum degree5 admits such a forced-edge certificate.

Next structural task: determine whether all relevant impossible completion systems admit a bounded certificate of this form (or a short chain of forced repairs), and derive existence of those certificates from the Ramsey and degree constraints. This would turn the global empirical closure law into a local verifiable obstruction theorem.
