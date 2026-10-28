# Native selected-point realization for the fixed Ramsey task

## Scope and candidate

Net node: `native-query-selection`. This is a bounded forward-realization attempt for the existing two-word discriminator, with all nine length-two words as additional exhaustive controls. It is not the uniform task-package conjecture or native Ramsey forcing.

The pattern is not an answer parameter. It is bound to the canonical source P packet's ordered phase window C0,M0,C1. Under the established four-coordinate lattice projection

$$
F(b)=(b_1+b_2,b_1+b_3,b_2+b_3),
$$

those source references are 000,110,101. The complete L_2 coloring is supplied input. The input word is the query request; neither its target point nor its color is an argument to the constructor.

## Native forward constructor

Retain the existing encoded word trace. Append a finite program selected by the counts of input letters 1 and 2. The exact program is preregistered in `contracts/ramsey-native-query-selection-attempt.v1.json`.

Each instruction is selected from actual `GenerativeAssemblyRules.outgoing` results and checked by `validateTransfer`. Native NN steps are included; the original word-trace implementation and production source modules are unchanged. Every suffix retains full source/target packets and charts, all five coefficient coordinates, phase frames and actual phase-advance witnesses. Their outside-context coefficient law remains declared model input, not derived physics.

Apply the same observation at every resulting terminal packet: the **first occurrence of its actual ordered phase window**, given by `phaseFrame(chart,origin).window[0]`. Thus selection changes the native path/terminal frame rather than attaching a host-computed target coordinate to an unchanged endpoint.

The geometric calculation behind the program is small. Write R for P reader advance, A for PN attachment and T for NN advance. With at most two nonzero letters, the original word prefix has zero, one or two P reader advances; PN/inverse-PN zero loops restore the complete packet. For one nonzero letter, the prefix first window point is 101. Letter 2 therefore needs no suffix; letter 1 uses R then A, making the N window's first point 110.

For two nonzero letters, the prefix P chart again has the canonical four primitive reference marks, with its retained origin and coefficient packet. Starting with A, the first three T steps traverse the source's fixed octahedral components. After two T steps the associated inverse-PN P reference has first point 202; after three it has first point 220. The N first window point after three T steps is 211. These are respectively the sums for words 22,11 and 12/21. The checker verifies these calculations against actual generated native geometry rather than prescribing their target coordinates to the producer.

## Verification and strongest rivals

The independent verifier knows the requested input word. It verifies the old word prefix, replays the native suffix, derives the terminal occurrence and only then compares its projected point with the task's arithmetic word sum. Arithmetic appears in this verifier, not in the forward selection compiler. The supplied color is read at the already selected point.

The strongest controls erase or exchange suffixes **and recompute consistent native endpoints, markers and colors**. Such paths can remain entirely native-valid while selecting the wrong query for the retained requested word. The task verifier must reject them. Additional controls change references, all-five-slot data, the requested word, coloring completeness or the reported color. Recoloring must leave the native selection path unchanged.

The source-valid wrong-query controls separate native path validity from the commuting word-to-point obligation. Merely validating transfers or attaching a point label would not pass this test.

## Exact residual

The instruction dispatcher is a bounded **host compiler** acting on supplied word tokens. Native transfers realize its selected point, but no autonomous native branching machine is established. The complete color-table lookup is an explicitly declared observation of input data, not a new P/N transfer. A host-only decoder is therefore not being promoted to a native controller.

The finite instruction table is restricted to this source-bound pattern and word length two. It is not a compositional addition algorithm for arbitrary words, nor admission of arbitrary native input packages. Those belong to `native-task-package-lift`. All nine word cases may pass while that uniform conjecture remains open.

Verification level: written finite source-geometry argument, actual native packet/phase replay and independent Python arithmetic/phase checks; not kernel verified, not full native task admission or forcing. The resulting receipt owns the executed outcomes and counts.

## Artifacts

- Producer/verifier: `research/voevodsky/ramsey-native-query-selection.mjs`.
- Native controls: `research/voevodsky/checkers/check_ramsey_native_query_selection.mjs`.
- Independent verifier/wrapper: `research/voevodsky/checkers/check_ramsey_native_query_selection.py`.
- Receipt: `research/voevodsky/results/ramsey-native-query-selection-v1.json`.
