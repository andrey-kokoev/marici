# SCC repository-local toolkit

Invoke an action with `python research/aspect/scc/scc.py toolkit <action> <contract.json>`.

Actions are `migrate`, `batch-audit`, `profile-diff`, `promotion-lint`, `provenance-lock`, `hostile-replay`, `dependency-view`, `dead-claims`, `monotonicity`, `fixtures`, `schema-compat`, `normalize`, `residual-census`, `coverage`, `budget-sensitivity`, and `interface-match`.

The canonical replay corpus is `research/aspect/scc/canonical_hostiles.v1.json`.

## Boundaries

Migration marks unlocated legacy objects `not_constructed`. Batch audit supports categorical apparatus, categorical residual, and explanation-debug contracts. Promotion lint traverses structured JSON but does not infer claims from prose. Provenance locking hashes regular in-root files and records declared JSON schema identities. Dependency views include Graphviz DOT. Interface matching certifies complete descriptor equality only; it neither constructs an overlap map nor proves a categorical pullback. Budget sensitivity propagates declared exact or directed-upper costs and does not optimize undeclared alternatives.
