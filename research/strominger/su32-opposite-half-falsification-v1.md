# Opposite-half falsification: no independent filter

## Result

**None of the 40 middle assignments is rejected by the reflected opposite-half reference constraints.** Each of the four complete covers still has ten surviving assignments.

This is not evidence that all 40 execute as native reversible processes. The stronger proposed test cannot be completed with the supplied operations: there is still no native middle transition or forward outgoing-half rule to execute and invert.

The audit instead establishes why the available opposite-half test cannot select a candidate: its constraints are reflected copies of the already checked incoming constraints. My proposed next test overestimated the independent information supplied by the opposite-half geometry.

## Correspondence fixed before testing

Use the same fixed reading `reading:0:-1` and its opposite `reading:0:1`. Construct middle-plane reflection from native coordinates once, for the complete carrier. Verify that it is a bijection on all 51 cells and squares to identity.

For both charts' fixed `[0,0]` reference frames, the reflected geometric reference correspondence gives

```
source P+ -> opposite local E+
source P- -> opposite local E-
source E+ -> opposite local P+
source E- -> opposite local P-
```

These are changes of local reference names. A record whose identity is `input:P+` remains `input:P+`, including its original entry provenance; it is not converted into a different record because its opposite local slot is called E+.

This correspondence is not fitted separately to any middle assignment. It is also not silently installed as a native signal transport law. The opposite registry is a pullback used to compare reference descriptions, not an observed or computed outgoing state.

## Checks

- Reflect all four channel nodes, four comparison nodes and both reconciliations: **10 full operand trees** validate in the opposite chart.
- Apply the inverse reference reflection: every complete original tree, including its child ordering and provenance, is recovered exactly.
- Check each offered P/E operand against its reflected target in all four covers: **48 side checks** pass.
- Check the selected pairs for all **40 candidates** against opposite offered supports: all pass.
- Check original payload identities and provenance for every selected slot: **480 identity checks** pass.
- A deliberately incorrect label correspondence is rejected by the opposite comparison validator.

The independently constructed opposite canonical tree may use a different lexical child ordering. The test compares its records while retaining the exact reflected original tree; it does not erase history to manufacture round-trip equality.

## Why there is no pruning

Write A_g and B_g for the two source operand record-label sets offered at a middle group g. Let rho be the single reflected reference renaming. The actual opposite comparison structure supplies the corresponding sets rho(A_g), rho(B_g), with P/E presentation exchanged.

For any candidate active pair Q_g,

```
Q_g subset (A_g union B_g)
    iff
rho(Q_g) subset (rho(A_g) union rho(B_g)).
```

So the opposite joint-availability test is equivalent to the source test. The counts are an implementation check of that structural equivalence, not forty independent pieces of evidence for physical reversibility.

Likewise, reflection squared is identity on geometric/reference descriptions. That is not a theorem that time evolution followed by its inverse recovers the state: no such evolution has been supplied.

## What remains genuinely untested

To test complete reversible execution, one needs:

1. A native operation at the middle, with a domain of actual retained record/occurrence states and an output at the actual layer-6 attachments.
2. A forward rule through the opposite half and an inverse on the admitted state domain.
3. Compatibility of these operations with retained outer views and central reconciliation, rather than a geometric correspondence between their locations.

No candidate-specific output maps, extra communication, independent output payload values, phase law or circular order were introduced to fill these gaps.

## Scientific disposition

- **Reflected reference compatibility:** all 40 candidates pass.
- **Selection by the opposite-half geometry:** provides no additional constraint in this construction.
- **Existence of a complete native reversible process:** neither verified nor falsified.

The productive conclusion is a stopping boundary for geometry-only filtering. Repeating reflected incidence or retention tests cannot select a native operation that the current specification leaves open. Any subsequent discriminator must be an independently justified requirement, not one manufactured to reduce the candidate count.

## Replay

```
node research/strominger/checkers/check_su32_opposite_half_falsification.mjs
```

Fresh headless execution passed. The checker validates the source hashes of its fixture, fixed-reading trace and six-pair enumeration before testing.

Receipt: `results/su32-opposite-half-falsification-v1/verification.json`.

Source implementations were not modified. `nativeExecutionTested` and `physicalReversibilityEstablished` remain false.
