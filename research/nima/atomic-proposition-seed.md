# A nullary proposition name initializes WG

## Question

What constructor supplies an initial state to WG without requiring an incoming state?

## Construction

`agda/AtomicPropositionSeed.agda` declares `dot : Object` with no operands and sets `initial = dot`. `Object` is the syntax of one atomic proposition name. An `Interpretation` separately assigns a proposition-valued type to that name; it does not supply a proof.

The checked statements are designed to distinguish naming from proving:

- `empty-interpretation` interprets the name as the empty type.
- `no-uniform-proof` refutes a function producing a proof at `dot` for every interpretation.
- `Run` combines this initial state with an explicitly supplied WG witness relation and transition rule. `first-arrow` extracts the first generated witness; `history` starts retained generation at `dot`; `zero-history` identifies its zero-step history with `empty`.

`Run.cycle1` through `Run.cycle5` prove that every endpoint in five recursive steps is `dot`, for any supplied WG rule. `Run.five-witnesses` proves the retained history has length five. These are uniform proofs, not an execution of a concrete transition rule: none has been supplied. The accumulated history is not fed back as the next state.

This is a singleton syntax, not yet a grammar generating distinct additional proposition names. It does not change the existing native constructor signature or the atomic reachability theorem.

## Verification

Fresh checking command:

```text
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module AtomicPropositionSeed -Fresh
```

Receipt: `results/agda-AtomicPropositionSeed.json`. The receipt, rather than this command listing, records whether checking passed.
