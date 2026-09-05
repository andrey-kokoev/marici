# Shifted accumulation splits into prefix and folded tail

Induction transports the previous split through the next addition. Component
associativity moves the new term into the tail fold. The zero case uses the
componentwise right-zero law.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-shifted-tail-term
  ( prefix : MariciNat)
  ( term : MariciNat → MariciRational)
  ( index : MariciNat)
  : MariciRational
  := term (marici-add index prefix)

#define marici-rational-shifted-accumulate-split-components
  ( prefix length : MariciNat)
  ( term : MariciNat → MariciRational)
  : marici-rational-forget
      (marici-rational-shifted-accumulate prefix length term)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-add
        (marici-rational-finite-sum prefix term)
        (marici-rational-finite-sum length
          (marici-rational-shifted-tail-term prefix term)))
  := match length
      ( marici-zero ⇒
          rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-finite-sum prefix term)
                marici-rational-zero))
            (marici-rational-forget
              (marici-rational-finite-sum prefix term))
            (marici-rational-add-zero-right-components
              (marici-rational-finite-sum prefix term))
      | marici-succ k induction ⇒
          concat MariciRawFraction
            (marici-rational-forget
              (marici-rational-shifted-accumulate
                prefix (marici-succ k) term))
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-add
                  (marici-rational-finite-sum prefix term)
                  (marici-rational-finite-sum k
                    (marici-rational-shifted-tail-term prefix term)))
                (term (marici-add k prefix))))
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-finite-sum prefix term)
                (marici-rational-finite-sum (marici-succ k)
                  (marici-rational-shifted-tail-term prefix term))))
            (marici-rational-add-component-congruent
              (marici-rational-shifted-accumulate prefix k term)
              (marici-rational-add
                (marici-rational-finite-sum prefix term)
                (marici-rational-finite-sum k
                  (marici-rational-shifted-tail-term prefix term)))
              (term (marici-add k prefix))
              (term (marici-add k prefix))
              induction refl)
            (marici-rational-add-assoc-components
              (marici-rational-finite-sum prefix term)
              (marici-rational-finite-sum k
                (marici-rational-shifted-tail-term prefix term))
              (term (marici-add k prefix))))
```

## Boundary

The shifted accumulator now has the canonical components of prefix plus the
independently folded shifted tail. Translated-addition cancellation therefore
identifies its difference from the prefix with that tail.
