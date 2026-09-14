# v174: selected L2-to-log-line comparison

The explicit detector now constructs the selected rank-one comparison to the
local logarithmic primitive line.

Integrally, send a Bockstein representative f to `rho0(f) gamma`. The A-image
maps to zero, so this descends to the Bockstein image modulo A. The distinguished
transition maps to `3 gamma`, not to the primitive generator. Hence the integral
image is the index-three sublattice of the log orientation line.

Over `Z[1/3]`, the normalized selector `rho0/3` maps the transition to primitive
gamma. Integrally there are three honest alternatives: adjoin a divided
transition cell, accept the index-three log line if physical normalization
permits, or supply separate authority to invert 3.

This constructs the local selected comparison but not the single ringed
filtered correspondence into the literal Q target.

Evidence is `results/L2-selected-log-line-comparison.json` from
`checkers/check_L2_selected_log_line_comparison.py`.
`rzk/202-l2-selected-log-line-comparison.rzk.md` passes all eight declarations
without assumptions.
