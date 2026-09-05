# Deciding positive right divisibility of canonical integers

Zero is divisible by every positive factor. For nonzero integers, total
positive-natural divisibility of the magnitude either lifts to a signed
cofactor or refutes every alleged integer cofactor after applying magnitude.

```rzk
#lang rzk-1
```

```rzk
#data MariciIntRightPositiveDivisibilityDecision
  ( factor-predecessor : MariciNat)
  ( value : MariciInt)
  := marici-int-right-positive-divisible
      ( witness : MariciIntRightPositiveDivides factor-predecessor value)
  | marici-int-right-positive-indivisible
      ( refutation : MariciIntRightPositiveDivides factor-predecessor value
        → MariciEmpty)

#define marici-int-factorization-gives-magnitude-equation
  ( q z : MariciInt)
  ( f : MariciNat)
  ( e : marici-int-mul q (marici-int-positive-denominator f)
    =_{MariciInt} z)
  : marici-mul (marici-int-magnitude q) (marici-succ f)
    =_{MariciNat} marici-int-magnitude z
  := concat MariciNat
      (marici-mul (marici-int-magnitude q) (marici-succ f))
      (marici-int-magnitude
        (marici-int-mul q (marici-int-positive-denominator f)))
      (marici-int-magnitude z)
      (rev MariciNat
        (marici-int-magnitude
          (marici-int-mul q (marici-int-positive-denominator f)))
        (marici-mul (marici-int-magnitude q) (marici-succ f))
        (marici-int-magnitude-positive-right-product q f))
      (ap MariciInt MariciNat
        (marici-int-mul q (marici-int-positive-denominator f)) z
        marici-int-magnitude e)
```

```rzk
#define marici-decide-int-right-positive-divisibility
  ( f : MariciNat)
  ( z : MariciInt)
  : MariciIntRightPositiveDivisibilityDecision f z
  := match z
      ( marici-int-zero ⇒
          marici-int-right-positive-divisible f marici-int-zero
            (marici-int-zero-right-positive-divides f)
      | marici-int-pos a ⇒
          match (marici-decide-positive-nat-right-divisibility f a)
            ( marici-positive-nat-right-divisible witness ⇒ match witness
                ( marici-positive-nat-right-divides-witness q equation ⇒
                    marici-int-right-positive-divisible f (marici-int-pos a)
                      (marici-magnitude-factorization-lifts-to-int
                        (marici-int-pos a) q f equation))
            | marici-positive-nat-right-indivisible not-divides ⇒
                marici-int-right-positive-indivisible f (marici-int-pos a)
                  (\ witness → match witness
                    ( marici-int-right-positive-divides-witness q equation ⇒
                        (match q into
                          (\ q-prime →
                            (marici-int-mul q-prime
                              (marici-int-positive-denominator f)
                              =_{MariciInt} marici-int-pos a) → MariciEmpty)
                          ( marici-int-zero ⇒ \ eq →
                              marici-zero-not-succ a
                                (marici-int-factorization-gives-magnitude-equation
                                  marici-int-zero (marici-int-pos a) f eq)
                          | marici-int-pos k ⇒ \ eq →
                              not-divides
                                (marici-positive-nat-right-divides-witness
                                  f a k
                                  (marici-int-factorization-gives-magnitude-equation
                                    (marici-int-pos k) (marici-int-pos a) f eq))
                          | marici-int-neg k ⇒ \ eq →
                              not-divides
                                (marici-positive-nat-right-divides-witness
                                  f a k
                                  (marici-int-factorization-gives-magnitude-equation
                                    (marici-int-neg k) (marici-int-pos a) f eq)))) equation)))
      | marici-int-neg a ⇒
          match (marici-decide-positive-nat-right-divisibility f a)
            ( marici-positive-nat-right-divisible witness ⇒ match witness
                ( marici-positive-nat-right-divides-witness q equation ⇒
                    marici-int-right-positive-divisible f (marici-int-neg a)
                      (marici-magnitude-factorization-lifts-to-int
                        (marici-int-neg a) q f equation))
            | marici-positive-nat-right-indivisible not-divides ⇒
                marici-int-right-positive-indivisible f (marici-int-neg a)
                  (\ witness → match witness
                    ( marici-int-right-positive-divides-witness q equation ⇒
                        (match q into
                          (\ q-prime →
                            (marici-int-mul q-prime
                              (marici-int-positive-denominator f)
                              =_{MariciInt} marici-int-neg a) → MariciEmpty)
                          ( marici-int-zero ⇒ \ eq →
                              marici-zero-not-succ a
                                (marici-int-factorization-gives-magnitude-equation
                                  marici-int-zero (marici-int-neg a) f eq)
                          | marici-int-pos k ⇒ \ eq →
                              not-divides
                                (marici-positive-nat-right-divides-witness
                                  f a k
                                  (marici-int-factorization-gives-magnitude-equation
                                    (marici-int-pos k) (marici-int-neg a) f eq))
                          | marici-int-neg k ⇒ \ eq →
                              not-divides
                                (marici-positive-nat-right-divides-witness
                                  f a k
                                  (marici-int-factorization-gives-magnitude-equation
                                    (marici-int-neg k) (marici-int-neg a) f eq)))) equation))))
```

## Boundary

Positive right divisibility of canonical integers is now fully decidable.
Common-factor selection must range nonunit factors and intersect this decision
with positive-denominator divisibility.
