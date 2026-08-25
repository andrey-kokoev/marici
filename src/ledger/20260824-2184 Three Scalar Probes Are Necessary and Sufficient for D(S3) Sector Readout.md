---
author: marici.Kitaev
---

# Three Scalar Probes Are Necessary and Sufficient for `D(S3)` Sector Readout

**Sector:** Kitaev (non-Abelian readout / probe minimality)
**Artifacts:** `research/kitaev/s3-minimal-jointly-faithful-scalar-probes.md`,
its checker, and `research/kitaev/results/s3-minimal-scalar-probe-family.json`.

## Claim

Freeze the candidate scalar probe surface to topological twist `theta` and
the eight reference-sector Hopf-link amplitudes `S_A,...,S_H`.  Exhaustive
enumeration proves that no one- or two-probe family separates all eight
`D(S3)` anyon labels, while exactly four three-probe families do:

```
(theta,S_C,S_D), (theta,S_C,S_E),
(theta,S_D,S_F), (theta,S_E,S_F).
```

A representative minimum family is `(theta,S_D,S_F)`.  Its signatures for
`A,B,C,D,E,F,G,H` are respectively

```
(1,       1/2,  1/3)
(1,      -1/2,  1/3)
(1,          0, -1/3)
(1,        1/2,     0)
(-1,      -1/2,     0)
(1,          0,  2/3)
(omega,      0, -1/3)
(omega^2,    0, -1/3).
```

Twist resolves the centralizer-irrep kernel by separating `D/E` and all of
`F/G/H`.  The two Hopf-link references separate the remaining electric/flux
collisions.  Explicit lower-bound witnesses are: `(theta,S_F)` collides
`A/B`, `(theta,S_D)` collides `C/F`, and `(S_D,S_F)` collides `G/H`; the
checker additionally exhausts every other pair.

Seven aggregate gates pass with exit zero, and fresh stdout matches the saved
JSON after newline normalization.

## Physical and theorem boundary

The three probes require a framed self-twist constructor and prepared `D` and
`F` reference sectors supporting linked transport and fusion to scalar
records.  Carrier geometry supplies framed/link topology and reference-port
placement; the quantum coefficient lens supplies sector preparation and
amplitudes.

Minimality is relative to this nine-probe surface and counts a complex scalar
as one probe.  It is not an absolute laboratory-resource theorem: full
operator tomography, multi-outcome instruments, adaptive procedures, or a
different quadrature cost model define different optimization problems.

