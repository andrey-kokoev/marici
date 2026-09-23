# Commuting saturation does not imply equivalent filling pencils

## Actual finite replay

Recheck both saturation orders on every restriction of the actual four-state A/B evidence carrier, now retaining the sets of intermediate source witnesses for every boundary pair. Its commuting restrictions happen to have equicardinal discrete intermediate fibers. This small source supplies no general proof-relevant interchange theorem.

## Independent obstruction fixture

Declare five source states arranged by two coordinate observers:

    (r0,c0,0), (r0,c0,1), (r0,c1,0), (r1,c0,0), (r1,c1,0).

One equivalence remembers the row, the other the column. Every row/column intersection is nonempty. Both composed endpoint relations are therefore total and equal: the saturations commute.

For endpoints a=(r0,c0,0) and c=(r1,c0,0), the row-then-column composite has two middle witnesses, (r0,c0,0) and (r0,c0,1). The column-then-row composite has one middle witness, (r1,c0,0).

With discrete source identity, these witness types cannot be equivalent. Distinct tagged states remain independently specified source states. Declaring them homotopic would change the source-equivalence contract, and an audit of the middle tag would have to descend through any proposed identification.

This is a separate mathematical fixture. It is not evidence of a hidden multiplicity defect in the actual four-state analytical family.

## A positive transport control

On the separately declared eight-state product {r0,r1} x {c0,c1} x {0,1}, every intersection has the same tagged two-point witness space. The explicit middle transport

    (row(a),col(c),tag) -> (row(c),col(a),tag)

is bijective with an explicit inverse. All 128 endpoint/middle checks pass. This control exposes the extra structure that makes witness comparison available. It is a different source, not an authorized completion of the five-state fixture.

A common cardinality alone does not select an equivalence: a two-point fiber already has two bijections. Source-declared transport and its higher coherence still require independent specification.

## Structural result

Existential endpoint compatibility, equivalence of filling pencils, and coherent equivalences across repeated diamonds are three separate levels. Kernel permutability settles the first; it does not imply the second. The third remains a substantive additional obligation after any individual bijections have been constructed.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_proof_relevant_saturation_diamonds.py

Artifact: `results/proof-relevant-saturation-diamonds.json`.
