# Soft D1 coefficient localization decision

```rzk
#lang rzk-1
#data NimaSoftD1CoefficientChoice
  := nima-coefficients-integral
  | nima-coefficients-invert-2
  | nima-coefficients-invert-6
  | nima-coefficients-invert-14
  | nima-coefficients-invert-21
  | nima-coefficients-invert-42
  | nima-coefficients-rational
#data NimaSoftD1LocalizedSaturation
  := nima-completed-image-still-nonsaturated
  | nima-completed-image-saturated-at-D12
#define nima-soft-D1-localized-saturation
  : NimaSoftD1CoefficientChoice -> NimaSoftD1LocalizedSaturation
  := \ choice -> match choice
       (nima-coefficients-integral => nima-completed-image-still-nonsaturated
       | nima-coefficients-invert-2 => nima-completed-image-still-nonsaturated
       | nima-coefficients-invert-6 => nima-completed-image-still-nonsaturated
       | nima-coefficients-invert-14 => nima-completed-image-still-nonsaturated
       | nima-coefficients-invert-21 => nima-completed-image-still-nonsaturated
       | nima-coefficients-invert-42 => nima-completed-image-saturated-at-D12
       | nima-coefficients-rational => nima-completed-image-saturated-at-D12)
#define nima-soft-D1-invert-42-saturates-D12
  : nima-soft-D1-localized-saturation nima-coefficients-invert-42
    = nima-completed-image-saturated-at-D12
  := refl
#define nima-soft-D1-invert-6-insufficient-D12
  : nima-soft-D1-localized-saturation nima-coefficients-invert-6
    = nima-completed-image-still-nonsaturated
  := refl
#define nima-soft-D1-invert-14-insufficient-D12
  : nima-soft-D1-localized-saturation nima-coefficients-invert-14
    = nima-completed-image-still-nonsaturated
  := refl
#define nima-soft-D1-invert-21-insufficient-D12
  : nima-soft-D1-localized-saturation nima-coefficients-invert-21
    = nima-completed-image-still-nonsaturated
  := refl
#data NimaSoftD1CoefficientDecisionScope
  := nima-D12-Smith-localization-result
  | nima-no-authorization-to-change-physical-coefficients
  | nima-integral-saturation-preferred-for-integral-amplitude
#define nima-soft-D1-coefficient-decision-scope : NimaSoftD1CoefficientDecisionScope
  := nima-no-authorization-to-change-physical-coefficients
```
