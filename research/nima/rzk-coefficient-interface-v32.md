# v32: recovered seven-triangle Morse primitive

**New consequence:** [`rzk-coefficient-interface-v33.md`](rzk-coefficient-interface-v33.md)
formalizes the rank-two filling coordinates and proves that preserving the
complete lower attachment selects the unique Morse filling class.

`rzk/42-seven-triangle-morse-primitive.rzk.md` completes task 6 and the full-Q
support formalization plan.

The generator extracts the seven selected primitive terms and all 15
differential entries leaving them from
`full_q_support_relative_morse_certificate.json`. It retains the nine distinct
boundary states required before cancellation, rather than keeping only the
three surviving roof terms.

The primitive has coefficients

    +1, +1, -1, -1, +1, -X03, +X03

on certificate states `38,246,247,273,274,307,309`. Rzk checks that its complete
boundary cancels to exactly

    state 22 - state 286 + X03 state 319,

which is the exported three-term corrected roof. The local formalization has
16 states, 15 differential entries, finite integral X03-polynomial
coefficients, and no inversions.

A fresh 71-file headless closure passed in 44.65 seconds. Evidence:

- `results/42-seven-triangle-morse-primitive.typecheck.json`
- `results/seven-triangle-generation.json`

All six requested tasks are now complete at the documented scopes. This proves
the selected Q nullhomotopy algebraically; it does not identify that
nullhomotopy with the conductor nullhomotopy under a physical extraordinary
comparison and therefore does not assign a value to physical Delta_J.
