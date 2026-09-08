# v26: six-direction first conductor map

**Next plan:** [`rzk-coefficient-interface-v27.md`](rzk-coefficient-interface-v27.md)
adds the two conductor comparison states of the full endpoint-relative source
as a generic checked fibre construction.

`rzk/37-six-direction-first-conductor-map.rzk.md` completes task 6 and the
six-step relative Morse-fibre formalization plan.

The module presents `I/I^2` by its six independent first-occurrence classes

    [X02], [X04], [X24], [X13], [X15], [X35].

It defines the six native endpoint directions and the induced map

    e_d^plus  |-> -t_d [X_d] tensor ell_plus,
    e_d^minus |-> -t_d [X_d] tensor ell_minus.

Each output retains a distinct endpoint-line label, occurrence direction, and
six-coordinate natural Rees monomial. No Rees parameter is inverted. The
source count, target slot, and individual Rees factor are exposed as checked
data.

A fresh 73-file headless closure passed in 35.90 seconds. Evidence:
`results/37-six-direction-first-conductor-map.typecheck.json`.

The six requested Rzk tasks are now represented and checked at their stated
finite/setoid scope. The complete 2,338-column chain-map replay and a physical
Q/support comparison remain outside this plan and continue to depend on
external construction or imported certificate evidence.
