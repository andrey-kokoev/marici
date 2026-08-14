# Research Documentation and Epistemic-Graph Lifecycle

This policy governs material research results in Marici. Its purpose is to
preserve reproducibility, claim boundaries, and epistemic history without
turning exploratory work into bookkeeping.

## Core lifecycle

```text
bounded question
  -> evidence artifact
  -> result packet
  -> verification
  -> ledger + graph, if material
  -> commit/push
```

Exploratory checkpoints stop after the result packet and evidence artifacts.
They do not require a ledger entry or graph event.

A result is **material** when it does at least one of the following:

- changes the status or scope of a scientific claim;
- closes, refines, or falsifies an epistemic-graph edge;
- introduces a reusable construction or obstruction;
- materially changes the next discriminating experiment.

Routine reruns, refactors, intermediate matrices, and confirming sign checks
are not material by themselves.

## Canonical result packet

Delegated and local bounded investigations use the same structured summary:

```json
{
  "claim": "...",
  "status": "proved|falsified|conditional|inconclusive",
  "assumptions": [],
  "evidence_refs": [],
  "factorization_test": {},
  "counterevidence": [],
  "next_experiment": "..."
}
```

This packet is the canonical structured account of the result. The ledger
expands it for human readers; the epistemic graph records only its material
DAG delta. Neither should independently reinvent the claim.

Status meanings are strict:

- `proved` means proved only in the stated model and scope;
- `falsified` identifies the exact claim version that failed, not the whole
  research program;
- `conditional` enumerates every unproved assumption on which the conclusion
  depends;
- `inconclusive` records what was learned and the smallest discriminating next
  experiment.

## Ledger entry

Every material result gets one concise, append-only-by-default entry in `src/ledger`
with five sections:

1. **Record** -- date, status, and exact scope.
2. **Claim** -- the typed theorem, construction, or falsifier.
3. **Evidence** -- inherited inputs, checker path, hash, and reproduction
   command.
4. **Boundary** -- assumptions, counterevidence, negative controls, and
   prohibited inferences.
5. **Consequence** -- what changed and the next falsifier.

Add more sections only when the mathematics benefits from them. Do not split
inputs, decisions, dependencies, and negative controls into repetitive
boilerplate.

The entry must distinguish whenever relevant:

- generic from resonant kinematics;
- associated-grade from full chain-level statements;
- bare amplitude data from factorization-marked geometry;
- carrier, coefficient, and physical-natural-transformation claims;
- tree-level from modular or all-topology completion.

Typographical and formatting corrections may edit an existing entry. A
semantic strengthening, weakening, or correction gets a new entry. Use a
graph `supersedes` relation only when the old claim is actually replaced; use
a refinement relation (currently `marici:refines`) when the old scoped result
remains true.

## Epistemic-graph delta

Before material work begins, query the graph for existing problems, claims,
criticisms, and tests so stable entity identities can be reused.

A typical admitted contribution contains only:

- one or two immutable source nodes;
- one primary claim, conjecture, criticism, or problem;
- one test and durable outcome;
- the few relations needed to place the result;
- one assessment only when the epistemic judgment of an existing entity
  changed.

Do not automatically create a criticism for every caveat, a new problem for
every `next_experiment`, or separate claims for equations that form one
theorem. The graph records a DAG change, not a copy of the ledger.

Prefer the core relations:

```text
derived_from  tests  addresses  criticizes  depends_on  supersedes
```

Use a namespaced relation such as `marici:refines` only when no core relation
expresses the intended edge.

Graph entities are stable identities. Scientific posture belongs in durable
test outcomes and assessments, so later evidence can update judgment without
rewriting history. Graph admission certifies schema, references, and graph
integrity; it does **not** certify scientific truth.

Use the atomic submit-review-admit graph operation. Fetch the current ledger
head immediately before a status-changing or superseding contribution and use
that exact head for compare-and-swap. `latest` is acceptable only for an
independent additive contribution.

Never edit the graph store, generated graph records, or MCP configuration by
hand. Commit the generated proposal, review, admission event, and idempotency
records with the evidence and ledger entry that they describe.

## Delegated work

A delegated task must be bounded around one falsifiable statement and must
specify its model and reasoning effort explicitly. It returns the canonical
result packet and reports changed files, verification, residuals, and
blockers.

Delegated evidence production and primary-agent curation are separate gates:

- the delegated task is complete when its packet, artifacts, and scoped checks
  are complete;
- the primary agent reads the artifacts and reruns decisive checks;
- the primary agent owns ledger wording, graph admission, and commit scope;
- delegated agents do not commit or modify MCP configuration unless that
  authority is explicitly assigned.

Temporary graph unavailability must not block evidence production. The parent
research frontier is not closed, however, until material evidence has been
curated and published.

## Definition of done

A material research result is complete when:

1. the exact claim or falsifier is scoped;
2. reproducible evidence passes;
3. the primary agent audits the decisive evidence;
4. one concise ledger entry and one sparse graph delta are created;
5. evidence, documentation, and generated graph records are committed and
   pushed together;
6. the next falsifier is named.

For an exploratory checkpoint, the result packet and evidence artifact are
sufficient.

## Long-running research discipline

A long or overnight run should normally produce at most one positive theorem
entry and one sharp blocker or falsifier entry. Intermediate observations stay
in the working context until they materially change the research DAG.

Do not force a positive result by fitting a desired matrix, adjoining
generators solely to make a square commute, or introducing an unmotivated
rational splitting. A clean falsifier that identifies the first canonical
identity to fail is a complete and valuable outcome.
