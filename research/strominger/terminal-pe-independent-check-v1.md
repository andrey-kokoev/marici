# Separate Python validation of terminal P/E witnesses

`checkers/check_terminal_pe_independent.py` reads saved coordinates, charts and
packets. It imports neither the JS generator/probe nor the solver.

It separately reconstructs native reader relations and the experimental
same-origin, terminal-proton-reader PE relation; checks five-coordinate maps,
reference vacancy, C1/M1 intersection, unit volumes, regular P reference
geometry, global roles, species counts and every occupied triangular contact;
and uses bitset transitive closure for rooted and electron-exit reachability.

Results:
- All 20 isotope deletion trials agree with the earlier experimental probe.
- Two N-14 and two Ne-21 candidates pass under the experimental rule.
- All 24 H-1 markings pass; corresponding H-2 controls retain native paths.
- 20 deliberate corruptions are rejected: coefficient maps, counts, reference
  cells, origins and role bindings (five mutations for each positive isotope).

This is a separate implementation of the specified finite-witness checks.
It shares the rule specification and serialized source witnesses. It does not
independently enumerate the full lattice/search universe or derive the added
reference-only-N permission. No production/viewer changes were made.

```sh
python research/strominger/checkers/check_terminal_pe_independent.py
```

Evidence: `results/terminal-pe-independent/verification.json`, with per-trial
results, negative controls, input hashes and checker hash.
