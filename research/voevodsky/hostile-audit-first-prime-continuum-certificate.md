# Hostile audit of the first-prime continuum certificate

## Problem

Does the final Arb calculation depend on an unproved normalization, localization constant, quadrature promotion, residual truncation, or positive-completion claim?

## Conjecture

The cutoff-250 certificate and its extension to the uncut first-prime form survive independent checks of all five interfaces.

## Rivals

1. the constant \(130/40\) does not dominate the negative multiplier;
2. the bad set was never rigorously reduced from radius 10000 to radius 100;
3. the Bernstein remainder is not uniform over all degree-159 entries;
4. the projected residual tail omits a projection or endpoint contribution;
5. positivity outside cutoff 250 uses the obsolete Fourier normalization.

## Tests and residuals

### Fourier normalization

The source coefficient \(1/(4\pi)\) multiplies the nonunitary Fourier norm. Plancherel changes the unitary multiplier to

\[
\frac{\operatorname{Re}\psi(1/4+iu/2)-\log\pi}{2}.
\]

The Arb cutoff-form checker uses this expression. Rival 5 fails.

### Pointwise localization constant

A 25,000-cell directed Arb subdivision of \([-250,250]\) gives

\[
\inf s(u)>-3.22238139761>-\frac{129}{40}.
\]

A separate directed exterior calculation gives

\[
s(u)>0.8935
\]

on \(100\leq|u|\leq10000\), and the Binet estimate covers larger frequencies. Hence

\[
s(u)\geq\frac1{40}-\frac{130}{40}\mathbf1_{[-100,100]}(u).
\]

Rivals 1 and 2 fail. The audit exposed that the earlier radius-100 claim lacked a direct interval artifact; `check_interval_exterior_multiplier_nonnegative.py` now supplies it.

### Uniform Gauss remainder

Every Legendre basis vector is normalized in \(L^2[-L,L]\). The Bernstein-ellipse argument bounds the product of any two Fourier transforms uniformly, independently of degree. The same \(10^{32}\) envelope therefore covers all \(160^2\) multiplier entries. Gauss exactness through degree 319 and the summed panel half-length 250 give entrywise remainder below

\[
1.873\times10^{-61}.
\]

Arb evaluation of nodes, weights, Bessel functions, and digamma values supplies directed centers. Rival 3 fails.

### Projected residual tail

Because the selected span lies in degrees 0 through 79,

\[
\langle p_n,QAZ\rangle=\langle p_n,AZ\rangle
\]

for every \(n\geq80\). Directed bounds give \(\|s\|_\infty<3.223\), \(\|Z\|<11.031\), multiplier tail below the registered \(4.36\times10^{-13}\) envelope, and endpoint tail below \(1.091\times10^{-452}\). Rival 4 fails.

### Final propagation

The concentration matrix is recomputed by an independent directed Arb Gauss calculation, giving

\[
\rho=0.0061940130287439028\ldots,
\quad
\alpha=0.0048694576565823159\ldots.
\]

The source endpoint is the half-sum of the two polar evaluations, so its matrix is \((a_+a_-^*+a_-a_+^*)/2\). An audit found that the original checker had omitted this factor \(1/2\). After repair, the cutoff-form matrix still has maximum entry radius below \(4.09\times10^{-21}\). Exact-decimal span algebra and the residual tail complete all 25 interval \(LDL^*\) pivots; the corrected minimum pivot lower bound is \(0.0017645830061413439\).

## Disposition

The five hostile rivals are rejected. The cutoff-250 continuum form is positive on the first-prime support window. Directed nonnegativity for \(|u|>250\) promotes this to the uncut form on the same window. The audit also confirms two historical corrections: replace the obsolete factor-40 inverse bound by the trace-derived inverse floor, and cite the new radius-100 exterior interval artifact. No other support window or RH implication is established.

## Verification

- `research/voevodsky/checkers/check_arb_cutoff_form_legendre_matrix.py`
- `research/voevodsky/results/arb_cutoff_form_legendre_matrix.json`
- `research/voevodsky/checkers/check_interval_multiplier_supremum.py`
- `research/voevodsky/results/interval_multiplier_supremum.json`
- `research/voevodsky/checkers/check_interval_exterior_multiplier_nonnegative.py`
- `research/voevodsky/results/interval_exterior_multiplier_nonnegative.json`
- `research/voevodsky/checkers/check_interval_endpoint_legendre_tail.py`
- `research/voevodsky/results/interval_endpoint_legendre_tail.json`
