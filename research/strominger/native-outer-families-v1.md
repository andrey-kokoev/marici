# Iteration10: actual native outer-family tables and mass-preserving leaf recovery

## Fresh obligation and result

The42-node net requested the missing native OUTER-family carrier, explicitly distinguishing it from the137-leaf table. The new encoding and live-source exporter now bind both actual terminal family trees to native Table fields.

`export_native_outer_families.py` reruns the previous generated/typed-DG/rung4 adapter and consumes its actual terminal objects. It independently serializes the original source leaf rows and both terminal forests. `--check` regenerates expected source text and rejects drift; it does not trust a manually transcribed count.

## Data retained and kernel checks

`NativeOuterFamilyEncoding.agda` represents each Row with its label, source, target, exact payload, declared mass, leaf index and complete nested member list. String keys use tagged codepoint lists; rational matrix entries use signed numerator/denominator pairs. The native table's Rows are occurrence indices of OUTER rows, so its carrier is correctly32 or1 rather than137.

The exported `ActualNativeOuterFamilies.agda` checks by reduction:

- inherited outer list length32 and common outer list length1;
- total declared mass137 in both cases;
- every leaf has unit mass and every internal family has the sum of its children's masses;
- recursively flattening and sorting by original leaf ID recovers the separately exported original Row list exactly for both policies;
- the complete inherited forest survives Complete packaging;
- unit weights on the32 outer families cannot equal their actual total mass137.

The leaf equality includes payloads, labels, endpoints and masses, not just leaf IDs or cardinality. The sorting convention matches the owner's canonical leaf ordering. Nested member trees are retained in the forest, not erased by its leaf projection.

The module uses the actual `TableFibrationCycle.Table` constructor and `restore-correct`: native source/target restoration preserves the table fields for these outer carriers. This is not an isomorphism from outer rows to leaves. It is a forest-membership projection to leaves and a separate restoration isomorphism on OUTER rows.

## Verification boundary

Mass accounting and equality of the exported finite trees are kernel-checked. Rational mean evaluation is still verified by the existing source checker, not computed in this Agda module. For example, the source rejects replacing weighted family means by equal outer-family weights; the kernel additionally certifies that those outer weights have the wrong total mass. A generic rational weighted-mean theorem is not claimed.

The exact export retains matrix payloads as data. It does not formalize the entire DG realization or supply the independently retained reference d by inference from those payloads.

Executed:

    python research/strominger/checkers/export_native_outer_families.py
    python research/strominger/checkers/check_native_outer_families.py

Live-source export comparison and fresh safe Cubical Agda closure passed with stable inputs. The adapter's source checks and hostile controls rerun. Receipt: `research/strominger/results/native-outer-families-agda-v1.json`.

## Remaining schedule gate

The native generated leaf table uses kind-tagged endpoint lists and occurrence labels. The newly exported terminal forest uses the owner's serialized Row keys and payloads. Both have now been independently checked, but there is not yet a KERNEL-checked comparison between the generated native leaf labels/endpoints and the serialized original leaf-row fields. Equal list counts do not supply that comparison.

Next: define that exact structural encoding on the generated native leaves, prove agreement with the exported original label/source/target fields, and package the predecessor/selector and outer forest together under this bridge. That closes the common-carrier gap needed by `rung-operation-schedule`; do not repeat another family-count or export-only wrapper.

The task remains open pending this comparison. Any later Feedback.run identification remains separate: the present construction uses Table and Complete APIs without invoking Feedback.run or filling an obstructed free seed. No unique grouping policy, physical normalization or universal phase semantics is inferred.
