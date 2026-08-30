---
author: marici.Kitaev
---

# Minimum `D(S3)` Scalar Readout Has Sharp Error Radius One Sixth

**Sector:** Kitaev (non-Abelian readout / deterministic robustness)
**Artifacts:** `research/kitaev/s3-scalar-probe-adversarial-margin.md`, its
checker, and `research/kitaev/results/s3-scalar-probe-noise-margin.json`.

## Claim

Equip each complex twist or Hopf-link coordinate with complex modulus and
signature vectors with the `L_infinity` metric.  Each of the four minimum
three-probe families for `D(S3)` sector readout has the same exact minimum
pairwise distance:

```
delta = 1/3.
```

Therefore arbitrary per-probe error strictly below `1/6` preserves unique
nearest-signature classification.

The bound is sharp.  For `(theta,S_D,S_F)`, the closest signatures

```
A = (1,1/2,1/3),   D = (1,1/2,0)
```

have midpoint `(1,1/2,1/6)`, exactly `1/6` from both.  Closed error balls
intersect at that boundary.  The remaining minimum families likewise have
distance `1/3`, with closest pair `A/D` or `B/D` depending on reference.

Exact `Q(omega)` arithmetic uses
`|a+b omega|^2=a^2-a b+b^2`; the comparison is by complex modulus rather than
formal symbol inequality.  The checker audits every label pair in all four
families and passes six aggregate gates.  Fresh stdout matches the saved JSON
after newline normalization.

## Boundary

This is a deterministic codebook radius.  It supplies no stochastic noise
law, sample complexity, confidence interval, calibration protocol,
correlated-fault model, or physical decoder.  Reweighting coordinates,
counting real and imaginary quadratures separately, or allowing adaptive or
operator-valued measurements changes the theorem.

