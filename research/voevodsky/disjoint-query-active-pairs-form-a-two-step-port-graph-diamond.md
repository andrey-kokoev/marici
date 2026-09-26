# Disjoint query active pairs form a two-step port-graph diamond

Fresh `check_disjoint_query_redex_diamond.py` first completes COPY, then compares Q1-step;Q2-step with Q2-step;Q1-step on six tiny support fixtures with both indices zero. The resulting ENTIRE live graphs agree under fresh-agent alpha-renaming, checked by rooted OUT1/OUT2 traversal retaining agent kinds, port names, and peer ports. Per-step port-linearity audits pass. This is stronger than agreeing on final Boolean outputs: the two local disjoint interactions have the same two-step successor graph modulo incidental IDs.

The result covers one kind of disjoint active-pair diamond. Other pairs (query/eraser, two erasers, COPY/query) and arbitrary indices need separate checks. A query principal meeting COPY's auxiliary is inactive, so COPY/query concurrency may involve enabled redexes elsewhere rather than a shared principal-principal critical pair. A general confluence theorem remains unproved.

Next enumerate PAIRS of enabled disjoint redexes on reachable small graphs, alpha-canonicalize both two-step successors and check the commuting diamond. Record a minimal counterexample if any pair fails; otherwise state bounded coverage before attempting a uniform proof.
