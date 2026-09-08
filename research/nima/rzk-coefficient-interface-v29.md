# v29: reduced seven-state Q complex

**Next checkpoint:** [`rzk-coefficient-interface-v30.md`](rzk-coefficient-interface-v30.md)
tensors the seven states with the independent occurrence Koszul factor and
checks all 14-state tensor signs.

`rzk/40-reduced-seven-state-q-cell.rzk.md` completes task 3 of the full-Q
support plan.

It defines the seven states

    T, h03, h14, h25, p03, p14, p25

and the exact reduced differential

    d(T)   = X03 p03 + X14 p14 + X25 p25,
    d(h03) = u03 p03,
    d(h14) = u14 p14,
    d(h25) = u25 p25.

Coefficients are finite integral polynomial expressions in six natural
exponents ordered `(X03,X14,X25,u03,u14,u25)`. None of the long occurrence or
normal variables is inverted. The three p states are terminal.

Rzk checks every generator square and extends square-zero to arbitrary finite
integral polynomial chains. A fresh 71-file headless closure passed in 33.91
seconds. Evidence: `results/40-reduced-seven-state-q-cell.typecheck.json`.

This is the contracted target complex itself, not yet an internal replay of the
393-state contraction. Tensoring it with the independent occurrence Koszul
factor to obtain the checked 14-state complex is the next task.
