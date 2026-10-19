# Mixed, site-dependent subdivision: bounded N-14 search

## Current result

No neutral 7P/7N/7e reference was found. Completed mixed-diagonal queries are
UNSAT through maximum origin 6. At origin 7 the packet universe completed,
but Z3 returned UNKNOWN after its 120-second search limit. This is not a
negative result at origin 7. Origin 8 was not queried after that stop.

A budget-only retry of the identical saved origin-7 input with Z3 5.3.1 and
unchanged seed also returned UNKNOWN after 600.009 solver seconds (635.880
seconds overall). The original input and receipts were hash-checked and
preserved. The longer retry does not strengthen the negative result: origin 7
remains unresolved. Optimize the encoding before increasing budgets again.
Retry evidence: `results/mixed-subdivision-n14/origin7-600s/verification.json`;
runner: `checkers/retry_mixed_n14_origin7.mjs`.

| Origin bound | Packets | Conditional operations | Choice items | Result |
|---|---:|---:|---:|---|
| 3 | 165 | 365 | 8 | UNSAT |
| 4 | 372 | 843 | 10 | UNSAT |
| 5 | 762 | 1,770 | 15 | UNSAT |
| 6 | 1,410 | 3,360 | 18 | UNSAT |
| 7 | 2,412 | 5,870 | 21 | UNKNOWN (120s solver limit) |

These results do not establish physical instability or an unbounded
impossibility. The large UNSAT queries have not received independently checked
formal UNSAT proofs.

## Scope and controls

`mixed-subdivision-model.mjs` adapts local geometry while inheriting the prior
`GenerativeAssemblyRules`. Each whole octahedron has one global three-valued
diagonal variable, shared by occupied components, references and lookahead
operations. Packet/chart requirements and conditional operations constrain the
same variables; different readers cannot independently subdivide the same item.
The canonical root marks/coordinates are held fixed, with its three possible
reference charts mutually exclusive under these global choices.

The solver retains exact particle counts, context/species/contact exclusions,
rooted paths, actual operation witnesses for contacts and E-exit reachability.
No new transport map, electron-contact exception or whole-octahedron particle
identity was added. A SAT branch is required to replay through source-rule
inspection and compatible rooted prefixes; no N-14 SAT witness has yet exercised
that branch.

Fresh small-case controls exhaust all 27 assignments to the three relevant
origin-1 item choices. Explicit source-operation enumeration and the symbolic
solver agree on all 369 composition/control queries. Every positive control
matches an enumerated configuration and passes original-rule exit inspection.
An explicit hostile control rejects two root readers requiring different
diagonals for the same octahedron. These controls share the geometry adapter;
they check the symbolic constraints against explicit execution, not a wholly
independent implementation of geometry.

Pairwise compatibility is cached by chart pair: the original `describe` guard
uses chart cells and aliases, not packet origins or coefficient permutations.
No geometric/contact condition was removed by this optimization.

Limits: 5,000 packets, 50,000 conditional operations, 100,000 local diagonal
evaluations; 120 seconds for Z3 search and 600 seconds for the entire solver
process including constraint construction. Earlier interrupted attempts had a
150-second overall process limit. The final saved origin-7 receipt is an actual
solver UNKNOWN (`canceled` after 120.008 seconds), not an inferred UNSAT.

Production/viewer and other-owner sources were not edited. The search receipts
contain source fingerprints and input hashes. No global coupled-field sewing,
binding energy, stability or viewer admission is asserted.

## Evidence and reproduction

- Prospective contract: `mixed-subdivision-protocol-v1.md`
- Search summary: `results/mixed-subdivision-n14/verification.json`
- Per-bound inputs, solver receipts and verification: same directory
- Small controls: `results/mixed-subdivision-n14/controls-verification.json`

```sh
node research/strominger/checkers/check_mixed_subdivision_controls.mjs
node research/strominger/checkers/search_mixed_n14.mjs
```

The next unresolved query is origin 7, not origin 8 or an unbounded search.
More efficient equivalent constraints or a larger declared solver budget may
resolve it; the current timeout supports neither existence nor nonexistence.
