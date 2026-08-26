# Indexed evaluator versus finite observation fiber

Owner: `marici.Buzzard`

Source locator: `Infinite static rank, one higher-order generator` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

The packet space is the rational finite-support module `Nat →₀ Rat`.
`indexedEvaluator index` is one Lean definition parameterized by a natural
coordinate index. It reads the selected coordinate as a linear port.

Lean proves the complete indexed family is jointly faithful: if every indexed
evaluation is zero, the packet is zero.

Lean also proves that every finite set of instantiated indices is not jointly
faithful. Given a finite set, choose an index outside it and use the singleton
packet supported there. Every instantiated evaluator returns zero, although
the packet is nonzero.

Thus a single finitely written evaluator schema and an infinite-static-rank
observation family coexist exactly. “One program” does not mean “one scalar
port” or “finite-dimensional readout.”

## Capability distinctions

The theorem separates:

- description size: one indexed Lean definition;
- logical index space: all natural numbers;
- instantiated finite port set: any chosen finite subset;
- joint faithfulness: achieved only by the complete indexed family in this
  fixture.

No uniform runtime, word-length bound, or finite executable observation fiber
is inferred from the finite schema.

## Boundary and missing interfaces

This is the coordinate-family hostile, not the theta valuation-constructor
algebra. A faithful sector upgrade needs:

- the typed source constructor monoid and its normal forms;
- the endpoint action `Eval(C,c)=L(Cc)`;
- proof that the evaluator is authorized by composition;
- the valuation-projector separation theorem;
- positivity/nonvanishing of the theta endpoint on isolated labels;
- an explicit cost or executability model if operational bounds are claimed.

The abstraction generalized the schema-versus-rank distinction while refusing
to identify logical constructor indices with execution epochs or primitive
ports.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/IndexedEvaluator.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/IndexedEvaluator.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/indexed-evaluator-infinite-rank.md`
