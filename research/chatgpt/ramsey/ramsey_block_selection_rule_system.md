# Selecting compatible blocks from precompiled low-order repair rules

ramsey_block_selection_repair_rules.py compiles a reusable rule system from only SINGLE-SWITCH and PAIR-SWITCH blue defects. Then it predicts all larger disjoint coalitions, without enumerating their independent sevens during selection. Completed outputs are checked afterward for verification.

Candidate operations are individually invalid but triangle-free two-edge switches. Give candidate i a selection bit x_i. Rules are:
1. Support conflicts: not(x_i and x_j) whenever the four-vertex supports overlap.
2. For each seven-set I created by switch i: x_i implies OR of all x_j whose added edges hit I and whose supports are compatible with i.
3. For each seven-set born only after the disjoint pair i,k: (x_i and x_k) implies OR of all compatible selected repairers of I.
Repeated repairer sets are merged; supersets of an already required repairer set are redundant and removed. Empty repairer sets forbid the triggering coalition.

These rules are NECESSARY without any catalogue assumption: a final independent seven from a selected birth set must be destroyed by some added edge. Disjoint-support updates cannot repair it by deleting edges. Thus the rule system cannot reject a valid coalition in its candidate domain.

Results across all ten regular catalogue types:115,348 nonempty disjoint candidate coalitions tested (including663 singles). Exactly31 pass the compiled rules:12 pairs,18 triples,one quintuple. Every predicted output is valid; no false positives. No valid outputs are missed by the necessity argument. Source191 predictions are5 pairs,10 triples,one quintuple; source190 has none. Source182 gives3pairs+2triples;183 onepair+onetriple;184 onepair;185 onepair+onetriple;186 onepair+fourtriples;187..189 none.

Therefore, IN THIS FINITE DOMAIN, singleton and pair-born repair rules completely determine valid coalitions of all possible sizes (at mostfive). No triple-born rule is needed, although the general bounded-birth theorem only guarantees sufficiency when rules up to aritythree are included. The quintuple is predicted from lower-order obligations; its five-way irreducibility does not require a primitive five-way constraint.

This is a constructive selection rule after a one-time defect compilation, not a claim that all obligations are visible from a small graph neighborhood. The precomputation still enumerates global independent sevens after individual and paired moves. Nor is the selection problem2-SAT: clauses may have many alternative repairers in their positive heads. The earlier2-SAT theorem concerned mandatory re-pairing choices AFTER deletion blocks were fixed, a different variable space.

Next explanatory task: show why triple-born constraints are redundant under the lower-order rule system, or derive the rule templates directly from graph structure instead of enumerating defects. The evidence establishes exact finite prediction but not a universal rule for arbitrary graph orders, nonregular starts, overlapping operations, or coalitions containing initially valid moves.

Artifacts: executable, JSON (all candidate switches, compact birth/repairer-mask clauses, counts, sample models), run log. Bit j of a repairer mask means candidate j can destroy the corresponding defect; zero means no compatible candidate can repair it.
