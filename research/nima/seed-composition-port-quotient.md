# Native proof of the composition-port quotient

## What is now proved, beyond finite tests

`agda/SeedCompositionPortQuotient.agda` proves the structural composition contract for ALL nonempty endpoint-typed paths of the actual six-arrow seed. It uses the existing append operation and arrival interpreter unchanged.

The previous rational-family checker tested the port-summary formula on finite registered families. The new theorem establishes its underlying path-level operation and contextual equivalence without a path-length bound.

## Carrier and operation

A positive path contains a supplied first occurrence and the remaining existing free path. Its source and target indices are part of its type. Joining two positive paths uses the existing `SeedFirstReturnActions.append` on their retained words.

For a path p:s->t, its port record retains s, t and its final arriving occurrence, with the existing target-membership witness. Since the final occurrence determines t, this is the typed version of the Python source/final-occurrence summary.

The theorem proves

    read(join(p,q)) = port-join(read(p),read(q)).

At matching endpoint indices, port-join retains the left source and right final arrival. The middle endpoint condition is mandatory; it cannot be inferred from an untyped final-arrival value alone.

The new `binary-congruence` theorem states that replacing BOTH operands by paths with the same typed port readings preserves the resulting port reading. Associativity of port composition is also proved.

## Exact two-sided contextual characterization

For positive parallel paths p,q:s->t, admit arbitrary typed prefixes h:a->s and suffixes k:t->b, including empty contexts, and use the existing arrival reader.

The key reduction is

    arrival(h ; p ; k, initial) = run(k, read(p)).

A nonempty middle path sets its arrival regardless of the incoming value. The suffix then acts through the existing interpreter. This yields both directions:

    read(p)=read(q)
      iff
    every typed prefix/suffix context gives equal arrival observations.

The converse uses empty prefix and suffix. The source table supplies an arriving occurrence at every vertex; the chosen witness is used only to evaluate this mathematical converse, not as a physical reset or preparation law.

This characterizes the arrival-only observational quotient WITHIN each fixed source/target type. The complete port record keeps those types explicitly. It is not a claim that different starting vertices may be forgotten, nor a theorem that the current physical interface contains only arrival questions.

## Relationship to coefficient families

The exact Python summary aggregates rational coefficients by starting vertex and final occurrence, while independently retaining admitted coarse support. Its binary formula is the finite distributive extension of the path-level port product.

The algebraic derivation and executable family checks remain in `seed-composition-port-summary.md`. This new Agda proof does not itself formalize arbitrary rational finite sums or the Boolean support/rational coefficient product. That boundary is explicit rather than hidden behind the word "formalized".

The existing checker now validates the fresh formal receipt and relevant source inventory before running its coefficient-family tests.

## What the synthesis now contains

- Actual seed occurrences and endpoints, rather than a fitted numerical carrier.
- An existing typed composition constructor, not a newly guessed dynamics.
- A typed summary that preserves binary composition.
- A necessary starting-port control from the prior executable collision.
- An exact all-context characterization for the frozen arrival task.
- A separate rational-family realization with support and coefficient cancellation handled explicitly.
- Full retained words and construction provenance outside the observational quotient.

This establishes a native structural candidate for an operation/readout interface. It still does not choose the intended T9, derive matrix amplitudes, identify the original J4, or select a physical task. In particular, history-length or earlier-role queries do not descend merely because all arrival contexts do.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedCompositionPortQuotient -Fresh
    python research/nima/checkers/check_seed_composition_port_summary.py

Fresh safe Cubical/guardedness closure passed with ignored interfaces and stable inputs.18 executable audit checks pass, covering the fresh formal-source binding as well as1024 basis products,81 coefficient-family products,216 triples, regrouping, support/cancellation, and remaining history collisions. The36 existing branch-composition checks rerun unchanged.

Artifacts:

- `agda/SeedCompositionPortQuotient.agda`
- `results/agda-SeedCompositionPortQuotient.json`
- refreshed `results/seed-composition-port-summary.json`

No existing primitive action, constructor policy, or physical normalization was changed. No new postulates or unresolved holes were introduced.
