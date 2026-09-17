# Total variation is too coarse, but the jump-leading tail fits

A 2200-node-per-segment scout evaluated the weighted variation of the four
dangerous prime images. The total-variation caps fail for the first three
vectors, by factors `104`, `7.5`, and `1.70`. Therefore the one-integration
absolute bound cannot close the residual gate.

The failure is localized to the smooth derivative integral, not the jumps.
The weighted jump masses are

\[
0.0019407,\quad0.0303920,\quad0.261463,\quad1.99576.
\]

Multiplying by the `N=5000` Legendre tail factor `0.00836913` gives leading
jump-tail bounds

\[
1.63\times10^{-5},\quad2.55\times10^{-4},\quad
2.19\times10^{-3},\quad1.67\times10^{-2},
\]

all below their residual budgets. The surviving task is therefore to integrate
the smooth piece by parts a second time. Since each piece is a polynomial of
degree at most 999, repeated integration terminates and produces only finitely
many boundary jets. No global total-variation estimate should be used.
