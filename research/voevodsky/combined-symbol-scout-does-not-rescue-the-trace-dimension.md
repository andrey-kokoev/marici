# The combined-symbol scout does not rescue the trace dimension

## Question

Does retaining exact gamma--prime cancellation make the trace-based finite tail reduction computationally feasible at \(L=\log2\)?

## Claim boundary

A deterministic floating scout estimates an approximately eighty-fold reduction relative to absolute prime domination, but the best tested dimension remains about \(2.5\times10^8\). Exact symbol cancellation helps materially but does not make the trace-only concentration certificate executable. The estimates are not interval-certified and do not bear on RH.

## Exact negative-depth constant

For the combined symbol \(a_L\), the global minimum bound is attained at \(u=0\): the gamma multiplier is minimal there and every prime cosine is one. Thus

\[
C_-(L,\delta)
=
C_{\rm low}^{\Gamma}+C_{\rm prime}(L)
\approx1.8984915358
\]

for every positive \(\delta\) whose bad set contains zero.

## Scout protocol

At \(L=\log2\), sample the symmetric bad set

\[
\Omega_{L,\delta}
=
\{u:a_L(u)<\delta\}
\]

by a deterministic irrational-rotation sequence with \(300{,}000\) points for each

\[
\delta\in\{0.05,0.1,0.2,0.4,0.8\}.
\]

The enclosing absolute cutoff is defined by

\[
m_\Gamma(R)=C_{\rm prime}(L)+\delta.
\]

Outside it, \(a_L(u)\geq\delta\) follows from the absolute cosine bound.

## Result

The best tested value is \(\delta=0.1\):

\[
R\approx2.3542\times10^9,
\]

\[
\frac{|\Omega_{L,\delta}|}{2R}
\approx0.01198,
\]

\[
|\Omega_{L,\delta}|
\approx5.6407\times10^7.
\]

The trace certificate then estimates

\[
M\approx2.4872\times10^8.
\]

This improves the absolute-bound scout from roughly \(1.9962\times10^{10}\), but remains computationally unusable.

## Disposition

The exact combined symbol is retained, but the trace inequality is now the dominant identified loss. A usable certificate needs certified decay of the concentration eigenvalues beyond the Shannon transition, not merely their sum. The next typed target is an explicit upper bound for

\[
\lambda_{M+1}(T_{L,\delta})
\]

in terms of \(M\) and the geometry of \(\Omega_{L,\delta}\), preferably using interval count or boundary complexity in addition to total measure.

## Scope

The scout uses floating arithmetic, asymptotic digamma evaluation, and quasimonte Carlo sampling. It neither encloses the bad set nor proves its measure. The displayed scale is diagnostic.

## Verification

- `research/voevodsky/checkers/scout_combined_symbol_bad_set_log2.py`
- `research/voevodsky/results/combined_symbol_bad_set_log2.json`
