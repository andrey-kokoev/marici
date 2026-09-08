# v22: relative physical cone fibre

**Next checkpoint:** [`rzk-coefficient-interface-v23.md`](rzk-coefficient-interface-v23.md)
adds two independently detectable formal endpoint lines with occurrence-degree
metadata and no coefficient inverses.

`rzk/33-relative-physical-fibre.rzk.md` completes the additive core of tasks 1
and 2 for the endpoint-derived comparison.

It extends the checked 11-state physical source J by one conductor state in
cone degree zero. The three road columns acquire their conductor-augmentation
entry, giving the differential of

    F = fib(epsilon r : J_B -> C[1])

at the conductor-coefficient specialization. The generated complex has 12
states and 19 signed arrows. Rzk checks every generator square and extends
square-zero to arbitrary finite integral chains.

The physical primitive z is also embedded. Its J-boundary cancels while its
new cone component is exactly the conductor unit; Rzk checks this coefficient
directly. Thus the module distinguishes the primitive in J from its behaviour
inside the fibre rather than silently treating z as a fibre cycle.

A fresh 71-file headless closure passed in 41.34 seconds. Evidence:

- `results/33-relative-physical-fibre.typecheck.json`
- `results/relative-fibre-generation.json`

Scope: this is the integral additive cone skeleton. The split-normalization
polynomial B-action, formal endpoint lines, 44-entry comparison, corrected
Morse-chain evaluation, and I/I^2 map remain subsequent tasks.
