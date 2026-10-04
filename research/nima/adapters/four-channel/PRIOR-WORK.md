# Prior-work reconciliation: constructor and four-step presentation

## Question and evidence boundary

Operator requested a search for an already established connection between the
rich constructor and its four-channel/four-step view. This is source inspection,
not a fresh re-verification of every historical receipt. The new four-channel
candidate must not replace the richer existing constructor interface.

## Direct connection already present

`research/nima/native-table-equivalence.md` and
`research/nima/agda/IndexedConstructorTables.agda` establish the relevant chain:

1. `syntax-iso` and `complete-equivalence` identify the original eight-form
   syntax and complete packages with independently defined native typed recursive
   tables. Values, type indices and witness payloads are retained.
2. `kernel-table` maps a native node into the actual `TableFibrationCycle.Table`.
   `kernel-four-return` proves four-step recovery of that table.
3. `research/nima/agda/NativeTableResolution.agda` supplies the corresponding
   kernel table/four-return theorem for retained derivations and a
   `closure-equivalence` with the original twelve-rule closure under transported
   source admission families.

This corrects any suggestion that a generic constructor-to-table connection is
still absent. What was not established by this search is identification of our
new OO/OR/RO/RR two-sort signature with the historical four-step operator.

## Exact meaning of the four steps

`research/nima/table-fibration.md` states the actual schedule:

```text
[L,S,T] -> [S[L,T]] -> [L,T,S] -> [T[L,S]] -> [L,S,T]
```

The operations retain homotopy-fiber membership witnesses and use a declared
reversed-unpacking convention. `four-correct` is a field-preserving table
isomorphism; `four-path` turns it into a path using univalence. This is not four
independent primitive channels and does not identify the retained execution
history with its initial history. Ordinary unpacking instead gives a two-step
return: the wiring convention is not forced by fibration alone.

## Other relevant established interfaces

- `research/nima/whole-package-generators.md`: whole-package E/Pi retain every
  input; comparisons retain endpoints, equivalence and actual filler; higher
  comparisons iterate; reify-history recovers the prior derivation. Reflecting
  the whole package raises the universe level.
- `research/nima/fibration-constructor-equivalence.md`: dependent sums are total
  fiber spaces, dependent products are sections of those fibers. Opposite-endpoint
  regrouping is NOT by itself a dependent product.
- `research/nima/parallel-label-fibration-check.md`: an earlier duplication audit
  explicitly warns against replacing full retained packages/higher comparisons
  with lossy endpoint summaries and rediscovering the resulting information loss.
- `research/nima/generating-grammar/COMPLETIONS-AND-POLICIES.md`: specific signed
  and rational set quotients already have constructed operations, descent proofs
  and native transport bridges. This is stronger than merely admitting an opaque
  quotient type, but not a general quotient or localization completeness theorem.
- `research/nima/four-charts-are-one-periodic-object-in-the-canonical-homeomorphism-groupoid.md`:
  a separate canonical Fourier model has one carrier with a four-phase action;
  its stable graded version has suspension monodromy. No identification with
  the table cycle should be inferred from the shared number four.

## Disposition

The retained native table presentation can preserve the full declared syntax;
"shadow" does not necessarily mean lossy. Loss occurs when a view actually
forgets labels, declarations, attachments, witnesses or histories.

The recent `FourChannelBridge.agda` counterexample concerns a deliberately weak
signature of four edge families with no composition payload. It is valid for
that signature, not a counterexample to the existing rich constructor. Its free
category/Yoneda construction is a conditional alternative, not the missing
implementation of Marici's established constructor-to-table bridge.

Reuse the existing package/rule/closure equivalences for further categorical
interpretation. Do not claim the four-step kernel generates every supplied type,
all quotient/limit universal properties, or all sector policies. The generating
 grammar's policy audit explicitly distinguishes those unimplemented adapters.
