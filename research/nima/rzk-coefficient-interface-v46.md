# v46: common spatial-correspondence gate

**Assembly update:** [`rzk-coefficient-interface-v47.md`](rzk-coefficient-interface-v47.md)
records the regulator vertex decomposition and distinguishes the section-bearing
triple intersection from the obstructed closed-support union.

`rzk/60-common-spatial-correspondence-gate.rzk.md` records the two mechanically
sharp consequences of the tested common carrier.

First, its genuine generic image is represented together with the supplied
Morse homotopy, and Rzk checks that the image is its boundary. The same identity
is lifted to a dependent pair retaining the codimension-three Gysin determinant
frame. Thus tensoring with the nonzero normal residue does not convert this
particular null generic morphism into the known nonzero reverse pairing.

Second, the actual mixed flag triangle has boundary

    [D03,c] - [o,c] + [o,D03].

The tempting smaller projection kills the triangle and both mixed edges while
retaining `[o,D03]`. Rzk computes the projected boundary as a primitive unit
edge and proves that an asserted chain-map equation would imply `0_Z=1_Z`.
This formally blocks transport of the old coefficient-one coordinate test to
the genuine relative flag quotient.

A fresh 73-file transitive closure passed in 26.97 seconds. Evidence:
`results/60-common-spatial-correspondence-gate.typecheck.json`.

Scope: the full 39-simplex middle carrier, two endpoint cone homotopies,
306-generator generic retraction, and 1,792 tensor-column checks remain in the
incoming certificate. The module captures the factorization obstruction, not a
no-go theorem for nonfactorizing complementary-support constructions.
