# Operational equality of computed normal forms

Raw fractions have decidable structural equality by independent numerator and
denominator decisions. Applying this decision to the total normalized
representatives gives an executable comparison now, while the Euclid theorem
remains necessary to prove that raw equivalence and normal-form equality agree.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-numerator
  ( p : MariciRawFraction)
  : MariciInt
  := match p (marici-raw-fraction a d ⇒ a)

#define marici-raw-fraction-denominator-predecessor
  ( p : MariciRawFraction)
  : MariciNat
  := match p (marici-raw-fraction a d ⇒ d)

#data MariciRawFractionEqualityDecision
  ( p q : MariciRawFraction)
  := marici-raw-fractions-equal
      ( path : p =_{MariciRawFraction} q)
  | marici-raw-fractions-unequal
      ( refutation : (p =_{MariciRawFraction} q) → MariciEmpty)

#define marici-raw-fraction-decide-equality
  ( p q : MariciRawFraction)
  : MariciRawFractionEqualityDecision p q
  := match p
      ( marici-raw-fraction a d ⇒ match q
        ( marici-raw-fraction b e ⇒
          match (marici-int-decide-equality a b)
            ( marici-int-equal numerator-path ⇒
                match (marici-nat-decide-equality d e)
                  ( marici-nat-equal denominator-path ⇒
                      marici-raw-fractions-equal
                        (marici-raw-fraction a d)
                        (marici-raw-fraction b e)
                        (marici-raw-fraction-component-path
                          a b d e numerator-path denominator-path)
                  | marici-nat-unequal denominator-refutation ⇒
                      marici-raw-fractions-unequal
                        (marici-raw-fraction a d)
                        (marici-raw-fraction b e)
                        (\ path → denominator-refutation
                          (ap MariciRawFraction MariciNat
                            (marici-raw-fraction a d)
                            (marici-raw-fraction b e)
                            marici-raw-fraction-denominator-predecessor
                            path)))
            | marici-int-unequal numerator-refutation ⇒
                marici-raw-fractions-unequal
                  (marici-raw-fraction a d)
                  (marici-raw-fraction b e)
                  (\ path → numerator-refutation
                    (ap MariciRawFraction MariciInt
                      (marici-raw-fraction a d)
                      (marici-raw-fraction b e)
                      marici-raw-fraction-numerator path)))))

#define marici-normalized-representatives-decide-equality
  ( p q : MariciRawFraction)
  : MariciRawFractionEqualityDecision
      (marici-normalized-raw-representative p)
      (marici-normalized-raw-representative q)
  := marici-raw-fraction-decide-equality
      (marici-normalized-raw-representative p)
      (marici-normalized-raw-representative q)
```

## Boundary

Computed normal forms can now be compared operationally without quotient or
uniqueness assumptions. A positive result is structural equality of the two
reduced representatives. A negative result does not yet refute raw-fraction
equivalence: that reflection direction requires reduced-representative
uniqueness, whose remaining arithmetic premise is the magnitude Euclid theorem.
