# One-law fresh-search milestone

## Question

Can fresh search derive `(x | x) | (x | x) = x` from the supplied candidate
axiom, without importing an existing Wolfram derivation or intermediate lemma?
The operator selected this smaller goal after the full adequacy search stalled.

## Claim boundary and preregistered test

SCC obligation: forward realization of an equational inference DAG as Cubical
paths, with input and conclusion preserved. This is one conditional law, not
Boolean reconstruction, adequacy, or autonomous formula selection.

Conjecture: proof-producing congruence closure of systematically generated
one-parameter axiom instances can reach double negation. Rivals: the ground
instance bound is insufficient; enumeration spends the budget elsewhere; or
an implementation defect produces a false equality. The risky consequence is
an independently replayable DAG ending at exactly the prescribed equation.

The search starts with the supplied axiom only. Its substitution pool is all
binary trees over one rigid parameter with at most five operations, ordered
by total substitution cost. No old consequence packet is read. Budget: one
60-second run, at most 30,000 instances, 100,000 syntax nodes, and 60,000
nontrivial unions. Exhaustion reports unresolved; the target is not changed.
Tests on small artificial axioms are implementation tests, not evidence for
the candidate. A successful candidate derivation must additionally pass a
fresh Agda check and a deliberately altered-conclusion negative control.

## Disposition

**Unresolved.** The frozen run stopped at the 30,000-instance cap after
12.64 seconds, with 67,976 syntax nodes and 32,426 internal unions (2,426
from congruence). The prescribed endpoints remained in different classes.
This defeats the bounded success expectation, not the law or the possibility
of another derivation. No larger-budget retry or replacement target was used.

The exported certificate contains only the input axiom: no target proof was
found, so no Agda goal theorem or kernel negative control was executed.
Independent replay binds that axiom to the selected candidate. Eleven
implementation/nonpromotion tests pass; the old completion audit also still
passes its 15 tests. Existing proof artifacts remain untouched.

Evidence: `research/nima/results/double-negation-search.json` and
`double-negation-audit.json`. Search execution:
`structured_command_execution:e_25120_1791120247720223300_330`.

Reproduction:

```text
python research/nima/checkers/test_ground_equational_milestone.py
python research/nima/checkers/ground_equational_milestone.py research/nima/results/algebra-formula-search.json research/nima/results/double-negation-search.json --ordinal 1488521
python research/nima/checkers/check_double_negation.py
```

The optional `--emit` audit mode refuses this unresolved result. The isolated
kernel driver is reserved for an actual emitted proof, not this run. Its
MCP parse preflight failed inside the tool's own `ParseFile(''C:...')` command
construction; this is a separate tooling defect, not a mathematical residual.
The driver therefore remains unexecuted and parser-unverified. Search source,
input, interpreter, bounds, PID, and completion status are recorded in the
ignored `.ai/tmp/scc-state/nima-double-negation-run.json`; no child process or
active search remains.
