# Fixed-preparation contextual exchange and a derived attachment lift

## Constructed object

For the same fixed chart and two paths in `su32-comparison-license-v1.md`, the geometric symmetry was not a comparison at the original preparation. This construction instead keeps that preparation fixed and exchanges the **ordered presentation of both comparison operands**.

Its domain is explicit: the complete signed-reference preparation, both actual five-cell path words, the existing shared-reference comparison point, and the antecedent record. It is not an operation from a standalone P+, E+ operand to a standalone P-, E+ operand. The missing P record is retained context, not newly generated information.

`su32-contextual-path-exchange.mjs` invokes the existing `channelOperand` and `compareAt` constructors. The latter already accepts either order of its two source-required inputs. The exchange sends

```
(preparation, [path A, path B], compareAt(A, B), antecedent)
    to
(preparation, [path B, path A], compareAt(B, A), antecedent).
```

Both channel witnesses remain complete. The input identities, reference binding, record values and antecedent are unchanged. The first argument is a presentation marker; no physical active-branch interpretation is inferred.

The presentation map is an involution. The separate `perform` interface retains and validates actual application receipts. Two applications recover the presentation but leave two receipts containing their full source and target states. This is not equality of the two-step construction history with an empty history.

## Reader distinction

The complete record reader returns the same three records at the comparison cell in either presentation. The fourth input record remains in the unchanged full preparation.

A history-sensitive reader distinguishes the two points: their ordered children and distinguished path are exchanged. The implementation does not pretend this reader is invariant; it specifies its action. Source and target states are validated against their preparation and exact source paths, so retaining only an endpoint or an unordered support is insufficient.

## Actual reference continuation

The comparison point is attached to the common terminal N through the existing `attachReference` constructor. Two consumer charts in the same reading admit this attachment. In each, the other reference is another actual comparison produced from the **same preparation**, not an invented external value.

The attachment carries the entire comparison point literally. Its existing `splitAttachment` operation recovers that point and the other operand. The contextual exchange therefore has a derived lift:

\[
\widehat\chi=\operatorname{attach}\circ\chi\circ\operatorname{recover}.
\]

This formula **defines** the lift; its commuting square is not an independently discovered native interchange law. The tests check that the existing constructors provide the required domains and recovery, that the inverse works, and that no retained field is lost.

The consumer point changes because its producer history changes. Its chart, physical N occurrence, preparation, antecedent and other operand remain fixed. Leaving the consumer unchanged while claiming to have exchanged the producer is rejected.

## Fresh tests

One fixed source chart is exercised on sixteen tagged Boolean payload preparations. Both consumer charts are checked at all four sign bindings: eight continuation frames and 128 attachment checks.

Seven negative controls reject:

- a discarded operand/context;
- a changed record inconsistent with the preparation;
- an invented path arrow;
- a changed preparation binding without its required packet changes;
- an unchanged consumer after a claimed producer exchange;
- an altered other consumer operand;
- a forged application receipt.

The value-independent record-copying construction explains its operation on arbitrary admitted JSON contents; the sixteen cases are regression tests, not a claim to exhaust that domain.

## What this licenses—and does not

This is an executable **candidate presentation comparison on contextualized records**, with a specified action and a reversible lift through an existing candidate attachment. It is stronger than merely recording a pair of histories, but weaker than establishing that the original standalone paths are natively equivalent.

The comparison and attachment APIs still declare themselves candidates. No Su-32 native `Resolve` derivation or compiler binding has been constructed. The remaining admission question is whether this contextual presentation relation is the intended source comparison, with the intended reader policy.

Nothing here supplies a comparison of a period-generator return with the identity. The exchange receipts carry no admitted period-count relation, so they cannot be used to choose any `d` in `period_relation_selection.md`. No source history is quotiented or discarded.

## Reproduction

```sh
node research/strominger/checkers/check_su32_contextual_path_exchange.mjs
python research/aspect/scc/scc.py check strominger-su32-contextual-path-exchange-v1
```

Receipt: `results/su32-contextual-path-exchange-v1/verification.json`. It retains a complete exchange, its attached presentations, two application receipts, counts, controls and source hashes. `nativeComparisonCompiled` remains false. Existing comparison/attachment implementations were not modified; no proof assistant was run.
