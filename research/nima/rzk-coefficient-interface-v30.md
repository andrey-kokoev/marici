# v30: fourteen-state occurrence-tensored Q complex

**Next checkpoint:** [`rzk-coefficient-interface-v31.md`](rzk-coefficient-interface-v31.md)
independently replays the complete sparse polynomial contraction and both
chain-map equations.

`rzk/41-q-occurrence-tensor.rzk.md` completes task 4 of the full-Q support
plan. It tensors every state of the reduced seven-state `Q_cell` with the two
states of the independent occurrence Koszul factor

    d(h_occ)=X35 p.

The result has 14 states and 19 polynomial arrows. Its coefficient monomials
retain seven natural exponents:

    (X03,X14,X25,u03,u14,u25; X35).

The auxiliary X35 is separate from the native normal data. On the four
homological degree-three Q states its occurrence arrow carries the negative
tensor sign; on the three degree-two p states it carries the positive sign.
The Q differential preserves the occurrence state.

Rzk checks all five cancellation shapes, every generator square, and
square-zero on arbitrary finite integral polynomial chains. A fresh 72-file
headless closure passed in 36.60 seconds. Evidence:

- `results/41-q-occurrence-tensor.typecheck.json`
- `results/q-occurrence-tensor-generation.json`

This checks the reduced 14-state target, not the contraction from 786 states.
Importing or regenerating the contraction identities is the next task.
