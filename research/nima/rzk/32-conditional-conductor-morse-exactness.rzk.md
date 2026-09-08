# Conditional conductor-Morse exactness by graded Leibniz

The physical comparison and admissibility predicates are intentionally
parameters.  This module checks the sign algebra once the required cochains
inhabit a common coefficient mapping complex.

```rzk
#lang rzk-1

#define nima-secondary-sign-identity (x y : MariciInt)
  : marici-int-add x (marici-int-negate y)
    = marici-int-negate (marici-int-add y (marici-int-negate x))
  := nima-frame-concat MariciInt
       (marici-int-add x (marici-int-negate y))
       (marici-int-add (marici-int-negate y) x)
       (marici-int-negate (marici-int-add y (marici-int-negate x)))
       (marici-int-add-comm x (marici-int-negate y))
       (nima-frame-concat MariciInt
         (marici-int-add (marici-int-negate y) x)
         (marici-int-add (marici-int-negate y)
           (marici-int-negate (marici-int-negate x)))
         (marici-int-negate (marici-int-add y (marici-int-negate x)))
         (nima-frame-ap MariciInt MariciInt (marici-int-add (marici-int-negate y))
           x (marici-int-negate (marici-int-negate x))
           (nima-frame-rev MariciInt
             (marici-int-negate (marici-int-negate x)) x
             (marici-int-negate-involutive x)))
         (nima-frame-rev MariciInt
           (marici-int-negate (marici-int-add y (marici-int-negate x)))
           (marici-int-add (marici-int-negate y)
             (marici-int-negate (marici-int-negate x)))
           (marici-int-negate-add y (marici-int-negate x))))

#define nima-conditional-graded-leibniz-exactness
  (K E H A R : U)
  (delta-k : K -> E)
  (delta-h : H -> A)
  (delta-r : R -> MariciInt)
  (compose-kh : K -> H -> R)
  (compose-eh : E -> H -> MariciInt)
  (compose-ka : K -> A -> MariciInt)
  (k : K) (e : E) (h : H) (a : A)
  (k-boundary : delta-k k = e)
  (h-boundary : delta-h h = a)
  (graded-leibniz :
    delta-r (compose-kh k h)
      = marici-int-add
          (compose-eh (delta-k k) h)
          (marici-int-negate (compose-ka k (delta-h h))))
  : marici-int-add (compose-ka k a) (marici-int-negate (compose-eh e h))
      = marici-int-negate (delta-r (compose-kh k h))
  := nima-frame-concat MariciInt
       (marici-int-add (compose-ka k a) (marici-int-negate (compose-eh e h)))
       (marici-int-negate
         (marici-int-add (compose-eh e h) (marici-int-negate (compose-ka k a))))
       (marici-int-negate (delta-r (compose-kh k h)))
       (nima-secondary-sign-identity (compose-ka k a) (compose-eh e h))
       (nima-frame-ap MariciInt MariciInt marici-int-negate
         (marici-int-add (compose-eh e h) (marici-int-negate (compose-ka k a)))
         (delta-r (compose-kh k h))
         (nima-frame-rev MariciInt
           (delta-r (compose-kh k h))
           (marici-int-add (compose-eh e h) (marici-int-negate (compose-ka k a)))
           (nima-frame-concat MariciInt
             (delta-r (compose-kh k h))
             (marici-int-add (compose-eh (delta-k k) h)
               (marici-int-negate (compose-ka k (delta-h h))))
             (marici-int-add (compose-eh e h)
               (marici-int-negate (compose-ka k a)))
             graded-leibniz
             (nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
               (compose-eh (delta-k k) h) (compose-eh e h)
               (marici-int-negate (compose-ka k (delta-h h)))
               (marici-int-negate (compose-ka k a))
               (nima-frame-ap E MariciInt (\ e' -> compose-eh e' h)
                 (delta-k k) e k-boundary)
               (nima-frame-ap MariciInt MariciInt marici-int-negate
                 (compose-ka k (delta-h h)) (compose-ka k a)
                 (nima-frame-ap A MariciInt (compose-ka k)
                   (delta-h h) a h-boundary))))))
```
