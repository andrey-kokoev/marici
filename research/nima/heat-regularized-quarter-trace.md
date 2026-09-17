# Heat-regularized quarter trace

Let

\[
L_n=\mathbb Z^{D_n}
\]

with quadratic number operator

\[
N\delta_m=\lVert m\rVert^2\delta_m.
\]

For every `t>0`, the heat operator is trace class:

\[
\operatorname{Tr}(e^{-tN})
=\left(\sum_{k\in\mathbb Z}e^{-tk^2}\right)^{|D_n|}
=\vartheta(t)^{|D_n|}.
\]

Pontryagin Fourier conjugates `N` to the Laplacian on the dual torus. The same regulator therefore applies in all four charts and commutes with the chart successor.

On the four-chart direct sum, let `P_i` project to chart `i`. Equal heat traces give

\[
\frac{\operatorname{Tr}(P_i e^{-tN_{tot}})}
{\operatorname{Tr}(e^{-tN_{tot}})}
=\frac14
\]

for every positive `t`.

## Restriction to the Catalan subspace

Every triangulation incidence vector has exactly `n-3` nonzero coordinates. Hence

\[
N\delta_{v_T}=(n-3)\delta_{v_T}.
\]

The heat operator is scalar on the finite Catalan subspace:

\[
e^{-tN}|_{H_n}=e^{-t(n-3)}I.
\]

Consequently heat weighting preserves every normalized Catalan rank trace. For the forced-channel projection,

\[
\frac{\operatorname{Tr}(P_n e^{-tN})}
{\operatorname{Tr}(e^{-tN}|_{H_n})}
=\frac{C_{n-3}}{C_{n-2}}
\longrightarrow\frac14.
\]

The same observation preserves the quarter-rotation character multiplicities. Thus one Fourier-invariant trace regularization simultaneously yields:

\[
\text{chart projection trace}=\frac14
\]

at finite degree and

\[
\text{forced-channel and geometric-character traces}\longrightarrow\frac14
\]

with their previously computed finite corrections.

This is an ordinary positive heat trace on the Hilbert completion. The stable categorical supertrace carries homological signs and is a separate invariant.

`check_heat_regularized_four_chart_trace.py` evaluates the theta trace at channel ranks 2, 20, and 54 for three positive heat times and verifies the normalized chart trace numerically.
