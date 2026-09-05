# Ordered index equations transport rational distance

A gap equation from `smaller` to `larger` can be rewritten through a supplied
successor presentation of `smaller`. Function congruence then transports both
sequence endpoints and hence their rational distance.

```rzk
#lang rzk-1
```

```rzk
#define marici-ordered-gap-endpoint-path
  ( local smaller larger gap : MariciNat)
  ( smaller-path : marici-succ local =_{MariciNat} smaller)
  ( larger-equation : marici-add gap smaller =_{MariciNat} larger)
  : marici-add gap (marici-succ local) =_{MariciNat} larger
  := concat MariciNat
      (marici-add gap (marici-succ local))
      (marici-add gap smaller)
      larger
      (ap MariciNat MariciNat
        (marici-succ local) smaller
        (\ endpoint → marici-add gap endpoint)
        smaller-path)
      larger-equation

#define marici-rational-sequence-distance-index-path
  ( sequence : MariciNat → MariciRational)
  ( left-index left-index-prime right-index right-index-prime : MariciNat)
  ( left-index-path : left-index =_{MariciNat} left-index-prime)
  ( right-index-path : right-index =_{MariciNat} right-index-prime)
  : marici-rational-distance (sequence left-index) (sequence right-index)
    =_{MariciRational}
    marici-rational-distance (sequence left-index-prime) (sequence right-index-prime)
  := concat MariciRational
      (marici-rational-distance (sequence left-index) (sequence right-index))
      (marici-rational-distance (sequence left-index-prime) (sequence right-index))
      (marici-rational-distance
        (sequence left-index-prime) (sequence right-index-prime))
      (ap MariciNat MariciRational left-index left-index-prime
        (\ index → marici-rational-distance
          (sequence index) (sequence right-index))
        left-index-path)
      (ap MariciNat MariciRational right-index right-index-prime
        (\ index → marici-rational-distance
          (sequence left-index-prime) (sequence index))
        right-index-path)

#define marici-exponent-two-ordered-distance-index-components
  ( local smaller larger gap : MariciNat)
  ( smaller-path : marici-succ local =_{MariciNat} smaller)
  ( larger-equation : marici-add gap smaller =_{MariciNat} larger)
  : marici-rational-forget
      (marici-rational-distance
        (marici-exponent-two-partial-sum
          (marici-add gap (marici-succ local)))
        (marici-exponent-two-partial-sum (marici-succ local)))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-distance
        (marici-exponent-two-partial-sum larger)
        (marici-exponent-two-partial-sum smaller))
  := ap MariciRational MariciRawFraction
      (marici-rational-distance
        (marici-exponent-two-partial-sum
          (marici-add gap (marici-succ local)))
        (marici-exponent-two-partial-sum (marici-succ local)))
      (marici-rational-distance
        (marici-exponent-two-partial-sum larger)
        (marici-exponent-two-partial-sum smaller))
      marici-rational-forget
      (marici-rational-sequence-distance-index-path
        marici-exponent-two-partial-sum
        (marici-add gap (marici-succ local)) larger
        (marici-succ local) smaller
        (marici-ordered-gap-endpoint-path
          local smaller larger gap smaller-path larger-equation)
        smaller-path)
```

## Boundary

The explicit ordered-tail metric theorem can now be transported to arbitrary
ordered indices once successor-cutoff decomposition supplies `local` and
`smaller-path`. Reciprocal antitonicity then weakens the local tolerance to the
requested cutoff tolerance.
