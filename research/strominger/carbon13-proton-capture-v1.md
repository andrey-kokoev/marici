# C-13 + proton: a compatible six-electron N-14 reference

**Superseded witnesses:** the [all-contact repair](assembly-contact-coverage-repair-v1.md)
reselected the C-13 parent. Current N-14+ witnesses add proton 47/orientation
1705 or proton 49/orientation 1865, both all-contact audited. The IDs and counts
below describe the historical selection; current data are in the repair note
and refreshed receipt.

## Question and controlled change

Try adding one proton to the selected C-13 reference without simultaneously
requiring a seventh electron. Keep every old nuclear cell, the six electron
cells, C/M roles and native readers. No production contact or phase rule is
relaxed. This tests a structural endpoint suggested by C-13 proton capture,
not the dynamics of that physical reaction.

## Result

**Two compatible endpoints were found**, each with 7P/7N/6e. Under the usual
particle-charge interpretation these are N-14+ ion references, not neutral
N-14 atoms.

| Added proton cell | Reader assignment | Preserves old readers |
|---|---:|---|
| 18 | 2713 | yes |
| 24 | 5425 | yes |

All neighboring regular proton attachment cells in the existing domain were
examined. Two extensions satisfy the retained geometry and role constraints.
All **12,288** reader assignments for those two candidates were compiled;
exactly the two above passed the unchanged phase compiler and audit.

The selected first witness has **54 history-bearing states**, covers **20/20
carriers**, and preserves every old C-13 reader and transport edge. No electron
is added, removed or moved in this retained-electron experiment.

## Bare-nucleus control

Stripping the electrons and their exclusive vertex-role constraints leaves the
same two valid nuclear geometries. At the selected charged witness's reader
assignment, the unchanged compiler rejects the bare candidate with
`phase-directed-dead-end`: its certificate demands terminal E exits, and the
bare candidate has none.

That is a limitation of this admission certificate for bare nuclei, not a
proof that the nuclear geometry is inconsistent or the nucleus cannot exist.
No nuclear-only exit convention was invented to bypass it. The bare control
was not an exhaustive phase search.

## Interpretation

The earlier obstruction applies to **neutral 7P/7N/7e packing**, not to every
reference having an N-14 nucleus. With six retained electrons, adding a proton
to C-13 works under the existing rules. This narrows the discrepancy to the
neutral-electron assembly requirement in this case.

We have not modeled photon emission, energy/momentum balance, capture rates,
binding, electron-cloud response or physical stability. Nor have we admitted
neutral N-14 or modified the viewer. In a stellar plasma, the actual reactants
may be much more highly ionized; the six-electron endpoint is a controlled
model test, not a claim about the dominant stellar charge state.

## Reproduction

```sh
node research/strominger/checkers/check_carbon13_proton_capture.mjs
```

Evidence: `results/carbon13-proton-capture/verification.json`, including both
geometry candidates, complete charged-case acceptance/rejection counts, the
bare control, source fingerprints and the first full phase certificate.
