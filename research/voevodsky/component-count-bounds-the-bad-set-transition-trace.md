# Component count bounds the bad-set transition trace

## Question

Can \(\operatorname{Tr}(T-T^2)\) be bounded explicitly from a finite interval enclosure of the bad-frequency set?

## Claim boundary

Yes. If the bad set is a union of \(N\) bounded intervals with total measure \(W\), its Fourier kernel has simultaneous mass and boundary-count bounds. Integrating their minimum against the exact spatial crossing weight gives a closed transition-trace estimate. The estimate is rigorous once \(N\) and \(W\) are certified; those enclosures remain open.

## Leakage identity

Let \(I=(-L,L)\), let \(\Omega\) be the bad-frequency set, and define

\[
k_\Omega(t)
=
\frac1{2\pi}
\int_\Omega e^{iut}du.
\]

For the time--frequency concentration operator,

\[
\operatorname{Tr}(T-T^2)
=
\int_{x\in I}
\int_{y\notin I}
|k_\Omega(x-y)|^2dy\,dx.
\]

For a fixed displacement \(t=x-y\), the measure of crossing pairs is

\[
\min(2L,|t|).
\]

Therefore

\[
\operatorname{Tr}(T-T^2)
=
\int_{\mathbb R}
\min(2L,|t|)|k_\Omega(t)|^2dt.
\]

## Fourier-kernel envelope

If \(\Omega\) is the disjoint union of \(N\) intervals with total measure \(W\), then

\[
|k_\Omega(t)|
\leq
\frac{W}{2\pi}
\]

by direct integration, while endpoint evaluation of every interval gives

\[
|k_\Omega(t)|
\leq
\frac{N}{\pi|t|}.
\]

Thus

\[
|k_\Omega(t)|
\leq
\min\left(
\frac{W}{2\pi},
\frac{N}{\pi|t|}
\right).
\]

The crossover is

\[
t_0=rac{2N}{W}.
\]

## Explicit transition bounds

If \(LW\geq N\), equivalently \(t_0\leq2L\), direct integration gives

\[
\operatorname{Tr}(T-T^2)
\leq
\frac{N^2}{\pi^2}
\left[
3+2\log\left(\frac{LW}{N}\right)
\right].
\]

If \(LW<N\), then

\[
\operatorname{Tr}(T-T^2)
\leq
\frac{4LWN-L^2W^2}{\pi^2}.
\]

Both formulas agree at \(LW=N\), where their value is \(3N^2/\pi^2\).

## Resulting dimension

For

\[
\eta=rac{\delta}{\delta+C_-},
\]

a sufficient concentration dimension is

\[
M
\geq
\frac{LW}{\pi}
+
\frac{1}{\eta}
\operatorname{Tr}(T-T^2),
\]

with the transition trace replaced by the appropriate displayed bound.

## Limitation

The estimate scales quadratically in the component count. If the oscillatory combined symbol creates very many bad intervals, this envelope may be worse than trace-only counting. That failure would identify boundary complexity, rather than bad-set measure, as the dominant obstruction. Cancellations between interval endpoints are discarded here.

## Disposition

The transition-trace formula is now explicit in two finite geometric statistics, \(N\) and \(W\). The next executable step is certified root isolation for \(a_L(u)=\delta\) on the finite absolute enclosure, yielding a rigorous component count and measure. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_component_transition_trace_bound.py`
- `research/voevodsky/results/component_transition_trace_bound.json`
