# Bounded all-schedule exploration

Fresh `check_all_schedules.py` explores every enabled rewrite from each reachable state for four short scan/conditional fixtures. Keys retain the complete instance dictionary, including named graph ports, allocator high-water, step count and diagnostic metadata. There is no forest canonicalization, alpha quotient or deletion of cyclic context information.

All four searches exhaust their pending frontier below the20000-state cap:577 distinct raw states,646 outgoing edges and93 branching states in total. They reach24 named terminal states, with exactly one expected typed observation/word per fixture and a single rewrite count per fixture (20,22,36,37). Prefix publications never change value along any examined edge. Named terminal multiplicity is not semantic nondeterminism: allocation history differs, public observations agree.

Expected results are literal semantic fixtures, not copied from a first-enabled run. A deliberate cap1 search reports incomplete, demonstrating that truncation is not silently counted as exhaustive success. Incomplete searches would fail the main report; partial counts would remain recorded.

This evidence is stronger than one schedule per fixture but not independent rule semantics: exploration invokes the production reducer. It neither proves general confluence nor explores large fuel values. The key's inclusion of step counters avoids unsound merges but means a hypothetical rewrite cycle would keep producing new states until the cap, not be recognized as a cycle.

Critical next proof: derive local commuting diamonds for disjoint active pairs in the reachable typed system, with allocation renaming and fixed public root identities. Pairwise disjointness alone is not enough unless replacements use outside slots linearly and names are fresh; the existing signature audit supplies the interface premise. A cyclic-safe graph isomorphism or explicit fresh-name bijection is needed to compare the two orders. This targets schedule independence rather than merely growing finite searches.
