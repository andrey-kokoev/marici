# Soft D1 five-cutoff Smith laws

```rzk
#lang rzk-1
#data NimaSoftD1VerifiedCutoffFamily
  := nima-cutoffs-n3-through-n7-with-D-equals4n
#define nima-soft-D1-verified-cutoff-family : NimaSoftD1VerifiedCutoffFamily
  := nima-cutoffs-n3-through-n7-with-D-equals4n
#data NimaSoftD1VerifiedSmithCountLaws
  := nima-unit-count-n-times-6n-plus5
  | nima-pure-two-count-n-times-2n-minus3
  | nima-nonunit-count-n-times-2n-plus1
  | nima-two-exponent-equals-nonunit-count
  | nima-seven-exponent-equals-4n
#define nima-soft-D1-verified-Smith-count-laws : NimaSoftD1VerifiedSmithCountLaws
  := nima-nonunit-count-n-times-2n-plus1
#data NimaSoftD1VerifiedInvariantFactorSupport
  := nima-only-1-2-14-42-occur-after-L2
#define nima-soft-D1-verified-invariant-factor-support
  : NimaSoftD1VerifiedInvariantFactorSupport
  := nima-only-1-2-14-42-occur-after-L2
#data NimaSoftD1SmithLawScope
  := nima-exactly-five-computed-cutoffs
  | nima-all-degree-proof-remains-open
#define nima-soft-D1-Smith-law-scope : NimaSoftD1SmithLawScope
  := nima-exactly-five-computed-cutoffs
```
