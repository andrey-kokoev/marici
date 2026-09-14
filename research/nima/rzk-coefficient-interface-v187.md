# v187: conductor/log primitive lines have opposite characters

Scalar primitive normalization does not identify the qg2 conductor line with
the logarithmic normal-link line. The normalized wall pullback has trivial
Kummer character `+1`, whereas the log primitive generator is reflection odd
with character `-1`.

For a one-dimensional equivariant comparison t in characteristic zero, the
intertwiner condition is `t=-t`, hence `t=0`. Therefore there is no nonzero
equivariant identification of the two lines as currently typed.

The ambient relative cut chain must supply a sign/orientation local system.
Tensoring the even conductor line with this sign line changes its character to
odd and makes a nonzero comparison possible. This orientation twist must be
source-derived from cut ordering or normal orientation; it cannot be supplied
by the scalar unit normalization of v186.

Evidence is `results/qg2-log-orientation-character-gate.json`.
`rzk/215-qg2-log-orientation-character-gate.rzk.md` passes all eight declarations
without assumptions.
