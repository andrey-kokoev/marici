# Expanded search finds D1 components and a working vendored Arb backend

## Fresh finding

The finite-double-contact sweep describes the enclosure functor D1 and its prime-tail estimate E* as missing. Repository-wide code search shows that the mathematical components were subsequently constructed in separate packets:

1. `log-gaussian-prime-tail-certificates-for-meta-observers.md` gives an explicit all-integer upper bound for the omitted von Mangoldt tail;
2. `the-prime-tail-in-the-rank-two-gate-has-an-explicit-erfc-bound.md` gives a closed erfc form after completing the logarithmic Gaussian square;
3. `the-gamma-heat-integral-has-an-erfc-series-with-certifiable-tail.md` replaces improper digamma quadrature by a convergent erfc/Hurwitz-zeta series or compact quadrature plus explicit tail;
4. `backend-independent-erfc-enclosures.md` supplies Taylor and integration-by-parts enclosures for erfc;
5. `source-formula-for-the-gaussian-translation-rectangle.md` fixes one complete endpoint--gamma--prime normalization;
6. several Arb checkers already perform certified point evaluation of closely related coupled coordinates.

Therefore D1 is no longer blocked by absence of tail formulas.

## Backend correction

`current-python-backend-cannot-certify-the-gamma-special-functions.md` is stale for the current mutable repository state. A compatible python-flint build is vendored at

```text
research/benincasa/.tmp_flint/flint/pyflint.cp314-win_amd64.pyd
```

and the active interpreter is Python 3.14.6. The backend loads with

```text
PYTHONPATH="$PWD/research/benincasa/.tmp_flint" python ...
```

A fresh execution of

```text
PYTHONPATH="$PWD/research/benincasa/.tmp_flint" \
python research/grothendieck/checkers/arb_dual_witness_center.py
```

succeeded and produced a directed Arb interval

\[
D=[9.6480298922185\pm2.28\times10^{-14}]
\]

at \((t,\xi)=(0.299,4.5025)\), conditional only on its separately stated analytic gamma and prime tails.

This proves that the present environment can execute Arb arithmetic, complex digamma evaluation, and validated `acb.integral`. No package installation is needed.

## What remains genuinely missing

The existing pieces are pointwise or observer-specific. D1 requires one convention-locked implementation that accepts an entire box

\[
[t_1,t_2]\times[\xi_1,\xi_2]
\]

and returns simultaneous enclosures for

\[
\Theta,
\qquad
\partial_\xi\Theta,
\qquad
\partial_{\xi\xi}\Theta.
\]

The remaining work is:

- reconcile the shifted-spectral Gaussian used by the double-contact kernel with the modulation Gaussian used by stationary translation rectangles;
- derive box-monotone cutoffs valid for every \(t,\xi\) in a box;
- include derivative polynomial factors in the prime-tail bounds;
- turn the gamma point integrand into a box-valued Arb integrand, or use the erfc series uniformly;
- package all endpoint, finite-prime, prime-tail, gamma-tail, quadrature, and rounding intervals in one fail-closed result;
- run the two required negative controls.

## External search result

The indexed PDF corpus contains no Rosser--Schoenfeld, von Mangoldt, Chebyshev, digamma, or pseudodifferential estimates beyond the current repository derivations. OpenAlex/Crossref searches recovered standard explicit-prime-estimate literature but no specialized Gaussian von Mangoldt tail sharper than the elementary partial-summation architecture already present here.

Hence the next nonredundant action is implementation and normalization reconciliation, not another search for a tail theorem or interval backend.
