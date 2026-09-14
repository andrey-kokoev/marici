# Soft D1 Smith torsion profile

```rzk
#lang rzk-1
#data NimaSoftD1ImageSmithFactorsD12
  := nima-image-Smith-ones69-twos8-fourteens3-fortytwos4-eightyfours3-fourtwenties2
#define nima-soft-D1-image-Smith-factors-D12 : NimaSoftD1ImageSmithFactorsD12
  := nima-image-Smith-ones69-twos8-fourteens3-fortytwos4-eightyfours3-fourtwenties2
#data NimaSoftD1CompletedSmithFactorsD12
  := nima-completed-Smith-ones69-twos9-fourteens8-fortytwos4
#define nima-soft-D1-completed-Smith-factors-D12
  : NimaSoftD1CompletedSmithFactorsD12
  := nima-completed-Smith-ones69-twos9-fourteens8-fortytwos4
#data NimaSoftD1SaturationPrimeProfile
  := nima-image-index-primes-2pow25-3pow9-5pow2-7pow12
  | nima-completed-index-primes-2pow21-3pow4-7pow12
  | nima-L2-removes-5-primary-but-retains-2-3-7-torsion
#define nima-soft-D1-saturation-prime-profile : NimaSoftD1SaturationPrimeProfile
  := nima-L2-removes-5-primary-but-retains-2-3-7-torsion
#data NimaSoftD1IntegralReplacementGate
  := nima-localize-away-from-2-3-7-or-saturate-integrally
  | nima-physical-coefficient-ring-choice-required
#define nima-soft-D1-integral-replacement-gate : NimaSoftD1IntegralReplacementGate
  := nima-physical-coefficient-ring-choice-required
```
