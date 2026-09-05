# Reduced uniqueness reduces to denominator uniqueness

Once equivalent fractions have the same positive denominator predecessor,
positive integer right cancellation forces their numerators to agree. Thus the
coprime part of reduced uniqueness only has to identify denominators.

```rzk
#lang rzk-1
```

```rzk
#define marici-equal-denominator-equivalent-numerators-equal
  ( a b : MariciInt)
  ( d : MariciNat)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction a d)
      (marici-raw-fraction b d))
  : a =_{MariciInt} b
  := marici-int-positive-right-injective d a b equivalent

#define marici-equal-denominator-equivalent-raw-fractions-equal
  ( a b : MariciInt)
  ( d : MariciNat)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction a d)
      (marici-raw-fraction b d))
  : marici-raw-fraction a d =_{MariciRawFraction}
      marici-raw-fraction b d
  := marici-raw-fraction-component-path
      a b d d
      (marici-equal-denominator-equivalent-numerators-equal
        a b d equivalent)
      refl

#define MariciEquivalentReducedDenominatorsEqual
  : U
  := ( a b : MariciInt)
    → ( d e : MariciNat)
    → MariciRawComponentsAreReduced a d
    → MariciRawComponentsAreReduced b e
    → marici-raw-fraction-equivalent
        (marici-raw-fraction a d)
        (marici-raw-fraction b e)
    → d =_{MariciNat} e
```

Transporting the second fraction and the equivalence along denominator equality
reduces the full theorem to the equal-denominator cancellation lemma.

```rzk
#define marici-reduced-components-uniqueness-from-denominators
  ( denominators-equal : MariciEquivalentReducedDenominatorsEqual)
  ( a b : MariciInt)
  ( d e : MariciNat)
  ( reduced-a : MariciRawComponentsAreReduced a d)
  ( reduced-b : MariciRawComponentsAreReduced b e)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction a d) (marici-raw-fraction b e))
  : marici-raw-fraction a d =_{MariciRawFraction}
      marici-raw-fraction b e
  := ind-path MariciNat d
      (\ e' denominator-path →
        (equivalent' : marici-raw-fraction-equivalent
          (marici-raw-fraction a d)
          (marici-raw-fraction b e'))
        → marici-raw-fraction a d =_{MariciRawFraction}
            marici-raw-fraction b e')
      (\ equivalent' →
        marici-equal-denominator-equivalent-raw-fractions-equal
          a b d equivalent')
      e
      (denominators-equal a b d e reduced-a reduced-b equivalent)
      equivalent

#define marici-reduced-representative-uniqueness-from-denominators
  ( denominators-equal : MariciEquivalentReducedDenominatorsEqual)
  : MariciReducedRepresentativeUniqueness
  := \ left → match left into
      (\ left-prime → (right : MariciReducedRawFraction)
        → marici-raw-fraction-equivalent
            (marici-reduced-raw-fraction-forget left-prime)
            (marici-reduced-raw-fraction-forget right)
        → marici-reduced-raw-fraction-forget left-prime
            =_{MariciRawFraction}
          marici-reduced-raw-fraction-forget right)
      ( marici-reduced-raw-fraction a d reduced-a ⇒
        \ right → match right into
          (\ right-prime →
            marici-raw-fraction-equivalent
              (marici-raw-fraction a d)
              (marici-reduced-raw-fraction-forget right-prime)
            → marici-raw-fraction a d =_{MariciRawFraction}
                marici-reduced-raw-fraction-forget right-prime)
          ( marici-reduced-raw-fraction b e reduced-b ⇒ \ equivalent →
              marici-reduced-components-uniqueness-from-denominators
                denominators-equal a b d e
                reduced-a reduced-b equivalent))
```

## Boundary

Full reduced-representative uniqueness is now reduced to one arithmetic
statement: equivalent reduced fractions have equal positive denominator
predecessors. The remaining coprime cross-product argument must establish that
statement; numerator equality then follows from already checked positive right
cancellation.
