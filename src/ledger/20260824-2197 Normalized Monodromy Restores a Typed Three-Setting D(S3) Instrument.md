---
author: marici.Kitaev
---

# Normalized Monodromy Restores a Typed Three-Setting `D(S3)` Instrument

**Sector:** Kitaev (non-Abelian instruments / controlled trace)
**Artifacts:** `research/kitaev/s3-normalized-monodromy-controlled-trace-probes.md`,
its checker, and
`research/kitaev/results/s3-normalized-monodromy-probe-surface.json`.

## Claim

The apparatus correction in ledger 2196 has a constructive replacement.  A
controlled-unitary trace test does not measure raw `S_ab`; on a maximally
mixed internal tensor-product space it measures

```
mu_ab = tr(M_ab)/(d_a d_b) = 6 S_ab/(d_a d_b).
```

All normalized monodromy expectations lie in `[-1,1]` and therefore define
direct Hadamard-test binary probabilities `(1+mu_ab)/2` under the stated
controlled-unitary and state-preparation capabilities.

Over the corrected atomic surface

```
{Re twist, Im twist, mu_A,...,mu_H},
```

three settings remain necessary and sufficient.  Exactly four minimum
families exist, with representative `(Im twist,mu_D,mu_F)`.  Its expectation
signatures for `A,...,H` are

```
(0,          1,    1)
(0,         -1,    1)
(0,          0, -1/2)
(0,        1/3,    0)
(0,       -1/3,    0)
(0,          0,    1)
(sqrt(3)/2,  0, -1/2)
(-sqrt(3)/2, 0, -1/2).
```

The minimum expectation gap is `1/2`, the binary probability gap is `1/4`,
and empirical-frequency error `<1/8` preserves unique classification.  Under
independent stationary calibrated Bernoulli repetitions,

```
P(max_j |p_hat_j-p_j| >= 1/8) <= 6 exp(-n/32),
```

so `ceiling(32 ln(6/alpha))` shots per setting suffice.  Seven checker gates
pass and fresh stdout matches the saved JSON.

## Boundary

The abstract dilation is typed conditional on coherent controlled monodromy
or twist and maximally mixed preparation on the relevant internal space.  No
local fault-tolerant controlled-ribbon synthesis or sector-uniform internal
state preparation is proved.  The statistical bound remains conditional on
its explicit i.i.d. calibration assumptions.

