# C3: the physical corner is the primitive dual detector of the global e6 difference

Use the normalization-component basis

\[
(C_+,C_-)
\]

and the primitive sheet boundary

\[
d_{\rm sh}=(-1,1).
\]

The integral normalization map sends the two sheet generators to their Picard classes. Hence

\[
d_{\rm sh}\longmapsto C_--C_+
=d_\infty
=3H-E_1-\cdots-E_6-3E_7.
\]

This is exactly the primitive global \(e_6\) component-difference class.

The physical local Betti covector has symmetric representative

\[
\eta=(-1/2,1/2),
\qquad
\eta(d_{\rm sh})=1.
\]

It admits an integral extension to the Picard lattice. Intersection with \(E_1\) restricts to

\[
(E_1\cdot C_+,E_1\cdot C_-)=(0,1),
\]

and therefore evaluates

\[
E_1\cdot(C_--C_+)=1.
\]

The representatives \((0,1)\) and \((-1/2,1/2)\) differ by the diagonal constant

\[
(1/2,1/2),
\]

which vanishes on every degree-zero sheet boundary. Thus they define the same reduced integral dual class.

Iteration 3 showed that the sourced physical occurrence pair maps to \(-\eta\). The two-node global Cech construction maps to \(d_\infty\). Iteration 4 placed the logarithmic and Cut-nearby coefficient operations on their common \(e_6\) conductor line.

Consequently C3 is confirmed up to overall orientation:

> The physical corner interval is the primitive dual detector of the same global component-difference class carried by the four-mark geometric construction.

Their common mod-two readout is

\[
(1,0).
\]

Certificate:

- `research/voevodsky/checkers/confirm_C3_local_global_e6_comparison.py`;
- `research/voevodsky/results/C3_local_global_e6_comparison.json`.
