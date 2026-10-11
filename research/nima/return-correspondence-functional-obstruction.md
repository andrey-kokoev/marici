# Obstruction to a total single-valued return correspondence

## Scope

Fixed Bool/notEquiv source `(false,false)`. The target is the completion-valued C4 state space `R.Vector`; the retained return section is the diagonal `x(i) = backward-section (false,false) i i`. Its endpoints are the target basis state `basis (true,true)` and source basis state `basis (false,false)`.

## Tested proposition

There is no relation `Rel(i,x,v)` on diagonal return-section points and C4 states that is simultaneously:

1. total on the diagonal section: for every `i`, some `v` satisfies `Rel(i,x(i),v)`;
2. single-valued: any two related states are equal;
3. endpoint-compatible: the start is related to `basis (true,true)` and the end to `basis (false,false)`.

## Derivation

Choose `f(i)` as the state supplied by totality. Single-valuedness, applied once to the chosen witness and once to each endpoint witness, gives

`f(i0) = basis (true,true)` and `f(i1) = basis (false,false)`.

The cubical family `i ↦ f(i)` is therefore a path between those basis states. But `TickLocalReturnSection.no-cubical-state-path` proves that no such path exists: evaluating coordinate `(false,false)` would identify `zeroCompletion` with `oneCompletion`, contradicted there using the nonzero-quarter separation result. Hence the three interface requirements are incompatible.

This rejects only a total, single-valued **Cubical state correspondence** with these endpoints. It does not reject a genuinely multivalued or partial relation, nor a metric-parameterized evolution whose parameter is external to Cubical `I`; it does not refute the broader source-derived lift conjecture.

## Proved diagnostic: current surface erases schedule tags

For any two Ticks `t,u` at the fixed source and any Cauchy parameters `a,b`, the current completion-valued surfaces agree. Let

`p = extract-source-attached t ∙ sym (extract-source-attached u) : src (extract t) ≡ src (extract u)`.

By definition, `return-target t = run leftFirst (src (extract t))`, and `return-surface t a b = U a b (basis (return-target t))`. Congruence therefore gives

`cong (λ q → U a b (basis (run leftFirst q))) p : return-surface t a b ≡ return-surface u a b`.

This proof uses the checked source-attachment law and the definitions of the candidate surface; it does not use either retained schedule tag. It proves tag-erasure for this candidate, not that every valid lift must be schedule-sensitive. If schedule order is part of the intended interpretation, the interface needs a separate schedule-indexed traversal of the local square. No Agda run was needed for this congruence derivation.

## Evidence and status

- State separation: `research/nima/agda/TickLocalReturnSection.agda` (`no-cubical-state-path`, `zero-not-one`).
- Fresh closure receipt for that exact source: `research/nima/results/agda-TickLocalReturnSection.json`.
- The selection argument above is a direct derivation from the stated relation laws; no additional Agda run was performed for the relational implication.
