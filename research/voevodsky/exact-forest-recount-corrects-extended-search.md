# Exact forest recount corrects the extended search

Fresh `check_exact_forest_rule_ledger.py` explores 141 inputs (all support words n<=2, both indices 0..n+2) using the name-independent tagged forest key and the unified invariant before and after every enabled individual-redex transition.

Corrected totals, summed separately per input: **11,278 forest-isomorphism classes and 23,559 transitions**. The earlier serial-dependent key reported 11,319 states and 23,641 transitions: 41 duplicate classes and 82 extra counted edges. E--N counts decrease from 1,376 to 1,335 and E--K from 419 to 378; all other rule counts are unchanged. All fifteen typed rules remain covered. Each input reaches exactly one correct four-agent BOOL--OUT terminal class (141 terminal classes counted per input).

This confirms that the old allocation-order issue affected the historical extended count, not just a constructed graph. Historical files are retained as the original runs, but their counts must not be advertised as exact alpha quotients; use `results/exact-forest-rule-ledger.json` for corrected evidence. No universal confluence or arbitrary-n preservation theorem follows from this finite search.

Next check every pair of simultaneously enabled individual redexes with the actual executable rewrite engine and compare both two-step results under the exact tagged key. Include two distinct erasers, not only different rule families, and use the unified invariant to distinguish stale-redex mistakes from actual noncommutation.
