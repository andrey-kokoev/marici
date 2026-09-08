# Explicit D03 packet specialization maps

This module connects the pre-specialization two-annihilator packet to the
fixed-beta normalized packet and then to the strict X35 occurrence summand.
The first map is the exact principal-factor evaluation: it records the
post-specialization primitives, rather than pretending that homology commutes
with the nonflat coefficient change.

```rzk
#lang rzk-1

#define nima-d03-factor-specialization-column
  : NimaD03ResonanceBasis -> NimaD03SpecializedPacket
  := \ (q,m) -> match q
       (nima-d03-resonance-omega => nima-d03-specialized-Omega-chain
       | nima-d03-resonance-Wu => nima-d03-specialized-S-chain
       | nima-d03-resonance-Wmu => nima-d03-specialized-Hmu-chain)

#define nima-d03-factor-specialization
  : NimaD03Resonance -> NimaD03SpecializedPacket
  := nima-sum-bind NimaD03ResonanceBasis NimaD03SpecializedState
       nima-d03-factor-specialization-column

#define nima-d03-factor-specialization-column-chain
  : (v : NimaD03ResonanceBasis) ->
    nima-sum-equal NimaD03SpecializedState
      (nima-d03-specialized-d (nima-d03-factor-specialization-column v))
      (nima-d03-factor-specialization (nima-d03-resonance-column v))
  := \ (q,m) -> (match q into (\ k -> (m' : NimaD03ResonanceMonomial) ->
       nima-sum-equal NimaD03SpecializedState
         (nima-d03-specialized-d
           (nima-d03-factor-specialization-column (k,m')))
         (nima-d03-factor-specialization
           (nima-d03-resonance-column (k,m')))) (
    nima-d03-resonance-omega => \ m' probe -> refl
  | nima-d03-resonance-Wu => \ m' probe -> refl
  | nima-d03-resonance-Wmu => \ m' probe -> refl
  )) m

#define nima-d03-theta-specializes-to-Z
  : nima-sum-equal NimaD03SpecializedState
      (nima-d03-factor-specialization nima-d03-theta)
      nima-d03-specialized-Z-chain
  := \ probe -> refl

#define nima-d03-specialized-to-x35-column
  : NimaD03SpecializedState -> NimaX35Summand
  := \ q -> match q
       (nima-d03-specialized-Omega => nima-sum-zero NimaX35SummandBasis
       | nima-d03-specialized-S => nima-sum-zero NimaX35SummandBasis
       | nima-d03-specialized-Hmu => nima-x35-Z marici-zero)

#define nima-d03-specialized-to-x35
  : NimaD03SpecializedPacket -> NimaX35Summand
  := nima-sum-bind NimaD03SpecializedState NimaX35SummandBasis
       nima-d03-specialized-to-x35-column

#define nima-d03-specialized-to-x35-column-chain
  : (q : NimaD03SpecializedState) ->
    nima-sum-equal NimaX35SummandBasis
      (nima-x35-summand-d (nima-d03-specialized-to-x35-column q))
      (nima-d03-specialized-to-x35 (nima-d03-specialized-column q))
  := \ q -> match q
       (nima-d03-specialized-Omega => \ probe -> refl
       | nima-d03-specialized-S => \ probe -> refl
       | nima-d03-specialized-Hmu => \ probe -> refl)

#define nima-d03-Z-enters-x35-summand
  : nima-sum-equal NimaX35SummandBasis
      (nima-d03-specialized-to-x35 nima-d03-specialized-Z-chain)
      (nima-x35-Z marici-zero)
  := \ probe -> nima-frame-concat MariciInt
       (nima-sum-eval NimaX35SummandBasis probe
         (nima-d03-specialized-to-x35 nima-d03-specialized-Z-chain))
       (nima-sum-eval NimaX35SummandBasis probe
         (nima-sum-add NimaX35SummandBasis (nima-x35-Z marici-zero)
           (nima-sum-zero NimaX35SummandBasis)))
       (nima-sum-eval NimaX35SummandBasis probe (nima-x35-Z marici-zero))
       refl
       (nima-sum-add-right-zero NimaX35SummandBasis
         (nima-x35-Z marici-zero) probe)

#define nima-d03-theta-specializes-to-x35-Z
  : nima-sum-equal NimaX35SummandBasis
      (nima-d03-specialized-to-x35
        (nima-d03-factor-specialization nima-d03-theta))
      (nima-x35-Z marici-zero)
  := nima-d03-Z-enters-x35-summand
```
