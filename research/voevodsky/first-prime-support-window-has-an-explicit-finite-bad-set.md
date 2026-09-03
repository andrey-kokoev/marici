# The first-prime support window has an explicit finite bad set

## Question

Does moving to the first support window containing only one prime power make the component-sensitive tail certificate executable?

## Claim boundary

A floating root-isolation scout at \(L=7/20\), where only \(n=2\) occurs, finds a bad set with modest Shannon trace but more than one thousand components. The component-envelope transition bound inflates the sufficient dimension above five million. This is not interval-certified. It shows that the quadratic component-count bound discards essential endpoint cancellation even in the one-frequency case.

## Support choice

Since

\[
\frac{\log2}{2}<\frac7{20}<\frac{\log3}{2},
\]

the prime sum contains only

\[
n=2.
\]

The combined symbol is

\[
a_L(u)
=
m_\Gamma(u)
-
\frac{\log2}{\sqrt2}\cos(u\log2).
\]

Its roots can be isolated by scanning each fraction of a cosine period and bisecting every sign change.

## Scout result

Among

\[
\delta\in\{0.02,0.05,0.1,0.2\},
\]

the smallest component-envelope dimension occurred at \(\delta=0.05\). The scout found approximately

\[
R=5571.05,
\qquad
N=1229,
\qquad
W=1831.30.
\]

The Shannon trace is only

\[
\frac{LW}{\pi}
\approx204.02.
\]

But the component envelope gives

\[
\operatorname{Tr}(T-T^2)
\lesssim277631.36
\]

and therefore

\[
M\gtrsim5.37\times10^6.
\]

## Oddball disposition

The large gap between Shannon trace \(204\) and sufficient dimension above five million is an explained bound defect. Applying the triangle inequality separately to \(1229\) interval endpoint pairs creates the \(N^2\) loss. The intervals arise from one coherent cosine phase, so their endpoint contributions are highly structured rather than arbitrary.

## Revised target

Do not use component count alone. For the one-prime window, exploit the near-periodic interval train directly in

\[
k_\Omega(t)
=
\frac1{2\pi it}
\sum_j
(e^{ib_jt}-e^{ia_jt}).
\]

The next useful quantity is the actual transition integral computed from the isolated endpoints, with interval arithmetic and controlled truncation. A successful bound should scale near the Shannon trace plus a boundary correction, not quadratically in the number of intervals.

## Scope

The current root isolation and digamma evaluations use ordinary floating arithmetic. They do not certify the root count, interval endpoints, transition trace, or RH.

## Verification

- `research/voevodsky/checkers/scout_single_prime_bad_set.py`
- `research/voevodsky/results/single_prime_bad_set.json`
