# Nested-set measure removes the single-prime connectivity gate

## Question

Is connectedness of every translated one-prime bad section actually needed to control the Abel modulation term?

## Claim boundary

No. The Fourier amplitude of each translated bad section can be written as an integral over the section itself. Exact nesting then makes the amplitude variation telescope by removed measure, regardless of connectivity or component count. This removes the left-half convexity gate. The dual-resonance integral remains to be bounded.

## Section amplitudes

In the reference cell of length \(p\), let

\[
S_{j+1}\subseteq S_j
\]

be the nested measurable bad sections already derived from gamma monotonicity. Define

\[
A_j(t)
=
it\int_{S_j}e^{ixt}dx.
\]

When \(S_j=[\alpha_j,\beta_j]\), this reduces to

\[
A_j(t)
=
e^{i\beta_jt}-e^{i\alpha_jt},
\]

but the integral definition remains valid for disconnected sections.

## Variation bound

Nesting gives

\[
A_j(t)-A_{j+1}(t)
=
it\int_{S_j\setminus S_{j+1}}e^{ixt}dx.
\]

Therefore

\[
|A_j(t)-A_{j+1}(t)|
\leq
|t|\,|S_j\setminus S_{j+1}|.
\]

Summing over \(j\) and using disjointness of successive removed layers,

\[
\operatorname{TV}_jA(t)
\leq
|t|
\sum_j|S_j\setminus S_{j+1}|
=
|t|(|S_0|-|S_{N-1}|)
\leq
|t|p.
\]

No interval endpoints or turning-point count appear.

## Abel consequence

The previous Abel estimate becomes

\[
|E(t)|
\leq
\min\left(
N,
\frac2{|1-e^{ipt}|}
\right)
\left(2+|t|p\right),
\]

because \(|A_{N-1}(t)|\leq2\).

This bound preserves periodic cancellation away from resonances and is valid for arbitrary measurable nested sections.

## Remaining gate

The right-hand side still has dual resonances at

\[
t=\frac{2\pi k}{p}.
\]

Near each resonance the trivial factor \(N\) must be used; away from it the reciprocal-distance factor applies. The next object is a piecewise integral of

\[
\min(2L,|t|)
\frac{|E(t)|^2}{4\pi^2t^2}
\]

with optimized resonance widths. The present bound grows like \(2+|t|p\), so a direct integral to infinity may still diverge; additional cancellation or an independent large-\(|t|\) endpoint estimate may be required.

## Disposition

Connectivity and component count are removed from the one-prime modulation gate. The residual is now purely the resonance and large-dual-coordinate integral. No transition-trace or RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_nested_set_fourier_variation.py`
- `research/voevodsky/results/nested_set_fourier_variation.json`
