# Alternating-sheet/Rees annihilator data

This module records the corrected minimal generators after the nonflat graph
substitution. It does not reuse the old principal six-normal formula.

```rzk
#lang rzk-1

#data NimaAlternatingCoefficientMode
  := nima-alternating-common-conductor
  | nima-alternating-plus-X13
  | nima-alternating-plus-X15
  | nima-alternating-plus-X35
  | nima-alternating-minus-X02
  | nima-alternating-minus-X04
  | nima-alternating-minus-X24

#data NimaAlternatingReesAnnihilatorGenerator
  := nima-annihilator-common
  | nima-annihilator-plus-13
  | nima-annihilator-plus-15
  | nima-annihilator-plus-35
  | nima-annihilator-minus-02
  | nima-annihilator-minus-04
  | nima-annihilator-minus-24

#define nima-rees-tau-plus : NimaShortReesMonomial6
  := (marici-zero,(marici-zero,(marici-zero,
       (marici-one,(marici-one,marici-one)))))
#define nima-rees-tau-minus : NimaShortReesMonomial6
  := (marici-one,(marici-one,(marici-one,
       (marici-zero,(marici-zero,marici-zero)))))
#define nima-rees-tau-plus-times-tau-minus : NimaShortReesMonomial6
  := (marici-one,(marici-one,(marici-one,
       (marici-one,(marici-one,marici-one)))))

#define nima-alternating-annihilator-mode
  : NimaAlternatingReesAnnihilatorGenerator -> NimaAlternatingCoefficientMode
  := \ g -> match g
       (nima-annihilator-common => nima-alternating-common-conductor
       | nima-annihilator-plus-13 => nima-alternating-plus-X13
       | nima-annihilator-plus-15 => nima-alternating-plus-X15
       | nima-annihilator-plus-35 => nima-alternating-plus-X35
       | nima-annihilator-minus-02 => nima-alternating-minus-X02
       | nima-annihilator-minus-04 => nima-alternating-minus-X04
       | nima-annihilator-minus-24 => nima-alternating-minus-X24)

#define nima-alternating-annihilator-rees
  : NimaAlternatingReesAnnihilatorGenerator -> NimaShortReesMonomial6
  := \ g -> match g
       (nima-annihilator-common => nima-rees-tau-plus-times-tau-minus
       | nima-annihilator-plus-13 => nima-rees-tau-plus
       | nima-annihilator-plus-15 => nima-rees-tau-plus
       | nima-annihilator-plus-35 => nima-rees-tau-plus
       | nima-annihilator-minus-02 => nima-rees-tau-minus
       | nima-annihilator-minus-04 => nima-rees-tau-minus
       | nima-annihilator-minus-24 => nima-rees-tau-minus)

#data NimaAlternatingOccurrenceSupport
  := nima-occurrence-support-conductor
  | nima-occurrence-support-plus
  | nima-occurrence-support-minus
  | nima-occurrence-support-mixed-zero

#define nima-alternating-support-product
  : NimaAlternatingOccurrenceSupport -> NimaAlternatingOccurrenceSupport ->
    NimaAlternatingOccurrenceSupport
  := \ a b -> match a
       (nima-occurrence-support-conductor => b
       | nima-occurrence-support-plus => match b
          (nima-occurrence-support-conductor => nima-occurrence-support-plus
          | nima-occurrence-support-plus => nima-occurrence-support-plus
          | nima-occurrence-support-minus => nima-occurrence-support-mixed-zero
          | nima-occurrence-support-mixed-zero => nima-occurrence-support-mixed-zero)
       | nima-occurrence-support-minus => match b
          (nima-occurrence-support-conductor => nima-occurrence-support-minus
          | nima-occurrence-support-plus => nima-occurrence-support-mixed-zero
          | nima-occurrence-support-minus => nima-occurrence-support-minus
          | nima-occurrence-support-mixed-zero => nima-occurrence-support-mixed-zero)
       | nima-occurrence-support-mixed-zero => nima-occurrence-support-mixed-zero)

#define nima-old-six-normal-graph-support-zero
  : nima-alternating-support-product
      nima-occurrence-support-plus nima-occurrence-support-minus
    = nima-occurrence-support-mixed-zero
  := refl

#data NimaProperNonemptyTripleSubset
  := nima-triple-subset-0
  | nima-triple-subset-1
  | nima-triple-subset-2
  | nima-triple-subset-01
  | nima-triple-subset-02
  | nima-triple-subset-12

#data NimaBoundaryAmbiguityFamily
  := nima-boundary-ambiguity-plus (inactive-minus : NimaProperNonemptyTripleSubset)
  | nima-boundary-ambiguity-minus (inactive-plus : NimaProperNonemptyTripleSubset)

#define nima-boundary-ambiguity-family-count : MariciNat
  := marici-succ (marici-succ (marici-succ (marici-succ
       (marici-succ (marici-succ (marici-succ (marici-succ
       (marici-succ (marici-succ (marici-succ (marici-succ marici-zero)))))))))))
```
