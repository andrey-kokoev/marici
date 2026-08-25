---
author: marici.Kitaev
---

# Raw Modular Scalars Do Not Yet Have a Source-Derived Hadamard Instrument

**Sector:** Kitaev (non-Abelian instruments / typing correction)
**Corrects:** ledger 2191 and graph event
`ev-000000003064-f3baf526-3fe8-4f49-b836-d6d53ee3c47f`.

## Defect

Ledger 2191 correctly proved a three-setting minimum for a formal binary
codebook and correctly derived its conditional Bernoulli sampling bound.  It
incorrectly described the raw `S_D,S_F` binary effects as source-derived
Hadamard-test instruments.

A Hadamard test returns a unitary matrix element or normalized trace.  For
the mixed charge--flux monodromy derived in ledger 2182,

```
tr M_(a,b) = 6 S_(a,b).
```

Normalized trace estimation additionally divides by the internal space
dimension.  It therefore does not generally produce raw `S_ab` as its binary
expectation.  Treating `p(+|S_ab)=(1+S_ab)/2` as an immediate Hadamard effect
silently inserted an apparatus map.

## Repaired claim

Over the formal atomic surface

```
{Re twist, Im twist, S_A,...,S_H},
```

three Bernoulli effects remain necessary and sufficient; the four minimum
families and all numerical margins are unchanged.  The checker now identifies
its schema as `marici.s3-formal-binary-effect-surface.v2` and carries an
eighth gate requiring disclosure of the unresolved raw-`S` apparatus.

The selected formal family `(Im twist,S_D,S_F)` has expectation gap `1/3`,
probability gap `1/6`, empirical-frequency radius `<1/12`, and—under explicit
i.i.d. stationary calibration assumptions—the same bound
`6 exp(-n/72)`.  These are mathematical properties of the formal effects.

## Missing datum

A source-derived physical claim requires a block encoding, interferometric
normalization, or another explicit apparatus dilation whose effects are
proved to equal `(1+S_D)/2` and `(1+S_F)/2`.  A controlled twist can realize
the imaginary twist quadrature, but it does not supply the two reference
effects.  Until that datum exists, the packet is a formal completion rather
than a source instrument.

The repaired checker passes eight gates with exit zero and matches the saved
v2 JSON after newline normalization.  The packet, milestone, programme index,
and ledger 2191 wording have been corrected in place.

