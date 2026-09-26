# Port multigraph forest audit

Implemented `checkers/check_port_multigraph_forest.py` using union-find over individual undirected PORT wires rather than deduplicated agent pairs. A second edge between the same agents is correctly a cycle; an agent self-loop is rejected. Negative controls use valid symmetric fully wired graphs with ordinary B arities, so rejection is not merely a missing-port error. An E--N tree is accepted. Fresh execution accepts 219 reachable classes and 452 transitions from four tiny fixtures.

This repairs an important premise of the written boundary proofs: distinct external attachments of a connected active pair cannot reconnect elsewhere in an actual forest. The earlier simple-agent adjacency check could collapse two port wires and miss this failure. The new helper is import-safe; its test driver runs only as __main__.

This turn discharges the multigraph-audit sub-obligation only. A unified validator for the complete invariant is still needed, including exact arities, original/copied tag consistency, the COPY source component, all phase roles, independent auxiliary-side roots, and terminal output constraints. Neither four-fixture testing nor this forest predicate establishes universal rewrite closure or confluence. Next compose those clauses into one diagnostic validator and reject malformed graphs clause-by-clause.
