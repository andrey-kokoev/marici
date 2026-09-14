# Soft D1 L2 defect completion

```rzk
#lang rzk-1
#data NimaSoftD1OddBocksteinGrowth
  := nima-beta-ranks-14-18-22-26
  | nima-canonical-ranks-13-17-21-25
  | nima-one-missing-generator-at-each-cutoff
#define nima-soft-D1-odd-Bockstein-growth : NimaSoftD1OddBocksteinGrowth
  := nima-one-missing-generator-at-each-cutoff
#data NimaSoftD1ResidualProvenance
  := nima-residual-from-minus-q-source-s11
  | nima-residual-target-three-a3-plus-three-a3b
#define nima-soft-D1-residual-provenance : NimaSoftD1ResidualProvenance
  := nima-residual-from-minus-q-source-s11
#data NimaSoftD1L2Transition
  := nima-L2-transition-adds-one-rank
  | nima-L2-completes-beta-image-at-all-tested-cutoffs
#define nima-soft-D1-L2-transition : NimaSoftD1L2Transition
  := nima-L2-completes-beta-image-at-all-tested-cutoffs
#data NimaSoftD1CompletionQualification
  := nima-truncations-16-20-24-28-pass
  | nima-total-cokernel-not-flat
  | nima-integral-Smith-and-global-chain-map-still-required
#define nima-soft-D1-completion-qualification : NimaSoftD1CompletionQualification
  := nima-integral-Smith-and-global-chain-map-still-required
```
