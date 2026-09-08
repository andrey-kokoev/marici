# v23: formal endpoint lines without inverses

**Next checkpoint:** [`rzk-coefficient-interface-v24.md`](rzk-coefficient-interface-v24.md)
imports all 22 nonzero source columns and 44 polynomial target entries into a
checked endpoint-line-valued sparse map.

`rzk/34-formal-endpoint-lines.rzk.md` completes task 3 of the relative
Morse-fibre plan.

The module introduces two distinct basis labels `L_+` and `L_-`. Their six
occurrence-degree vectors are respectively

    (0,0,0,-1,-1,-1),
    (-1,-1,-1,0,0,0),

in the order `(02,04,24,13,15,35)`. These values are grading metadata only:
the lines are not represented by Laurent monomials, scalar reciprocals, or a
localization of the coefficient ring.

The endpoint-refined target is represented by finite integral sums on
`L_+ x F` and `L_- x F`. Rzk checks recovery under each matching line
projection and vanishing under the opposite projection. Thus the two labelled
summands remain independently detectable rather than being identified after
forgetting occurrence grade.

A fresh 72-file headless closure passed in 35.84 seconds. Evidence:
`results/34-formal-endpoint-lines.typecheck.json`.

Tasks 4--6 remain: generate the sparse endpoint map, evaluate the corrected
Morse chain, and encode its six-direction derived conductor symbol.
