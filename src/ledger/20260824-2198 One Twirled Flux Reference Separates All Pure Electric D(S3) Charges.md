---
author: marici.Kitaev
---

# One Twirled Flux Reference Separates All Pure-Electric `D(S3)` Charges

**Sector:** Kitaev (non-Abelian instruments / reference twirling)
**Artifacts:** `research/kitaev/s3-electric-one-setting-reference-twirl.md`,
its checker, and `research/kitaev/results/s3-electric-reference-twirl.json`.

## Claim

Uniformly conjugating a fixed transposition flux by all elements of `S3`
produces each of the three transpositions exactly twice.  A fixed three-cycle
similarly produces each cycle exactly three times.  This supplies uniform
conjugacy-class reference mixtures by classical random gauge conjugation.

On the standard electric charge `C`, the averaged actions are

```
(1/3) sum_transpositions rho_C(t) = 0,
(1/2) sum_three-cycles rho_C(c) = -I/2.
```

They are scalar, so the unknown electric target's internal density matrix
drops out.  No target-sector maximally mixed preparation is required.

A single normalized-monodromy setting using the twirled `D` reference has

```
mu_D(A)=1, mu_D(B)=-1, mu_D(C)=0,
```

and binary plus probabilities `1,0,1/2`.  It therefore separates all three
pure-electric sectors.  The expectation gap is one, probability gap `1/2`,
and unique empirical-frequency radius `<1/4`.  Under the explicit independent
stationary assumptions,

```
P(|p_hat-p| >= 1/4) <= 2 exp(-n/8),
```

so `ceiling(8 ln(2/alpha))` shots suffice.  Seven exact gates pass and fresh
stdout matches the saved JSON.

## Boundary

The result requires a constructible `D` reference, uniform random group
conjugation, and controlled monodromy.  It does not prove local fault
tolerance or extend the state-independence result to flux/dyon targets.  It
is a one-setting theorem only on `A,B,C`, not on all eight sectors.

