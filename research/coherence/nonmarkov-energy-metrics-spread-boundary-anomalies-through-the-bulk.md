# Non-Markov energy metrics spread boundary anomalies through the bulk

## Comparison

Use nine ordered contexts and permit anomaly support on the seven interior sites. Compare two positive kernels with \(0<\rho<1\).

### Markov exponential kernel

\[
K_{ij}=\rho^{|i-j|}.
\]

The minimum-energy lift of boundary data is supported only at the extreme allowed sites.

### Gaussian non-Markov kernel

\[
G_{ij}=\rho^{(i-j)^2}.
\]

This is a sampled squared-exponential kernel. Its inverse is dense rather than tridiagonal.

For the same boundary target, the minimum-energy lift has nonzero coefficients at every allowed interior site.

## Exact finite result

With \(\rho=1/2\), allowed sites \(1,\ldots,7\), and boundary target \((1,0)\):

```text
Markov lift support:     {1, 7}
non-Markov lift support: {1, 2, 3, 4, 5, 6, 7}
```

The calculation is exact rational arithmetic.

## Meaning

Boundary localization is not a universal consequence of positive energy minimization. It is a theorem about the Markov Green kernel.

```text
tridiagonal precision
-> conditional separation
-> extreme-site boundary representers

nonlocal precision
-> no conditional separation
-> bulk-supported representers
```

Thus whether a boundary discrepancy is explained as a boundary source or a bulk history diagnoses the locality structure of the chosen metric.

## Block-universe interpretation

In the Markov block, the interior is conditionally screened by the nearest admissible boundary layer. In a non-Markov block, boundary conditions couple directly to the entire interior, so the minimum-energy global explanation is delocalized.

This yields a useful model distinction:

- **boundary-local block:** finite-order local precision;
- **bulk-entangled block:** nonlocal precision;
- **mixed block:** sparse local precision plus low-rank or decaying nonlocal corrections.

The mixed case is the next realistic extreme: determine how rapidly an arbitrarily small nonlocal precision perturbation destroys exact boundary localization.

## Verification

```text
python research/coherence/check_nonmarkov_bulk_anomaly_lift.py
```

Artifacts:

- `check_nonmarkov_bulk_anomaly_lift.py`
- `nonmarkov-bulk-anomaly-lift.v1.json`
