# One fixed Su-32 reading: trace to the first missing continuation

## Outcome

The complete **reference-information prefix** is consistent for one fixed incoming reading. It does not yet extend to a source-defined outgoing wiring.

The obstruction to proceeding is not a conflicting sign choice or lost input record. It is the absence of a signed-record operation across the middle. Four globally complete geometric covers are available, but none specifies which records become the outgoing presentation or how their reference contexts and provenance are retained.

There are two levels of status:

- **Native source:** layer-4 comparison sites explicitly retain `comparisonWitness: null` and `outputPairing: null`. Their geometry is established; the lossless join remains a candidate interpretation, not a derived native operation.
- **Granting that candidate baseline:** the prefix is executable through central reconciliation and retains all outer views. The first missing extension is a joint layer-4 → middle-N → layer-6 record/occurrence map, compatible with both the outer branches and central reconciliation.

Thus we have located the missing operation, not completed a physical process.

## Fixed preparation

- Reading: `reading:0:-1`.
- Incoming N: `neutron:0,0,2,1`.
- Opposite outgoing N: `neutron:2,2,0,-1`.
- Sign binding: `[0,0]`, an explicit presentation choice, not an intrinsic sign on each cell.
- Four independently tagged records: `input:P+`, `input:P-`, `input:E+`, `input:E-`.

There is one authoritative input registry. Branch appearances refer to these identities; they are not additional independent input records. Both the input identity and its entry provenance are retained.

## What the trace checks

1. **Layer 2:** four reference cells are actually adjacent to the incoming N and bind the four record labels.
2. **Layer 3:** all four P/E combinations occur at the prescribed four N cells; both reference attachments use actual shared faces.
3. **Layer 4 outer branches:** all eight single-channel views are retained, with their actual incoming channel and charged-cell destination. Treating them as views is an information-model projection, not a newly asserted physical transfer law.
4. **Layer 4 central comparisons:** the four existing shared-reference join candidates retain their full operands and provenance. Equal shared records agree in identity and payload; different signed records stay distinct.
5. **Central N:** both reconciliation orders recover the exact four-record registry and retain their different derivations. This does not replace the outer branches or establish a central-to-peripheral route.
6. **Entire middle cover:** freshly regenerate the existing global incidence assignments. Each of four covers uses all twelve layer-4 charged cells exactly once across six peripheral N groups; every source and target attachment has a shared-face witness. Reflection pairs the complete opposite charged plane and identifies the opposite incoming reading. It is not used to infer payload transport.

Whole covers are considered before their restrictions are checked. No locally chosen reader path is extended into a purported global wiring, and no cover is silently selected as the native one.

## New diagnostic: six channels do not already mean six two-record outputs

Annotating each complete middle cover with its offered input record supports gives, in every case, the sorted support sizes

```
2, 3, 3, 3, 3, 4.
```

These are unions of the two offered operands' labels, **not computed middle outputs**. They show why a count of six geometrically valid P/E-cell pairings does not by itself implement the proposed six signed-pair outputs.

For example, one candidate connects the following at `neutron:0,2,1,0`:

```
source P cell: proton:0,1,1,0
  offered records: {P+, P-, E+}
source E cell: electron:-1,1,1,-1
  offered records: {P-, E+}
```

The shared records agree, so there is no information-level conflict. But the joint available information contains three independent records. Selecting an active pair would require a rule distinguishing that pair from its retained context; dropping the third record would violate the lossless requirement unless it remained recoverable elsewhere under a specified global map.

In particular, **a P cell is not synonymous with a single P payload, nor an E cell with a single E payload**. A shared-reference comparison carries contextual records of both roles.

This is not a no-go theorem for six outputs. An active pair plus retained context could be adequate. The specification does not yet supply that separation or its outgoing attachment.

## Precisely missing object

For the actual fixed input and complete carrier, supply a source-defined operation that determines together:

- the selected complete middle correspondence (or a rule explaining admissible alternatives);
- each outgoing active record/pair and its retained reference context;
- how the actual layer-6 occurrence receives it, rather than merely its reflected cell location;
- compatibility with all retained outer views and the central comparison histories;
- subsequent attachment to the outgoing signed presentation, with recovery of the four independent identities.

The current receipt leaves every `middleOperation` and `targetPayloads` null. No projection, scattering rule, relabelling of different records, or circle-fiber action is installed to force completion.

The distinction matters: **reflection closes the geometry; it does not close the record semantics.**

## Verification and artifacts

Checker: `checkers/check_su32_fixed_reading_trace.mjs`.

Receipt: `results/su32-fixed-reading-trace-v1/verification.json`, including the full input registry, twelve layer-4 views, both central derivations, all four annotated complete middle covers, native unresolved comparison sites and source hashes.

Replay from fresh geometry:

```sh
node research/strominger/checkers/check_sulfur32_middle_layer.mjs
node research/strominger/checkers/check_su32_fixed_reading_trace.mjs
```

An initial test incorrectly used the fixture's whole-depth `comparisons` table as though it were its four entry comparison sites. That schema mismatch was corrected by selecting the opposite entry chart and querying the native obligation builder directly. The corrected checker passed; no native operation or fixture schema was modified.

The checks establish a conditional reference trace and a concrete missing continuation—not completed wiring, a physical law, or a circle bundle.
