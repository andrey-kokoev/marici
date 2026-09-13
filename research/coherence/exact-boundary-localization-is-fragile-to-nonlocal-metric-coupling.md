# Exact boundary localization is fragile to nonlocal metric coupling

## Mixed metric

Start with the Markov Green metric

\[
K_{ij}=\rho^{|i-j|}
\]

and perturb it by a nonlocal squared-exponential metric

\[
G_{ij}=\rho^{(i-j)^2}.
\]

Set

\[
W_\varepsilon=K+\varepsilon G,
\qquad \varepsilon>0.
\]

Use the original two Markov boundary covectors and compute the minimum-\(W_\varepsilon\)-energy anomaly lift on an allowed interior interval.

## Immediate support transition

At \(\varepsilon=0\), the lift is supported exactly at the two extreme allowed sites.

For every tested \(\varepsilon>0\), however small, every strict interior coefficient is nonzero. Exact boundary localization disappears immediately.

For nine contexts and \(\rho=1/2\), the largest strict-bulk coefficient behaves as:

| \(\varepsilon\) | maximum bulk coefficient | ratio to \(\varepsilon\) |
|---:|---:|---:|
| \(10^{-3}\) | \(4.606\times10^{-4}\) | 0.4606 |
| \(10^{-4}\) | \(4.610\times10^{-5}\) | 0.4610 |
| \(10^{-5}\) | \(4.610\times10^{-6}\) | 0.4610 |
| \(10^{-6}\) | \(4.610\times10^{-7}\) | 0.4610 |

Thus bulk leakage is first order:

\[
\|u_{\rm bulk}\|_\infty
=C\varepsilon+O(\varepsilon^2),
\qquad C\approx0.4610
\]

for this finite model.

## Structural meaning

```text
exactly Markov precision:
  exact boundary support

arbitrarily small nonlocal coupling:
  global bulk support of small amplitude
```

Boundary localization is structurally fragile as a support statement but perturbatively stable as an amplitude statement.

## Interpretation

This separates two notions:

- **exact locality:** all forbidden bulk coefficients vanish identically;
- **effective locality:** bulk coefficients are small relative to a nonlocality parameter.

Realistic systems with weak long-range couplings should be expected to exhibit effective, not exact, boundary localization.

The bulk leakage profile can serve as a detector for hidden non-Markov interactions. Its first derivative at \(\varepsilon=0\) records how the nonlocal metric couples boundary representers into the interior.

## Verification

```text
python research/coherence/check_small_nonlocal_metric_perturbation.py
```

All matrix calculations use exact rational arithmetic; only the reported magnitudes are converted to floating point.

Artifacts:

- `check_small_nonlocal_metric_perturbation.py`
- `small-nonlocal-metric-perturbation.v1.json`
