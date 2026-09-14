# Tangential coefficient amplitude calibration

This is the verified coefficient-level calibration for the future physical
amplitude.  It records the established scalar formula without promoting it to
the physical supported trace.

```rzk
#lang rzk-1

#define nima-tangential-coefficient-amplitude
  (beta a b c : MariciInt) : MariciInt
  := marici-int-negate
       (marici-int-mul beta (marici-int-add a (marici-int-add b c)))

#define nima-tangential-coefficient-amplitude-ap
  (beta : MariciInt) (x y : MariciInt) (p : x = y)
  : marici-int-negate (marici-int-mul beta x)
    = marici-int-negate (marici-int-mul beta y)
  := idJ (MariciInt, x,
       (\ y' p' -> marici-int-negate (marici-int-mul beta x)
         = marici-int-negate (marici-int-mul beta y')),
       refl, y, p)

#define nima-tangential-amplitude-sum-invariant
  (beta a b c a' b' c' : MariciInt)
  (same-total : marici-int-add a (marici-int-add b c)
    = marici-int-add a' (marici-int-add b' c'))
  : nima-tangential-coefficient-amplitude beta a b c
    = nima-tangential-coefficient-amplitude beta a' b' c'
  := nima-tangential-coefficient-amplitude-ap beta
       (marici-int-add a (marici-int-add b c))
       (marici-int-add a' (marici-int-add b' c')) same-total

#define nima-tangential-trace-difference-vanishes
  (beta a b c a' b' c' : MariciInt)
  (same-total : marici-int-add a (marici-int-add b c)
    = marici-int-add a' (marici-int-add b' c'))
  : nima-tangential-coefficient-amplitude beta a b c
    = nima-tangential-coefficient-amplitude beta a' b' c'
  := nima-tangential-amplitude-sum-invariant beta a b c a' b' c' same-total

#data NimaTangentialAmplitudeCalibrationStatus
  := nima-coefficient-formula-minus-beta-total
  | nima-equal-total-traces-have-equal-amplitude
  | nima-not-yet-identified-with-physical-supported-amplitude
#define nima-tangential-amplitude-calibration-status
  : NimaTangentialAmplitudeCalibrationStatus
  := nima-coefficient-formula-minus-beta-total
```
