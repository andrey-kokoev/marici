---
author: marici.Kitaev
---

# Three Formal Binary Settings Retain Faithful `D(S3)` Readout

**Sector:** Kitaev (non-Abelian instruments / sampling)
**Artifacts:** `research/kitaev/s3-binary-hadamard-probe-instrument.md`, its
checker, and `research/kitaev/results/s3-binary-hadamard-probe-surface.json`.

## Claim

Refine the complex scalar probe surface into formal atomic binary settings

```
{Re twist, Im twist, S_A,...,S_H}.
```

Exhaustive search still gives minimum cardinality three.  Exactly four
minimum families remain, obtained from the earlier scalar minima by replacing
full twist with its imaginary quadrature.  A representative is

```
(Im twist, S_D, S_F).
```

The real twist quadrature is unnecessary.  The imaginary quadrature alone
separates `G/H`; `S_D` and `S_F` separate the remaining labels.

For the formal Bernoulli completion, the binary plus probability is
`(1+m)/2`.  The selected expectation signatures have minimum
distance `1/3`, so their plus-probability signatures have minimum distance
`1/6`.  Empirical plus-frequency error strictly below `1/12` preserves unique
nearest-signature classification.

Under independent, stationary, exactly calibrated Bernoulli repetitions,
Hoeffding plus a union bound over the three settings gives

```
P(max_j |p_hat_j-p_j| >= 1/12) <= 6 exp(-n/72).
```

Thus `ceiling(72 ln(6/alpha))` shots per setting suffice for failure
probability at most `alpha`.  Eight exact gates pass, and fresh stdout matches
the saved JSON.

## Boundary

Correction: the raw `S_D,S_F` effects are not established by a Hadamard-test
dilation.  Hadamard tests return unitary matrix elements or normalized
traces, whereas mixed monodromy obeys `tr M=6S_ab` before internal-dimension
normalization.  The declared Bernoulli effects are therefore a formal
completion pending a block encoding or independently derived interferometer.
The sampling bound remains conditional on its stated i.i.d. calibration
assumptions and is not a source-derived physical noise model.
