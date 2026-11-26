---
author: marici.Voevodsky
---

# 4346 — Ramsey Growth Depends on Core Capacity and Joint Coverage

**Question:** [Entry 4345](20261125-4345%20Ramsey%20Branches%20Can%20Agree%20Through%20Arbitrarily%20Many%20Moves.md) showed that branches can agree through arbitrarily many moves. What now connects compatibility to witness size?

**Answer:** For the triangle-free row, growth has an exact description. It depends on how many whole red neighborhoods a core can support, less the size lost by choosing that core. Tests across all roots can exclude whole classes before we solve for those neighborhoods. No new Ramsey number follows from this entry.

## An exact target replaces a guessed increment

Write \(M_k=R(3,k)-1\). In a \((3,k+1)\) graph, fix a root. Its blue neighbors form a \((3,k)\) core \(C\). Its \(d\) red neighbors are mutually blue. Each has a red support in \(C\) that contains no red edge. For every blue clique \(Q\) of the core, at least \(\max(0,d+|Q|-k)\) supports must meet \(Q\). Otherwise \(Q\) and the neighbors that miss it form a forbidden blue clique. These requirements also suffice. Let \(\operatorname{cap}_k(C)\) be the largest feasible \(d\). Then

\[
M_{k+1}-M_k=1+\max_C\{\operatorname{cap}_k(C)-(M_k-|C|)\}.
\]

The maximum includes smaller cores. At \((3,6)\), a tested 12-vertex core supported four neighbors, while the maximum 13-vertex core could not support three. The [category specification](../../research/voevodsky/ramsey-threshold-category.md) separates threshold inclusion, induced extension, and restriction to a root core.

The million-cell rank fit is not a Ramsey error measurement. The [interval audit](../../research/voevodsky/checkers/ramsey_interval_error_1000.py) found one unordered bound violation for the original formula, at \((3,13)\). Most other cells remain undecided. Changing the diagonal discount did not repair this boundary cell. A two-step row rule passed the stored intervals through 26, but a parity-dependent one-step rule reproduces its predictions exactly. The fit does not establish a two-step mechanism. [Parity test](../../research/voevodsky/results/ramsey_row3_parity.json).

## Constraints across roots reduce the search

For a triangle-free red graph on \(n\) vertices, the sum of the red edge counts in all blue root cores is \(n e(G)-\sum_v d(v)^2\). The core census and this identity recover two known thresholds:

- At order 18 for \((3,6)\), the average core has 20 edges. No possible core has fewer. Equality forces a single 12-vertex core type. Its required fractional support mass exceeds five. A separate construction attains 17 vertices. [Counts and rational certificate](../../research/voevodsky/results/ramsey_36_edge_average.json).
- At order 23 for \((3,7)\), the average and a local degree count force red degree six at every vertex. Each root then has a 16-vertex core with 33 red edges. In every one of the 39 types, six supports would miss some blue five-clique twice. That clique and the two neighbors would form a blue seven-clique. A separate construction attains 22 vertices. [Degree reduction](../../research/voevodsky/results/ramsey_37_edge_average.json) · [Independent generation of all 39 residual types and integer certificates](../../research/voevodsky/results/ramsey_37_catalogue_free.json). The latter check removes reliance on the stored catalogue for the **33-edge class**, not for every input to the degree reduction.
- At order 28 for \((3,8)\), some degree-seven root must have a 20-vertex core with 44–49 edges, using the stored edge minima. Six-clique demands exclude the 15 stored 44-edge types. For 224 sampled 48–49-edge cores, five-clique demands and six-clique demands each admit fractional solutions. Their conjunction excludes every sample. This is not a census of the whole window. [Joint certificates](../../research/voevodsky/results/ramsey_38_joint_window.json). Reversing the test on a fixed 27-vertex seed gave concrete blocked attachments and repair costs, not an order-28 witness. [Repair test](../../research/voevodsky/results/ramsey_38_break_triple.json).

## When arithmetic represents an actual graph square

If both optimal sides survive in one optimal endpoint over the same optimal seed, their intersection is exactly the seed. The mixed difference then counts vertices outside their union. In one 17-vertex \((4,4)\) endpoint, 272 pairs of maximum sides share a maximum five-vertex seed. Six vertices remain outside each union. But all 3,536 seed matches failed for the tested maximum 13-vertex \((3,5)\) and 17-vertex \((4,4)\) sides. Compatible orders do not guarantee compatible embeddings. Two 24-vertex sides can coexist over a 17-vertex seed in a 36-vertex \((5,5)\) graph; optimality is open. [Positive square](../../research/voevodsky/results/ramsey_maximum_square_33.json) · [Negative square](../../research/voevodsky/results/ramsey_asymmetric_square_all.json) · [36-vertex witness](../../research/voevodsky/results/ramsey_four_square_endpoint_36_cadical195_25s.json).

On the constant-sum path from \((3,7)\) to \((7,3)\), a verified 29-vertex middle graph retains both a 17-vertex seed and a selected 24-vertex seed. Only one of seven tested 17-vertex types permits their largest possible overlap in a legal union. We did not close the path. [Middle join](../../research/voevodsky/results/ramsey_sum10_middle_join.json).

## What survives a change of test or description

- **Same verdict is weaker than same witnesses.** On 16 initial order-11 cores, testing only blue triples and four-cliques gave the full extension verdict. Generating all 105 core types produced four counterexamples. Every demand size matters somewhere. We recorded `R36-CORE11-34` as refuted. [Independent witness replay](../../research/voevodsky/results/ramsey_distill_unseen_replay.json). An omitted demand is safe if the retained demands plus its negation are impossible. This preserves witnesses but cost more than a direct verdict in the timed small tests.
- **Separate capacities need not compose.** One failed 12-vertex core at degree four has a fractional cover of mass four but no whole cover. Exactly 14 individual demands suffice to certify failure; no 13 suffice. At degree five the same core fails by weighted counting alone. [Minimum certificate](../../research/voevodsky/results/ramsey_capacity_minimum.json) · [Counting test](../../research/voevodsky/results/ramsey_capacity_counting_test.json).
- **Square completion selects a useful obstruction, not a unique cause.** On the stored 35-vertex \((3,9)\) graph, 315 blue eight-cliques from saturated alternating squares already force nine deletions. None of 100 equally large random samples did. Of 3,920 saturated wedges, 140 split their seven completions into symmetry orbits of sizes 3, 3, and 1. In 70 cases an exchange swaps the triples but preserves cyclic order. This is not the opposite ordered join from the earlier subdivision work. The proposed reversal-specific deletion signal did not beat a matched control. [Square cuts](../../research/voevodsky/results/ramsey_saturated_square_cuts.json) · [Exchange](../../research/voevodsky/results/ramsey_wedge_join_reversal.json) · [Control](../../research/voevodsky/results/ramsey_reversal_cut_control.json).
- **Counts on one side can lose the attachment assignment.** The rook and Shrikhande graphs have identical three-state header transition counts for every color word, but differ on \((4,5)\) legality. This refutes the specified count law, not every transport law. In the separate marked-attachment experiment, exact overlap tables from both sides recovered all 360 single hidden blue colors across 36 tested completions, given the other nine marked colors. For two hidden colors, the minimum fixed panel had five readings on core 7 and three on core 28. These readings come from the completed graph; this is reconstruction, not prediction of optimal order. [Transport falsifier](../../research/voevodsky/results/ramsey_header_transport_falsifier.json) · [Two-sided test](../../research/voevodsky/results/ramsey_exact_overlap_transfer.json) · [Minimum panels](../../research/voevodsky/results/ramsey_minimum_two_panel.json).

**Unanswered:** For Ramsey growth, the main gap is coverage of the remaining 20-vertex core types in the order-28 test. For panel selection, the immediate gap is different: does the evidence distinguish a good panel, and can the selector find it? On core 7, a greedy panel and a known optimum both had zero sampled log loss, but recovered 6 and 45 of 45 pairs under exact tests. With a fixed five-reading budget, four added exact counterexamples raised held-out recovery from 2/22 to 12/22. After the prespecified ten additions it returned to 2/22. Do not select the intermediate round after seeing the answers. Next compare exact optimization with greedy selection **on the same augmented evidence**, then validate against the full constraints. [Log-loss audit](../../research/voevodsky/results/ramsey_panel_log_audit.json) · [Feedback trajectory](../../research/voevodsky/results/ramsey_panel_feedback.json).

Ledger sequence claim: `seqclaim-f7896d09a6ac03be09f85a68`.
