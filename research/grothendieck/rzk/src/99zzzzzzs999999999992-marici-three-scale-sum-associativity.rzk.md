# Three-scale sum numerator associativity

Distributivity expands both bracketings of a three-fraction sum. Integer
multiplication associativity and commutativity align the three scaled terms, and
integer addition associativity identifies the resulting sums.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-three-scale-sum-associativity
  ( a b c d e f : MariciInt)
  : marici-int-add
      (marici-int-mul
        (marici-int-add (marici-int-mul a e) (marici-int-mul b d)) f)
      (marici-int-mul c (marici-int-mul d e))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul a (marici-int-mul e f))
      (marici-int-mul
        (marici-int-add (marici-int-mul b f) (marici-int-mul c e)) d)
  := concat MariciInt
      (marici-int-add
        (marici-int-mul
          (marici-int-add (marici-int-mul a e) (marici-int-mul b d)) f)
        (marici-int-mul c (marici-int-mul d e)))
      (marici-int-add
        (marici-int-add
          (marici-int-mul a (marici-int-mul e f))
          (marici-int-mul b (marici-int-mul d f)))
        (marici-int-mul c (marici-int-mul d e)))
      (marici-int-add
        (marici-int-mul a (marici-int-mul e f))
        (marici-int-mul
          (marici-int-add (marici-int-mul b f) (marici-int-mul c e)) d))
      (concat MariciInt
        (marici-int-add
          (marici-int-mul
            (marici-int-add (marici-int-mul a e) (marici-int-mul b d)) f)
          (marici-int-mul c (marici-int-mul d e)))
        (marici-int-add
          (marici-int-add
            (marici-int-mul (marici-int-mul a e) f)
            (marici-int-mul (marici-int-mul b d) f))
          (marici-int-mul c (marici-int-mul d e)))
        (marici-int-add
          (marici-int-add
            (marici-int-mul a (marici-int-mul e f))
            (marici-int-mul b (marici-int-mul d f)))
          (marici-int-mul c (marici-int-mul d e)))
        (ap MariciInt MariciInt
          (marici-int-mul
            (marici-int-add (marici-int-mul a e) (marici-int-mul b d)) f)
          (marici-int-add
            (marici-int-mul (marici-int-mul a e) f)
            (marici-int-mul (marici-int-mul b d) f))
          (\ first-summand → marici-int-add first-summand
            (marici-int-mul c (marici-int-mul d e)))
          (marici-int-mul-add-right-distrib
            (marici-int-mul a e) (marici-int-mul b d) f))
        (marici-int-add-congruent
          (marici-int-add
            (marici-int-mul (marici-int-mul a e) f)
            (marici-int-mul (marici-int-mul b d) f))
          (marici-int-add
            (marici-int-mul a (marici-int-mul e f))
            (marici-int-mul b (marici-int-mul d f)))
          (marici-int-mul c (marici-int-mul d e))
          (marici-int-mul c (marici-int-mul d e))
          (marici-int-add-congruent
            (marici-int-mul (marici-int-mul a e) f)
            (marici-int-mul a (marici-int-mul e f))
            (marici-int-mul (marici-int-mul b d) f)
            (marici-int-mul b (marici-int-mul d f))
            (marici-int-mul-assoc a e f)
            (marici-int-mul-assoc b d f)) refl))
      (concat MariciInt
        (marici-int-add
          (marici-int-add
            (marici-int-mul a (marici-int-mul e f))
            (marici-int-mul b (marici-int-mul d f)))
          (marici-int-mul c (marici-int-mul d e)))
        (marici-int-add
          (marici-int-mul a (marici-int-mul e f))
          (marici-int-add
            (marici-int-mul b (marici-int-mul d f))
            (marici-int-mul c (marici-int-mul d e))))
        (marici-int-add
          (marici-int-mul a (marici-int-mul e f))
          (marici-int-mul
            (marici-int-add (marici-int-mul b f) (marici-int-mul c e)) d))
        (marici-int-add-assoc
          (marici-int-mul a (marici-int-mul e f))
          (marici-int-mul b (marici-int-mul d f))
          (marici-int-mul c (marici-int-mul d e)))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-mul b (marici-int-mul d f))
            (marici-int-mul c (marici-int-mul d e)))
          (marici-int-mul
            (marici-int-add (marici-int-mul b f) (marici-int-mul c e)) d)
          (\ rest → marici-int-add
            (marici-int-mul a (marici-int-mul e f)) rest)
          (rev MariciInt
            (marici-int-mul
              (marici-int-add (marici-int-mul b f) (marici-int-mul c e)) d)
            (marici-int-add
              (marici-int-mul b (marici-int-mul d f))
              (marici-int-mul c (marici-int-mul d e)))
            (concat MariciInt
              (marici-int-mul
                (marici-int-add (marici-int-mul b f) (marici-int-mul c e)) d)
              (marici-int-add
                (marici-int-mul (marici-int-mul b f) d)
                (marici-int-mul (marici-int-mul c e) d))
              (marici-int-add
                (marici-int-mul b (marici-int-mul d f))
                (marici-int-mul c (marici-int-mul d e)))
              (marici-int-mul-add-right-distrib
                (marici-int-mul b f) (marici-int-mul c e) d)
              (marici-int-add-congruent
                (marici-int-mul (marici-int-mul b f) d)
                (marici-int-mul b (marici-int-mul d f))
                (marici-int-mul (marici-int-mul c e) d)
                (marici-int-mul c (marici-int-mul d e))
                (concat MariciInt
                  (marici-int-mul (marici-int-mul b f) d)
                  (marici-int-mul b (marici-int-mul f d))
                  (marici-int-mul b (marici-int-mul d f))
                  (marici-int-mul-assoc b f d)
                  (ap MariciInt MariciInt
                    (marici-int-mul f d) (marici-int-mul d f)
                    (\ product → marici-int-mul b product)
                    (marici-int-mul-comm f d)))
                (concat MariciInt
                  (marici-int-mul (marici-int-mul c e) d)
                  (marici-int-mul c (marici-int-mul e d))
                  (marici-int-mul c (marici-int-mul d e))
                  (marici-int-mul-assoc c e d)
                  (ap MariciInt MariciInt
                    (marici-int-mul e d) (marici-int-mul d e)
                    (\ product → marici-int-mul c product)
                    (marici-int-mul-comm e d))))))))
```

## Boundary

The numerator identity for raw-fraction addition associativity is now proved.
Encoded denominator associativity and cross-product transport remain before
rational addition can be used to split a shifted accumulator into prefix plus
independently folded tail.
