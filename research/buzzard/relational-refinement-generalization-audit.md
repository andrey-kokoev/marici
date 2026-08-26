# Relational-refinement generalization audit

Owner: `marici.Buzzard`

Disposition: proposed common abstraction failed; retain specialized witnesses.

## Question

Should equality-based `SemanticModelCheck.Faithful` be generalized now to a
shared relational-refinement interface?

## Candidate frozen instances

The library contains several exact, non-equality constructions:

- `ConcurrentFenceRefinement` chooses a two-site sequential order, proves
  observation agreement, and respects both real-time precedence directions.
- `FiniteConcurrentRefinement` chooses a permutation of arbitrary finite
  operations, proves observation agreement, and proves real-time ordering.
- `FaithfulFiniteConcurrentRefinement` additionally requires unique operation
  identities.
- `CompletionKernel.OperatorSquare` carries source and target linear
  embeddings, injectivity, a source and completed operator, a named extension
  mechanism, and a commuting square.
- `successorMap` is the canonical quotient map induced by an explicit nested
  submodule witness.

## Failure of the proposed common type

A bare relation `R : Model -> Source -> Prop` can encode each final agreement
statement, but it discards the data that makes the witness meaningful:

- order choice and real-time precedence;
- permutation of the same operation occurrences;
- identity faithfulness;
- linearity and injective embeddings;
- canonical extension mechanism;
- quotient provenance from a specific inclusion.

Those fields are not optional decorations. Existing hostile examples show
that sequential agreement need not respect real time and that an explainable
history with duplicate identities need not admit faithful refinement.
Completion hostiles separately show that a carrier embedding cannot
manufacture an operator. A common relation would accept all these weakened
witnesses unless it rebuilt the specialized structures as ad hoc side fields.

## Decision

Keep `SemanticModelCheck.Faithful` as pointwise equality for the finite checks
where equality has actually been established. Do not weaken it preemptively.

Keep concurrency, completion, and quotient refinement specialized. Their
common English word “refinement” is not yet evidence for one Lean structure.

The smallest plausible future interface is not a binary relation alone. It
would need typed source/model objects, an observation map, occurrence
transport, and a law family selected by the source sector. That proposal
currently reduces no duplication: every consumer would immediately recover
its specialized witness.

## Reopening condition

Revisit only when at least two sectors independently need the same nontrivial
transport fields and the same composition law, with hostile tests showing
that the shared interface preserves real-time, identity, linear, and quotient
provenance distinctions.

## Verification boundary

This was a source/type audit and introduced no Lean declaration. The first
search used an incorrect project-relative path from the repository root; it
was immediately rerun from `research/buzzard/marici_formal/` against the
actual files. No conclusion relies on the failed search.

The last aggregate Lean verification remains `Build completed successfully
(8735 jobs)`. No Git command or site build was run.
